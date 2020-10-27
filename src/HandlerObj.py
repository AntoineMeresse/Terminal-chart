class HandlerObj:

    def __init__(self, genGraph, extractData, imageSave):
        #print("Init handlerObj.")
        self.genGraph = genGraph
        self.graphDatas = self.genGraph.graphDatas
        self.extractData = extractData
        self.imageSave = imageSave
        
        # The order is important.
        self.commands = [
            "-fs",

            "-file",
            "-skip",
            "-s",
            "-x",
            "-y",

            "-gray",

            "-proc",
            "-yf",
            "-xf",
            "-pres",
            "-mg",
            "-ming",
            "-maxg",
            "-medg",

            "-xname",
            "-yname",
            "-title",
            "-legend",
            
            "-rotateX",

            "-xlim",
            "-ylim",

            "-code",
            "-log",

            #GraphTypes
            "-bar",
            "-stack",
            "-scatter",
            "-plot",
            "-dens",
            "-hmap",
            "-box",

            #Save Image
            "-save"
        ]

        # To execute commands, call the function link to the key(arg)
        self.handler = {
            "-skip": extractData.skipFirstLine,
            "-x": extractData.extract_column_x,
            "-y": extractData.extract_column_y,
            "-bar": genGraph.barGraph,
            "-title": genGraph.setTitle,
            "-xname": genGraph.setAxisName_X,
            "-yname": genGraph.setAxisName_Y,
            "-rotateX": genGraph.rotate_text_x_label,
            "-code": genGraph.external_code,
            "-file": extractData.setFile,
            "-scatter": genGraph.scatterGraph,
            "-plot": genGraph.plotGraph,
            "-save": imageSave.saveAsImage,
            "-log": genGraph.logScale,
            "-s": extractData.setSeparator,
            "-xlim": genGraph.setXlim,
            "-ylim": genGraph.setYlim,
            "-pres": genGraph.presentationMode,
            "-proc": self.graphDatas.processingDatas,
            "-legend": self.graphDatas.addLegends,
            "-dens": genGraph.densityGraph,
            "-stack": genGraph.stackGraph,
            "-xf": self.graphDatas.setXf,
            "-yf": self.graphDatas.setYf,
            "-hmap": genGraph.heatmap,
            "-gray": genGraph.grayScale,
            "-mg": self.graphDatas.movingAverage,
            "-ming": self.graphDatas.movingMinimum,
            "-maxg": self.graphDatas.movingMaximum,
            "-medg": self.graphDatas.movingMedian,
            "-fs": self.genGraph.initFigure,
            "-box": self.genGraph.boxplot,
        }

    def void(self):
        """
        To implement handler which doesn't have function yet
        """
        print("Void Function")

    def void(self, param):
        """
        To implement handler which doesn't have function yet (function with params)
        """
        print(param)
