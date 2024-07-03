# Create EFI application

<img align="right" src="https://github.com/electux/gen_efi_app/blob/dev/docs/gen_efi_app_logo.png" width="25%">

**gen_efi_app** is tool for creating EFI project skeleton.

Developed in **[python](https://www.python.org/)** code.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

[![gen_efi_app python checker](https://github.com/electux/gen_efi_app/actions/workflows/gen_efi_app_python_checker.yml/badge.svg)](https://github.com/electux/gen_efi_app/actions/workflows/gen_efi_app_python_checker.yml) [![gen_efi_app package checker](https://github.com/electux/gen_efi_app/actions/workflows/gen_efi_app_package_checker.yml/badge.svg)](https://github.com/electux/gen_efi_app/actions/workflows/gen_efi_app_package.yml) [![GitHub issues open](https://img.shields.io/github/issues/electux/gen_efi_app.svg)](https://github.com/electux/gen_efi_app/issues) [![GitHub contributors](https://img.shields.io/github/contributors/electux/gen_efi_app.svg)](https://github.com/electux/gen_efi_app/graphs/contributors)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [Installation](#installation)
    - [Install using pip](#install-using-pip)
    - [Install using build](#install-using-build)
    - [Install using py setup](#install-using-py-setup)
    - [Install using docker](#install-using-docker)
- [Dependencies](#dependencies)
- [Tool structure](#tool-structure)
- [Docs](#docs)
- [Contributing](#contributing)
- [Copyright and Licence](#copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### Installation

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
chmod 755 /usr/local/lib/python3.9/dist-packages/usr/local/bin/gen_efi_app_run.py
ln -s /usr/local/lib/python3.9/dist-packages/usr/local/bin/gen_efi_app_run.py /usr/local/bin/gen_efi_app_run.py
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

### Dependencies

**gen_efi_app** requires next modules and libraries

* [ats-utilities - Python App/Tool/Script Utilities](https://electux.github.io/ats-utilities)

### Tool structure

**gen_efi_app** is based on OOP

Generator structure

```bash
    gen_efi_app/
         ├── conf/
         │   ├── gen_efi_app.cfg
         │   ├── gen_efi_app.logo
         │   ├── gen_efi_app_util.cfg
         │   ├── project.yaml
         │   └── template/
         │       ├── cflags.template
         │       ├── ldflags.template
         │       ├── main.template
         │       ├── makefile.template
         │       ├── objects.template
         │       └── ocflags.template
         ├── __init__.py
         ├── log/
         │   └── gen_efi_app.log
         ├── pro/
         │   ├── __init__.py
         │   ├── read_template.py
         │   └── write_template.py
         ├── py.typed
         └── run/
             └── gen_efi_app_run.py
    
    6 directories, 17 files
```

### Docs

[![Documentation Status](https://readthedocs.org/projects/gen_efi_app/badge/?version=latest)](https://gen-efi-app.readthedocs.io/en/latest/?badge=latest)

More documentation and info at

* [gen_efi_app.readthedocs.io](https://gen-efi-app.readthedocs.io/en/latest/)
* [www.python.org](https://www.python.org/)

### Contributing

[Contributing to gen_efi_app](CONTRIBUTING.md)

### Copyright and Licence

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2020 - 2024 by [electux.github.io/gen_efi_app](https://electux.github.io/gen_efi_app/)

**gen_efi_app** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/electux/gen_efi_app/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.python.org/psf/donations/)
