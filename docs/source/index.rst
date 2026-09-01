Generate EFI application configuration/build setup
----------------------------------------------------

**gen_efi_app** is toolset for generation of EFI application configuration/build setup.

Developed in `python <https://www.python.org/>`_ code.

The README is used to introduce the tool and provide instructions on
how to install the tool, any machine dependencies it may have and any
other information that should be provided before the tool is installed.

|gen_efi_app python checker| |gen_efi_app python package| |gen_efi_app interface checker| |gen_efi_app isp checker| |gen_efi_app srp checker| |github issues| |documentation status| |github contributors|

.. |gen_efi_app python checker| image:: https://github.com/electux/gen_efi_app/actions/workflows/gen_efi_app_python_checker.yml/badge.svg
   :target: https://github.com/electux/gen_efi_app/actions/workflows/gen_efi_app_python_checker.yml

.. |gen_efi_app python package| image:: https://github.com/electux/gen_efi_app/actions/workflows/gen_efi_app_package_checker.yml/badge.svg
   :target: https://github.com/electux/gen_efi_app/actions/workflows/gen_efi_app_package.yml

.. |gen_efi_app interface checker| image:: https://github.com/electux/gen_efi_app/actions/workflows/gen_efi_app_interface_checker.yml/badge.svg
   :target: https://github.com/electux/gen_efi_app/actions/workflows/gen_efi_app_interface_checker.yml

.. |gen_efi_app isp checker| image:: https://github.com/electux/gen_efi_app/actions/workflows/gen_efi_app_isp_checker.yml/badge.svg
   :target: https://github.com/electux/gen_efi_app/actions/workflows/gen_efi_app_isp_checker.yml

.. |gen_efi_app srp checker| image:: https://github.com/electux/gen_efi_app/actions/workflows/gen_efi_app_srp_checker.yml/badge.svg
   :target: https://github.com/electux/gen_efi_app/actions/workflows/gen_efi_app_srp_checker.yml

.. |github issues| image:: https://img.shields.io/github/issues/electux/gen_efi_app.svg
   :target: https://github.com/electux/gen_efi_app/issues

.. |github contributors| image:: https://img.shields.io/github/contributors/electux/gen_efi_app.svg
   :target: https://github.com/electux/gen_efi_app/graphs/contributors

.. |documentation status| image:: https://readthedocs.org/projects/gen-efi-app/badge/?version=latest
   :target: https://gen-efi-app.readthedocs.io/en/latest/?badge=latest

.. toctree::
   :maxdepth: 4
   :caption: Contents

   self
   modules

🚀 Installation
---------------

|gen_efi_app python3 build|

.. |gen_efi_app python3 build| image:: https://github.com/electux/gen_efi_app/actions/workflows/gen_efi_app_python3_build.yml/badge.svg
   :target: https://github.com/electux/gen_efi_app/actions/workflows/gen_efi_app_python3_build.yml

Navigate to release `page`_ download and extract release archive.

.. _page: https://github.com/electux/gen_efi_app/releases

To install **gen_efi_app** type the following

.. code-block:: bash

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

You can use Docker to create image/container, or You can use pip to install

.. code-block:: bash

    # pyton3
    pip3 install gen_efi_app

📦 Dependencies
---------------

**gen_efi_app** requires next modules and libraries

* `ats-utilities - Python App/Tool/Script Utilities <https://pypi.org/project/ats-utilities/>`_

📁 Tool structure
-----------------

**gen_efi_app** is based on OOP.

Tool structure

.. code-block:: bash

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

✨ Features
-----------

* Automatically scaffolds EFI application projects with proper configuration and build setups.
* Provides a modular and extensible architecture based on OOP and SOLID principles.
* Includes command line interface (CLI) support via a command/executor structure.
* Robust validation of project bundles, dependencies, and options.
* Comes with configurable templates and JSON schema definitions.
* High code quality with full type checking.

📊 Code coverage
----------------

.. csv-table:: Code coverage
   :file: coverage_table.csv
   :widths: 60, 10, 10, 20
   :header-rows: 1

🛠 Usage
--------

Install package

.. code-block:: bash

    pip3 install gen_efi_app

Prepare main entry point by downloading `main.py` or create your own.

.. code-block:: bash

    wget -O main.py https://raw.githubusercontent.com/electux/gen_efi_app/main/main.py

Running tool for creating new EFI application project

.. code-block:: bash

    python3 main.py create --name mytool --output ./demo/

📚 Docs
-------

More documentation and info at

* `gen-efi-app.readthedocs.io <https://gen-efi-app.readthedocs.io>`_
* `www.python.org <https://www.python.org/>`_

👥 Contributing
---------------

`Contributing to gen_efi_app <https://github.com/electux/gen_efi_app/blob/dev/CONTRIBUTING.md>`_

📄 Copyright and licence
-------------------------

Copyright (C) 2020 - 2026 by `electux.github.io/gen_efi_app <https://electux.github.io/gen_efi_app>`_

**gen_efi_app** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.
