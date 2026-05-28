import pcbnew
import os


class OPCBHealthAnalyzer(pcbnew.ActionPlugin):

    def defaults(self):
        self.name = "OPCB Health Analyzer"
        self.category = "PCB Analysis"
        self.description = "Analyzes PCB statistics and generates health report"

    def analyze_board(self, board):

        tracks = 0
        vias = 0
        top_tracks = 0
        bottom_tracks = 0

        for item in board.GetTracks():

            if isinstance(item, pcbnew.PCB_TRACK):
                tracks += 1

                layer_name = item.GetLayerName()

                if layer_name == "F.Cu":
                    top_tracks += 1

                elif layer_name == "B.Cu":
                    bottom_tracks += 1

            if isinstance(item, pcbnew.PCB_VIA):
                vias += 1

        footprints = len(board.GetFootprints())

        copper_layers = board.GetCopperLayerCount()

        report = f"""
================================
      PCB HEALTH REPORT
================================

Board File :
{board.GetFileName()}

-------------------------------
GENERAL STATISTICS
-------------------------------

Total Tracks       : {tracks}
Total Vias         : {vias}
Total Footprints   : {footprints}
Copper Layers      : {copper_layers}

-------------------------------
LAYER STATISTICS
-------------------------------

Top Layer Tracks   : {top_tracks}
Bottom Layer Tracks: {bottom_tracks}

================================
Analysis Complete
================================
"""

        print(report)

        report_path = os.path.join(
            os.path.dirname(board.GetFileName()),
            "pcb_health_report.txt"
        )

        with open(report_path, "w") as f:
            f.write(report)

        pcbnew.wxMessageBox(
            f"PCB Health Report Generated Successfully!\n\nSaved at:\n{report_path}",
            "OPCB Health Analyzer"
        )

    def Run(self):

        board = pcbnew.GetBoard()

        if board is None:
            pcbnew.wxMessageBox(
                "No PCB Board Opened!",
                "OPCB Health Analyzer"
            )
            return

        self.analyze_board(board)


OPCBHealthAnalyzer().register()