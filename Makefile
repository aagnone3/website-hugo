.DEFAULT_GOAL := help
REMOTE_HOST ?= website
STAGE_DIR ?= staging
SITE_NAME ?= anthonyagnone.com
HUGO_BUILD_DIR ?= /opt/hugo/public

.PHONY: help
help: ## Display help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "%-30s %s\n", $$1, $$2}'

.PHONY: clean
clean:
	@rm -rf public
	@find . -type f -name "*.pyc" -delete
	@find . -type f -name __pycache__ | xargs rm -rf

.PHONY: init
init: clean
	git submodule sync && git submodule update --init

.PHONY: build
site: clean  ## Build static site
	HUGO_ENV=production hugo -v -d $(HUGO_BUILD_DIR)

.PHONY: verify
verify: build
	htmlproofer $(HUGO_BUILD_DIR) --allow-hash-href --check-html --empty-alt-ignore --disable-external

.PHONY: server
local_server: build  ## Start a local server for the site
	hugo server \
		-D \
		--disableFastRender

.PHONY: stage
stage: ## Transfer to staging directory on remote host
	rsync -e 'ssh -o BatchMode=yes -F etc/ssh_cfg' -azru . $(REMOTE_HOST):$(STAGE_DIR)/$(SITE_NAME)

.PHONY: deploy
deploy: ## Transfer to deploy directory on remote host
	rsync -e 'ssh -o BatchMode=yes -F etc/ssh_cfg' -azru . $(REMOTE_HOST):$(SITE_NAME)
