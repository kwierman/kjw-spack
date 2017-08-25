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
from spack import *
import os
import fnmatch
import subprocess


class Larcv(MakefilePackage):
    """Computer vision framework for data from Liquid Argon TPCs.
    """

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/HEP-DL/LArCV/"
    url      = "https://github.com/HEP-DL/LArCV/archive/pnnl1.1.2.tar.gz"

    version('1.1.2', 'fef3293a1f3dc20401c2108bff9b8937')
    depends_on('root')
    extends('python+shared+tk')

    def edit(self, spec, prefix):

      for root, dirnames, filenames in os.walk('.'):
          for filename in fnmatch.filter(filenames, 'GNUmakefile'):
            makefile = os.path.join(root, filename)
            with working_dir(self.build_directory):
                print("Editing: {}".format(makefile))
                makefile = FileFilter(makefile.strip())
                makefile.filter('\$\{LARCV_BASEDIR\}',
                                self.build_directory)
                makefile.filter('\$\(LARCV_APPDIR\)',
                                os.path.join(self.build_directory, 'app'))
                makefile.filter('\$\(LARCV_COREDIR\)',
                                os.path.join(self.build_directory, 'core'))
                makefile.filter('\$\(LARCV_BUILDDIR\)',
                                os.path.join(self.build_directory, 'build'))
                makefile.filter('\$\(LARCV_LIBDIR\)',
                                os.path.join(self.build_directory, 'lib'))
                makefile.filter('\$\(LARCV_BINDIR\)',
                                os.path.join(self.build_directory, 'bin'))
      with working_dir(self.build_directory):
          makefile = FileFilter('Makefile/GNUmakefile.CORE')
          makefile.filter('\$\{LARCV_BASEDIR\}',
                          self.build_directory)
          makefile.filter('\$\(LARCV_APPDIR\)',
                          os.path.join(self.build_directory, 'app'))
          makefile.filter('\$\(LARCV_COREDIR\)',
                          os.path.join(self.build_directory, 'core'))
          makefile.filter('\$\(LARCV_BUILDDIR\)',
                          os.path.join(self.build_directory, 'build'))
          makefile.filter('\$\(LARCV_LIBDIR\)',
                          os.path.join(self.build_directory, 'lib'))
          makefile.filter('\$\(LARCV_BINDIR\)',
                          os.path.join(self.build_directory, 'bin'))
          makefile.filter('\$\(LARCV_INCDIR\)',
                          os.path.join(self.build_directory, 'inc'))
          makefile.filter('rlibmap *',
                          'genreflex  -o $(LARCV_LIBDIR)/$(ROOTMAP) -l $(LARCV_LIBDIR)/liblarcv.so  LinkDef.h')

    def build(self, spec, prefix):
      os.environ['LARCV_BASEDIR'] = self.build_directory
      os.environ['LARCV_COREDIR'] = os.path.join(self.build_directory, 'core')
      os.environ['LARCV_CXX'] = 'g++'
      print(subprocess.check_output(['make','-d'], shell=True))
      #make()

    def install(self, spec, prefix):
      subdirs=['ROI', 'mac', 'app', 'core', 'production', 'bin', 'doc', 'python', 'build', 'example', 'ups']
      for subdir in subdirs:
        install_tree(subdir, join_path(prefix, subdir))

    def setup_dependent_environment(self, spack_env, run_env, dspec):
      print(spack_env, run_env, dspec)

    def setup_environment(self, spack_env, run_env):
      print(spack_env, run_env)
