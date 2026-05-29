import pcbnew


class DRCSummary:
    def __init__(self, board):
        self.board = board

    def count_tracks(self):
        return len(self.board.GetTracks())

    def count_vias(self):
        vias = 0
        for item in self.board.GetTracks():
            if isinstance(item, pcbnew.PCB_VIA):
                vias += 1
        return vias

    def count_unconnected_pads(self):
        pads = 0
        for footprint in self.board.GetFootprints():
            for pad in footprint.Pads():
                if pad.GetNetCode() == 0:
                    pads += 1
        return pads

    def detect_overlaps(self):
        tracks = list(self.board.GetTracks())
        overlaps = 0

        for i in range(len(tracks)):
            for j in range(i + 1, len(tracks)):
                if tracks[i].GetStart() == tracks[j].GetStart():
                    overlaps += 1

        return overlaps

    def generate_report(self):
        tracks = self.count_tracks()
        vias = self.count_vias()
        pads = self.count_unconnected_pads()
        overlaps = self.detect_overlaps()

        status = "GOOD"

        if pads > 0 or overlaps > 0:
            status = "WARNING"

        report = f"""
=== PCB DRC SUMMARY ===
Tracks: {tracks}
Vias: {vias}
Unconnected Pads: {pads}
Possible Overlaps: {overlaps}
Board Status: {status}
"""

        return report