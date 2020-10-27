import sys
import re
from src.GenGraph import *


class ExtractData:

    def __init__(self, genGraph):
        #print("Init extractData.")
        self.datas = list()
        self.datasDefine = False
        self.file = "pipe" # Cas de base ou l'on prend des données de stdin
        
        self.genGraph = genGraph
        
        self.separator = " " # Separateur par défaut

    def setSeparator(self, sep):
        """
        Method to change the separator, default is whitespace (" ")

        Example(s):

        >>> obj = ExtractData(GenGraph())
        >>> obj.separator
        ' '
        
        >>> obj.setSeparator(1)
        Traceback (most recent call last):
        ...
        AssertionError
        
        >>> obj.setSeparator(",")
        >>> obj.separator
        ','
        """
        assert(type(sep)==str)
        self.separator = sep

    def data_from_pipe(self):
        """
        return : list of lines. Line are string.
        """
        return sys.stdin.readlines()

    def data_from_file(self, filename):
        """
        return : list of lines. Line are string.
        """
        with open(filename,'r') as fl:
            return fl.readlines()

    def setFile(self, filename):
        """
        Method to change file, default value of file is pipe. 

        Example(s):

        >>> obj = ExtractData(GenGraph())
        >>> obj.file
        'pipe'
        >>> obj.setFile(["datas/simpleDatas.txt"])
        >>> obj.file
        ['datas/simpleDatas.txt']
        """
        self.file = filename

    def getData(self):
        r"""
        Method to ...

        return : list of lines

        Example(s):

        >>> obj = ExtractData(GenGraph())
        >>> obj.file = ["datas/simpleDatas.txt"] # Fichier d'exemple avec 13 lignes
        >>> obj.getData()
        [['Mois       Temperature Moyenne\n', 'Janvier    2\n', 'Fevrier    3\n', 'Mars       4\n', 'Avril      12\n', 'Mai        14\n', 'Juin       21\n', 'Juillet    24\n', 'Aout       26 \n', 'Septembre  14\n', 'Octobre    15\n', 'Novembre   10\n', 'Decembre   0']]
        """
        if(not self.datasDefine):
            if(self.file == "pipe"):
                print("PIPE")
                self.datas.append(self.data_from_pipe())
            else:
                for elem in self.file:
                    if elem != '':
                        self.datas.append(self.data_from_file(elem))
                        self.genGraph.graphDatas.files.append(elem)
            self.datasDefine = True
        return self.datas


    def skipFirstLine(self):
        r"""
        Method to skip first line of your file data

        Example(s):

        >>> obj = ExtractData(GenGraph())
        >>> obj.file = ["datas/simpleDatas.txt"] # Fichier d'exemple avec 13 lignes
        >>> obj.getData()
        [['Mois       Temperature Moyenne\n', 'Janvier    2\n', 'Fevrier    3\n', 'Mars       4\n', 'Avril      12\n', 'Mai        14\n', 'Juin       21\n', 'Juillet    24\n', 'Aout       26 \n', 'Septembre  14\n', 'Octobre    15\n', 'Novembre   10\n', 'Decembre   0']]
        >>> firstelem = obj.datas[0]
        >>> len(firstelem)
        13
        >>> obj.skipFirstLine()
        >>> firstelem = obj.datas[0]
        >>> len(firstelem)
        12
        """
        self.datas = self.getData()
        for i in range(len(self.datas)):
            self.datas[i] = self.datas[i][1:len(self.datas[i])]


    def getCleanData(self,lign):
        """
        Method to extract and create a clean data list.

        param lign        : a string of datas
        return            : a list of clean elements split by a separator 

        Example(s):

        >>> obj = ExtractData(GenGraph())
        >>> lign = "udev                 4052132        0    4052132   0% /dev\\n"
        >>> obj.getCleanData(lign)
        ['udev', '4052132', '0', '4052132', '0%', '/dev']

        >>> obj.setSeparator(",")
        >>> lign = "udev         ,       4052132   ,     0  ,  4052132 ,  0% ,/dev\\n"
        >>> obj.getCleanData(lign)
        ['udev', '4052132', '0', '4052132', '0%', '/dev']
        """
        tmp = re.sub("\n+", "", lign)
        splt = tmp.split(self.separator)
        res = list()
        for elem in splt:
            e = elem.strip()
            if elem != "":
                res.append(e)  # Fix problem
        return res


    def extract_column(self, columnNumber):
        """
        param columnNumber : colomn number
        return             : a list

        Example(s):

        >>> obj = ExtractData(GenGraph())
        >>> obj.file = ["datas/simpleDatas.txt", "datas/simpleDatas2.txt"]
        
        >>> obj.extract_column(4) # Erreur
        Traceback (most recent call last):
        ...
        AssertionError

        >>> obj.extract_column(0)
        [['Mois', 'Janvier', 'Fevrier', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Aout', 'Septembre', 'Octobre', 'Novembre', 'Decembre'], ['Mois', 'Janvier', 'Fevrier', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Aout', 'Septembre', 'Octobre', 'Novembre', 'Decembre']]

        >>> obj.extract_column(1)
        [['Temperature', '2', '3', '4', '12', '14', '21', '24', '26', '14', '15', '10', '0'], ['Temperature', '4', '5', '6', '14', '16', '23', '26', '28', '16', '17', '12', '2']]
        """
        datas = self.getData()
        res = list()
        for elem in datas:
            tmp = list()
            for lign in elem:
                infos = self.getCleanData(lign)
                assert(columnNumber <= len(infos))
                e = (infos[columnNumber])
                tmp += [e]
            res.append(tmp)
        return res


    def extract_column_x(self,columnNumber):
        """
        Method to extract datas for x axis in matplotlib

        param columnNumber : colomn number

        Example(s):

        >>> graph = GenGraph()
        >>> obj = ExtractData(graph)
        >>> obj.file = ["datas/simpleDatas.txt"]

        >>> graph.graphDatas.getNames()
        []
        >>> obj.extract_column_x([0])
        >>> len(graph.graphDatas.getNames()[0])
        13
        """
        assert (type(columnNumber) == list)
        for elem in columnNumber:
            res = self.extract_column(elem)
            for e in res:
                self.genGraph.graphDatas.addNames(e)

    def extract_column_y(self,columnNumber):
        """
        Method to extract datas for y axis in matplotlib

        param columnNumber : colomn number

        Example(s):

        >>> graph = GenGraph()
        >>> obj = ExtractData(graph)
        >>> obj.file = ["datas/simpleDatas.txt"]

        >>> graph.graphDatas.getValues()
        []
        >>> obj.extract_column_y([0, 1])
        >>> len(graph.graphDatas.getValues())
        2
        """
        assert(type(columnNumber) == list)
        for elem in columnNumber:
            res = self.extract_column(elem)
            for e in res:
                self.genGraph.graphDatas.addValues(e)

