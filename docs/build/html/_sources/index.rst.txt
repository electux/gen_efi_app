Create EFI application
-----------------------

☯️ **gen_efi_app** is tool for creating EFI project skeleton.

Developed in 🐍 `python <https://www.python.org/>`_ code.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

|python package| |github issues| |documentation status| |github contributors|

.. |python package| image:: https://img.shields.io/github/workflow/status/electux/gen_efi_app/gen_efi_app_python_checker?style=flat&label=gen_efi_app%20python%20checker
   :target: https://img.shields.io/github/workflow/status/electux/gen_efi_app/gen_efi_app_python_checker

.. |github issues| image:: https://img.shields.io/github/issues/electux/gen_efi_app.svg
   :target: https://github.com/electux/gen_efi_app/issues

.. |github contributors| image:: https://img.shields.io/github/contributors/electux/gen_efi_app.svg
   :target: https://github.com/electux/gen_efi_app/graphs/contributors

.. |documentation status| image:: https://readthedocs.org/projects/gen_efi_app/badge/?version=latest
   :target: https://gen_efi_app.readthedocs.io/projects/gen_efi_app/en/latest/?badge=latest

.. toctree::
   :maxdepth: 4
   :caption: Contents

   self
   modules

Installation
-------------

|install python2 package| |install python3 package|

.. |install python2 package| image:: https://img.shields.io/github/workflow/status/electux/gen_efi_app/gen_efi_app_python2_build?style=flat&label=gen_efi_app%20python2%20build
   :target: https://img.shields.io/github/workflow/status/electux/gen_efi_app/gen_efi_app_python2_build

.. |install python3 package| image:: https://img.shields.io/github/workflow/status/electux/gen_efi_app/gen_efi_app_python3_build?style=flat&label=gen_efi_app%20python3%20build
   :target: https://img.shields.io/github/workflow/status/electux/gen_efi_app/gen_efi_app_python3_build

Navigate to release `page`_ download and extract release archive 📦.

.. _page: https://github.com/electux/gen_efi_app/releases

To install **gen_efi_app** 📦 type the following

.. code-block:: bash

    tar xvzf gen_efi_app-x.y.z.tar.gz
    cd gen_efi_app-x.y.z
    #python2
    pip install -r requirements.txt
    python setup.py install_lib
    python setup.py install_egg_info
    python setup.py install_data
    #python3
    pip3 install -r requirements.txt
    python3 setup.py install_lib
    python3 setup.py install_egg_info
    python3 setup.py install_data

You can use Docker to create image/container, or You can use pip to install 📦

.. code-block:: bash

    #python2
    pip install gen_efi_app
    #python3
    pip3 install gen_efi_app

|github docker checker|

.. |github docker checker| image:: https://img.shields.io/github/workflow/status/electux/gen_efi_app/gen_efi_app_docker_checker?style=flat&label=gen_efi_app%20docker%20checker
   :target: https://img.shields.io/github/workflow/status/electux/gen_efi_app/gen_efi_app_docker_checker

Dependencies
-------------

**gen_efi_app** requires next modules and libraries

* `ats-utilities - Python App/Tool/Script Utilities <https://pypi.org/project/ats-utilities/>`_

Tool structure
------------------

**gen_efi_app** is based on OOP

🧰 Code structure

.. code-block:: bash

    gen_efi_app/
    ├── conf/
    │   ├── gen_efi_app.cfg
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
    │   ├── config/
    │   │   ├── __init__.py
    │   │   ├── pro_name.py
    │   │   └── template_dir.py
    │   ├── __init__.py
    │   ├── read_template.py
    │   └── write_template.py
    └── run/
        └── gen_efi_app_run.py

Copyright and licence
----------------------

|license: gpl v3| |license: apache 2.0|

.. |license: gpl v3| image:: https://img.shields.io/badge/license-gplv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. |license: apache 2.0| image:: https://img.shields.io/badge/License-Apache%202.0-blue.svg
   :target: https://opensource.org/licenses/Apache-2.0

Copyright (C) 2020 by `electux.github.io/gen_efi_app <https://electux.github.io/gen_efi_app>`_

**gen_efi_app** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.x/3.x or,
at your option, any later version of Python 3 you may have available.

🌎 🌍 🌏 Lets help and support PSF.

|python software foundation|

.. |python software foundation| image:: https://raw.githubusercontent.com/electux/gen_efi_app/dev/docs/psf-logo-alpha.png
   :target: https://www.python.org/psf/

|donate|

.. |donate| image:: https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif
   :target: https://psfmember.org/index.php?q=civicrm/contribute/transact&reset=1&id=2

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
