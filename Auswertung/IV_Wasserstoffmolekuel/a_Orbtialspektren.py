import sys

import matplotlib.pyplot as plt

sys.path.append("..")
from header.APbrainLite import *

sys.path.append("..")
from header.APbrainLite import *
from header.PlottenInCool import *

# ---DATEN---
bSpektrum = DatenEinlesen("../../Messwerte/Tag-2/Teil_1_B.dat") # Spektrum für Doppekugel ohne Blende
cSpektrum55 = DatenEinlesen("../../Messwerte/Tag-2/Teil_1_C_Durchmesser_055mm.dat") # Spektrum für Doppekugel mit Blendendurchmesser 5.5mm
cSpektrum11 = DatenEinlesen("../../Messwerte/Tag-2/Teil_1_C_Durchmesser_11mm.dat") # Spektrum für Doppekugel mit Blendendurchmesser 5.5mm
cSpektrum15 = DatenEinlesen("../../Messwerte/Tag-2/Teil_1_C_Durchmesser_15mm.dat") # Spektrum für Doppekugel mit Blendendurchmesser 5.5mm
cSpektrum20 = DatenEinlesen("../../Messwerte/Tag-2/Teil_1_C_Durchmesser_20mm.dat") # Spektrum für Doppekugel mit Blendendurchmesser 5.5mm

# Spektren für Orbitale im 2sigma, 2p Zustand
hSpektrum = DatenEinlesen("../../Messwerte/Tag-2/Teil_1_H.dat") # Spektrum bei Verdrillung der Kugeln um 180 Grad
iSpektrum = DatenEinlesen("../../Messwerte/Tag-2/Teil_1_I.dat") # Spektrum bei 0 Grad

Spektren = [cSpektrum55, cSpektrum11, cSpektrum15, cSpektrum20]
BlendenDurchmesser = [5.5, 11, 15, 20]


# ---PLOTTE TRANSFERFUNKTION + MAXIMUM---
Maximum = BestimmeExtrema(bSpektrum[1], Nachbarn=150)[-1]
Maximum = WerttupelL(bSpektrum[0][Maximum], 10)
print("MAXIMUM TRANSFERFUNKTION: ", Maximum)

plt.plot(*bSpektrum, label="Transferfunktion")
VertikaleLinien([Maximum], "Peak")
LabelPlot("Frequenz in Hz", "Amplitude")
SpeicherPlot("IV_Transferfunktion.jpg")


# ---PLOTTE DATEN FÜR BLENDEN---
for i, Spektrum in enumerate(Spektren):
    plt.plot(*Spektrum, label="Blendendurcmesser %smm" % str(BlendenDurchmesser[i]))

LabelPlot("Frequenz in Hz", "Amplitude")
SpeicherPlot("IV_a_Spektren.jpg")


# ---PLOTTE DATEN FÜR 2SIGMA, 2P ORBITALE---

# wähle relevantes Frequenzspektrum aus
UntereGrenze, ObereGrenze = BestimmeCutoffIndex(hSpektrum[0], 2200), BestimmeCutoffIndex(hSpektrum[0], 2600)

hSpektrum[0] = hSpektrum[0][UntereGrenze:ObereGrenze]
hSpektrum[1] = hSpektrum[1][UntereGrenze:ObereGrenze]
iSpektrum[0] = iSpektrum[0][UntereGrenze:ObereGrenze]
iSpektrum[1] = iSpektrum[1][UntereGrenze:ObereGrenze]

plt.plot(*hSpektrum, label=r"$\alpha=180°$")
plt.plot(*iSpektrum, label=r"$\alpha=0°$")

LabelPlot("Frequenz in Hz", "Amplitude")
SpeicherPlot("IV_e_Spektren.jpg")

# TODO
