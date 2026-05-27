import pcbnew

class PCBStatistics:

    def __init__(self, board):
        self.board = board

    def get_statistics(self):

        tracks = len(self.board.GetTracks())
        footprints = len(self.board.GetFootprints())
        drawings = len(self.board.GetDrawings())

        vias = 0

        for item in self.board.GetTracks():
            if isinstance(item, pcbnew.PCB_VIA):
                vias += 1

        nets = self.board.GetNetCount()

        return {
            "Tracks": tracks,
            "Footprints": footprints,
            "Drawings": drawings,
            "Vias": vias,
            "Nets": nets
        }