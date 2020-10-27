import argparse


class Arguments:

    def __init__(self,handlerObject):
        #  print("Init arguments")
        self.handlerObject = handlerObject
        self.initParser()

    def initParser(self):
        self.parser = argparse.ArgumentParser(description="Generate graphics")

        self.parser.add_argument('-x', '--xvalue', type=int, dest="-x", nargs="+", help= "Choisir la colonne (-x) pour l'axe des abscisses.")
        self.parser.add_argument('-y', '--yvalue', type=int, dest="-y",  nargs="+", help= "Choisir la colonne (-y) pour l'axe des ordonees.")
        self.parser.add_argument('-r', '--rotateX', type=int,  dest="-rotateX",  help= "Permet d'appliquer une rotation (degres) des labels")

        self.parser.add_argument('-title', '--titleGraph',  dest="-title", type=str, help = "Titre du graphe" )
        self.parser.add_argument('-xname', '--xAxisName',  dest="-xname", type=str, help = "Nom de l'axe des x" )
        self.parser.add_argument('-yname', '--yAxisName',  dest="-yname", type=str, help = "Nom de l'axe des y" )
        self.parser.add_argument('-code', '--codePython',  dest="-code", type=str, nargs="+", help = "Permet d'écrire du code python" )
        self.parser.add_argument('-log', '--logScale',  dest="-log", type=str, help = "Permet de changer l'echelle en logarithmique" )
        self.parser.add_argument('-save', '--saveGraph',  dest="-save", type=str, help = "Sauvegarder une image, metadata disponible pour format : PNG, PDF" )

        self.parser.add_argument('-file', '--fileOrStdin', type=str, dest="-file", default="pipe", nargs="+", help="Ouvrir un fichier de données")
        self.parser.add_argument('-s', '--separator', dest="-s", type=str, help = "Changer le séparateur par défaut (' ', espace)")

        self.parser.add_argument('-skip', '--skipFirstLine',  dest="-skip", action='store_true', help = "Ne pas prendre en compte la première ligne d'un fichier" )

        self.parser.add_argument('-bar', '--barGraph',  dest="-bar", action='store_true', help = "Permet de creer un graphe de type : bar")
        self.parser.add_argument('-stack', '--stackedBar', dest="-stack", action='store_true', help="Permet de creer un graphe de type : Stacked bar")
        self.parser.add_argument('-plot', '--plotGraph',  dest="-plot", action='store_true', help = "Permet de creer un graphe de type : plot")
        self.parser.add_argument('-scatter', '--scatterGraph',  dest="-scatter", action='store_true', help = "Permet de creer un graphe de type : scatter")
        self.parser.add_argument('-dens', '--density', dest="-dens", action='store_true', help="Permet de creer un graphe de densité")
        self.parser.add_argument("-hmap" , "--heatmap", dest="-hmap", nargs="?", const="-1", type=int,  help="Permet de creer un graphe de type : heatmap")  # -1 default value
        self.parser.add_argument('-box', '--boxplotGraph',  dest="-box", nargs="?", const="long", type=str, help = "Permet de creer un graphe de type : Boxplot")

        self.parser.add_argument('-xlim', "--xlimits", dest="-xlim", type=int, nargs="+", help="Permet de spécifier la borne min et max de l'axe des abscisses")
        self.parser.add_argument('-ylim', "--ylimits", dest="-ylim", type=int, nargs="+",help="Permet de spécifier la borne min et max de l'axe des ordonées")

        self.parser.add_argument('-pres', '--presentationMode', dest="-pres", action='store_true', help="Permet de passer en mode présentation")

        self.parser.add_argument('-proc', '--processingData',  dest="-proc", type=str, help = "Appliquer une operation sur les données. Pour utiliser la données précedente utiliser (x-1)")

        self.parser.add_argument("-g", "--gray", dest="-gray", action='store_true', help="GrayScale")

        # Filtre Données
        self.parser.add_argument('-xf', '--xfilter', dest="-xf", type=str, help="Filtre sur les x")
        self.parser.add_argument('-yf', '--yfilter', dest="-yf", type=str, help="Filtre sur les y")

        self.parser.add_argument('-l', '--legend', dest="-legend", type=str, nargs="+", help="Permet d'ajouter une légende aux données affichées")

        # Valeur glissante
        self.parser.add_argument("-mg", "--moyenneGlissante", dest="-mg", nargs="?", const="2", type=int, help="Moyenne Glissante")
        self.parser.add_argument("-ming", "--minGlissante", dest="-ming", nargs="?", const="2", type=int, help="Min Glissante")
        self.parser.add_argument("-maxg", "--maxGlissante", dest="-maxg", nargs="?", const="2", type=int, help="Max Glissante")
        self.parser.add_argument("-medg", "--medianeGlissante", dest="-medg", nargs="?", const="2", type=int, help="Mediane Glissante")

        # Taille de l'image
        self.parser.add_argument("-fs", "--figuresize", dest="-fs", type=float, nargs='+', help="Permet de spécifier la hauteur/largeur ( inches )")

        self.args = self.parser.parse_args()

    def args_dict(self):
        """
        Method to build a dictionary. Key : an arg, value are the params.
        """
        res = dict()
        for arg in self.handlerObject.commands:
            res[arg] = getattr(self.args, arg)
        return(res)

if __name__ == "__main__":
    pass
