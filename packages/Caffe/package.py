

##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install caffe
#
# You can edit this file again by typing:
#
#     spack edit caffe
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *

class Caffe(CMakePackage):
    """The LArBy's version of Caffe. This should shadow the builtin version
    of Caffe and thus link against the LArCV-Caffe API.

    """

    homepage = "https://github.com/HEP-DL/caffe"
    url      = "https://github.com/HEP-DL/caffe/archive/pnnl1.0.0.tar.gz"

    version('pnnl1.0.0', '0824d897d36d3bb80f39b77d27d1be90')


    depends_on('larcv')
    depends_on('cmake')
    depends_on('opencv')
    depends_on('protobuf')
    depends_on('leveldb')
    depends_on('hdf5')
    depends_on('boost')
    depends_on('openblas')
    extends('python+shared+tk')
    depends_on('gflags')
    depends_on('glog')
    depends_on('lmdb')

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args