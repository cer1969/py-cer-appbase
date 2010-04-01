# -*- coding: utf-8 -*-
# CRISTIAN ECHEVERRÍA RABÍ 

from cer.application import Application, AppIni
import wx
import rxfile

#-----------------------------------------------------------------------------------------

name = "AppBase"
version = "0.1.0"
copyright = u"Cristian Echeverría"

#-----------------------------------------------------------------------------------------
# Application

app = Application(name, version, copyright)
app.register("cerapp")
app.resman = rxfile.resman

#-----------------------------------------------------------------------------------------
# User options

_x, _y, _w, _h = wx.GetClientDisplayRect()

ini = AppIni(app.toAppDir("data/%s.ini" % name))
ini.addSection("app")
ini.addInt("app.width",  900, vmin=600, vmax=_w)
ini.addInt("app.height", 700, vmin=400, vmax=_h)
ini.load(create=True)

app.ini = ini