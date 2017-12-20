# Copyright (c) Sydney Erickson 2017
import os

import buildlib
import buildsettings

os.chdir(buildsettings.buildbase + "/pkg-src")

buildlib.execute_shell("tar -xvf mercurial-4.4.2.tar.gz")
os.chdir("mercurial-4.4.2")	
buildlib.execute_shell("make local")
buildlib.execute_shell("mv ./hg {}/bin".format(buildsettings.builddir))