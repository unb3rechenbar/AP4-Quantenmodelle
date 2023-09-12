import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.append("..")
from header.APbrainLite import *

sys.path.append("..")
from header.APbrainLite import *
from header.PlottenInCool import *

# ---DATEN---
Oszi1 = DatenEinlesen("../../Messwerte/Tag-2/NewFile1.csv", ZeilenCutoff=2, Spaltenzahl=4,
                      Spaltensep=",") # Daten aus 4.g), für 1-sigma-Orbitale

# Daten aus 4.j)
# Daten für Resonanz bei f=2295
Oszi90Grad2295 = DatenEinlesen("../../Messwerte/Tag-2/NewFile4.csv", ZeilenCutoff=2, Spaltenzahl=4,
                      Spaltensep=",")
Oszi90Grad2295Cutoff = [0, 200]
Oszi90Grad2295Label = "Phasen2205_90Grad"

Oszi180Grad2295 = DatenEinlesen("../../Messwerte/Tag-2/NewFile8.csv", ZeilenCutoff=2, Spaltenzahl=4,
                      Spaltensep=",")
Oszi180Grad2295Cutoff = [0, 200]
Oszi180Grad2295Label = "Phasen2205_180Grad"


# Daten für Resonanz bei f=2306
Oszi0Grad2306 = DatenEinlesen("../../Messwerte/Tag-2/NewFile6.csv", ZeilenCutoff=2, Spaltenzahl=4,
                      Spaltensep=",")
Oszi0Grad2306Cutoff = [0, 200]
Oszi0Grad2306Label = "Phasen2306_0Grad"

Oszi90Grad2306 = DatenEinlesen("../../Messwerte/Tag-2/NewFile5.csv", ZeilenCutoff=2, Spaltenzahl=4,
                      Spaltensep=",")
Oszi90Grad2306Cutoff = [0, 200]
Oszi90Grad2306Label = "Phasen2306_90Grad"

Oszi180Grad2306 = DatenEinlesen("../../Messwerte/Tag-2/NewFile9.csv", ZeilenCutoff=2, Spaltenzahl=4,
                      Spaltensep=",")
Oszi180Grad2306Cutoff = [0, 200]
Oszi180Grad2306Label = "Phasen2306_180Grad"


# Daten für Resonanz bei f=2456
Oszi0Grad2456 = DatenEinlesen("../../Messwerte/Tag-2/NewFile7.csv", ZeilenCutoff=2, Spaltenzahl=4,
                      Spaltensep=",")
Oszi0Grad2456Cutoff = [0, 200]
Oszi0Grad2456Label = "Phasen2456_0Grad"

Oszi90Grad2456 = DatenEinlesen("../../Messwerte/Tag-2/NewFile6.csv", ZeilenCutoff=2, Spaltenzahl=4,
                      Spaltensep=",")
Oszi90Grad2456Cutoff = [0, 200]
Oszi90Grad2456Label = "Phasen2456_90Grad"



OsziDaten = [Oszi90Grad2295, Oszi180Grad2295,
             Oszi0Grad2306, Oszi90Grad2306, Oszi180Grad2306,
             Oszi0Grad2456, Oszi90Grad2456]
OsziCutoffs = [Oszi90Grad2295Cutoff, Oszi180Grad2295Cutoff,
               Oszi0Grad2306Cutoff, Oszi90Grad2306Cutoff, Oszi180Grad2306Cutoff,
               Oszi0Grad2456Cutoff, Oszi90Grad2456Cutoff]
OsziLabel = [Oszi90Grad2295Label, Oszi180Grad2295Label,
               Oszi0Grad2306Label, Oszi90Grad2306Label, Oszi180Grad2306Label,
               Oszi0Grad2456Label, Oszi90Grad2456Label]

# ---PLOTTE DATTEN---
def RenormalisiereListe(Liste, Amplitude=1): # normiert Listenwerte auf gegebene Amplitude
    Liste = np.array(Liste)
    Liste = Liste/max(Liste) * Amplitude
    return Liste

for i, Oszi in enumerate(OsziDaten):
    untereGrenze, obereGrenze = BestimmeCutoffIndex(Oszi[0], OsziCutoffs[i][0]), BestimmeCutoffIndex(Oszi[0], OsziCutoffs[i][1])

    Oszi[0] = Oszi[0][untereGrenze:obereGrenze]
    Oszi[2] = RenormalisiereListe(Oszi[2][untereGrenze:obereGrenze])
    Oszi[3] = RenormalisiereListe(Oszi[3][untereGrenze:obereGrenze]) - 2.25

    plt.plot(Oszi[0], Oszi[2], color="blue", label="oben")
    plt.plot(Oszi[0], Oszi[3], color="violet", label="unten")
    LabelPlot("Frequenz in Hz", "Normalisierte Amplitude")
    SpeicherPlot("IV_j_%s.jpg" % OsziLabel[i])

# TODO
