###############################################################################
# The Institute for the Design of Advanced Energy Systems Integrated Platform
# Framework (IDAES IP) was produced under the DOE Institute for the
# Design of Advanced Energy Systems (IDAES), and is copyright (c) 2018-2021 by the
# software owners: The Regents of the University of California, through Lawrence
# Berkeley National Laboratory,  National Technology & Engineering Solutions of
# Sandia, LLC, Carnegie Mellon University, West Virginia University Research
# Corporation, et al.  All rights reserved.
#
# NOTICE.  This Software was developed under funding from the U.S. Department of
# Energy and the U.S. Government consequently retains certain rights. As such, the
# U.S. Government has been granted for itself and others acting on its behalf a
# paid-up, nonexclusive, irrevocable, worldwide license in the Software to
# reproduce, distribute copies to the public, prepare derivative works, and
# perform publicly and display publicly, and to permit other to do so.
#
###############################################################################
"""
IDAES Data Management Framework (DMF)

The DMF lets you save, search, and retrieve provenance related
to your models.
"""
__author__ = 'Dan Gunter'

import logging

from .dmfbase import DMF, DMFConfig           # noqa: F401
from .getver import get_version_info          # noqa: F401
from .userapi import get_workspace            # noqa: F401
from .userapi import find_property_packages   # noqa: F401
from .userapi import index_property_packages  # noqa: F401
from . import resource                        # noqa: F401
# DMF version is the same as IDAES version
from idaes import __version__                 # noqa


# default log format
h = logging.StreamHandler()
h.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] '
                                 '%(name)s: %(message)s'))
logging.getLogger('idaes.dmf').addHandler(h)
logging.getLogger('idaes.dmf').propagate = False
