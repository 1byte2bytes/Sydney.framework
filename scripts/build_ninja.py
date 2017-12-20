# Copyright (c) Sydney Erickson 2017
import os

import buildlib
import buildsettings

os.chdir(buildsettings.buildbase + "/pkg-src")

buildlib.execute_shell("tar -xvf ninja-1.8.2.tar.gz")
os.chdir("ninja-1.8.2")	
buildlib.execute_shell("./configure.py --bootstrap")
buildlib.execute_shell("mv ./ninja {}/bin".format(buildsettings.builddir))