import pcbnew
import wx

class HelloPlugin(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "Hello FOSSEE"
        self.category = "Test"
        self.description = "My first plugin"

    def Run(self):
        # Using the standard cross-platform wxWidgets messaging implementation
        wx.MessageBox("Hello FOSSEE Internship!", "FOSSEE Plugin", wx.OK | wx.ICON_INFORMATION)

HelloPlugin().register()