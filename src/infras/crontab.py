from django.core.management import call_command
from uwsgidecorators import cron


@cron(0, -1, -1, -1, -1)
def convert_subtitle_encoding(signum: int):
    call_command('check')
