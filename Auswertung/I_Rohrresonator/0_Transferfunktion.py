import sys
sys.path.append("..")
from header.APbrainLite import *
from header.PlottenInCool import *


# ---DATEN---
TransferDaten = DatenEinlesen("../../Messwerte/Tag-1/vorversuch.dat")
Peaks = [WerttupelL(450, 20), WerttupelL(2090, 20), WerttupelL(4520, 20), WerttupelL(8060, 20)]    # in Hz


# ---PLOTS---
PlotKartesisch(*TransferDaten, xLabel="Frequenz in Hz", yLabel="Amplitude", DiagrammTitel="Transferfunktion ",
               VertikaleLinien=Peaks, VertikaleLinienLabel="Peaks", DatenLabel="Messdaten", mode="save",
               Pfad="Transferfunktion.jpg")

