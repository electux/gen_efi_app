# Create EFI application

<img align="right" src="https://raw.githubusercontent.com/electux/gen_efi_app/dev/docs/gen_efi_app_logo.png" width="25%">

**gen_efi_app** is tool for creating EFI project skeleton.

Developed in **[python](https://www.python.org/)** code.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

[![gen_efi_app python checker](https://github.com/electux/gen_efi_app/actions/workflows/gen_efi_app_python_checker.yml/badge.svg)](https://github.com/electux/gen_efi_app/actions/workflows/gen_efi_app_python_checker.yml) [![gen_efi_app package checker](https://github.com/electux/gen_efi_app/actions/workflows/gen_efi_app_package_checker.yml/badge.svg)](https://github.com/electux/gen_efi_app/actions/workflows/gen_efi_app_package.yml) [![gen_efi_app interface checker](https://github.com/electux/gen_efi_app/actions/workflows/gen_efi_app_interface_checker.yml/badge.svg)](https://github.com/electux/gen_efi_app/actions/workflows/gen_efi_app_interface_checker.yml) [![gen_efi_app isp checker](https://github.com/electux/gen_efi_app/actions/workflows/gen_efi_app_isp_checker.yml/badge.svg)](https://github.com/electux/gen_efi_app/actions/workflows/gen_efi_app_isp_checker.yml) [![gen_efi_app srp checker](https://github.com/electux/gen_efi_app/actions/workflows/gen_efi_app_srp_checker.yml/badge.svg)](https://github.com/electux/gen_efi_app/actions/workflows/gen_efi_app_srp_checker.yml) [![GitHub issues open](https://img.shields.io/github/issues/electux/gen_efi_app.svg)](https://github.com/electux/gen_efi_app/issues) [![GitHub contributors](https://img.shields.io/github/contributors/electux/gen_efi_app.svg)](https://github.com/electux/gen_efi_app/graphs/contributors)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [🚀 Installation](#-installation)
    - [Install using pip](#install-using-pip)
    - [Install using build](#install-using-build)
    - [Install using py setup](#install-using-py-setup)
    - [Install using docker](#install-using-docker)
- [📦 Dependencies](#-dependencies)
- [📁 Tool structure](#-tool-structure)
  - [✨ Features](#-features)
- [📊 Code coverage](#-code-coverage)
- [🛠 Usage](#-usage)
- [📚 Docs](#-docs)
- [👥 Contributing](#-contributing)
- [📄 Copyright and licence](#-copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### 🚀 Installation

Used next development environment

![debian linux os](https://raw.githubusercontent.com/electux/gen_efi_app/dev/docs/debtux.png)

[![gen_efi_app python3 build](https://github.com/electux/gen_efi_app/actions/workflows/gen_efi_app_python3_build.yml/badge.svg)](https://github.com/electux/gen_efi_app/actions/workflows/gen_efi_app_python3_build.yml)

Currently there are three ways to install package
* Install process based on using pip mechanism
* Install process based on build mechanism
* Install process based on setup.py mechanism
* Install process based on docker mechanism

##### Install using pip

**gen_efi_app** is located at **[pypi.org](https://pypi.org/project/gen_efi_app/)**.

You can install by using pip

```bash
# python3
pip3 install gen_efi_app
```

##### Install using build

Navigate to release **[page](https://github.com/electux/gen_efi_app/releases/)** download and extract release archive.

To install **gen_efi_app** type the following

```bash
tar xvzf gen_efi_app-x.y.z.tar.gz
cd gen_efi_app-x.y.z/
# python3
wget https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py 
python3 -m pip install --upgrade setuptools
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade build
pip3 install -r requirements.txt
python3 -m build --no-isolation --wheel
pip3 install ./dist/gen_efi_app-*-py3-none-any.whl
rm -f get-pip.py
chmod 755 /usr/local/lib/python3.10/dist-packages/usr/local/bin/gen_efi_app_run.py
ln -s /usr/local/lib/python3.10/dist-packages/usr/local/bin/gen_efi_app_run.py /usr/local/bin/gen_efi_app_run.py
```

##### Install using py setup

Navigate to **[release page](https://github.com/electux/gen_efi_app/releases)** download and extract release archive.

To install **gen_efi_app** locate and run setup.py with arguments

```bash
tar xvzf gen_efi_app-x.y.z.tar.gz
cd gen_efi_app-x.y.z
# python3
pip3 install -r requirements.txt
python3 setup.py install_lib
python3 setup.py install_egg_info
```

##### Install using docker

You can use Dockerfile to create image/container.

### 📦 Dependencies

**gen_efi_app** requires next modules and libraries

* [ats-utilities - Python App/Tool/Script Utilities](https://pypi.org/project/ats-utilities/)

### 📁 Tool structure

**gen_efi_app** is based on OOP.

Tool structure

<details>
<summary><b>Click to expand framework structure</b></summary>

```bash
    gen_efi_app/
         ├── core/
         │   ├── __init__.py
         │   ├── model/
         │   │   ├── __init__.py
         │   │   └── project_setup.py
         │   └── service/
         │       ├── engine.py
         │       ├── __init__.py
         │       ├── iservice.py
         │       └── isubprocessor.py
         ├── engine.py
         ├── infrastructure/
         │   ├── cli/
         │   │   ├── engine.py
         │   │   ├── icli.py
         │   │   ├── __init__.py
         │   │   └── setup/
         │   │       ├── bundle.py
         │   │       ├── dep_validator.py
         │   │       ├── dependencies.py
         │   │       ├── factory.py
         │   │       ├── __init__.py
         │   │       ├── keys.py
         │   │       ├── opt_validator.py
         │   │       ├── options.py
         │   │       ├── registry.py
         │   │       └── validator.py
         │   ├── command/
         │   │   ├── command.py
         │   │   ├── gen_efi_command_definition.py
         │   │   ├── gen_efi_command_executor.py
         │   │   ├── icommand_definition.py
         │   │   ├── icommand_executor.py
         │   │   └── __init__.py
         │   ├── config/
         │   │   ├── gen_efi_app.cfg
         │   │   ├── gen_efi_app.logo
         │   │   ├── scheme.json
         │   │   └── templates.tgz
         │   ├── __init__.py
         │   └── subprocessor.py
         ├── __init__.py
         ├── py.typed
         └── setup/
             ├── bundle.py
             ├── dep_validator.py
             ├── dependencies.py
             ├── factory.py
             ├── __init__.py
             ├── keys.py
             ├── opt_validator.py
             ├── options.py
             ├── registry.py
             └── validator.py

     10 directories, 45 files
```
</details>

#### ✨ Features

* Automatically scaffolds EFI application projects with proper configuration and build setups.
* Provides a modular and extensible architecture based on OOP and SOLID principles.
* Includes command line interface (CLI) support via a command/executor structure.
* Robust validation of project bundles, dependencies, and options.
* Comes with configurable templates and JSON schema definitions.
* High code quality with full type checking.

### 📊 Code coverage

<details>
<summary><b>Click to expand code coverage</b></summary>

| Name | Stmts | Miss | Cover |
|------|-------|------|-------|
| `gen_efi_app/__init__.py` | 9 | 0 | 100%|
| `gen_efi_app/core/__init__.py` | 9 | 0 | 100%|
| `gen_efi_app/core/model/__init__.py` | 9 | 0 | 100%|
| `gen_efi_app/core/model/project_setup.py` | 14 | 0 | 100%|
| `gen_efi_app/core/service/__init__.py` | 9 | 0 | 100%|
| `gen_efi_app/core/service/engine.py` | 27 | 0 | 100%|
| `gen_efi_app/core/service/iservice.py` | 14 | 0 | 100%|
| `gen_efi_app/core/service/isubprocessor.py` | 14 | 0 | 100%|
| `gen_efi_app/engine.py` | 57 | 0 | 100%|
| `gen_efi_app/infrastructure/__init__.py` | 9 | 0 | 100%|
| `gen_efi_app/infrastructure/cli/__init__.py` | 9 | 0 | 100%|
| `gen_efi_app/infrastructure/cli/engine.py` | 39 | 0 | 100%|
| `gen_efi_app/infrastructure/cli/icli.py` | 15 | 0 | 100%|
| `gen_efi_app/infrastructure/cli/setup/__init__.py` | 9 | 0 | 100%|
| `gen_efi_app/infrastructure/cli/setup/bundle.py` | 22 | 0 | 100%|
| `gen_efi_app/infrastructure/cli/setup/dep_validator.py` | 36 | 0 | 100%|
| `gen_efi_app/infrastructure/cli/setup/dependencies.py` | 18 | 0 | 100%|
| `gen_efi_app/infrastructure/cli/setup/factory.py` | 35 | 0 | 100%|
| `gen_efi_app/infrastructure/cli/setup/keys.py` | 26 | 0 | 100%|
| `gen_efi_app/infrastructure/cli/setup/opt_validator.py` | 36 | 0 | 100%|
| `gen_efi_app/infrastructure/cli/setup/options.py` | 15 | 0 | 100%|
| `gen_efi_app/infrastructure/cli/setup/registry.py` | 24 | 0 | 100%|
| `gen_efi_app/infrastructure/cli/setup/validator.py` | 43 | 0 | 100%|
| `gen_efi_app/infrastructure/command/__init__.py` | 9 | 0 | 100%|
| `gen_efi_app/infrastructure/command/command.py` | 16 | 0 | 100%|
| `gen_efi_app/infrastructure/command/gen_efi_command_definition.py` | 24 | 0 | 100%|
| `gen_efi_app/infrastructure/command/gen_efi_command_executor.py` | 23 | 0 | 100%|
| `gen_efi_app/infrastructure/command/icommand_definition.py` | 14 | 0 | 100%|
| `gen_efi_app/infrastructure/command/icommand_executor.py` | 14 | 0 | 100%|
| `gen_efi_app/infrastructure/subprocessor.py` | 55 | 0 | 100%|
| `gen_efi_app/setup/__init__.py` | 9 | 0 | 100%|
| `gen_efi_app/setup/bundle.py` | 23 | 0 | 100%|
| `gen_efi_app/setup/dep_validator.py` | 36 | 0 | 100%|
| `gen_efi_app/setup/dependencies.py` | 19 | 0 | 100%|
| `gen_efi_app/setup/factory.py` | 48 | 0 | 100%|
| `gen_efi_app/setup/keys.py` | 27 | 0 | 100%|
| `gen_efi_app/setup/opt_validator.py` | 34 | 0 | 100%|
| `gen_efi_app/setup/options.py` | 12 | 0 | 100%|
| `gen_efi_app/setup/registry.py` | 32 | 0 | 100%|
| `gen_efi_app/setup/validator.py` | 48 | 0 | 100%|
| **Total** | 941 | 0 | 100% |

</details>

### 🛠 Usage

Install package

```bash
pip3 install gen_efi_app
```

Prepare main entry point by downloading [main.py](https://raw.githubusercontent.com/electux/gen_efi_app/main/main.py) or create your own.


```bash
wget -O main.py https://raw.githubusercontent.com/electux/gen_efi_app/main/main.py
```

Running tool for creating new EFI application project

```bash
python3 main.py create --name mytool --output ./demo/
```

### 📚 Docs

[![Documentation Status](https://readthedocs.org/projects/gen-efi-app/badge/?version=latest)](https://gen-efi-app.readthedocs.io/en/latest/?badge=latest)

More documentation and info at

* [gen-efi-app.readthedocs.io](https://gen-efi-app.readthedocs.io)
* [www.python.org](https://www.python.org/)

### 👥 Contributing

[Contributing to gen_efi_app](CONTRIBUTING.md)

### 📄 Copyright and licence

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2020 - 2026 by [electux.github.io/gen_efi_app](https://electux.github.io/gen_efi_app)

**gen_efi_app** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/electux/gen_efi_app/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.python.org/psf/donations/)
