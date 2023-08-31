import sys

import numpy as np
import matplotlib.pyplot as plt

sys.path.append("..")
from header.APbrainLite import *
from header.PlottenInCool import *


# ---DATEN---
gSpektrum = DatenEinlesen("../../Messwerte/Tag-1/teil2_180grad_g.dat")  # Resonanzspektrum aus 2.g)

# Polschnitte aus 2.g) (Resonanzen von 1200 Hz bis 7000 Hz)
gPolschnitt2300 = DatenEinlesen("../../Messwerte/Tag-1/teil2_2300Hz.dat", ZeilenCutoff=3, Spaltenzahl=3)
gPolschnitt3694 = DatenEinlesen("../../Messwerte/Tag-1/teil2_3694Hz.dat", ZeilenCutoff=3, Spaltenzahl=3)
gPolschnitt4982 = DatenEinlesen("../../Messwerte/Tag-1/teil2_circa4982Hz.dat", ZeilenCutoff=3, Spaltenzahl=3)
gPolschnitt6221 = DatenEinlesen("../../Messwerte/Tag-1/teil2_6221Hz.dat", ZeilenCutoff=3, Spaltenzahl=3)

gPolschnitte = [gPolschnitt2300, gPolschnitt3694, gPolschnitt4982, gPolschnitt6221]
gPolschnitteFrequenzen = [2300, 3694, 4982, 6221]
gPolschnitteQuantenzahlen = [[(1, 0)], [(2,0)], [(3, 0)], [(5, 0)]]  # Liste mit Tupeln (l,m)    # vergleiche https://espanol.libretexts.org/Quimica/Qu%C3%ADmica_F%C3%ADsica_y_Te%C3%B3rica/Qu%C3%ADmica_F%C3%ADsica_%28LibreTexts%29/06%3A_El_%C3%A1tomo_de_hidr%C3%B3geno/6.02%3A_Las_funciones_de_onda_de_un_rotador_r%C3%ADgido_se_denominan_arm%C3%B3nicos_esf%C3%A9ricos


hSpektrum0 = DatenEinlesen("../../Messwerte/Tag-1/teil2_h_0grad.dat") # Resonanzspektrum aus 2.g) bei 0 Grad
hSpektrum90 = DatenEinlesen("../../Messwerte/Tag-1/teil2_h_90grad.dat") # Resonanzspektrum aus 2.g) bei 90 Grad
hSpektrum180 = DatenEinlesen("../../Messwerte/Tag-1/teil2_h_180grad.dat") # Resonanzspektrum aus 2.g) bei 180 Grad

hSpektren = [hSpektrum0, hSpektrum90, hSpektrum180]
hSpektrenWinkel = [0, 90, 180]

# Polschnitte aus 2.h) (Doppelpeak bei ca. 5000 Hz)
hPolschnitt4965 = DatenEinlesen("../../Messwerte/Tag-1/teil2_h_4965Hz_polar.dat", ZeilenCutoff=3, Spaltenzahl=3)
hPolschnitt4986 = DatenEinlesen("../../Messwerte/Tag-1/teil2_h_4986Hz_polar.dat", ZeilenCutoff=3, Spaltenzahl=3)

hPolschnitte = [hPolschnitt4965, hPolschnitt4986]
hPolschnitteFrequenzen = [4965, 4986]
hPolschnitteQuantenzahlen = [[(0,0)], [(3,0)]]    # Tupel (l,m)

# --DEFINIERE LEGENDRE-FITFUNKTIONEN---
# Nomenklatur: LegendreFitLM, mit L und M als jeweiligen Quantenzahlen


def LegendreFit00(theta, a):
    return np.array([a for _ in theta])


def LegendreFit10(theta, a):
    return a * abs(np.cos(theta))


def LegendreFit20(theta, a):
    return a / 2 * abs(3 * np.cos(theta)**2 - 1)


def LegendreFit30(theta, a):
    return a / 2 * abs(5 * np.cos(theta)**3 - 3 * np.cos(theta))


def LegendreFit40(theta, a):
    return a / 8 * abs(35 * np.cos(theta)**4 - 30 * np.cos(theta)**2 + 3)


def LegendreFit50(theta, a):
    return a / 8 * abs(63 * np.cos(theta)**5 - 70 * np.cos(theta)**3 + 15 * np.cos(theta))


# erster Index: Quantenzahl l; zweiter Index: Quantenzahl m
FitMatrix = [[LegendreFit00],
             [LegendreFit10],
             [LegendreFit20],
             [LegendreFit30],
             [LegendreFit40],
             [LegendreFit50]]


# ---POLSCHNITTE MIT FITS PLOTTEN (FUNKTIONEN)---
def GradZuRadians(Grad):
    return list(2 * np.pi / 360 * g for g in Grad)


