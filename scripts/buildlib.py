# Copyright (c) Sydney Erickson 2017
# This script contains the base build functions

from __future__ import print_function

import os
import subprocess

import buildsettings

def execute_shell(command):
	print("[EXECUTION] " + command)
	p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	retval = p.wait()
	if retval != 0:
		for line in p.stdout.readlines():
			print(line.decode("utf-8"), end='')
		exit(-1)

def build_configure(archive_name, configure_extra_args, custom_prefix=None):
	os.chdir(buildsettings.buildbase + "/pkg-src")
	project_name = archive_name.rsplit(".", 2)[0]
	if os.path.isdir(project_name) == True:
		return

	execute_shell("tar -xvf " + archive_name)
	os.chdir(project_name)
	execute_shell("./configure --prefix={} {}".format(buildsettings.builddir, configure_extra_args))
	execute_shell("make -j$(sysctl -n hw.ncpu)")
	execute_shell("make install")

def build_cmake(archive_name, configure_extra_args, custom_prefix=None):
	os.chdir(buildsettings.buildbase + "/pkg-src")
	project_name = archive_name.rsplit(".", 2)[0]
	if os.path.isdir(project_name) == True:
		return

	execute_shell("tar -xvf " + archive_name)
	os.chdir(project_name)
	execute_shell("mkdir build")
	os.chdir("build")
	execute_shell("cmake -G \"Unix Makefiles\" -DCMAKE_INSTALL_PREFIX:PATH=/{} ../".format(buildsettings.builddir))
	execute_shell("make  -j$(sysctl -n hw.ncpu)")
	execute_shell("make install")