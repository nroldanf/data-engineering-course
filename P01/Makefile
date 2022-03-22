CD = $(shell pwd)
PYTHON_IMAGE := python-base
DOCKERFILES_DIR := dockerfiles/
INGESTION_DIR := ingestion

default: build create-db download processing data-quality

build:
	docker build -t ${PYTHON_IMAGE} -f dockerfiles/Dockerfile.python ${DOCKERFILES_DIR}

create-db:
	docker-compose up -d

download:
	docker run -v ${CD}:/app -it ${PYTHON_IMAGE} python ${INGESTION_DIR}/download.py

processing:
	docker run -v ${CD}:/app -it ${PYTHON_IMAGE} python ${INGESTION_DIR}/processing.py

data-quality:
	docker run -v ${CD}:/app -it python ${DOWNLOAD_DIR}/data-quality.py
