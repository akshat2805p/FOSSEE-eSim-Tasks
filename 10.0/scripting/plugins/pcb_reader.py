import pcbnew
import wx

class PCBStatisticsPlugin(pcbnew.ActionPlugin):

    def defaults(self):
        self.name = "PCB Statistics Plugin"
        self.category = "PCB Tools"
        self.description = "Displays PCB statistics"

    def Run(self):

        board = pcbnew.GetBoard()

        # Count tracks
        track_count = 0

        # Count vias
        via_count = 0

        tracks = board.GetTracks()

        for item in tracks:
            if isinstance(item, pcbnew.TRACK):
                track_count += 1

            if isinstance(item, pcbnew.VIA):
                via_count += 1

        # Count footprints/components
        footprint_count = len(board.GetFootprints())

        # Get board dimensions
        bbox = board.GetBoardEdgesBoundingBox()

        width = pcbnew.ToMM(bbox.GetWidth())
        height = pcbnew.ToMM(bbox.GetHeight())

        # Create statistics text
        stats = f"""
PCB Statistics

Tracks: {track_count}
Vias: {via_count}
Footprints: {footprint_count}

Board Width: {width:.2f} mm
Board Height: {height:.2f} mm
"""

        # Show popup message
        wx.MessageBox(stats, "PCB Statistics Plugin")


# Register plugin
PCBStatisticsPlugin().register()