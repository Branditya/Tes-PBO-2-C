import wx
import helloWx

class subclass(helloWx.MyFrame1):
    def __init__(self,parent):
        helloWx.MyFrame1.__init__(self, parent)
        
app = wx.App()
frame = helloWx.MyFrame1(parent=None)
frame.Show()
app.MainLoop()