# -*- coding: utf-8 -*-
# CRISTIAN ECHEVERRÍA RABÍ 

import cer.widgets.resource.resourcemaker as rm

#-----------------------------------------------------------------------------------------

crm = rm.ResourceMaker()
crm.UpdateImages(rm.RESNUVOLA, imgNames=["cw_file_open", "cw_file_save", "cw_file_save_as",
                                         "cw_help", "cw_quit"])

crm.AddImageDir("./z_res", "*.png", raw=True)
#crm.AddImageList("list",16,16,["eprog","eok","edel","erepg"])
crm.Make("./apy/rxfile.py")