from uwsgidecorators import cron


@cron(0, -1, -1, -1, -1)
def self_kill_if_update_available(signum: int):
    pass
