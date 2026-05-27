import pcbnew
import wx

from .analyzer_core import PCBStatistics
from .report_generator import generate_report

class PCBHealthAnalyzer(pcbnew.ActionPlugin):

    def defaults(self):
        self.name = "PCB Health Analyzer"
        self.category = "PCB Analysis"
        self.description = "Analyze PCB design quality"

    def Run(self):

        board = pcbnew.GetBoard()

        analyzer = PCBStatistics(board)

        stats = analyzer.get_statistics()

        message = ""

        for key, value in stats.items():
            message += f"{key}: {value}\n"

        generate_report(stats)

        wx.MessageBox(
            message,
            "PCB Health Analyzer"
        )

PCBHealthAnalyzer().register()