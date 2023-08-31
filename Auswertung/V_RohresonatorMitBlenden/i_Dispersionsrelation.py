import sys

import matplotlib.pyplot as plt

sys.path.append("..")
from header.APbrainLite import *
from header.PlottenInCool import *


# ---DATEN---
# Daten zum PLotten aus 5.l) - 5.o) (lange Segmente)
lSeg8KeineBlende = DatenEinlesen("../../Messwerte/Tag-1/teil1_60cm.dat") # 8 Rohre ohne Blenden
lSeg8 = DatenEinlesen("../../Messwerte/Tag-2/Teil_2_O.dat") # 8 Rohre, 7 Blenden

# Daten zur Dispersionsrelation aus 5.l - 5.o)
lSeg8KeineBlendeDisp = DatenEinlesen("DispersionDaten/Seg8KeineBlende.dat")
lSeg1Disp = DatenEinlesen("DispersionDaten/Seg1.dat")
lSeg2Disp = DatenEinlesen("DispersionDaten/Seg2.dat")
lSeg3Disp = DatenEinlesen("DispersionDaten/Seg3.dat")
lSeg4Disp = DatenEinlesen("DispersionDaten/Seg4.dat")
lSeg8Disp = DatenEinlesen("DispersionDaten/Seg8.dat")

lKonfigurationen = [lSeg8KeineBlendeDisp, lSeg1Disp, lSeg2Disp, lSeg3Disp, lSeg4Disp, lSeg8Disp]
lKonfigurationenBlenden = ["8 Seg./ 0 Blenden", "1 Seg./ 0 Blenden", "2 Seg./ 1 Blende", "3 Seg./ 2 Blenden",
                           "4 Seg./ 3 Blenden", "8 Seg./ 7 Blenden"]


# Daten zum Plotten aus 5.p) - 5.r)
pSeg12KeineBlende = DatenEinlesen("../../Messwerte/Tag-2/Teil_2_P.dat") # 12 kurze Rohre ohne Blenden
pSeg12 = DatenEinlesen("../../Messwerte/Tag-2/Teil_2_Q.dat") # 12 kurze Rohre, 11 Blenden
pSeg12Dotiert = DatenEinlesen("../../Messwerte/Tag-2/Teil_2_R.dat") # 12 Rohre (11 kurze und 1 langes an 8. Stelle), 11 Blenden

# Daten zur Dispersionsrelation aus 5.l) - 5.o)
pSeg12KeineBlendeDisp = DatenEinlesen("DispersionDaten/KurzeSeg12KeineBlende.dat")
pSeg12Disp = DatenEinlesen("DispersionDaten/KurzeSeg12.dat")

pKonfigurationen = [pSeg12KeineBlendeDisp, pSeg12Disp]
pKonfigurationenBlenden = ["12 Seg./ 0 Blenden", "12 Seg./ 11 Blenden"]

# ---PLOTTE RESONANZKURVEN---
# Daten aus 5.l) - 5.o)
plt.plot(*lSeg8KeineBlende, alpha=0.5, label="8 Seg./ 0 Blenden")
plt.plot(*lSeg8, label="8 Seg./ 7 Blenden")

LabelPlot("Frequenz in Hz", "Amplitude")
SpeicherPlot("V_i_Resonanzspektrum_Lang.jpg")

# Daten aus 5.p) - 5.r)
plt.plot(*pSeg12KeineBlende, alpha=0.5, label="12 Seg./ 0 Blenden")
plt.plot(*pSeg12, label="12 Seg./ 11 Blenden")

LabelPlot("Frequenz in Hz", "Amplitude")
SpeicherPlot("V_l_Resonanzspektrum_Kurz.jpg")

plt.plot(*pSeg12, alpha=0.5, label="Regulär")
plt.plot(*pSeg12Dotiert, label="Dotiert")

LabelPlot("Frequenz in Hz", "Amplitude")
SpeicherPlot("V_o_Resonanzspektrum_Dotiert.jpg")


# ---PLOTTE DISPERSIONSRELATIONEN---
LangeLaenge = 0.075 # in m
KurzeLaenge = 0.05  # in m

# Daten aus 5.l) - 5.o)
for Blenden, Dispersion in zip(lKonfigurationenBlenden, lKonfigurationen):
    kVektoren = [n * np.pi / LangeLaenge for n in Dispersion[0]]

    plt.scatter(kVektoren, Dispersion[1], label=Blenden, marker="s", s=12)

LabelPlot("Richtungsvektor k in 1/m", "Frequenz in Hz")
SpeicherPlot("V_j_Dispersionsrelation_Lang.jpg")


# Daten aus 5.p) - 5.r)
for Blenden, Dispersion in zip(pKonfigurationenBlenden, pKonfigurationen):
    kVektoren = [n * np.pi / KurzeLaenge for n in Dispersion[0]]

    plt.scatter(kVektoren, Dispersion[1], label=Blenden, marker="s", s=12)

LabelPlot("Richtungsvektor k in 1/m", "Frequenz in Hz")
SpeicherPlot("V_l_Dispersionsrelation_Kurz.jpg")
