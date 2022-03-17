# PYTHON_PATH=$$(which python3)
# SHELL:=/bin/zsh
# CONDA_ACTIVATE=source $$(conda info --base)/etc/profile.d/conda.sh ; conda activate ; conda activate
CD = $(shell pwd)
PYTHON_IMAGE := python-base
DOCKERFILES_DIR := dockerfiles/
INGESTION_DIR := ingestion

default: build download processing

# download-files:
# 	( \
# 		mkdir files csv; \
# 		source pyenv/bin/activate; \
# 		python ingestion.py; \
# 	)


# set-conda-env:
# 	( \
# 		virtualenv -p ${PYTHON_PATH} pyenv; \
# 		source pyenv/bin/activate; \
# 		python -m pip install -r requirements.txt; \
# 	)
build:
	docker build -t ${PYTHON_IMAGE} -f dockerfiles/Dockerfile.python ${DOCKERFILES_DIR}

create-db:
	mkdir db
	docker-compose up --build -d

download:
	docker run -v ${CD}:/app -it ${PYTHON_IMAGE} python ${INGESTION_DIR}/download.py

processing:
	docker run -v ${CD}:/app -it ${PYTHON_IMAGE} python ${INGESTION_DIR}/processing.py

data-quality:
	docker run -v ${CD}:/app -it python ${DOWNLOAD_DIR}/data-quality.py
