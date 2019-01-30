---
layout: default
title: Source code
parent: Contributing code
nav_order: 1
permalink: /contributing-code/source-code/
---

# Source code

- TOC
{:toc}
---


## Directory structure

* **bot** - placeholder for bot specific artifacts (e.g. fuzzers, corpora).
* **configs** - sample project config, also used for tests.
* **coverage** - stores coverage data for tests.
* **deployment** - stores deployment artifacts such as source code archives.
* **docker** - sample docker images, tested on Google Cloud VMs.
* **docs** - this documentation.
* **local** - artifacts for local testing (e.g. install_deps.bash for ClusterFuzz deps).
* **resources** - helper binaries needed by bots (e.g. llvm-symbolizer).
* **src** - source code root.
  * **appengine** - App Engine specific files (Python 2).
    * **handlers** - backend code for various web pages.
    * **libs** - general helper libraries (e.g. access control).
    * **private** - components code for various web pages (Polymer 2).
    * **templates** - template code of various web pages (Polymer 2).
  * **go** - go code.
  * **python** - python 2 code.
    * **bot** - bot specific code.
    * **tests** - tests for core and App Engine code.
    * rest are *package* level directories.
  * **third_party** - third-party package dependencies.
  * **requirements.txt** - platform agnostic package list (Python 2).
  * **platform_requirements.txt** - platform dependent package list (Python 2).
* **bower.json** - component dependencies for Polymer 2.
* **butler.py** - helper script for various command line tasks (e.g. testing, deployment).