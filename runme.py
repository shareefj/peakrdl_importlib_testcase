import importlib_metadata as m
from peakrdl.plugins.entry_points import get_entry_points

print("Finding PeakRDL exporters using get_entry_points()")
exporters = get_entry_points("peakrdl.exporters")
for e in exporters:
    print("  " + e.name)

print("\n\nFinding PeakRDL exporters using importlib_metadata")
exporters = m.entry_points(group="peakrdl.exporters")
for e in exporters:
    print("  " + e.name)