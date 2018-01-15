# Copyright (c) Sydney Erickson 2017
import buildlib
import buildsettings

import build_autoconf
import build_gmp

buildlib.build_configure("isl-0.18.tar.gz", "--with-gmp-prefix={}".format(buildsettings.builddir))