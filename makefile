CURRENT_DIR := $(dir $(abspath $(firstword $(MAKEFILE_LIST))))

# Python variables:
PYTHON_VERSION = 3.13

# Docker variables:
DOCKER_DIR = ./docker
DOCKER_FILE = $(DOCKER_DIR)/Dockerfile
DOCKER_FILE_DEVCONTAINER = $(DOCKER_DIR)/Dockerfile.dev

DOCKER_TAG = kaszanas/sc2anonserverpy
DEVCONTAINER = kaszanas/sc2anonserverpy-devcontainer

############################
#### Using the tools #######
############################
.PHONY: run
run_server: ## Run the server
	docker run -it --rm \
		-v ".\processing:/app/processing"
		$(DOCKER_TAG) \
		python3 grpc_server.py

.PHONY: run_client
run_client: ## Run the client without multiprocessing
	docker run -it --rm \
		-v ".\processing:/app/processing"
		$(DOCKER_TAG) \
		python3 grpc_client.py \
			--input_dir /app/processing/demos/input \
			--output_dir /app/processing/demos/output \
			--agents 1 \
			--chunksize 1 \
			--use_multiprocessing False

############################
#### Docker commands #######
############################
.PHONY: docker_build
docker_build: ## Builds the image containing all of the tools.
	@echo "Building the Dockerfile: $(DOCKER_FILE)"
	@echo "Using Python version: $(PYTHON_VERSION)"
	docker build \
		--build-arg="PYTHON_VERSION=$(PYTHON_VERSION)" \
		-f $(DOCKER_FILE) . \
		--tag=$(DOCKER_TAG)


.PHONY: docker_run_it
docker_run_it: ## Run the container in interactive mode
	docker run -it --rm $(DOCKER_TAG)


.PHONY: docker_build_devcontainer
docker_build_devcontainer: ## Builds the devcontainer image.
	@echo "Building the Dockerfile: $(DOCKER_FILE_DEVCONTAINER)"
	@echo "Setting tag to: $(DEVCONTAINER)"
	@echo "Using Python version: $(PYTHON_VERSION)"
	docker build \
		--build-arg="PYTHON_VERSION=$(PYTHON_VERSION)" \
		-f $(DOCKER_FILE_DEVCONTAINER) . \
		--tag=$(DEVCONTAINER)


############################
#### GitHub Actions ########
############################
.PHONY: docker_pre_commit_action
docker_pre_commit_action: ## Runs pre-commit hooks using Docker.
	@echo "Running pre-commit hooks using Docker."
	@make docker_build_devcontainer
	@echo "Using the devcontainer image: $(DEVCONTAINER)"
	docker run \
		$(DEVCONTAINER) \
		pre-commit run --all-files


.PHONY: help
help: ## Show available make targets
	@awk '/^[^\t ]*:.*?##/{sub(/:.*?##/, ""); printf "\033[36m%-30s\033[0m %s\n", $$1, substr($$0, index($$0,$$2))}' $(MAKEFILE_LIST)
