from libs.django.command import CommonBaseCommand


class Command(CommonBaseCommand):
    title = 'Manual'
    help = 'Manual'

    def add_arguments(self, parser):
        parser.add_argument('-o', type=int, dest='offset', required=False)
        parser.add_argument('-l', type=int, dest='limit', required=False)

    def run(self, *args, **options):
        offset = options.get('offset', 0)
        limit = options.get('limit', 1000)

        self.log_info(f'{offset}-{limit} done')
