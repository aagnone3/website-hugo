.DEFAULT_GOAL := help

.PHONY: help
help: ## Display help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "%-30s %s\n", $$1, $$2}'

.PHONY: clean
clean:
	@rm -rf public
	@find . -type f -name "*.pyc" -delete
	@find . -type f -name __pycache__ | xargs rm -rf

.PHONY: build
build: clean  ## Build static site
	hugo

.PHONY: server
server: build  ## Start a local server for the site
	hugo server \
		-D \
		--disableFastRender
