.DEFAULT_GOAL := help

## GENERAL ##
APP_DIR         = "app"
VENV_DIR        = "venv"
ENV							= dev
## RESULT_VARS ##
PROJECT_NAME    = aptitus-masterdata-testapi
CONTAINER_NAME  = ${PROJECT_NAME}_dev
IMAGE_DEV       = ${PROJECT_NAME}:dev


##################################################################
#### Development Commands
##################################################################

ssh: ## Conectar al container por el protocolo ssh
	docker container run --workdir "/${APP_DIR}" --rm -it -v "${PWD}/${VENV_DIR}":/${VENV_DIR} -v "${PWD}/${APP_DIR}":/${APP_DIR} ${IMAGE_DEV} "/bin/zsh"

build: ## Construir imagen para development
	docker build -f docker/dev/Dockerfile -t $(IMAGE_DEV) docker/dev/ --no-cache

venv-create: ## Crea el entorno virtual (virtualenv)
	@docker container run --workdir "/${APP_DIR}" --rm -it -v "${PWD}/${VENV_DIR}":/${VENV_DIR} -v "${PWD}/${APP_DIR}":/${APP_DIR} --tty=false ${IMAGE_DEV}  python3 -m venv /${VENV_DIR}
	@sudo chown ${USER}:${USER} ${VENV_DIR}

venv-install-lib: ## Instala las librerias en el entorno virtual (virtualenv)
	docker container run --workdir "/${APP_DIR}" --rm -it -v "${PWD}/${VENV_DIR}":/${VENV_DIR} -v "${PWD}/${APP_DIR}":/${APP_DIR} --tty=false ${IMAGE_DEV}  "/${VENV_DIR}/bin/pip" install -r requirements.txt

tests: ## Run behave Tests
	docker container run --workdir "/${APP_DIR}" -e "ENV=$(ENV)" --rm -v "${PWD}/${VENV_DIR}":/${VENV_DIR} -v "${PWD}/${APP_DIR}":/${APP_DIR} ${IMAGE_DEV} "/${VENV_DIR}/bin/behave" --no-capture

install:
	make venv-create;
	make venv-install-lib;
##################################################################
###### Help
##################################################################
help:
	@grep -E '^[a-zA-Z_-]+.+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-16s\033[0m %s\n", $$1, $$2}'
	@echo