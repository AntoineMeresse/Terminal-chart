import numpy as np
from dateutil.parser import parse
from statistics import median

class GraphDatas:

    def __init__(self):
        self.names = list()
        self.values = list()
        self.files = list()

        self.legends = list()
        # Filtre
        self.xf = None
        self.yf = None
        self.namesTMP = list()
        self.valuesTMP = list()

    def isOnlyNumbers(self, dataList):
        """
        Method to check if a list is composed only of digits.

        :param dataList: a list
        :return: a boolean

        Example(s):

        >>> graph = GraphDatas()
        >>> liste1 = ["a","b","c","d"]
        >>> liste2 = ["a","b","3","4"]
        >>> liste3 = ["1","2","3","4"]
        >>> graph.isOnlyNumbers(liste1)
        False
        >>> graph.isOnlyNumbers(liste2)
        False
        >>> graph.isOnlyNumbers(liste3)
        True
        """
        for elem in dataList:
            try:
                float(elem)
            except ValueError:
                return False
        return True

    def isOnlyDate(self, dataList):
        """
        Method to check if a list is composed only of dates
        :param dataList: a list
        :return: a boolean

        Example(s):

        >>> graph = GraphDatas()
        >>> liste1 = ["a","b","c","d"]
        >>> liste2 = ["2020-08-12","2020-08-12","2020-08-12","2020-08-12"]
        >>> liste3 = ["1","2","3","2020-08-12"]
        >>> graph.isOnlyDate(liste1)
        False
        >>> graph.isOnlyDate(liste2)
        True
        >>> graph.isOnlyDate(liste3)
        True
        """
        cpt = 0
        for elem in dataList:
            try:
                parse(elem)
                cpt+=1
            except ValueError:
                pass
        return cpt == len(dataList)

    def convert_list_of_dates(self, dataList):
        """
        Method to convert a list composed only of dates into a list of date object.

        :param dataList:

        Example(s):

        >>> graph = GraphDatas()
        >>> liste1 = ["a","b","c","d"]
        >>> newList = graph.convert_list_of_dates(liste1)
        >>> newList
        ['a', 'b', 'c', 'd']

        >>> liste2 = ["2020-08-12","2020-08-12","2020-08-12","2020-08-12"]
        >>> newList = graph.convert_list_of_dates(liste2)
        >>> newList
        [datetime.datetime(2020, 8, 12, 0, 0), datetime.datetime(2020, 8, 12, 0, 0), datetime.datetime(2020, 8, 12, 0, 0), datetime.datetime(2020, 8, 12, 0, 0)]
        """
        if self.isOnlyDate(dataList):
            res = list()
            for elem in dataList:
                res += [parse(elem)]
            return res
        return dataList


    def convert_list_of_num(self, dataList):
        """
        Method to convert a list composed only of digits into a list of numbers.

        Example(s):

        >>> graph = GraphDatas()
        >>> liste2 = ["a","b",3,4]
        >>> newList = graph.convert_list_of_num(liste2)
        >>> newList
        ['a', 'b', 3, 4]

        >>> liste3 = ["1","2","3","4"]
        >>> newList = graph.convert_list_of_num(liste3)
        >>> newList
        [1.0, 2.0, 3.0, 4.0]
        """
        if self.isOnlyNumbers(dataList):
            res = list()
            for elem in dataList:
                res += [float(elem)]
            return res
        return dataList

    def convertList(self, dataList):
        """
        Method to convert in the correct types the datas
        :param dataList: a list
        :return: a list

        Example(s):

        >>> graph = GraphDatas()
        >>> liste1 = ["a","b","c","d"]
        >>> newList = graph.convertList(liste1)
        >>> newList
        ['a', 'b', 'c', 'd']

        >>> liste2 = ["2020-08-12","2020-08-12","2020-08-12","2020-08-12"]
        >>> newList = graph.convertList(liste2)
        >>> newList
        [datetime.datetime(2020, 8, 12, 0, 0), datetime.datetime(2020, 8, 12, 0, 0), datetime.datetime(2020, 8, 12, 0, 0), datetime.datetime(2020, 8, 12, 0, 0)]

        >>> liste3 = ["1","2","3","4"]
        >>> newList = graph.convertList(liste3)
        >>> newList
        [1.0, 2.0, 3.0, 4.0]
        """
        if self.isOnlyNumbers(dataList): # Obligatoirement en premier car un liste du num est detecté comme date !
            return self.convert_list_of_num(dataList)
        elif self.isOnlyDate(dataList):
            return self.convert_list_of_dates(dataList)
        else:
            return dataList


    def addNames(self, namesList):
        """
        Method to add a list of datas to names list.

        :param namesList : a list of datas.

        Example(s):
        >>> graph = GraphDatas()
        >>> graph.names
        []
        >>> graph.addNames(['A','B','C','D'])
        >>> graph.names
        [array(['A', 'B', 'C', 'D'], dtype='<U1')]

        >>> graph.addNames(12)
        Traceback (most recent call last):
        ...
        AssertionError: namesList has to be a list
        """
        assert (type(namesList) == list), "namesList has to be a list"
        self.names += [np.asarray(self.convertList(namesList))]

    def addValues(self, valuesList):
        """
        Method to add datas to values list.

        :param valuesList : a list of datas.

        Example(s):

        >>> graph = GraphDatas()
        >>> graph.values
        []
        >>> graph.addValues(["1","2","3","4"])
        >>> graph.values
        [array([1., 2., 3., 4.])]

        >>> graph.addValues(12)
        Traceback (most recent call last):
        ...
        AssertionError: valuesList has to be a list
        """
        assert (type(valuesList) == list), "valuesList has to be a list"
        self.values += [np.asarray(self.convertList(valuesList))]

    def addLegends(self, legend):
        """
        Method to ... todo

        :param legend: a string

        Example(s):
        >>> graph = GraphDatas()
        >>> graph.legends
        []
        >>> graph.addLegends(["test"])
        >>> graph.legends
        ['test']

        >>> graph.addLegends(1)
        Traceback (most recent call last):
        ...
        AssertionError: a legend has to be a list
        """
        assert(type(legend) == list), "a legend has to be a list"
        for elem in legend:
            self.legends.append(elem)


    def getNames(self):
        """
        Method to return a list : names
        :return: a list

        Example(s):

        >>> g = GraphDatas()
        >>> g.getNames()
        []
        >>> g.addNames(['11','22'])
        >>> g.getNames()
        [array([11., 22.])]
        """
        if self.names == [] and self.values != []:
            v = list()
            maxinvalues = max([len(x) for x in self.values])
            for i in range(0,len(self.values)):
                v.append([i for i in range(0, maxinvalues)])
            self.names = v
            return v
        else:
            return self.names

    def getValues(self):
        """
        Method to return a list : values
        :return: a list

        Example(s):

        >>> g = GraphDatas()
        >>> g.getValues()
        []
        >>> g.addValues(['1','2'])
        >>> g.getValues()
        [array([1., 2.])]
        """
        return self.values

    def getFiles(self):
        """
        Method to return a list : files names
        :return: a list

        Example(s):

        >>> g = GraphDatas()
        >>> g.getFiles()
        []
        >>> g.files.append('f1')
        >>> g.files.append('f2')
        >>> g.getFiles()
        ['f1', 'f2']
        """
        return self.files

    def getLegends(self):
        """
        Method to return a list : legends
        :return: a list
        """
        return self.legends

    def processingDatas(self, expression):
        """
        Method to process datas. (x-1) in the expression if you want to change values by using the previous one.
        :param expression: a string

        Example(s):

        >>> graph = GraphDatas()
        >>> graph.values
        []
        >>> graph.addValues(["1","2","3","4"])
        >>> graph.values
        [array([1., 2., 3., 4.])]

        >>> graph.processingDatas("x+2")
        [array([3., 4., 5., 6.])]

        >>> graph.processingDatas("x*100")
        [array([300., 400., 500., 600.])]

        >>> graph.processingDatas("x+(2/20)")
        [array([300.1, 400.1, 500.1, 600.1])]

        >>> graph2 = GraphDatas()
        >>> graph2.addValues(["1","2","3","4"])
        >>> graph2.processingDatas("2*(x**2)")
        [array([ 2.,  8., 18., 32.])]

        >>> graph3 = GraphDatas()
        >>> graph3.addValues(["10","100","1000","10000"])
        >>> graph3.processingDatas("x = x - (x-1)")
        [array([  10.,   90.,  900., 9000.])]
        >>> graph3.processingDatas("x = x + (x-1) + 1")
        [array([  10.,  101.,  991., 9901.])]
        """
        assert(type(expression) == str), "expression has to be a string"
        for i in range(len(self.values)):
            if "(x-1)" in expression:
                self.previousValueExpression(expression,i)
            else:
                self.normalExpression(expression, i)
        return self.values

    def normalExpression(self,expression, i):
        """
        Method used in processingData. normalExpression is here to simplify the code. Tested in processingData.
        """
        value = "self.values[" + str(i) + "]"
        exp = expression.replace("x", value)
        code = "{} = {}".format(value, exp)
        exec(code)

    def previousValueExpression(self,expression, i):
        """
        Method used in processingData. PreviousValueExpression is here to simplify the code. Tested in processingData.
        Use (x-1) in the expression if you want to change values by using the previous one.
        """
        value_cpy = [x for x in self.values[i]]
        for j in range(1,len(self.values[i])):
            tmp1 = "self.values[" + str(i) + "]["+str(j)+"]"
            tmp2 = "value_cpy["+str(j-1) + "]"
            code = expression.replace("(x-1)", tmp2)
            code = code.replace("x", tmp1)
            exec(code)

    def setXf(self, xfilter):
        """
        Method to set X filter

        :param xfilter: a String

        Example(s):

        >>> g = GraphDatas()
        >>> g.setXf("x < 10")
        >>> g.xf
        'x < 10'
        """
        self.xf = xfilter
        self.filtersCall()

    def setYf(self, yfilter):
        """
        Method to set Y filter

        :param yfilter: a String

        Example(s):

        >>> g = GraphDatas()
        >>> g.setYf("y != 12")
        >>> g.yf
        'y != 12'
        """
        self.yf = yfilter
        self.filtersCall()

    def filtersCall(self):
        """
        Method to call each type of filter (x and y)
        """
        if self.xf is not None:
            self.filterValueX(self.xf)
        elif self.yf is not None:
            self.filterValueY(self.yf)

    def evalExpression(self, elem, exp):
        """
        Method to evaluate an expression

        :param elem: an element from a list
        :param exp: and expression
        :return: a boolean

        Example(s):

        >>> graph = GraphDatas()
        >>> graph.evalExpression(3,"x >= 2 and x < 5 and x != 4")
        True
        >>> graph.evalExpression(3,"x >= 20 and x < 5 and x != 4")
        False
        >>> graph.evalExpression(3,"y >= 0 and y < 50 and y != 4")
        True
        """
        if type(elem) == np.str_:
            tmp = exp.replace("x", "'"+elem+"'")
            tmp = tmp.replace("y", "'"+elem+"'")
        else:
            tmp = exp.replace("x", str(elem))
            tmp = tmp.replace("y", str(elem))
        return eval(tmp)

    def initTmpList(self):
        """
        Method to init a list

        Example(s):

        >>> g = GraphDatas()
        >>> g.addNames(['1','2','3','4'])
        >>> g.addValues(['5','6','7','8'])
        >>> g.addValues(['9','10','11','12'])
        >>> g.names
        [array([1., 2., 3., 4.])]
        >>> g.values
        [array([5., 6., 7., 8.]), array([ 9., 10., 11., 12.])]
        >>> g.initTmpList()
        >>> g.namesTMP
        [[]]
        >>> g.valuesTMP
        [[], []]
        """
        for names in self.names:
            self.namesTMP.append([])
        for values in self.values:
            self.valuesTMP.append([])

    def addNamesValuesIndex(self, index):
        """
        Method to append names and values for elements at index given.

        Example(s):

        >>> g = GraphDatas()
        >>> g.addNames(['1','2','3','4'])
        >>> g.addValues(['5','6','7','8'])
        >>> g.addValues(['9','10','11','12'])
        >>> g.initTmpList()
        >>> g.addNamesValuesIndex(2)
        >>> g.namesTMP
        [['3.0']]
        >>> g.valuesTMP
        [['7.0'], ['11.0']]
        """
        for i in range(len(self.names)):
            self.namesTMP[i].append(str(self.names[i][index]))
        for j in range(len(self.values)):
            self.valuesTMP[j].append(str(self.values[j][index]))

    def replaceNamesAndValues(self):
        """
        Method to clear names and values list, then add names and values from temporary list (filter)
        """
        self.names = list()
        self.values = list()
        for e in self.namesTMP:
            self.addNames(e)
        for e2 in self.valuesTMP:
            self.addValues(e2)

    def filterValueX(self, expression):
        """
        Method to apply a filter on x values.

        :param expression: a String

        Example(s):

        >>> g = GraphDatas()
        >>> g.addNames(['1','2','3','4'])
        >>> g.addValues(['5','6','7','8'])
        >>> g.addValues(['9','10','11','12'])
        >>> g.values
        [array([5., 6., 7., 8.]), array([ 9., 10., 11., 12.])]
        >>> g.filterValueX("x != 3")
        >>> g.values
        [array([5., 6., 8.]), array([ 9., 10., 12.])]
        >>> g.names
        [array([1., 2., 4.])]
        """
        try:
            n = self.names[0]
            self.initTmpList()
            for i in range(len(n)):
                if self.evalExpression(n[i], expression):
                    self.addNamesValuesIndex(i)
            self.replaceNamesAndValues()
        except IndexError:
            pass

    def filterValueY(self, expression):
        """
        Method to apply a filter on y values.

        :param expression: a String

        Example(s):

        >>> g = GraphDatas()
        >>> g.addNames(['1','2','3','4'])
        >>> g.addValues(['5','6','7','8'])
        >>> g.addValues(['9','10','11','12'])
        >>> g.values
        [array([5., 6., 7., 8.]), array([ 9., 10., 11., 12.])]
        >>> g.filterValueY("y < 7 or y > 10")
        >>> g.values
        [array([ 5.,  6., nan, nan]), array([nan, nan, 11., 12.])]
        """
        for sublist in range(len(self.values)):
            for elem in range(len(self.values[sublist])):
                if not self.evalExpression(self.values[sublist][elem], expression):
                    self.values[sublist][elem] = np.nan


    def averageLst(self,lst):
        """
        Method to calculate the average of a list. Round applied

        Example(s):

        >>> g = GraphDatas()
        >>> lst = g.averageLst([1,2,3,3])
        >>> lst
        2.25
        """
        return round(sum(lst) / len(lst), 2)

    def replaceValues(self, lst):
        """
        Method to replace values

        Example(s):

        >>> g = GraphDatas()
        >>> g.addValues(["1", "2", "3"])
        >>> g.values
        [array([1., 2., 3.])]
        >>> g.replaceValues([["4", "5", "6"]])
        >>> g.values
        [array([4., 5., 6.])]
        """
        for i in range(0, len(self.values)):
            for j in range(0, len(self.values[i])):
                tmp = lst[i][j]
                if tmp == 'nan':
                    self.values[i][j] = np.nan
                else:
                    self.values[i][j] = tmp


    def movingValues(self, type, n):
        """
        Method to calculate moving values ( average , min, max, median).
        This function is tested in 4 differents functions :
            - movingAverage
            - movingMinimum
            - movingMaximum
            - movingMedian

        :param type: a String ( average, min, max, median)
        :param n: an int, the number of values taken into account
        """
        lst = list()
        for sublist in range(0,len(self.values)):
            sublist_tmp = list()
            length = len(self.values[sublist])
            if length > 2:
                for i in range(0, length):
                    if (i + 1 - n) >= 0:
                        tmp = self.values[sublist][(i-n+1):i+1]
                        if type == "average":
                            sublist_tmp.append(self.averageLst(tmp))
                        elif type == "min":
                            sublist_tmp.append(min(tmp))
                        elif type == "max":
                            sublist_tmp.append(max(tmp))
                        elif type == "mediane":
                            sublist_tmp.append(median(tmp))
                    else:
                        sublist_tmp.append('nan')
            lst.append(sublist_tmp)
        self.replaceValues(lst)

    def movingAverage(self, n):
        """
        Method to calculate moving average.

        :param n: an int, the number of values taken into account

        Example(s):

        >>> g = GraphDatas()
        >>> g.addNames(['1','2','3','4','5','6','7','8','9','10'])
        >>> g.addValues(['0.3','0.40','0.60','0.90','0.50','0.20','-0.10','-0.30','0.0','0.10'])
        >>> g.movingAverage(3)
        >>> g.values #doctest: +NORMALIZE_WHITESPACE
        [array([  nan,   nan,  0.43,  0.63,  0.67,  0.53,  0.2 , -0.07, -0.13, -0.07])]

        >>> g2 = GraphDatas()
        >>> g2.addNames(['1','2','3','4','5','6','7','8','9','10'])
        >>> g2.addValues(['0.3','0.40','0.60','0.90','0.50','0.20','-0.10','-0.30','0.0','0.10'])
        >>> g2.movingAverage(6)
        >>> g2.values #doctest: +NORMALIZE_WHITESPACE
        [array([ nan,  nan,  nan,  nan,  nan, 0.48, 0.42, 0.3 , 0.2 , 0.07])]
        """
        self.movingValues("average", n)

    def movingMinimum(self, n):
        """
        Method to calculate moving minimum.

        :param n: an int, the number of values taken into account

        Example(s):

        >>> g = GraphDatas()
        >>> g.addNames(['1','2','3','4','5','6','7','8','9','10'])
        >>> g.addValues(['0.3','0.40','0.60','0.90','0.50','0.20','-0.10','-0.30','0.0','0.10'])
        >>> g.movingMinimum(3)
        >>> g.values #doctest: +NORMALIZE_WHITESPACE
        [array([ nan,  nan,  0.3,  0.4,  0.5,  0.2, -0.1, -0.3, -0.3, -0.3])]

        >>> g2 = GraphDatas()
        >>> g2.addNames(['1','2','3','4','5','6','7','8','9','10'])
        >>> g2.addValues(['0.3','0.40','0.60','0.90','0.50','0.20','-0.10','-0.30','0.0','0.10'])
        >>> g2.movingMinimum(6)
        >>> g2.values #doctest: +NORMALIZE_WHITESPACE
        [array([ nan,  nan,  nan,  nan,  nan,  0.2, -0.1, -0.3, -0.3, -0.3])]
        """
        self.movingValues("min", n)

    def movingMaximum(self, n):
        """
        Method to calculate moving maximum.

        :param n: an int, the number of values taken into account

        Example(s):

        >>> g = GraphDatas()
        >>> g.addNames(['1','2','3','4','5','6','7','8','9','10'])
        >>> g.addValues(['0.3','0.40','0.60','0.90','0.50','0.20','-0.10','-0.30','0.0','0.10'])
        >>> g.movingMaximum(3)
        >>> g.values #doctest: +NORMALIZE_WHITESPACE
        [array([nan, nan, 0.6, 0.9, 0.9, 0.9, 0.5, 0.2, 0. , 0.1])]

        >>> g2 = GraphDatas()
        >>> g2.addNames(['1','2','3','4','5','6','7','8','9','10'])
        >>> g2.addValues(['0.3','0.40','0.60','0.90','0.50','0.20','-0.10','-0.30','0.0','0.10'])
        >>> g2.movingMaximum(6)
        >>> g2.values #doctest: +NORMALIZE_WHITESPACE
        [array([nan, nan, nan, nan, nan, 0.9, 0.9, 0.9, 0.9, 0.5])]
        """
        self.movingValues("max", n)

    def movingMedian(self, n):
        """
        Method to calculate moving median.

        :param n: an int, the number of values taken into account

        Example(s):

        >>> g = GraphDatas()
        >>> g.addNames(['1','2','3','4','5','6','7','8','9','10'])
        >>> g.addValues(['0.3','0.40','0.60','0.90','0.50','0.20','-0.10','-0.30','0.0','0.10'])
        >>> g.movingMedian(3)
        >>> g.values #doctest: +NORMALIZE_WHITESPACE
        [array([ nan,  nan,  0.4,  0.6,  0.6,  0.5,  0.2, -0.1, -0.1,  0. ])]

        >>> g2 = GraphDatas()
        >>> g2.addNames(['1','2','3','4','5','6','7','8','9','10'])
        >>> g2.addValues(['0.3','0.40','0.60','0.90','0.50','0.20','-0.10','-0.30','0.0','0.10'])
        >>> g2.movingMedian(6)
        >>> g2.values #doctest: +NORMALIZE_WHITESPACE
        [array([ nan,  nan,  nan,  nan,  nan, 0.45, 0.45, 0.35, 0.1 , 0.05])]
        """
        self.movingValues("mediane", n)







