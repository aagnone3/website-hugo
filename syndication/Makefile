IMAGE ?= aagnone/circleci-hugo
TAG ?= latest

.PHONY: help
help: ## Display help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "%-30s %s\n", $$1, $$2}'

.PHONY: image
image: ## Build the container
	docker build \
		-t $(IMAGE) \
		.

.PHONY: run
run: ## Run the container
	docker run \
		-ti \
		--mount type=bind,source="$(shell echo ${PWD}/../)",target=/opt/hugo \
		--rm \
		$(IMAGE) \
		bash

.PHONY: login
login:
	docker login

.PHONY: push
push: ## Push the image to Docker Hub
	docker push $(IMAGE):$(TAG)
