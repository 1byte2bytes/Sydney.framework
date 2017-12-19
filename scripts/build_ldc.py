# Copyright (c) Sydney Erickson 2017
import buildlib
import buildsettings

buildlib.build_cmake("ldc-1.6.0-src.tar.gz", "-DCMAKE_BUILD_TYPE=Release")