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
import subprocess
import os

class Larlite(MakefilePackage):
    """ Lightweight analysis framework for Liquid Argon TPCs"""
    homepage = "https://github.com/HEP-DL/larlite/"
    url      = "https://github.com/HEP-DL/larlite/archive/pnnl1.1.4.tar.gz"
    build_targets = []

    version('1.1.4', 'd260e7b45c6c2ccb20658e039374e34d')
    depends_on('root')
    extends('python+shared+tk')

    def edit(self, spec, prefix):

        with working_dir(self.build_directory):
            makefile = FileFilter('GNUmakefile')
            makefile.filter('LARLITE_BASEDIR')

            if '+mpi' in spec:
                makefile.filter('MPI .*', 'MPI := t')
            if '+debug' in spec:
                makefile.filter('NDEBUG.*', '#')
            if '+omp' in spec:
                makefile.filter('OMP.*', 'OMP := t')
            if '+prof' in spec:
                makefile.filter('PROF.*', 'PROF := t')


    def check(self):
      pass

    def installcheck(self):
      pass

    def _do_build_or_install(self):
      #larlite_env = os.environ.copy()
      os.environ['LARLITE_BASEDIR'] = self.build_directory
      os.environ['LARLITE_COREDIR'] = os.path.join(self.build_directory,'core')
      os.environ['LARLITE_USERDEVDIR'] = os.path.join(self.build_directory,'UserDev')

      with working_dir(self.build_directory):
        print(subprocess.check_output(['./config/setup.sh']))
      with working_dir(self.build_directory):
        make()

    def build(self,spec, prefix):
      self._do_build_or_install()

    def install(self, spec, prefix):
      subdirs=['UserDev','core','main','bin','doc','python','config','lib','ups']
      for subdir in subdirs:
        install_tree(subdir, join_path(prefix, subdir))

    def _setup_larlite_env(self, spack_env, run_env):
      print(self.prefix)
      spack_env.set('LARLITE_BASEDIR', self.prefix)
      run_env.set('LARLITE_BASEDIR', self.prefix)

    def setup_dependent_environment(self, spack_env, run_env, dspec):
      self._setup_larlite_env(spack_env, run_env)

    def setup_environment(self, spack_env, run_env):
      self._setup_larlite_env(spack_env, run_env)
