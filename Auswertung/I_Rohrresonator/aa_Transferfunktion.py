import sys
import matplotlib.pyplot as plt

sys.path.append("..")
from header.APbrainLite import *
from header.PlottenInCool import *


# ---DATEN---
TransferDaten = DatenEinlesen("../../Messwerte/Tag-1/vorversuch.dat")
Peaks = [WerttupelL(450, 20), WerttupelL(2090, 20), WerttupelL(4520, 20), WerttupelL(8060, 20)]    # in Hz


# ---PLOTS---
plt.plot(*TransferDaten, label="Messdaten")
VertikaleLinien(Peaks, Label="Peaks")
LabelPlot("Frequenz in Hz", "Ampltiude")
SpeicherPlot("I_Transferfunktion.jpg")
