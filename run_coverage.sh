#!/bin/bash
#
# @brief   gen_efi_app
# @version 1.3.7
# @date    Sat Aug 07 07:35:10 2026
# @company None, free software to use 2026
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

python3 coverage/ats_coverage.py gen_efi_app
pylint gen_efi_app > gen_efi_app.report
echo "Done"
