import os

import chardet
from django.conf import settings

from libs.django.command import CommonBaseCommand


class Command(CommonBaseCommand):
    title = 'Convert subtitle encoding'
    help = 'Convert subtitle encoding'

    def run(self, *args, **options):
        self._tour_directory(settings.MOUNT_PATH)

    def _tour_directory(self, directory: str):
        self.log_info(f'[TOUR] {directory}')
        for _, directories, files in os.walk(directory):
            for sub_directory in directories:
                self._tour_directory(os.path.join(directory, sub_directory))

            for filename in files:
                if filename.endswith('.srt') or filename.endswith('.smi'):
                    self._convert(os.path.join(directory, filename))

    def _convert(self, filename):
        with open(filename, 'rb') as f:
            contents = f.read()

        chdt = chardet.detect(contents)
        if chdt['encoding'] == 'utf-8':
            return

        if chdt['confidence'] < 0.8:
            raise Exception

        self.log_info(f'[CONVERTED] {filename}')

        with open(filename, 'rb') as original_file:
            with open(f'{filename}.bak', 'wb') as backup_file:
                backup_file.write(original_file.read())

        # with open(filename, 'w') as f:
        #     f.write(contents.decode(chdt['encoding']))
