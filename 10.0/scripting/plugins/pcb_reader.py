import pcbnew
import wx
import csv
import os

class PCBStatisticsPlugin(pcbnew.ActionPlugin):

    def defaults(self):
        self.name = "PCB Statistics Exporter"
        self.category = "PCB Tools"
        self.description = "Shows PCB statistics and exports them to CSV"

    def Run(self):
        board = pcbnew.GetBoard()

        track_count = len(board.GetTracks())
        footprint_count = len(board.GetFootprints())
        drawing_count = len(board.GetDrawings())

        stats = [
            ["Item", "Count"],
            ["Tracks", track_count],
            ["Footprints", footprint_count],
            ["Drawings", drawing_count]
        ]

        # Message display
        message = (
            f"Tracks: {track_count}\n"
            f"Footprints: {footprint_count}\n"
            f"Drawings: {drawing_count}"
        )

        wx.MessageBox(message, "PCB Statistics")

        # Export CSV
        output_file = os.path.join(os.path.expanduser("~"), "pcb_stats.csv")

        with open(output_file, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(stats)

        wx.MessageBox(
            f"CSV Exported Successfully!\nSaved at:\n{output_file}",
            "Export Complete"
        )

PCBStatisticsPlugin().register()