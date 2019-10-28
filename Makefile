.PHONY: all help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

# docker
docker-cmd: install-package run

docker-uwsgi-cmd: install-package run


# install
install-package:
	@pipenv install --dev


# run
run:
	@python src/manage.py convert_subtitle_encoding

run-uwsgi:
	@pipenv run uwsgi --ini /htdocs/www/docs/wsgi/uwsgi.ini --import infras.crontab

shell:
	@pipenv shell

# pre-processing
lint:
	@pipenv run pylint ./src/ --rcfile=.pylintrc
	@pipenv run flake8

# docker
docker-up:
	@docker-compose up

docker-rebuild-up:
	@docker-compose up --force-recreate --build

docker-kill-all:
	@docker ps -a -q | xargs docker rm -f

docker-logs:
	@docker-compose logs -f video-manager

docker-bash:
	@docker-compose exec video-manager /bin/bash
