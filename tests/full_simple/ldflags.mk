# cflags.mk
# Copyright (C) 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
#
# full_simple is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# full_simple is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program_name. If not, see <http://www.gnu.org/licenses/>.

LIB = /usr/lib
EFI_LIB = /usr/lib
EFI_CRT_OBJS = /usr/lib/crt0-efi-x86_64.o
EFI_LDS = /usr/lib/elf_x86_64_efi.lds

LDFLAGS = \
	-nostdlib \
	-znocombreloc \
	-T $(EFI_LDS) \
	-shared \
	-Bsymbolic \
	-L $(EFI_LIB) \
	-L $(LIB) \
	$(EFI_CRT_OBJS)
