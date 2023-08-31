import sys

import matplotlib.pyplot as plt

sys.path.append("..")
from header.APbrainLite import *
from header.PlottenInCool import *
import aa_Transferfunktion as transfer


# ---DATEN---
xResonanzkurve, yResonanzkurve = DatenEinlesen("../../Messwerte/Tag-1/teil1_125cm.dat") # Daten aus 1.d)


# ---PLOTTE ROHDATEN---
plt.plot(xResonanzkurve, yResonanzkurve, label="Messdaten")
LabelPlot("Frequenz in Hz", "Amplitude")
SpeicherPlot("I_f_Rohspektrum.jpg")

# ---PRÄPERIERE DATEN---
zeigeSpektrum = False
if zeigeSpektrum:
    plt.plot(xResonanzkurve, yResonanzkurve)
    VertikaleLinien(transfer.Peaks)
    plt.show()
    exit()

vorigePeaks = 4      # Anzahl der Peaks, die vor einer ausgewählten Maximumsfrequenz der Transferfunktion (grob 5000) liegen
vordererCutoff, hintererCutoff = BestimmeCutoffIndex(xResonanzkurve, 5000), BestimmeCutoffIndex(xResonanzkurve, 13500)

# Daten im folgenden Intervall sollten nicht verzerrt sein
xResonanzkurve = xResonanzkurve[vordererCutoff: hintererCutoff]
yResonanzkurve = yResonanzkurve[vordererCutoff: hintererCutoff]


# ---BESTIMME FIT-INTERVALLE---
Peaks = BestimmeExtrema(yResonanzkurve, func=max, Nachbarn=20)[1:-1]    # erster und letzter Peak sind nur Grenzerscheinungen
Valleys = BestimmeExtrema(yResonanzkurve, func=min, Nachbarn=20)[1:]    # erstes Valley ist doppelt

# suche für jeden Peak die zwei nächstliegenden Valleys und nehme Bereich dazwischen als Fitintervall
Intervalle = []
for p in Peaks:
    ValleysKopie = list(v for v in Valleys)
    ValleysKopie.sort(key= lambda v: abs(xResonanzkurve[v] - xResonanzkurve[p]))
    a, b = ValleysKopie[0], ValleysKopie[1]

    Intervalle.append((min(a, b), max(a, b), p))


# ---PLOTTE VORBEREITETE DATEN---
for i, p in enumerate(Peaks):
    if i == 0:
        plt.axvline(xResonanzkurve[p], color="red", label="Peaks")
    else:
        plt.axvline(xResonanzkurve[p], color="red")

Farben = ["firebrick", "orange", "yellow", "green", "cyan", "navy", "purple"]
for i, (a,b, p) in enumerate(Intervalle):
    plt.axvspan(xResonanzkurve[a], xResonanzkurve[b], alpha=0.25, color=Farben[i])

plt.plot(xResonanzkurve, yResonanzkurve, label="Messdaten")
LabelPlot("Frequenz in Hz", "Amplitude")
SpeicherPlot("I_f_LorentzfitVorbereitung.jpg")


# ---LORENTZ-FIT FÜR JEDES INTERVALL---
def LorentzFit(w, A, w0, y, c):
    return A / ((w - w0)**2 + y**2) + c

Ordnungen = []
FitParameter = []

for n, (a, b, p) in enumerate(Intervalle):
    xDaten = np.array(xResonanzkurve[a:b])
    yDaten = np.array(yResonanzkurve[a:b])

    # rate Anfangswerte für Parameter
    w0 = xResonanzkurve[p]
    c = yDaten[-1]
    y = 40
    A = (yResonanzkurve[p] - c) * y**2

    Parameter = BestimmeFitParameter(WerttupelListe(xDaten, 0), WerttupelListe(yDaten, 0.01), LorentzFit,
                                     WerteGeraten=[A, w0, y, c])
    Ordnungen.append(n + vorigePeaks)
    FitParameter.append(Parameter)

print(ErstelleTabelle(["Ordnung", "Amplitude", "Eigenfrequenz", "Dämpfungskonstante", "Offset"],
                      [(n,*p) for n, p in zip(Ordnungen, FitParameter)],
                      Unterschrift="Fitparameter für die verschiedenen Resonanzordnungen", Label="tab:LorentzParameter"))


# ---EXEMPLARISCHER FITPLOT---
a, b, p = Intervalle[0]
xDaten, yDaten = xResonanzkurve[a:b], yResonanzkurve[a:b]
plt.plot(xDaten, yDaten, label="Messdaten")
PlotteFit(xDaten, LorentzFit, FitParameter[0], Label="Lorentz-Fitkurve")
LabelPlot("Frequenz in Hz", "Amplitude")
SpeicherPlot("I_f_LorentzfitBeispiel.jpg")


# ---BESTIMME LEBENSDAUER---
Daempfungskonstante = []
Lebensdauer = []

for A, w0, y, c in FitParameter:
    Daempfungskonstante.append(y)
    Lebensdauer.append(1 / y)


# ---PLOTTE LEBENSDAUER UND DÄMPFUNG---
fig, axis1 = plt.subplots()

axis1.scatter(Ordnungen, Daempfungskonstante, color="red", label="Dämpfungsparameter")
axis1.set_xlabel("Frequenz in Hz", fontsize=12)
axis1.set_ylabel("Dämpfung in Hz", fontsize=12)
axis1.tick_params(axis="y", labelcolor="red")

axis2 = axis1.twinx()

axis2.scatter(Ordnungen, Lebensdauer, marker="s", color="blue", label="Lebensdauer")
axis2.set_ylabel("Zeit in s", fontsize=12)
axis2.tick_params(axis="y", labelcolor="blue")

axis1.legend(fontsize=12)
axis2.legend(fontsize=12)

fig.tight_layout()
SpeicherPlot("I_f_Lebensdauer.jpg")

# TODO
# Frequenzspektren aus 1.c) und 1.d) plotten
# NUR FÜR DATEN AUS 1.d): sieben+ Peaks auswählen und für die Messpunkte um jeden dieser Peak einen Lorentz-Fit
# (Skript-Gleichung 1.10) aufnehmen -> Parameter Dämpfungskonstante y bestimmen
# ACHTUNG: nur Peaks auswählen, deren Frequenzen größer sind als die Peaks der Transferfunktion, siehe 0_Transferfunktion.py
# y und 1/y über Resonanzordnung plotten
