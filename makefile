CURRENT_DIR := $(dir $(abspath $(firstword $(MAKEFILE_LIST))))

# Python variables:
PYTHON_VERSION = 3.13

# Docker variables:
DOCKER_DIR = ./docker
DOCKER_FILE = $(DOCKER_DIR)/Dockerfile

DOCKER_TAG = kaszanas/sc2anonserverpy

############################
#### Using the tools #######
############################
.PHONY: run
run_server: ## Run the server
	docker run -it --rm \
		$(DOCKER_TAG) \
		python3 grpc_server.py

.PHONY: run_client
run_client: ## Run the client
	docker run -it --rm \
		$(DOCKER_TAG) \
		python3 grpc_client.py


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


.PHONY: help
help: ## Show available make targets
	@awk '/^[^\t ]*:.*?##/{sub(/:.*?##/, ""); printf "\033[36m%-30s\033[0m %s\n", $$1, substr($$0, index($$0,$$2))}' $(MAKEFILE_LIST)
