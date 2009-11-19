# -*- coding: utf-8 -*-
# CRISTIAN ECHEVERRÍA RABÍ 

import config   # requerido
import wx
from wx.lib import colourdb
from mainframe import MainFrame

#-----------------------------------------------------------------------------------------

def run(capture=False):
    """ Run the application.
        capture: True to capture stderr and stdout in special window
    """
    wxapp = wx.PySimpleApp(capture)
    colourdb.updateColourDB()
    wxapp.SetAssertMode(wx.PYAPP_ASSERT_EXCEPTION) #wx.PYAPP_ASSERT_DIALOG
    MainFrame().Show(True)
    wxapp.MainLoop()