def ErgaenzeSymmetrie(Winkel, Radius):
    n = len(Winkel)

    # für Winkelbereich 180-270 Grad: spiegele y-Werte/ trage sie in umgekehrter Reihenfolge ein
    NeueWinkel = []

    for j in range(n):
        NeueWinkel.append(360 - Winkel[j])
        Radius.append(Radius[n - j - 1])
    Winkel += reversed(NeueWinkel)

    # für Winkelbereich 270-360 Grad: kopiere y-Werte vom Bereich 90 bis 180 Grad
    for j in range(n):
        Winkel.append(Winkel[j] + 180)
        Radius.append(Radius[j])

    # für Winkelbereich 0-90 Grad: wie bei 180-270 Grad
    NeueWinkel = []

    for j in range(n):
        NeueWinkel.append(180 - Winkel[j])
        Radius.append(Radius[n - j - 1])
    Winkel += reversed(NeueWinkel)


    return Winkel, Radius


# ---FÜHRE FITS DURCH---
# Daten aus 2.g)
gPolschnittAmplituden = []

for i, gPolschnitt in enumerate(gPolschnitte):
    gPolschnittAmplituden.append([])

    Winkel, Amplitude = gPolschnitt[1:]

    for LM in gPolschnitteQuantenzahlen[i]:
        Parameter = BestimmeFitParameter(WerttupelListe(GradZuRadians(Winkel), 0.01), WerttupelListe(Amplitude, 0.01),
                                         FitMatrix[LM[0]][LM[1]])

        gPolschnittAmplituden[-1].append(Parameter)
        print("Resonanz %i: " % i, Parameter[0])


# Daten aus 2.h)
hPolschnittAmplituden = []

for i, hPolschnitt in enumerate(hPolschnitte):
    hPolschnittAmplituden.append([])
    Winkel, Amplitude = hPolschnitt[1:]

    for LM in hPolschnitteQuantenzahlen[i]:
        Parameter = BestimmeFitParameter(WerttupelListe(GradZuRadians(Winkel), 0.01), WerttupelListe(Amplitude, 0.01),
                                         FitMatrix[LM[0]][LM[1]])

        hPolschnittAmplituden[-1].append(Parameter)


# ---PLOTTE DATEN MIT FITS---

# Daten aus 2.g)
for i, gPolschnitt in enumerate(gPolschnitte):
    for j, LM in enumerate(gPolschnitteQuantenzahlen[i]):
        plt.axes(projection="polar")

        Winkel, Amplitude = ErgaenzeSymmetrie(gPolschnitt[1], gPolschnitt[2])
        Winkel = GradZuRadians(Winkel)

        PlotteFit(Winkel, FitMatrix[LM[0]][LM[1]], gPolschnittAmplituden[i][j], Label="Legendre-Fit", Fill=True,
                  FillFarbe="blue", FillTransparenz=0.25)
        plt.plot(Winkel, Amplitude, label="Messdaten", color="red", linewidth=1, marker="s")
        LabelPlot(r"Winkel $\theta$ in °", "Amplitude", LegendenPos="best", yPadding=30)
        SpeicherPlot("II_i_Polschnitt_%i_%i%i.jpg" % (gPolschnitteFrequenzen[i], LM[0], LM[1]))


# Daten aus 2.h)
for i, hPolschnitt in enumerate(hPolschnitte):
    for j, LM in enumerate(hPolschnitteQuantenzahlen[i]):
        plt.axes(projection="polar")

        Winkel, Amplitude = ErgaenzeSymmetrie(hPolschnitt[1], hPolschnitt[2])
        Winkel = GradZuRadians(Winkel)

        PlotteFit(Winkel, FitMatrix[LM[0]][LM[1]], hPolschnittAmplituden[i][j], Label="Legendre-Fit", Fill=True,
                  FillFarbe="blue", FillTransparenz=0.25)
        plt.plot(Winkel, Amplitude, label="Messdaten", color="red", linewidth=1, marker="s")
        LabelPlot(r"Winkel $\theta$ in °", "Amplitude", LegendenPos="best", yPadding=30)
        SpeicherPlot("II_j_Polschnitt_%i_%i%i.jpg" % (hPolschnitteFrequenzen[i], LM[0], LM[1]))


# ---PLOTTE RESONANZSPEKTREN ZU POLSCHNITTEN---
# für Polschnitte aus g
plt.plot(*gSpektrum, label="Messdaten")
VertikaleLinien(WerttupelListe(gPolschnitteFrequenzen, 10), Label="Peaks")
LabelPlot("Frequenz in Hz", "Amplitude")
SpeicherPlot("II_i_Resonanzspektrum.jpg")

# für Polschnitte aus h
for hSpektrum, Winkel in zip(hSpektren, hSpektrenWinkel):
    plt.plot(*hSpektrum, label="Messdaten")
    VertikaleLinien(WerttupelListe(hPolschnitteFrequenzen, 1), Label="Peaks")
    LabelPlot("Frequenz in Hz", "Amplitude")
    SpeicherPlot("II_i_Resonanzspektrum_%i_Grad.jpg" % Winkel)

# TODO
# für alle Daten aus 2.g), 2.h): in Polarkoordinatensystem die Polschnitte plotten
# für passende l,m (idk, einfach Ausprobieren?) je einen Legendre-Fit durchführen
# (Funktionen sind in Skripttabelle 1.1.; für Fit diese noch mit einer konstanten Amplitude als Fitparameter skalieren)
