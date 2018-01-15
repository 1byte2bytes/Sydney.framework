# Copyright (c) Sydney Erickson 2017
import buildlib
import buildsettings

import build_autoconf
import build_isl
import build_cloog
import build_gmp
import build_mpfr
import build_mpc

buildlib.build_configure("gcc-7.2.0.tar.gz", "--with-isl={} --with-cloog={} --with-gmp={} --with-mpfr={} --with-mpc={} --disable-nls --enable-languages=c,c++ --without-headers --target=i686-elf"
	.format(buildsettings.builddir, buildsettings.builddir, buildsettings.builddir, buildsettings.builddir, buildsettings.builddir))