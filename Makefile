.DEFAULT_GOAL := help
REMOTE_HOST ?= website
STAGE_DIR ?= staging
SITE_NAME ?= anthonyagnone.com

.PHONY: help
help: ## Display help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "%-30s %s\n", $$1, $$2}'

.PHONY:
stage: ## Transfer to staging directory on remote host
	rsync -azru . $(REMOTE_HOST):$(STAGE_DIR)/$(SITE_NAME)

.PHONY:
deploy: ## Transfer to deploy directory on remote host
	rsync -azru . $(REMOTE_HOST):$(SITE_NAME)
