from src.Arguments import *
from src.HandlerObj import *
from src.ImageSave import *
from src.ExtractData import *
from src.GenGraph import *


class Main:

    def __init__(self):
        self.genGraphObject = GenGraph()  # Objet genGraph
        self.extractDataObject = ExtractData(self.genGraphObject)  # Objet extractData
        self.imageSave = ImageSave()  # Objet imageSave
        self.handlerObject = HandlerObj(self.genGraphObject, self.extractDataObject, self.imageSave)  # Objet handlerObj
        self.arguments = Arguments(self.handlerObject)  # Objet arguments
          
    def mainFunction(self):
        options = self.arguments.args_dict()
        for command,param in options.items():
            # print(command+","+str(param)+", type : "+str(type(param)))
            if( ((type(param) != type(None)) and (param != False)) or (type(param) == int)):
                # Obliger de tester int car 0 considérer comme False !
                if(param == True and (type(param) != int)): # print("Cas commande sans params")
                    self.handlerObject.handler[command]()
                else: #print("Avec params")
                    if (command == "-save"):
                        return self.handlerObject.handler[command](param)
                    else:
                        self.handlerObject.handler[command](param)
        self.genGraphObject.displayGraph()


if __name__ == '__main__':
    m = Main()
    m.mainFunction()
