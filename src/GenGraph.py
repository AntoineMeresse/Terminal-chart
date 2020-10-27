import os
import matplotlib as mpl
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using non-interactive Agg backend')
    mpl.use('Agg')
import matplotlib.pyplot as plt
from src.GraphDatas import *
from scipy.stats import gaussian_kde

class GenGraph:

    def __init__(self):
        # print("Init genGraph.")
        self.graphDatas = GraphDatas() # On délégue le travail a cette classe

        # Prop Affichage
        self.title = ""
        self.xAxisName = ""
        self.yAxisName = ""
        self.xLabelRotate = 0

        self.labelTextSize = 13
        self.titleTextSize = 16
        self.lineWidth = 2

        # Borne
        self.xmin = None
        self.xmax = None

        self.ymin = None
        self.ymax = None

        #Gray
        self.gray = False

        self.linestyle = ['-', '--', '-.', ':', (0, (3, 1, 1, 1, 1, 1))] # https://matplotlib.org/3.1.0/gallery/lines_bars_and_markers/linestyles.html
        self.markers = [".", "o", "^", "s", "*", "D"] # https://matplotlib.org/3.2.1/api/markers_api.html
        self.hatch = ['/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '*']

        self.fig = None

    def initFigure(self, figureSize):
        """
        Method to init a figure to change the size of an image using args.
        Not working yet.
        :param figureSize: a list
        """
        # A regarder : https://stackoverflow.com/questions/9603230/how-to-use-matplotlib-tight-layout-with-figure
        self.fig, self.ax = plt.subplots(nrows=1, ncols=1, figsize=figureSize)
        plt.figure(figsize=figureSize)


    def grayScale(self):
        """
        Method to set gray scale
        """
        self.gray = True
        plt.style.use('grayscale')

    def presentationMode(self):
        """
        Method to change font size, ... TODO
        """
        self.titleTextSize = 22
        self.labelTextSize = 19
        self.lineWidth = 5
        plt.rcParams.update({'font.size': 18})

    def setTitle(self, title):
        """
        Method to add a title to the graph.

        :param title : a string for the title

        Example(s):

        >>> graph = GenGraph()
        >>> graph.title
        ''

        >>> graph.setTitle("New title")
        >>> graph.title
        'New title'


        >>> graph.setTitle(1234)
        Traceback (most recent call last):
        ...
        AssertionError: title has to be a string
        """
        assert(type(title) == str), "title has to be a string"
        self.title = title.encode().decode('unicode-escape')
        plt.title(self.title, fontsize=self.titleTextSize)

    def setAxisName_X(self, xAxisName):
        """
        Method to add a name to x axis on the graph.

        :param xAxisName : a string for the axis name

        Example(s):

        >>> graph = GenGraph()
        >>> graph.xAxisName
        ''
        >>> graph.setAxisName_X("X Axis")
        >>> graph.xAxisName
        'X Axis'

        >>> graph.setAxisName_X(1234)
        Traceback (most recent call last):
        ...
        AssertionError: xAxisName has to be a string
        """
        assert(type(xAxisName) == str), "xAxisName has to be a string"
        self.xAxisName = xAxisName
        plt.xlabel(self.xAxisName, fontsize=self.labelTextSize)

    def setAxisName_Y(self, yAxisName):
        """
        Method to add a name to y axis on the graph.

        :param yAxisName : a string for the axis name

        Example(s):

        >>> graph = GenGraph()
        >>> graph.yAxisName
        ''
        >>> graph.setAxisName_Y("Y Axis")
        >>> graph.yAxisName
        'Y Axis'

        >>> graph.setAxisName_Y(1234)
        Traceback (most recent call last):
        ...
        AssertionError: yAxisName has to be a string
        """
        assert(type(yAxisName) == str), "yAxisName has to be a string"
        self.yAxisName = yAxisName
        plt.ylabel(self.yAxisName, fontsize=self.labelTextSize)

    def rotate_text_x_label(self, angle):
        """
        Method to rotate label on x axis.

        :param angle: a number

        Example(s):

        >>> graph = GenGraph()
        >>> graph.xLabelRotate
        0

        >>> graph.rotate_text_x_label(90)
        >>> graph.xLabelRotate
        90

        >>> graph.rotate_text_x_label("test")
        Traceback (most recent call last):
        ...
        AssertionError: angle has to be a number
        """
        assert(type(angle) == float or type(angle) == int), "angle has to be a number"
        self.xLabelRotate = angle;
        plt.xticks(rotation=self.xLabelRotate)

    def external_code(self, code):
        """
        Method to execute python code.

        :param code: a list of string

        Example(s):

        >>> graph = GenGraph()
        >>> code = ["print(1)","print(3)","print(2)"]
        >>> graph.external_code(code)
        1
        3
        2

        >>> code2 = ["a = 2\\na+=1\\nprint(a==3)"]
        >>> graph.external_code(code2)
        True
        """
        for elem in code:
            exec(elem)

    def logScale(self, axis):
        """
        Method to change axis scale to log !! On ne peut changer que l'axe y à voir !!

        :param axis: a string

        Example(s):

        >>> graph = GenGraph()
        >>> graph.logScale("unknown")
        'No changes'

        >>> graph.logScale("x")
        'X axis scale change to Log'

        >>> graph.logScale("y")
        'Y axis scale change to Log'

        >>> graph.logScale("xy")
        'X and Y scale change to Log'

        >>> graph.logScale("yx")
        'X and Y scale change to Log'
        """
        if(axis == "x"):
            plt.xscale('symlog')
            return "X axis scale change to Log"
        elif(axis == "y"):
            plt.yscale('symlog')
            return "Y axis scale change to Log"
        elif(axis == "xy" or axis == "yx"):
            plt.xscale('symlog')
            plt.yscale('symlog')
            return "X and Y scale change to Log"
        else:
            return "No changes"


    def setXlim(self,minMaxlist):
        """
        Method to set min and max for the x axis.
        :param minMaxlist: a list which contains a min and a max

        Example(s):

        >>> g = GenGraph()
        >>> g.xmin == None
        True
        >>> g.xmax == None
        True

        >>> g.setXlim([10,20])
        >>> g.xmin
        10
        >>> g.xmax
        20

        >>> g.setXlim([1,2,3])
        Traceback (most recent call last):
        ...
        AssertionError: the length of the list has to be 2
        """
        assert(len(minMaxlist)==2),"the length of the list has to be 2"
        self.xmin = minMaxlist[0]
        self.xmax = minMaxlist[1]
        plt.xlim(self.xmin,self.xmax)

    def setYlim(self,minMaxlist):
        """
        Method to set min and max for the y axis.
        :param minMaxlist: a list which contains a min and a max

        Example(s):

        >>> g = GenGraph()
        >>> g.ymin == None
        True
        >>> g.ymax == None
        True

        >>> g.setYlim([10,20])
        >>> g.ymin
        10
        >>> g.ymax
        20

        >>> g.setYlim([1,2,3])
        Traceback (most recent call last):
        ...
        AssertionError: the length of the list has to be 2
        """
        assert(len(minMaxlist)==2),"the length of the list has to be 2"
        self.ymin = minMaxlist[0]
        self.ymax = minMaxlist[1]
        plt.ylim(self.ymin,self.ymax)

    def legends(self, lst=None):
        """
        Method to add a legend.
        """
        legends = self.graphDatas.getLegends()
        if len(legends) > 0:
            if lst is None:
                plt.legend(legends)
            else:
                plt.legend(lst, legends)

    def marge(self):
        """
        Method to auto adjust margin
        """
        if self.fig != None:
            print("MARRRGE")
            self.fig.tight_layout()
        else:
            plt.tight_layout()

    def barGraph(self):
        """
        Method to draw a bar graph.
        """
        x = self.graphDatas.getNames()[0]
        y = self.graphDatas.getValues()
        nbElem = len(y)
        if nbElem <= 1:
            plt.bar(x, y[0])
        else:
            barWidth = 0.3
            r = list()
            r.append(np.arange(len(y[0])))
            for i in range(1, nbElem):
                r.append([x + barWidth for x in r[i-1]])
            for j in range(0, nbElem):
                if not self.gray:
                    plt.bar(r[j], y[j], width=barWidth)
                else:
                    plt.bar(r[j], y[j], width=barWidth, hatch=self.hatch[j])
            plt.xticks([r + barWidth for r in range(len(y[0]))], x)
        self.legends()
        self.marge()

    def scatterGraph(self):
        """
        Method to draw a scatterGraph
        """
        for i in range(len(self.graphDatas.getValues())):
            x = self.graphDatas.getNames()[0]
            y = self.graphDatas.getValues()[i]
            if not self.gray:
                plt.scatter(x, y)
            else:
                plt.scatter(x, y, marker=self.markers[i])

        self.legends()
        self.marge()

    def plotGraph(self):
        """
        Method to draw a plotGraph
        """
        for i in range(len(self.graphDatas.getValues())):
            x = self.graphDatas.getNames()[0]
            y = self.graphDatas.getValues()[i]
            if not self.gray:
                plt.plot(x, y, linewidth=self.lineWidth)
            else:
                plt.plot(x, y, linestyle=self.linestyle[i], linewidth=self.lineWidth)
        self.legends()
        self.marge()

    def heatmap(self, args):
        """
        Method to draw a heatmap graph.
        """
        x = self.graphDatas.getNames()[0]
        y = self.graphDatas.getValues()[0]
        if args == -1:
            plt.hist2d(x, y, cmap=plt.cm.jet)
        else:
            plt.hist2d(x, y, (args, args), cmap=plt.cm.jet)
        plt.colorbar()
        self.marge()
        if self.gray:
            plt.gray()

    def densityGraph(self):
        """
        Method to draw a density graph, same as scatter but color of points change with the density.
        If it's not an usefull type of graph, can be deleted and also the import ( from scipy.stats import gaussian_kde ).
        """
        for i in range(len(self.graphDatas.getValues())):
            x = self.graphDatas.getNames()[0]
            y = self.graphDatas.getValues()[i]
            xy = np.vstack([x, y])
            z = gaussian_kde(xy)(xy)
            idx = z.argsort()
            plt.scatter(x[idx], y[idx], c=z[idx], s=50, edgecolor='')
        self.marge()

    def stackGraph(self):
        """
        Method to draw a stacked bar graph
        """
        n = len(self.graphDatas.getValues()[0])
        ind = np.arange(n)

        names = self.graphDatas.getNames()[0]
        values = self.graphDatas.getValues()
        r = list()

        barWidth = 1

        r.append(plt.bar(ind, values[0], width=barWidth))

        for i in range(1,len(values)):
            if i >= 2:
                somme = values[0]
                for j in range(1,i):
                    somme += values[j]
                if not self.gray:
                    r.append(plt.bar(ind, values[i], bottom=somme, width=barWidth))
                else:
                    r.append(plt.bar(ind, values[i], bottom=somme, width=barWidth, hatch=self.hatch[i]))
            else:
                if not self.gray:
                    r.append(plt.bar(ind, values[i], bottom=values[i-1], width=barWidth))
                else:
                    r.append(plt.bar(ind, values[i], bottom=values[i - 1], width=barWidth, hatch=self.hatch[i]))
        plt.xticks(ind, names)
        self.legends(r)
        self.marge()

    def boxplot(self, filenameSize):
        """
        Method to draw a boxplot graph.
        """
        plt.boxplot(self.graphDatas.values)
        if filenameSize in ["short", "s"]:
            fname = list()
            for x in self.graphDatas.getFiles():
                fname.append(x.split("/")[-1])
        else:
            fname = self.graphDatas.getFiles()
        plt.xticks([x for x in range(1, len(self.graphDatas.getValues())+1)], fname)
        self.legends()
        self.marge()

    def displayGraph(self):
        """
        Method to display the graph
        """
        plt.show()
