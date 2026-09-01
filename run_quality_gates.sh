#!/bin/bash
#
# @brief   gen_efi_app
# @version 1.3.7
# @date    Sat Aug 07 07:35:10 2026
# @company None, free software to use 2026
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

python3 gates/gates/interfaces_checker.py gen_efi_app
python3 gates/gates/isp_checker.py gen_efi_app
python3 gates/gates/limits_checker.py gen_efi_app
python3 gates/gates/srp_checker.py gen_efi_app

echo "Done"
