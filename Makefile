.DEFAULT_GOAL := help
REMOTE_HOST ?= website
STAGE_DIR ?= staging
SITE_NAME ?= anthonyagnone.com
HUGO_BUILD_DIR ?= /home/user/public
IMAGE ?= aagnone/circleci-hugo
TAG ?= latest

# execute the commands in the Docker container if on a circleci instance
# TODO if not, plug in environment variables also
ifdef CIRCLE_BRANCH
    define DOCKER_INVOCATION
    $(MAKE) -f Makefile.ci TARGET
    endef
else
    define DOCKER_INVOCATION
    docker run \
		-ti \
		-e DEV_API_TOKEN=${DEV_API_TOKEN} \
		-e DEV_ARTICLES_URL=${DEV_ARTICLES_URL} \
		-e DEV_URL=${DEV_URL} \
		-e MEDIUM_API_URL=${MEDIUM_API_URL} \
		-e MEDIUM_API_VERSION=${MEDIUM_API_VERSION} \
		-e MEDIUM_CLIENT_ID=${MEDIUM_CLIENT_ID} \
		-e MEDIUM_CLIENT_SECRET=${MEDIUM_CLIENT_SECRET} \
		-e MEDIUM_INTEGRATION_TOKEN=${MEDIUM_INTEGRATION_TOKEN} \
		-e TWITTER_ACCESS_TOKEN_KEY=${TWITTER_ACCESS_TOKEN_KEY} \
		-e TWITTER_ACCESS_TOKEN_SECRET=${TWITTER_ACCESS_TOKEN_SECRET} \
		-e TWITTER_CONSUMER_KEY=${TWITTER_CONSUMER_KEY} \
		-e TWITTER_CONSUMER_SECRET=${TWITTER_CONSUMER_SECRET} \
		--mount type=bind,source="$(shell pwd)",target=/home/user \
		--mount type=bind,source=$(HOME)/.ssh,target=/home/user/.ssh \
		--rm \
		$(IMAGE) \
		$(MAKE) -f Makefile.ci TARGET
    endef
endif

.PHONY: help
help: ## Display help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "%-30s %s\n", $$1, $$2}'

.PHONY: test
test: ## Enter a shell in the Docker container
	$(subst TARGET,$@,${DOCKER_INVOCATION})

.PHONY: shell
shell: ## Enter a shell in the Docker container
	$(subst TARGET,$@,${DOCKER_INVOCATION})

.PHONY: clean
clean: ## Clear out temporary files
	$(subst TARGET,$@,${DOCKER_INVOCATION})

.PHONY: init
init: clean ## Initialize git submodules
	$(subst TARGET,$@,${DOCKER_INVOCATION})

.PHONY: site
site: init ## Build static site
	$(subst TARGET,$@,${DOCKER_INVOCATION})

.PHONY: verify
verify: site ## Perform verifications on the generated site
	$(subst TARGET,$@,${DOCKER_INVOCATION})

.PHONY: server
local_server: ## Start a local server for the site
	$(subst TARGET,$@,${DOCKER_INVOCATION})

.PHONY: stage
stage: verify ## Transfer to staging directory on remote host
	$(subst TARGET,$@,${DOCKER_INVOCATION})

.PHONY: deploy
deploy: verify ## Transfer to deploy directory on remote host
	$(subst TARGET,$@,${DOCKER_INVOCATION})
