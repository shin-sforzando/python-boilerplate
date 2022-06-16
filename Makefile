# -*- coding: utf-8 -*-

TIMESTAMP := $(shell date +%Y%m%d%H%M%S)
MAKEFILE_DIR := $(dir $(realpath $(firstword $(MAKEFILE_LIST))))
OS_NAME := $(shell uname -s)

CMD_DOCKER := docker
CMD_DOCKER_COMPOSE := docker compose

MAIN_CONTAINER_APP := app
MAIN_CONTAINER_SHELL := bash
OPEN_TARGET := http://0.0.0.0:8000/

OPTS :=
.DEFAULT_GOAL := default
.PHONY: default init ps build up renew shell logs follow open hide reveal start format lint test pytest doc sphinx deploy stop down clean prune help

default: up ## 常用
	make open
	make follow

init: ## 初期
ifeq ($(OS_NAME),Darwin)
	brew install git-cliff
	brew install git-secret
	brew install direnv
	brew install lefthook
endif
	direnv allow
	lefthook install
	@if [ $(OS_NAME) = "Darwin" ]; then say "The initialization process is complete." ; fi

ps: ## 状況
	$(CMD_DOCKER_COMPOSE) ps --all

build: ## 構築
	$(CMD_DOCKER_COMPOSE) build
	@if [ $(OS_NAME) = "Darwin" ]; then say "The building process is complete." ; fi

up: build ## 起動
	$(CMD_DOCKER_COMPOSE) up --detach --remove-orphans
	@if [ $(OS_NAME) = "Darwin" ]; then say "The container has been launched." ; fi

renew: down clean build ; ## 転生
	$(CMD_DOCKER_COMPOSE) up --detach --remove-orphans --force-recreate
	@if [ $(OS_NAME) = "Darwin" ]; then say "The container has been renewed." ; fi

shell: ## 接続
	$(CMD_DOCKER_COMPOSE) run --rm --no-deps $(MAIN_CONTAINER_APP) $(MAIN_CONTAINER_SHELL)

logs: ## 記録
	$(CMD_DOCKER_COMPOSE) logs --timestamps

follow: ## 追跡
	$(CMD_DOCKER_COMPOSE) logs --timestamps --follow

open: ## 閲覧
	@if [ $(OS_NAME) = "Darwin" ]; then open ${OPEN_TARGET} ; fi

hide: ## 秘匿
	git secret hide -vm

reveal: ## 暴露
	git secret reveal -vf

start: stop ## 開始
	@if [ $(OS_NAME) = "Darwin" ]; then say "Start the application." ; fi
	$(CMD_DOCKER_COMPOSE) run --rm --no-deps --service-ports $(MAIN_CONTAINER_APP) python src/main.py

format: ## 整形
	$(CMD_DOCKER_COMPOSE) run --rm --no-deps $(MAIN_CONTAINER_APP) black $(OPTS) .
	@if [ $(OS_NAME) = "Darwin" ]; then say "The format process is complete." ; fi

lint: ## 検証
	$(CMD_DOCKER_COMPOSE) run --rm --no-deps $(MAIN_CONTAINER_APP) flake8 $(OPTS)
	@if [ $(OS_NAME) = "Darwin" ]; then say "The lint process is complete." ; fi

test: pytest ## 試験
	@if [ $(OS_NAME) = "Darwin" ]; then say "The test process is complete." ; fi

pytest: build ## 試験
	$(CMD_DOCKER_COMPOSE) run --rm --no-deps $(MAIN_CONTAINER_APP) pytest $(OPTS)

doc: sphinx ## 文書

sphinx: format ## 文書
	$(CMD_DOCKER_COMPOSE) run --rm --no-deps $(MAIN_CONTAINER_APP) sphinx-apidoc --force --output-dir docs .
	$(CMD_DOCKER_COMPOSE) run --rm --no-deps $(MAIN_CONTAINER_APP) sphinx-build -a -b html docs docs/_build/
	@if [ $(OS_NAME) = "Darwin" ]; then say "The document generation is complete." ; fi
	make open OPEN_TARGET="./docs/_build/index.html"

deploy: ## 配備
	echo "TODO: Not Implemented Yet!"
	@if [ $(OS_NAME) = "Darwin" ]; then say "The deployment process is complete." ; fi

stop: ## 停止
	$(CMD_DOCKER_COMPOSE) stop

down: ## 削除
	$(CMD_DOCKER_COMPOSE) down --rmi all --remove-orphans

clean: down ## 掃除
	rm -rfv logs/*
	find . -type f -name "*.log" -prune -exec rm -rf {} +
	rm -rfv .mypy_cache
	rm -rfv .pytest_cache
	rm -rfv .coverage.*
	@if [ $(OS_NAME) = "Darwin" ]; then say "The cleanup process is complete." ; fi

prune: ## 破滅
	$(CMD_DOCKER) system prune --all --force --volumes
	@if [ $(OS_NAME) = "Darwin" ]; then say "The pruning process is complete." ; fi

help: ## 助言
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
