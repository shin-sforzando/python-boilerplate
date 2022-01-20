# broad-boilerplate

<!-- Badges -->
[![Last Commit](https://img.shields.io/github/last-commit/shin-sforzando/broad-boilerplate)](https://github.com/shin-sforzando/broad-boilerplate/graphs/commit-activity)
[![CI](https://github.com/shin-sforzando/broad-boilerplate/actions/workflows/ci.yml/badge.svg)](https://github.com/shin-sforzando/broad-boilerplate/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/shin-sforzando/broad-boilerplate/branch/main/graph/badge.svg?token=TDCVLUJ4RF)](https://codecov.io/gh/shin-sforzando/broad-boilerplate)
[![GitHub Pages](https://github.com/shin-sforzando/broad-boilerplate/actions/workflows/pages.yml/badge.svg)](https://shin-sforzando.github.io/broad-boilerplate/)
[![Commitizen friendly](https://img.shields.io/badge/commitizen-friendly-brightgreen.svg)](http://commitizen.github.io/cz-cli/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

<!-- Screenshots -->
|![Screenshot 1](https://placehold.jp/32/3d4070/ffffff/720x480.png?text=Screenshot%201)|![Screenshot 2](https://placehold.jp/32/703d40/ffffff/720x480.png?text=Screenshot%202)|
|:---:|:---:|
|Screenshot 1|Screenshot 2|

<!-- Synopsis -->
**broad-boilerplate** is a template repository for using Docker & Python.

See. [API Document](https://shin-sforzando.github.io/broad-boilerplate/)

<!-- TOC -->
- [Prerequisites](#prerequisites)
- [How to](#how-to)
  - [Use this template](#use-this-template)
  - [Initialize](#initialize)
  - [Develop](#develop)
    - [Start](#start)
    - [Format](#format)
    - [Lint](#lint)
    - [Test](#test)
  - [Document](#document)
    - [API Document](#api-document)
    - [CHANGELOG](#changelog)
  - [Deploy](#deploy)
- [Misc](#misc)
- [Notes](#notes)
  - [LICENSE](#license)
  - [Contributors](#contributors)

## Prerequisites

- [Lefthook](https://github.com/evilmartians/lefthook) as *Git Hooks Manager*
- [Docker](https://www.docker.com) as *Environment Isolator*
  - [Python](https://www.python.org) (Version 3.10 or higher)
    - [black](https://github.com/psf/black) as *Formatter*
      - [blacken-docs](https://github.com/asottile/blacken-docs)
    - [flake8](https://pypi.org/project/flake8/) as *Linter*
    - [pdoc](https://github.com/mitmproxy/pdoc) as *Document Generator*
    - [loguru](https://github.com/Delgan/loguru) as *Logger*

## How to

```shell
$ make help
init                 初回
ps                   状況
build                構築
up                   起動
renew                転生
shell                接続
logs                 記録
follow               追跡
open                 閲覧
hide                 秘匿
reveal               暴露
start                開始
format               整形
lint                 検証
test                 試験
doc                  文書
deploy               配備
stop                 停止
down                 削除
clean                掃除
prune                破滅
help                 助言
```

### Use this template

- [ ] Replace the string `shin-sforzando` with the actual project owner
- [ ] Replace the string `broad-boilerplate` with the actual project name
- [ ] `lefthook install` to install git hooks
- [ ] Check the [repository secrets](https://github.com/shin-sforzando/broad-boilerplate/settings/secrets/actions)
  - [ ] `git secret remove dev@sforzando.co.jp\(FF810D98\).asc` to delete it
  - [ ] Set `CODECOV_TOKEN` if it's private
- [ ] Prepare [GitHub Pages](https://github.com/shin-sforzando/broad-boilerplate/settings/pages)
- [ ] Integrate with Slack: `/github subscribe shin-sforzando/broad-boilerplate reviews comments branches commits:*`
- [ ] **Delete this section!**

### Initialize

```shell
make init
```

### Develop

Commands that are often used during development should be prepared in `default`.

```shell
make
```

#### Start

```shell
make start
```

#### Format

```shell
make format
```

#### Lint

```shell
make lint
```

#### Test

```shell
make test
```

### Document

#### API Document

When the main branch is updated, `pages.yml` will update the [API Document](https://shin-sforzando.github.io/broad-boilerplate/).

If you want to generate the documentation manually,

```shell
make doc
```

#### CHANGELOG

Use [git-cliff](https://github.com/orhun/git-cliff) like,

```shell
git cliff --output CHANGELOG.md
```

### Deploy

```shell
make deploy
```

## Misc

## Notes

This repository is [Commitizen](https://commitizen.github.io/cz-cli/) friendly.

### LICENSE

See [LICENSE](LICENSE).

### Contributors

- [sforzando LLC. and Inc.](https://sforzando.co.jp/)
  - [Shin'ichiro Suzuki](https://github.com/shin-sforzando)
