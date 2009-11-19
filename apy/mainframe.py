# -*- coding: utf-8 -*-
# CRISTIAN ECHEVERRÍA RABÍ

from __future__ import division
import wx, os
import wx.lib.agw.flatnotebook as fnb

from cer.widgets import cw

#-----------------------------------------------------------------------------------------
# Menú y Toolbar

cmd = cw.CommandList()
cmd_open   = cmd.Item(u"Abrir...",       "OnOpen",        "cw_file_open")
cmd_save   = cmd.Item(u"Grabar",         "OnSave",        "cw_file_save")
cmd_saveas = cmd.Item(u"Grabar como...", "OnSaveAs",      "cw_file_save_as")
cmd_quit   = cmd.Item(u"Salir",          "OnCloseWindow", "cw_quit")
cmd_about  = cmd.Item(u"Acerda de...",   "OnAbout",       "cw_help", u"Acerca de Parábola")

# Menú
mbd = cw.MenuBar(
    cw.Menu(u"Archivo",  cmd_open, cmd_save, cmd_saveas, None, cmd_quit),
    cw.Menu(u"Ayuda",    cmd_about)
)

#-----------------------------------------------------------------------------------------

NB_STYLE = (fnb.FNB_VC8 | fnb.FNB_TABS_BORDER_SIMPLE | fnb.FNB_DROPDOWN_TABS_LIST |
             fnb.FNB_NO_X_BUTTON | fnb.FNB_X_ON_TAB | fnb.FNB_NO_NAV_BUTTONS)

class MainFrame(wx.Frame):
    def __init__(self):
        
        title = "%s %s" % (cerapp.info.name, cerapp.info.version)
        size = (cerapp.ini.app_width, cerapp.ini.app_height)
        
        wx.Frame.__init__(self, None, -1, title, size=size)
        
        self.SetMenuBar(mbd.Make())
        self.CreateStatusBar(2)
        self.SetIcon(cerapp.resman.Icon("taoEd_ico"))
        
        self.nb = fnb.FlatNotebook(self, wx.ID_ANY, style=NB_STYLE)
        
        self.Bind(fnb.EVT_FLATNOTEBOOK_PAGE_CHANGED, self.OnPageChanged, self.nb)
        self.Bind(fnb.EVT_FLATNOTEBOOK_PAGE_CLOSING, self.OnPageClosing, self.nb)
        self.Bind(fnb.EVT_FLATNOTEBOOK_PAGE_CLOSED,  self.OnPageClosed, self.nb)
        
        self.UpdateMenu()
        
        cmd.Bind(self)
        self.Bind(wx.EVT_CLOSE,self.OnCloseWindow)
        self.Center(wx.BOTH)
    
    def UpdateMenu(self):
        n = self.nb.GetPageCount()
        enable = True if n > 0 else False
        mb = self.GetMenuBar()
        mb.GetMenu(0).Enable(mbd[0][1].Id, enable)
        mb.GetMenu(0).Enable(mbd[0][2].Id, enable)
        
    def OnOpen(self,event=None):
        filename = wx.FileSelector(message="Abrir archivo...", default_path=os.getcwd(),
            wildcard="Pad file (*.zpk)|*.zpk", flags=wx.OPEN|wx.CHANGE_DIR, parent=self
        )
        if filename == "":
            return
        n = self.nb.GetPageCount()
        pages = (self.nb.GetPage(i) for i in range(n))
        files = (x.filename for x in pages)
        
        if filename in files:
            wx.MessageBox(u"El archivo ya está abierto", caption="Abrir Archivo", style=wx.OK)
            return
        
        try:
            page = Page(self.nb, filename)
            self.nb.AddPage(page, page.GetPageName(), True)
            self.UpdateMenu()
        except ValueError:
            wx.MessageBox(u"Formato de archivo incorrecto", caption="Abrir Archivo", style=wx.ICON_ERROR)
            return
    
    def OnSave(self,event=None):
        page = self.nb.GetPage(self.nb.GetSelection())
        page.Save()
    
    def OnSaveAs(self,event=None):
        filename = wx.FileSelector(message="Abrir archivo...", default_path=os.getcwd(),
            wildcard="Pad file (*.zpk)|*.zpk", flags=wx.SAVE|wx.CHANGE_DIR|wx.OVERWRITE_PROMPT,
            parent=self
        )
        if filename == "":
            return
        pos = self.nb.GetSelection()
        page = self.nb.GetPage(pos)
        page.Save(filename)
        self.nb.SetPageText(pos, page.GetPageName())
        self.UpdateTitle()
    
    def UpdateTitle(self):
        info = cerapp.info
        page = self.nb.GetPage(self.nb.GetSelection())
        title = "%s %s - %s" % (info.name, info.version, page.filename)
        self.SetTitle(title)
        
    def OnPageChanged(self, event):
        self.UpdateTitle()
        event.Skip()
    
    def OnPageClosing(self,event):
        page = self.nb.GetPage(event.GetSelection())
        page.BeforeClose()
        event.Skip()
    
    def OnPageClosed(self, event):
        n = self.nb.GetPageCount()
        if n == 0:
            title = "%s %s" % (cerapp.info.name, cerapp.info.version)
            self.SetTitle(title)
            self.UpdateMenu()
        event.Skip()

    
    #-------------------------------------------------------------------------------------
    # Generales
    
    def OnAbout(self, event):
        title    = "Acerca de %s" % cerapp.info.name
        bigText  = " %s - %s (R)" % (cerapp.info.name, cerapp.info.version)
        longText = (
            u'\n CRISTIAN ECHEVERRÍA RABÍ\n' 
            u' Punto de partida para nuevas aplicaciones\n'
        )
        cw.about(self, title, bigText, longText, (350,150), cerapp.resman.Bitmap("logo"))
    
    #def OnManual(self, event):
    #    os.startfile(cerapp.info.man_path)
    
    def OnCloseWindow(self, event=None):
        self.Destroy()
    
    def NoImplementado(self, event=None):
        print "No implementado"
