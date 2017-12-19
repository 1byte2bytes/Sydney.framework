# Copyright (c) Sydney Erickson 2017
import buildlib
import buildsettings

buildlib.build_cmake("swift-swift-4.0.3-RELEASE.tar.gz", "-DCMAKE_BUILD_TYPE=Release")