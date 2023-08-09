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
gPolschnitteQuantenzahlen = [(1, 0), [(2,0), (3, 0)], (5, 0)]  # Tupel (l,m)    # vergleiche https://espanol.libretexts.org/Quimica/Qu%C3%ADmica_F%C3%ADsica_y_Te%C3%B3rica/Qu%C3%ADmica_F%C3%ADsica_%28LibreTexts%29/06%3A_El_%C3%A1tomo_de_hidr%C3%B3geno/6.02%3A_Las_funciones_de_onda_de_un_rotador_r%C3%ADgido_se_denominan_arm%C3%B3nicos_esf%C3%A9ricos

# Polschnitte aus 2.h) (Doppelpeak bei ca. 5000 Hz)
hPolschnitt4965 = DatenEinlesen("../../Messwerte/Tag-1/teil2_h_4965Hz_polar.dat", ZeilenCutoff=3, Spaltenzahl=3)
hPolschnitt4986 = DatenEinlesen("../../Messwerte/Tag-1/teil2_h_4986Hz_polar.dat", ZeilenCutoff=3, Spaltenzahl=3)
hPolschnitteQuantenzahlen = [(0,0), ()]    # Tupel (l,m)

# --DEFINIERE LEGENDRE-FITFUNKTIONEN---



# ---POLSCHNITTE MIT FITS PLOTTEN---
def GradZuRadians(Grad):
    return list(2 * np.pi / 360 * g for g in Grad)

def ErgaenzeSymmetrie(Winkel, Radius):
    n = len(Winkel)

    for i in range(1, 4):
        for j in range(n):
            Winkel.append(Winkel[j] + 90 * i)
            Radius.append(Radius[j])

    return Winkel, Radius

plt.axes(projection = "polar")
plt.scatter(GradZuRadians(gPolschnitt2300[1]), gPolschnitt2300[2])
plt.show()

# TODO
# für alle Daten aus 2.g), 2.h): in Polarkoordinatensystem die Polschnitte plotten
# für passende l,m (idk, einfach Ausprobieren?) je einen Legendre-Fit durchführen
# (Funktionen sind in Skripttabelle 1.1.; für Fit diese noch mit einer konstanten Amplitude als Fitparameter skalieren)
