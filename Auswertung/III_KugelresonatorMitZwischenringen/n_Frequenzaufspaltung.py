import sys

import matplotlib.pyplot as plt

sys.path.append("..")
from header.APbrainLite import *
from header.PlottenInCool import *


# ---DATEN---
Spektrum0 = DatenEinlesen("../../Messwerte/Tag-1/teil3_l_0mm.dat")  # Resonanzspektrum für keinen Zwischenring
Spektrum3 = DatenEinlesen("../../Messwerte/Tag-1/teil3_l_3mm.dat")  # Spektum für Ringdicke von 3mm
Spektrum6 = DatenEinlesen("../../Messwerte/Tag-1/teil3_l_6mm.dat")  # Spektum für Ringdicke von 6mm
Spektrum9 = DatenEinlesen("../../Messwerte/Tag-1/teil3_l_9mm.dat")  # Spektum für Ringdicke von 9mm

Spektren = [Spektrum0, Spektrum3, Spektrum6, Spektrum9]
Ringdicken = [0, 3, 6, 9]


# ---PLOTTE DATEN---
for i, Spektrum in enumerate(Spektren):
    plt.plot(*Spektrum, label="Ringdicke %imm" % Ringdicken[i])

LabelPlot("Frequenz in Hz", "Amplitude", LegendenPos = "lower left")
SpeicherPlot("III_n_Ringdickenspektrum.jpg")


# ---BESTIMMTE MAXIMA---
MaximaIndizies = []

for Spektrum in Spektren:
    MaximaIndizies.append(BestimmeExtrema(Spektrum[1]))


# ---BESTIMME MAXIMAAUFSPALTUNG + LINEARER FIT---
Aufspaltung = []
FrequenzUnsicherheit = 10


for i, Maxima in enumerate(MaximaIndizies):
    if len(Maxima) == 1:    # keine Aufspaltung
        Aufspaltung.append(WerttupelL(0,FrequenzUnsicherheit))
    elif len(Maxima) == 2:
        Maximum1, Maximum2 = Maxima

        Maximum1, Maximum2 = WerttupelListe([Spektren[i][0][Maximum1], Spektren[i][0][Maximum2]], FrequenzUnsicherheit)
        Aufspaltung.append(Maximum2 - Maximum1)

Parameter = BestimmeFitParameter(WerttupelListe(Ringdicken,0), Aufspaltung, lambda x, m, n: m * x + n)
print("FITPARAMETER: Steigung in Hz/mm, y-Achsenabschnit in Hz", Parameter)

# ---PLOTTE AUFSPALTUNG + EINZELNE MAXIMA---

Unsicherheit = [a.Unsicherheit for a in Aufspaltung]
plt.errorbar(Ringdicken, WerteListe(Aufspaltung), label="Aufspaltung", fmt="s", yerr=Unsicherheit)
PlotteFit(Ringdicken, lambda x, m, n: m * x + n, Parameter, Farbe="red", Label="Linearer Fit")

LabelPlot("Ringdicke in mm", "Frequenz in mm")
SpeicherPlot("III_n_Frequenzaufspaltung.jpg")


# TODO
# Daten aus 3.l) gemeinsam plotten
# für jede Ringdicke: Position der Maxima mit Lorentz-Fit bestimmen (Skript-Gleichung 1.10)
# Differenz aufeinanderfolgender Maxima berechnen
# Differenzen gleicher Ordnung über Ringdicke plotten
