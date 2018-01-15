# Copyright (c) Sydney Erickson 2017
import buildlib
import buildsettings

import build_autoconf
import build_gmp
import build_mpfr

buildlib.build_configure("mpc-1.1.0.tar.gz", "--with-gmp={} --with-mpfr={}".format(buildsettings.builddir, buildsettings.builddir))