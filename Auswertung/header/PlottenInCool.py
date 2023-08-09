import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(7, 5))


# vertikale Linien einzeichnen
def VertikaleLinien(VertikaleLinien, Label=""):
    for i, W in enumerate(VertikaleLinien):
        if i == len(VertikaleLinien) - 1:
            plt.axvspan(W.Wert - W.Unsicherheit, W.Wert + W.Unsicherheit, color="red", alpha=0.5, label=Label)
        else:
            plt.axvspan(W.Wert - W.Unsicherheit, W.Wert + W.Unsicherheit, color="red", alpha=0.5, label="")


# initiailisert Beschriftungen und Legende
def LabelPlot(xLabel, yLabel, LegendenPos=None):
    plt.xlabel(xLabel, fontsize=12)
    plt.ylabel(yLabel, fontsize=12)

    if LegendenPos is None:
        plt.legend(fontsize=12)
    else:
        plt.legend(fontsize=12, loc=LegendenPos)

# speichert Plots
def SpeicherPlot(Pfad):
    plt.savefig("../../Versuchsbericht/Bilddateien/Auswertung/" + Pfad)
    plt.clf()


# plottet Fitkurve
def PlotteFit(xDaten, FitKurve, Fitparameter, Label="Fit-Kurve", Datenweite=1000):
    xDaten = np.linspace(min(xDaten), max(xDaten), Datenweite)
    plt.plot(xDaten, FitKurve(xDaten, *Fitparameter), label=Label)


# bestimmt Index, ab dem Listenelemente bestimmen Wert übersteigen
def BestimmeCutoffIndex(Liste, Cutoff):
    for i in range(len(Liste)):
        if Liste[i] >= Cutoff:
            return i

    return len(Liste) - 1


# testet, ob Punkt lokaler Extremalpunkt in der Umgebung ist
def _istExtremum(Punkt, Umgebung, func=max):
    if Punkt == func(Umgebung):
        return True


# findet optische Extrema im Graphen (Nachbarn: Anzahl von Datenpunkten JE rechts und links, von denen ein Punkt extremal sein muss)
# func: max für Maximum, min für Minimum
def BestimmeExtrema(Daten, Nachbarn=10, func=max):
    Extrema = []

    for i in range(len(Daten)):
        if _istExtremum(Daten[i], Daten[i - min(i, Nachbarn) : i + min(len(Daten) - 1 - i, Nachbarn)], func=func):
            Extrema.append(i)

    return Extrema
