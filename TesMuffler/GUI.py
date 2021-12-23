#!/usr/bin/env python3
"""
__author__  = "Blaze Sanders"
__email__   = "blaze.d.a.sanders@gmail.com"
__company__ = "TesCustoms"
__status__  = "Development"
__date__    = "Late Updated: 2021-12-21"
__doc__     = "Graphical User Interface to update sounds on device
"""
# Import wxPython GUI library
import wx
import wx.grid

import webbrowser

# Pixel offset CONSTANTS for the MacOS menu bar and (left or right) dock icons
MACOS_SAFE_TOP_OFFSET = 25
MACOS_SAFE_LEFT_OFFSET = 50
MACOS_SAFE_RIGHT_OFFSET = MACOS_SAFE_LEFT_OFFSET
MACOS_SAFE_BOTTOM_OFFSET = 5

DEFAULT_FRAME_WIDTH = 1000
DEFAULT_FRAME_HEIGHT = 1000

NUM_GRID_ROWS = 10
NUM_GRID_COLS = NUM_GRID_ROWS
GRID_PIXEL_SIZE = 100


class MyApp(wx.App):
    def __init__(self):
        super().__init__(clearSigInt=True)
        self.InitFrame()

    def InitFrame(self):
        xWidth, yHeight = wx.GetDisplaySize()
        xCenter = int(xWidth/2)
        frame = MainFrame(parent=None, title="TesMuffler Sound Control", pos=(xCenter, MACOS_SAFE_TOP_OFFSET), size=(DEFAULT_FRAME_WIDTH, DEFAULT_FRAME_HEIGHT))
        frame.Show()

class MainFrame(wx.Frame):
    def __init__(self, parent, title, pos, size):
        super().__init__(parent=parent, title=title, pos=pos, size=size)
        self.OnInit()

    def OnInit(self):
        panel = MainPanel(parent=self)


class MainPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent=parent, kid=1, size=(DEFAULT_FRAME_WIDTH, DEFAULT_FRAME_HEIGHT))
        
        # Layout the 1st panel for Main Frame
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        # Create the menu bar
        #self.CreateMenuBar()
        
        # Create an alignment grid to elements
        alignmentGrid = LayoutGrid(parent=self)


class LayoutGrid(wx.grid.Grid):
    """https://wxpython.org/Phoenix/docs/html/wx.grid.Grid.html

    Args:
        wx ([type]): [description]
    """
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.InitGrid()

    def InitGrid(self):
        self.CreateGrid(NUM_GRID_ROWS, NUM_GRID_COLS)
        for i in range(NUM_GRID_ROWS):
            self.SetRowSize(i, GRID_PIXEL_SIZE)
            self.SetColSize(i, GRID_PIXEL_SIZE)

        # Format the grid
        self.HideColLabels()
        self.HideRowLabels()
        self.SetDefaultCellAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)
        self.SetDefaultCellBackgroundColour(wx.WHITE)
        self.SetDefaultCellTextColour(wx.BLACK)
        self.SetDefaultCellFont(wx.Font(pointSize=12, family=wx.FONTFAMILY_DEFAULT, style=wx.FONTSTYLE_NORMAL, weight=wx.FONTWEIGHT_NORMAL))
        self.SetDefaultCellOverflow(True)
        

class LayoutGrid2(wx.GridSizer):
    def __init__(self, rows, cols, vgap, hgap):
        super().__init__(rows, cols, vgap, hgap)
        self.rows = rows
        self.cols = cols
        self.vgap = vgap
        self.hgap = hgap

    def Add(self, item, flag=0, border=0, pos=(0, 0)):
        super().Add(item, flag, border, pos)
        self.AddGrowableRow(pos[0])
        self.AddGrowableCol(pos[1])

def UnitTest():
    app = wx.App(clearSigInt=True)
    frame = wx.Frame(parent=None, id=wx.ID_ANY, title="TesMuffler Sound Control", pos=(MACOS_SAFE_LEFT_OFFSET, MACOS_SAFE_TOP_OFFSET))    # pos=(X,Y) from top left corner
    panel = wx.Panel(parent=frame, id=wx.ID_ANY)

    welcomeText = wx.StaticText(parent=panel, id=wx.ID_ANY, label="Welcome to the TesMuffler Sound Control GUI", pos=(10, 10))
    welcomeText.SetFont(wx.Font(12, 74, 90, 92, False, "Arial"))
    
    
    
    self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
    
    
    bSizer1 = wx.BoxSizer(wx.VERTICAL)
    
    self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, "Sound Update", wx.DefaultPosition, wx.DefaultSize, 0)
    self.m_staticText1.Wrap(-1)
    self.m_staticText1.SetFont(wx.Font(16, 74, 90, 92, False, "Arial"))
    
    bSizer1.Add(self.m_staticText1, 0, wx.ALL, 5)
    
    self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, "Select a sound to update", wx.DefaultPosition, wx.DefaultSize, 0)
    self.m_staticText2.Wrap(-1)
    self.m_staticText2.SetFont(wx.Font(12, 74, 90, 92, False, "Arial"))
    
    bSizer1.Add(self.m_staticText2, 0, wx.ALL, 5)
    
    self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, "Select a sound to update", wx.DefaultPosition, wx.DefaultSize, 0)
    self.m_staticText3.Wrap(-1)
    self.m_staticText3.SetFont(wx.Font(12, 74, 90, 92, False, "Arial"))
    
    bSizer1.Add(self.m_staticText3, 0, wx.ALL, 5)

    frame.Show()
    app.MainLoop()


if __name__ == "__main__":
    app = MyApp()
    #app.InitFrame()
    app.MainLoop()
