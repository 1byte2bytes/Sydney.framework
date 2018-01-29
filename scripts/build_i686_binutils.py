# Copyright (c) Sydney Erickson 2017
import buildlib
import buildsettings

import build_autoconf

buildlib.build_configure("binutils-2.30.tar.gz", "--with-sysroot --disable-nls --disable-werror --target=i686-elf")