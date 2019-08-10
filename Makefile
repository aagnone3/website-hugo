.DEFAULT_GOAL := help
REMOTE_HOST ?= website
STAGE_DIR ?= staging
SITE_NAME ?= anthonyagnone.com
HUGO_BUILD_DIR ?= /opt/hugo/public
IMAGE ?= aagnone/circleci-hugo
TAG ?= latest

# execute the commands in the Docker container if on a circleci instance
ifdef CIRCLE_BRANCH
    define DOCKER_INVOCATION
    $(MAKE) -f \
		Makefile.ci TARGET
    endef
else
    define DOCKER_INVOCATION
    docker run \
		-ti \
		--mount type=bind,source="$(shell pwd)",target=/opt/hugo \
		--rm \
		$(IMAGE) \
		$(MAKE) -f Makefile.ci TARGET
    endef
endif

.PHONY: help
help: ## Display help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "%-30s %s\n", $$1, $$2}'

.PHONY: clean
clean:  ## Build static site
	$(subst TARGET,$@,${DOCKER_INVOCATION})

.PHONY: init
init: clean
	$(subst TARGET,$@,${DOCKER_INVOCATION})

.PHONY: site
site: init  ## Build static site
	$(subst TARGET,$@,${DOCKER_INVOCATION})

.PHONY: verify
verify: site
	$(subst TARGET,$@,${DOCKER_INVOCATION})

.PHONY: server
local_server:  ## Start a local server for the site
	$(subst TARGET,$@,${DOCKER_INVOCATION})

.PHONY: stage
stage: ## Transfer to staging directory on remote host
	$(subst TARGET,$@,${DOCKER_INVOCATION})

.PHONY: deploy
deploy: ## Transfer to deploy directory on remote host
	$(subst TARGET,$@,${DOCKER_INVOCATION})
