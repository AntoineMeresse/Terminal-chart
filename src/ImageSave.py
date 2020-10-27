import matplotlib.pyplot as plt
import os 
import piexif
import piexif.helper
from PIL import Image
import sys


class ImageSave:

    def __init__(self):
        #print("Init imageSave")
        pass

    def directoryCheck(self, dirName):
        """
        Method to create a directory with the given path
        :param dirName: a String (path)
        """
        os.makedirs(dirName, exist_ok=True)

    def saveAsImage(self, nameFile):
        """
        Method to save a graph as an image. Metada are available for png and pdf format.
        :param nameFile: a String (file name)
        """
        fullpath = nameFile
        dirs = fullpath.split("/")
        directory = "/".join(dirs[0:(len(dirs)-1)])+"/"
        
        self.directoryCheck(directory)
        
        print("\n>>>>>> "+fullpath+" has been created.")
        plt.savefig(fullpath, metadata={"Title" : self.getArgs()}) # Title ( pdf ), png key libre

    def getArgs(self):
        """
        Method to get all args and create a string for the metadata
        """
        return(" ".join(sys.argv))

