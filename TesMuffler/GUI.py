#!/usr/bin/env python3
"""
__author__  = "Blaze Sanders"
__email__   = "blaze.d.a.sanders@gmail.com"
__company__ = "TesCustoms"
__status__  = "Development"
__date__    = "Late Updated: 2021-12-22"
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

MACOS_TITLEBAR_OFFSET = 25

DEFAULT_FRAME_WIDTH = 1000
DEFAULT_FRAME_HEIGHT = DEFAULT_FRAME_WIDTH

NUM_GRID_ROWS = 5
NUM_GRID_COLS = NUM_GRID_ROWS
GRID_PIXEL_SIZE = DEFAULT_FRAME_WIDTH/NUM_GRID_ROWS

DEFAULT_FONT_SIZE = 12


class MyApp(wx.App):
    def __init__(self):
        super().__init__(clearSigInt=True)
        self.InitFrame()

    def InitFrame(self):
        xWidth, yHeight = wx.GetDisplaySize()
        xCenter = int(xWidth/2)
        frame = MainFrame(parent=None,
                          title="TesMuffler Sound Control", 
                          pos=(xCenter, MACOS_SAFE_TOP_OFFSET), 
                          size=(DEFAULT_FRAME_WIDTH, DEFAULT_FRAME_HEIGHT+MACOS_TITLEBAR_OFFSET))
        #TODO frame.SetIcon(wx.Icon('icon.ico', wx.BITMAP_TYPE_ICO))
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)
        self.timer.Start(100)
        frame.Show()

    def OnTimer(self, event):
        print("TODO") #https://www.daniweb.com/programming/software-development/threads/299928/wxpython-loop-how-to-update


class MainFrame(wx.Frame):
    def __init__(self, parent, title, pos, size):
        # Create non resizeable frame as the 1st frame of the application
        # https://wxpython.org/Phoenix/docs/html/wx.Frame.html
        DISABLE_FRAME_RESIZE = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX)
        super().__init__(parent=parent, title=title, pos=pos, size=size, style=DISABLE_FRAME_RESIZE)
        self.OnInit()

    def OnInit(self):
        wx.Bell()                       # Beep to indicate program is running
        panel = MainPanel(parent=self)


class MainPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent=parent, id=1, size=(DEFAULT_FRAME_WIDTH, DEFAULT_FRAME_HEIGHT))
        
        # Layout the 1st panel for Main Frame
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        
        # Create the menu bar
        #TODO
        
        welcomeText = wx.StaticText(parent=self, id=1, label="Welcome to the TesMuffler Sound Control GUI", pos=(10, 100))
        welcomeText.SetFont(wx.Font(22, 74, 90, 92, False, "Source Sans Pro"))
        
        # Create an alignment grid for elements
        layout = LayoutGrid(parent=self)


class LayoutGrid(wx.grid.Grid):
    """https://wxpython.org/Phoenix/docs/html/wx.grid.Grid.html

    Args:
        wx ([type]): [description]
    """
    def __init__(self, parent):
        super().__init__(parent=parent, id=wx.ID_ANY, pos=(0, 0), size=(DEFAULT_FRAME_WIDTH, DEFAULT_FRAME_HEIGHT))
        self.InitGrid()

    def InitGrid(self):
        self.CreateGrid(NUM_GRID_ROWS, NUM_GRID_COLS)
        for i in range(NUM_GRID_ROWS):
            self.SetRowSize(i, int(GRID_PIXEL_SIZE))
            self.SetColSize(i, int(GRID_PIXEL_SIZE))

        # Format the grid
        self.ShowScrollbars(wx.SHOW_SB_NEVER, wx.SHOW_SB_NEVER)
        self.HideColLabels()
        self.HideRowLabels()
        self.SetDefaultCellAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)
        self.SetDefaultCellBackgroundColour(wx.WHITE)
        self.SetDefaultCellTextColour(wx.BLACK)
        self.SetDefaultCellFont(wx.Font(pointSize=DEFAULT_FONT_SIZE, family=wx.FONTFAMILY_MODERN, style=wx.FONTSTYLE_NORMAL, weight=wx.FONTWEIGHT_NORMAL))
        self.SetDefaultCellOverflow(False)
        
    def FillGrid(self, rowNum, colNum, text):
        self.SetCellValue(rowNum, colNum, text)

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
    


if __name__ == "__main__":
    app = MyApp()
    #app.InitFrame()
    #app.MacReopenApp()
    
    app.MainLoop()
