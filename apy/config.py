# -*- coding: utf-8 -*-
# CRISTIAN ECHEVERRÍA RABÍ 

from cer.application import AppInfo, AppIni
import wx
import rxfile

#-----------------------------------------------------------------------------------------

name = "AppBase"
version = "0.1.0"

#-----------------------------------------------------------------------------------------

# User options
_x, _y, _w, _h = wx.GetClientDisplayRect()
ini = AppIni(cerapp.toAppDir("data/%s.ini" % name))
ini.add_section("app")
ini.add_int("app.width",  900, vmin=600, vmax=_w)
ini.add_int("app.height", 700, vmin=400, vmax=_h)
ini.load(create=True)

# Application information
info = AppInfo(name, version)

#-----------------------------------------------------------------------------------------

cerapp.ini = ini
cerapp.info = info
cerapp.resman = rxfile.resman