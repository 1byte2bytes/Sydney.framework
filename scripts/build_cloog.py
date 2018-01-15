# Copyright (c) Sydney Erickson 2017
import buildlib
import buildsettings

import build_autoconf
import build_gmp
import build_isl

buildlib.build_configure("cloog-0.18.4.tar.gz", "--with-gmp-prefix={} --with-isl-prefix={}".format(buildsettings.builddir, buildsettings.builddir))