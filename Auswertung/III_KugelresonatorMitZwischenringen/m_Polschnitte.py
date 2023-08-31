import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.append("..")
from header.APbrainLite import *
from header.PlottenInCool import *


# ---DATEN---
# Polschnitte aus 2.j) und 2.k)
Polschnitt2093 = DatenEinlesen("../../Messwerte/Tag-1/teil3_j_2093Hz.dat", ZeilenCutoff=2, Spaltenzahl=3)
Polschnitt2263 = DatenEinlesen("../../Messwerte/Tag-1/teil3_j_2263Hz.dat", ZeilenCutoff=2, Spaltenzahl=3)
Polschnitt3464 = DatenEinlesen("../../Messwerte/Tag-1/teil3_k_3464Hz.dat", ZeilenCutoff=2, Spaltenzahl=3)
Polschnitt3645 = DatenEinlesen("../../Messwerte/Tag-1/teil3_k_3645Hz.dat", ZeilenCutoff=2, Spaltenzahl=3)

Polschnitte = [Polschnitt2093, Polschnitt2263, Polschnitt3464, Polschnitt3645]
PolschnitteFrequenzen = [2093, 2263, 3464, 3645]
PolschnitteQuantenzahlen = [0, 1, 1, 2]  # Liste mit Quantenzahl m    # vergleiche https://espanol.libretexts.org/Quimica/Qu%C3%ADmica_F%C3%ADsica_y_Te%C3%B3rica/Qu%C3%ADmica_F%C3%ADsica_%28LibreTexts%29/06%3A_El_%C3%A1tomo_de_hidr%C3%B3geno/6.02%3A_Las_funciones_de_onda_de_un_rotador_r%C3%ADgido_se_denominan_arm%C3%B3nicos_esf%C3%A9ricos


# ---DEFINIERE LEGENDRE-FITFUNKTION---
# Nomenklatur: LegendreFitM, mit M als jeweiligen Quantenzahl
def LegendreFit0(theta, a):
    return np.array([a for _ in theta])


def LegendreFit1(theta, a):
    return a * np.absolute(np.cos(theta))


def LegendreFit2(theta, a):
    return a * np.absolute(np.cos(2 * theta))

FitMatrix = [LegendreFit0, LegendreFit1, LegendreFit2]


# ---POLSCHNITTE MIT FITS PLOTTEN (FUNKTIONEN)---
def GradZuRadians(Grad):
    return list(2 * np.pi / 360 * g for g in Grad)


def ErgaenzeSymmetrie(Winkel, Radius):
    n = len(Winkel)

    # für Winkelbereich 180-360 Grad: spiegele y-Werte/ trage sie in umgekehrter Reihenfolge ein
    NeueWinkel = []

    for j in range(n-1):
        NeueWinkel.append(360 - Winkel[j])
        Radius.append(Radius[n - j - 1])
    Winkel += reversed(NeueWinkel)

    return Winkel, Radius


# ---FÜHRE FITS DURCH---
PolschnittAmplituden = []

for i, Polschnitt in enumerate(Polschnitte):
    Winkel, Amplitude = Polschnitt[1:]

    M = PolschnitteQuantenzahlen[i]
    Parameter = BestimmeFitParameter(WerttupelListe(GradZuRadians(Winkel), 0.01), WerttupelListe(Amplitude, 0.01),
                                         FitMatrix[M])

    PolschnittAmplituden.append(Parameter)
    print("Amplitude zu Peak bei %i Hz: " % PolschnitteFrequenzen[i], Parameter[0])


# ---PLOTTE DATEN MIT FITS---

# Daten aus 2.g)
for i, Polschnitt in enumerate(Polschnitte):
    M = PolschnitteQuantenzahlen[i]
    plt.axes(projection="polar")

    Winkel, Amplitude = ErgaenzeSymmetrie(Polschnitt[1], Polschnitt[2])
    Winkel = GradZuRadians(Winkel)

    PlotteFit(Winkel, FitMatrix[M], PolschnittAmplituden[i], Label="Legendre-Fit", Fill=True,
                  FillFarbe="blue", FillTransparenz=0.25)

    plt.plot(Winkel, Amplitude, label="Messdaten", color="red", linewidth=1, marker="s")
    LabelPlot(r"Winkel $\theta$ in °", "Amplitude", LegendenPos="best", yPadding=30)
    SpeicherPlot("III_jk_Polschnitt_%i_%i.jpg" % (PolschnitteFrequenzen[i], M))

# TODO
# für alle Daten aus 3.j), 3.k): in Polarkoordinatensystem die Polschnitte plotten (dabei Theta in Phi mithilfe von
# Frage 1 umrechnen)
# für passende l,m (idk, einfach Ausprobieren?) je einen Legendre-Fit durchführen
# (Funktionen sind in Auswertungspunkt 3.m); für Fit diese noch mit einer konstanten Amplitude als Fitparameter skalieren)
