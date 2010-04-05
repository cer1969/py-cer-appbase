# -*- coding: utf-8 -*-
# CRISTIAN ECHEVERRÍA RABÍ 

import sys, glob, os
import cer.application.distribution as distro
from apy.config import app

#-----------------------------------------------------------------------------------------

# There's a problem with wxPython that prevent using 'bundle_files = 2'
bundle_files = 3

data_files = [
    #("data", glob.glob("data/*.*"))
    (".", glob.glob("*.ini"))
]

#-----------------------------------------------------------------------------------------
# Python 2.6 requirements

# Path to vc++ runtime redist manifest & dlls 
dlls26path = r"C:\Documents and Settings\cecheverria\Mis documentos\030_Devel\Lib\py26"
dlls26list =  glob.glob(os.path.join(dlls26path, "*.*"))


if sys.version_info[:2] >= (2,6):
    
    # Needed to find dlls
    sys.path.append(dlls26path)
    
    # The next line works too, but I think is safer on the root directory
    # data_files.append(("Microsoft.VC90.CRT", dlls26list))
    data_files.append((".", dlls26list))

#-----------------------------------------------------------------------------------------
# Py2exe options

options = distro.getOptions(
    compressed = 1,
    optimize = 2, 
    bundle_files = bundle_files,
    dll_excludes = ['w9xpopen.exe'],
)

#-----------------------------------------------------------------------------------------

distro.makeExe(
    #windows = [app],
    console = [app],
    data_files = data_files,
    options = options,
    #zipfile = "runtime.zip"
)