# PYTHON_PATH=$$(which python3)
# SHELL:=/bin/zsh
# CONDA_ACTIVATE=source $$(conda info --base)/etc/profile.d/conda.sh ; conda activate ; conda activate
CD = $(shell pwd)

default: set-conda-env download-files

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

create-db:
	mkdir db
	docker-compose up --build -d

ingest:
	mkdir files csv
	docker build -t ingestion -f ingestion/Dockerfile.python ingestion
	docker run -v ${CD}:/app ingestion