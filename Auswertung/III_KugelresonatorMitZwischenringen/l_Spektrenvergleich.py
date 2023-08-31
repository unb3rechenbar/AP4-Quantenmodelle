import sys

import matplotlib.pyplot as plt


sys.path.append("..")
from header.APbrainLite import *
from header.PlottenInCool import *


# ---DATEN---
gSpektrum = DatenEinlesen("../../Messwerte/Tag-1/teil2_180grad_g.dat")  # Resonanzspektrum aus 2.g)
iSpektrum = DatenEinlesen("../../Messwerte/Tag-1/teil3_i.dat")  # Resonanzspektrum aus 3.i)

Peaks = [2093, 2263, 3464, 3645]

# ---PLOTTE DATEN---

plt.plot(*gSpektrum, label="Ohne Ringe")
plt.plot(*iSpektrum, label="Mit Ringen")
VertikaleLinien(WerttupelListe(Peaks, 5), Label="Peaks")
LabelPlot("Frequenz in Hz", "Amplitude", LegendenPos="lower right")
SpeicherPlot("III_l_Vergleichspektrum.jpg")


# ---PLOTTE DETAILAUFNAHME---
untereGrenze, obereGrenze = BestimmeCutoffIndex(iSpektrum[0], 1800), BestimmeCutoffIndex(iSpektrum[0], 3800)

iSpektrum[0] = iSpektrum[0][untereGrenze:obereGrenze]
iSpektrum[1] = iSpektrum[1][untereGrenze:obereGrenze]

plt.plot(*iSpektrum, label="Messdaten")
LabelPlot("Frequenz in Hz", "Amplitude", LegendenPos="lower right")
SpeicherPlot("III_l_Vergleichspektrum_Nahaufnahme.jpg")

# TODO
# Spektren aus 2.g) und 3.i) in gemeinsamen Diagram plotten
