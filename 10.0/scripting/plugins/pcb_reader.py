import pcbnew
import wx

class PCBReader(pcbnew.ActionPlugin):

    def defaults(self):
        self.name = "Day 2 - PCB Reader"
        self.category = "Learning Plugins"
        self.description = "Reads PCB information and shows a pop-up"

    def Run(self):
        # 1. Get the current board
        board = pcbnew.GetBoard()
        
        # 2. Extract all the required data
        footprints = len(list(board.GetFootprints()))
        tracks = len(list(board.GetTracks()))
        vias = sum(1 for track in board.GetTracks() if track.GetClass() == "VIA")
        nets = board.GetNetCount()
        layers = board.GetCopperLayerCount()
        file_name = board.GetFileName()
        
        # Convert thickness from internal units to millimeters
        thickness = board.GetDesignSettings().GetBoardThickness() / 1000000.0
        
        # 3. Create a formatted display string
        msg = f"Board File: {file_name}\n"
        msg += f"Board Thickness: {thickness} mm\n"
        msg += f"Total Footprints: {footprints}\n"
        msg += f"Total Tracks: {tracks}\n"
        msg += f"Total Vias: {vias}\n"
        msg += f"Total Nets: {nets}\n"
        msg += f"Copper Layers: {layers}"
        
        # 4. Show a pop-up alert box
        wx.MessageBox(msg, "FOSSEE Day 2 - PCB Reader", wx.OK | wx.ICON_INFORMATION)

# 5. Register the plugin so KiCad can see it
PCBReader().register()