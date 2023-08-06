def StandardPGFPlot(
        X: list,
        Y: list,
        Xerror: list,
        Yerror: list,
        RegSetting: list,
        Labels: list,
        Caption: str,
        Label: str,
        Conf: list
    ):
    """Standard PGFPlot für LaTeX. Erzeugt ein PGFPlot mit den übergebenen Parametern.

    Args:
        X (list): _description_
        Y (list): _description_
        Xerror (list): _description_
        Yerror (list): _description_
        RegSetting (list): _description_
        Labels (list): _description_
        Caption (str): _description_
        Label (str): _description_
        Conf (list): _description_
    """

    colors = ["red","blue","green","yellow","orange","brown","pink"]
    
    if Conf[0] != 0:
        def Tabellenblock(X,Y,Xerror,Yerror):
            print("\t\t\tX\tY\txerror\tyerror\t\\\\")
            for i in range(0,len(X)):
                print("\t\t\t" , X[i] , "\t" , Y[i] , "\t" , Xerror[i] , "\t" , Yerror[i] , "\t\\\\")
        if Conf[1] == 0:
            print("\\begin{figure}[H]\n")
        elif Conf[1] == 1:
            print("\\begin{subfigure}[b]{0.4\\textwidth}\n")
        else:
            print("Fehlerhafte Konfigurationsanweisung!")
            exit()
        print("\t\\centering\n\t\\begin{tikzpicture}\n\t\t\\pgfplotsset{width=6.5cm,compat=1.3,legend style={font=\\footnotesize}}\n\t\t\\begin{axis}[xlabel={" + Labels[0] + "},ylabel={" + Labels[1] + "},legend cell align=left,legend pos=north west]\n\t\t")      
        for i,(x,y) in enumerate(zip(X,Y)):
            print("\\addplot+[only marks,color=" + colors[i % len(colors)] + ",mark=square,error bars/.cd,x dir=both,x explicit,y dir=both,y explicit,error bar style={color=black}] table[x=X,y=Y,x error=xerror,y error=yerror,row sep=\\\\]{")
            Tabellenblock(x,y,Xerror,Yerror[i])
            print("\t\t};")
            print("\t\t% \\addlegendentry{Messpunkte Datensatz " + str(i) + "}\n")
            if RegSetting[i] == 1:
                print("\t\t\\addplot[] table[row sep=\\\\,y={create col/linear regression={y=Y}}]{")
                Tabellenblock(x,y,Xerror,Yerror[i])
                print("\t\t};")
                print("\t\t\\addlegendentry{%\n\t\t\t$\pgfmathprintnumber{\pgfplotstableregressiona} \cdot x\pgfmathprintnumber[print sign]{\pgfplotstableregressionb}$ lin. Regression} %")
            else:
                continue
        
        print("\t\t\\end{axis}\n\t\t\\end{tikzpicture}")
        print("\t\\caption{" + Caption + "}\n\t\\label{fig:" + Label + "}")
        
        if Conf[1] == 0:
            print("\\end{figure}")
        elif Conf[1] == 1:
            print("\\end{subfigure}")
        else:
            print("Fehlerhafte Konfigurationsanweisung!")
            exit()
    else:
        pass