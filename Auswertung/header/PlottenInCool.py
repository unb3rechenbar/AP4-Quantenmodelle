import matplotlib.pyplot as plt


# kartesischer Plot
def PlotKartesisch(x, y, xLabel="", yLabel="", DiagrammTitel="", DatenLabel="", VertikaleLinien=[], VertikaleLinienLabel="",
                   Pfad="plot.jpg", mode="show", xTicks=None, yTicks=None):

    # Diagrammgröße
    plt.figure(figsize=(7, 5))


    # Daten plotten
    plt.plot(x, y, label=DatenLabel)


    # x-Achse einstellen
    if xTicks is not None:
        plt.locator_params(axis="x", nbins=xTicks)


    # vertikale Linien einzeichnen
    for i, W in enumerate(VertikaleLinien):
        if i == len(VertikaleLinien) - 1:
            plt.axvspan(W.Wert - W.Unsicherheit, W.Wert + W.Unsicherheit, color="red", alpha=0.5, label=VertikaleLinienLabel)
        else:
            plt.axvspan(W.Wert - W.Unsicherheit, W.Wert + W.Unsicherheit, color="red", alpha=0.5, label="")

    # Label & co.
    plt.xlabel(xLabel, fontsize=12)
    plt.ylabel(yLabel, fontsize=12)

    #plt.title(DiagrammTitel)
    plt.legend(fontsize=12)

    # fertiges Produkt
    plt.plot()
    if mode == "show":
        plt.show()
    elif mode == "save":
        plt.savefig("../../Versuchsbericht/Bilddateien/Auswertung/" + Pfad)

    plt.clf()
