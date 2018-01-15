# Copyright (c) Sydney Erickson 2017
import buildlib
import buildsettings

import build_autoconf
import build_gmp

buildlib.build_configure("mpfr-4.0.0.tar.gz", "--with-gmp={}".format(buildsettings.builddir))