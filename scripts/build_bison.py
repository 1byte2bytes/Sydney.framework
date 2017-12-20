# Copyright (c) Sydney Erickson 2017
import buildlib
import buildsettings

# THIS IS USING MY BRANCH BECAUSE HIGH SIERRA NEEDS A PATCH THAT ISN'T IN A RELEASE BINARY YET.
# BISON 3.0.5 (WHENEVER THAT COMES OUT) SHOULD CONTAIN THE FIX AND WE CAN REVERT TO RELEASE.

buildlib.build_configure("bison-3.0.4.tar.gz", "")