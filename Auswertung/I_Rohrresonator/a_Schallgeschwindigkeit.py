import sys

import matplotlib.pyplot as plt

sys.path.append("..")
from header.APbrainLite import *
from header.PlottenInCool import *
import aa_Transferfunktion as transfer


# ---DATEN---
Ordnungen = [i for i in range(1, 11)]   # ersten 10 Ordnungen
Rohrlaenge = WerttupelL(0.60, 0.001)   # in m
PeaksUnsicherheit = 20

ResonanzkurveComputer = DatenEinlesen("../../Messwerte/Tag-1/teil1_60cm.dat") # Daten aus 1.c)
PeaksComputer = [296, 591, 874, 1163, 1446, 1741, 2024, 2326, 2597, 2898]


# ---PLOT FÜR COMPUTER-RESOKURVE---
Cutoff = BestimmeCutoffIndex(ResonanzkurveComputer[0], 3000)
ResonanzkurveComputer[0], ResonanzkurveComputer[1] = ResonanzkurveComputer[0][:Cutoff], ResonanzkurveComputer[1][:Cutoff]

plt.plot(*ResonanzkurveComputer, label="Messdaten")
VertikaleLinien(transfer.Peaks[:2], Label="Peaks der Transferfunktion")
LabelPlot("Frequenz in Hz", "Amplitude", LegendenPos="lower left")
SpeicherPlot("I_c_Resonanzspektrum.jpg")


# ---LINEARE FITS---
LinearerFit = lambda  x, m, n: m * x + n

ParameterComputer = BestimmeFitParameter(WerttupelListe(Ordnungen, 0), WerttupelListe(PeaksComputer, PeaksUnsicherheit), LinearerFit) # für Daten aus 1.c)

print("COMPUTERDATEN (FIT): Steigung, y-Achsenabschnitt in Hz: ", *ParameterComputer)

# ---SCHALLGESCHWINDIGKEIT + Signi-Test---
def berechneSchallgeschwindigkeit(Laenge, Steigung):
    return 2 * Laenge * Steigung


SchallComputer = berechneSchallgeschwindigkeit(Rohrlaenge, ParameterComputer[0])

print("COMPUTERDATEN: Schallgeschwindigkeit in m/s: ", SchallComputer)


# ---PLOTS FÜR LINEARE FITS---
plt.errorbar(Ordnungen, PeaksComputer, fmt="s", yerr=PeaksUnsicherheit, color="red", label="Computerdaten")    # Daten aus 1.c
PlotteFit(Ordnungen, LinearerFit, ParameterComputer, Label="Fit (Computerdaten)")
LabelPlot("Ordnung n", "Resonanzfrequenz in Hz")
SpeicherPlot("I_Schallgeschwindigkeitfit.jpg")


# ---Signifikanztest mit Literaturwert---
SchallLiteratur = WerttupelL(344, 0)
print("Vereinbarkeit: ", Signifikanztest(SchallComputer, SchallComputer))

# TODO
# lineare Regression von Resonanzfrequenzen über Ordnung (einmal mit Oskzilloskop Daten aus 1.a), einmal mit den Daten
# aus 1.c))
# aus Steigung Schallgeschwindigkeit berechnen
# Signifikanztest mit Literaturwert
