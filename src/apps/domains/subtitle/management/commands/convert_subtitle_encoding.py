import os

import chardet
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from apps.domains.subtitle.models import Subtitle
from libs.django.command import CommonBaseCommand


class Command(CommonBaseCommand):
    title = 'Convert subtitle encoding'
    help = 'Convert subtitle encoding'

    def run(self, *args, **options):
        self._tour_directory(settings.MOUNT_PATH)

    def _tour_directory(self, directory: str):
        for _, directories, files in os.walk(directory):
            for sub_directory in directories:
                self._tour_directory(os.path.join(directory, sub_directory))

            for filename in files:
                if filename.endswith('.srt') or filename.endswith('.smi'):
                    self._convert(os.path.join(directory, filename))

    def _convert(self, file_path):
        try:
            with open(file_path, 'rb') as f:
                contents = f.read()

        except FileNotFoundError:
            return

        try:
            subtitle = Subtitle.objects.get(file_path=file_path)

        except ObjectDoesNotExist:
            subtitle = Subtitle()
            subtitle.file_path = file_path
            subtitle.save()

        if subtitle.encoding_type == 'utf-8':
            return

        chdt = chardet.detect(contents)
        if subtitle.encoding_type != chdt['encoding']:
            subtitle.encoding_type = chdt['encoding']
            subtitle.save()

        if chdt['encoding'] == 'utf-8':
            return

        if chdt['confidence'] < 0.8:
            self.log_info(f'[DETECT_ERROR] {file_path}: {chdt["encoding"]}, {chdt["confidence"]}')
            return

        self.log_info(f'[CONVERTED] {file_path}')

        with open(file_path, 'rb') as original_file:
            with open(f'{file_path}.bak', 'wb') as backup_file:
                backup_file.write(original_file.read())

        with open(file_path, 'w') as f:
            f.write(contents.decode(chdt['encoding']))

        subtitle.encoding_type = 'utf-8'
        subtitle.save()
