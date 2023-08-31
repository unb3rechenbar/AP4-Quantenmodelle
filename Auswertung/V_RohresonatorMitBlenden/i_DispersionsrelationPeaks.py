import sys

import matplotlib.pyplot as plt

sys.path.append("..")
from header.APbrainLite import *
from header.PlottenInCool import *


# ---DATEN---
# Maxima der Transferunktion
TransferMaxima = [450, 2090, 4520, 8060]

# Daten aus 5.l) - 5.o) (lange Segmente)
lSeg8KeineBlende = DatenEinlesen("../../Messwerte/Tag-1/teil1_60cm.dat") # 8 Rohre ohne Blenden
lSeg1 = DatenEinlesen("../../Messwerte/Tag-2/Teil_2_L.dat") # 1 Rohr, keine Blende
lSeg2 = DatenEinlesen("../../Messwerte/Tag-2/Teil_2_M.dat") # 2 Rohre, 1 Blende
lSeg3 = DatenEinlesen("../../Messwerte/Tag-2/Teil_2_N_3Segmente.dat") # 3 Rohre, 2 Blenden
lSeg4 = DatenEinlesen("../../Messwerte/Tag-2/Teil_2_N_4Segmente.dat") # 4 Rohre, 3 Blenden
lSeg8 = DatenEinlesen("../../Messwerte/Tag-2/Teil_2_O.dat") # 8 Rohre, 7 Blenden

# Daten aus 5.p) - 5.q)
pSeg12KeineBlende = DatenEinlesen("../../Messwerte/Tag-2/Teil_2_P.dat") # 12 kurze Rohre ohne Blenden
pSeg12 = DatenEinlesen("../../Messwerte/Tag-2/Teil_2_Q.dat") # 12 kurze Rohre, 11 Blenden

# ---SETUP ZUM PEAK-ABLESEN---
Peaks = []


def EnterPeak(event):
    Peaks.append(event.xdata)
    print("Peak %i: " % len(Peaks), event.xdata)


def SpeicherPeaks(Name):
    with open("DispersionDaten/%s.dat" % Name, "w") as f:
        for i, Peak in enumerate(Peaks):
            f.write("%i %s\n" % (i + 1, str(Peak)))


# ---MANUELLES PEAK-ABLESEN
Datenset = pSeg12
Dateiname = "KurzeSeg12"

fig, ax = plt.subplots(1, 1)
ax.plot(*Datenset)

for TMaxima in TransferMaxima:
    ax.axvline(TMaxima, color="red", alpha=0.5)

fig.canvas.mpl_connect("button_press_event", EnterPeak)
plt.show()
SpeicherPeaks(Dateiname)
