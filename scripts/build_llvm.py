# Copyright (c) Sydney Erickson 2017
import buildlib
import buildsettings

import build_cmake

buildlib.build_cmake("llvm-5.0.0.src.tar.bz2", "-DCMAKE_BUILD_TYPE=Release -DLLVM_TARGETS_TO_BUILD=X86")