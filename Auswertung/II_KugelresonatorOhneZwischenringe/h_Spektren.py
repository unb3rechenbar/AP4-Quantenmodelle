import sys

import matplotlib.pyplot as plt

sys.path.append("..")
from header.APbrainLite import *
from header.PlottenInCool import *


# ---DATEN---

Kugel0 = DatenEinlesen("../../Messwerte/Tag-1/teil2_0grad.dat") # Daten aus 2.f), für den Winkel 0 Grad
Kugel60 = DatenEinlesen("../../Messwerte/Tag-1/teil2_60grad.dat") # Daten aus 2.f), für den Winkel 60 Grad
Kugel120 = DatenEinlesen("../../Messwerte/Tag-1/teil2_120grad.dat") # Daten aus 2.f), für den Winkel 120 Grad
Kugel180 = DatenEinlesen("../../Messwerte/Tag-1/teil2_180grad.dat") # Daten aus 2.f), für den Winkel 180 Grad

KugelDaten = [Kugel0, Kugel60, Kugel120, Kugel180]
KugelDatenLabels = [r"$\alpha=0°$", r"$\alpha=60°$", r"$\alpha=120°$", r"$\alpha=180°$"]

# ---PLOTTE DATEN---
for i in range(len(KugelDaten)):
    plt.plot(*KugelDaten[i],  label=KugelDatenLabels[i])
    LabelPlot("Frequenz in Hz", "Amplitude")
    SpeicherPlot("II_f_Spektrum_%i_Grad.jpg" % (60 * i))
    print("II_f_Spektrum_%i_Grad.jpg" % (60 * i))


# TODO
# Spektrum aus 2.f) plotten