from matplotlib.testing.compare import compare_images
import os
import shutil

def noseTestsImages(image1, image2):
    """

    Doc Link : https://matplotlib.org/devdocs/api/testing_api.html

    :param image1: the first image (ref)
    :param image2: the second image
    """
    tol = 0.000
    res = compare_images(image1, image2, tol, True)
    assert(res is None), "If not None, that means that the two images are not equals"

def test_yname():
    os.system("python3 main.py -x 0 -y 1 -skip -bar -file datas/simpleDatas.txt -save imageRef/tests/yname.png -yname 'Y name'")
    noseTestsImages("./imageRef/yname.png", "./imageRef/tests/yname.png")

def test_xname():
    os.system("python3 main.py -x 0 -y 1 -skip -bar -file datas/simpleDatas.txt -save imageRef/tests/xname.png -xname 'X name'")
    noseTestsImages("./imageRef/xname.png", "./imageRef/tests/xname.png")

def test_title():
    os.system("python3 main.py -x 0 -y 1 -skip -bar -file datas/simpleDatas.txt -save imageRef/tests/title.png -title 'This is a \n Title'")
    noseTestsImages("./imageRef/title.png", "./imageRef/tests/title.png")

def test_rotate():
    os.system("python3 main.py -x 0 -y 1 -skip -bar -file datas/simpleDatas.txt -save imageRef/tests/rotate.png -r 75")
    noseTestsImages("./imageRef/rotate.png", "./imageRef/tests/rotate.png")

def test_logscale():
    os.system("python3 main.py -file datas/randomPoints.txt -x 0 -y 1 -skip -scatter -r 90 -log xy -title 'X & Y log' -save imageRef/tests/log.png")
    noseTestsImages("./imageRef/log.png", "./imageRef/tests/log.png")

def test_externalCode():
    os.system('python3 main.py -code "plt.figure(figsize=(10,6))" "plt.plot([1,2,3,4],[10,200000,3000,400000])" -save imageRef/tests/code.png')
    noseTestsImages("./imageRef/code.png", "./imageRef/tests/code.png")

def test_xlim():
    os.system("python3 main.py -file datas/randomPoints.txt -x 0 -y 1 -skip -scatter -r 90 -xlim 0 50 -save imageRef/tests/xlim.png")
    noseTestsImages("./imageRef/xlim.png", "./imageRef/tests/xlim.png")
    
def test_ylim():
    os.system("python3 main.py -file datas/randomPoints.txt -x 0 -y 1 -skip -scatter -r 90 -ylim 0 60 -save imageRef/tests/ylim.png")
    noseTestsImages("./imageRef/ylim.png", "./imageRef/tests/ylim.png")

def test_legend():
    os.system("python3 main.py -file datas/randomPoints.txt -x 0 -y 1 -skip -scatter -r 90 -l 'Test' -save imageRef/tests/legend.png")
    noseTestsImages("./imageRef/legend.png", "./imageRef/tests/legend.png")

def test_xfilter():
    os.system('python3 main.py -file datas/randomPoints.txt -x 0 -y 1 -skip -scatter -r 90 -xf "(x > 10 and x < 30) or (x > 80 and x < 100)"  -save imageRef/tests/xfilter.png')
    noseTestsImages("./imageRef/xfilter.png", "./imageRef/tests/xfilter.png")

def test_yfilter():
    os.system('python3 main.py -file datas/randomPoints.txt -x 0 -y 1 -skip -scatter -r 90 -yf "(x > 20 and x < 40) or (x > 90 and x < 100)"  -save imageRef/tests/yfilter.png')
    noseTestsImages("./imageRef/yfilter.png", "./imageRef/tests/yfilter.png")

def test_processingDatas():
    os.system('python3 main.py -x 0 -y 1 -file datas/listes_points.txt -plot -title "Multiplie par 10" -xname "x axis" -yname "y axis" -proc "x*10" -save imageRef/tests/processing_mul10.png')
    noseTestsImages("./imageRef/processing_mul10.png", "./imageRef/tests/processing_mul10.png")

def test_movingValues():
    os.system('python3 main.py -x 0 -y 1 2 -file datas/moyenneGlissante.txt -plot -skip -title "Donnees avec moyenne glissante par Trimestre" -xname "Date" -yname "Prix" -r 75 -mg 3 -save imageRef/tests/movingAverage.png')
    noseTestsImages("./imageRef/movingAverage.png", "./imageRef/tests/movingAverage.png")

def test_bar_graph():
    """
    Bar Graph Test
    """
    # Normal Bar Graph
    os.system("python3 main.py -x 0 -y 1 -skip -bar -file datas/simpleDatas.txt -save imageRef/tests/bar_graph.png")
    noseTestsImages("./imageRef/bar_graph.png", "./imageRef/tests/bar_graph.png")

    os.system('python3 main.py -x 0 -y 1 2 3 -file datas/simpleDatas_2years.txt -bar -title "3 barres" -skip -r 60 -l "2018" "2019" "2020" -save imageRef/tests/bar_graph2.png')
    noseTestsImages("./imageRef/bar_graph2.png", "./imageRef/tests/bar_graph2.png")

    # Stacked Bar
    os.system('python3 main.py -x 0 -y 1 2 3 -file datas/simpleDatas_2years.txt -stack -title "3 barres" -skip -r 60 -l "2018" "2019" "2020" -save imageRef/tests/stackbar_graph.png')
    noseTestsImages("./imageRef/stackbar_graph.png", "./imageRef/tests/stackbar_graph.png")

def test_scatter_graph():
    os.system('python3 main.py -x 0 -y 1 2 3 -file datas/simpleDatas_2years.txt -scatter -title "3 scatters" -skip -r 60 -l "2018" "2019" "2020" -save imageRef/tests/scatter_graph.png')
    noseTestsImages("./imageRef/scatter_graph.png", "./imageRef/tests/scatter_graph.png")

def test_plot_graph():
    os.system('python3 main.py -x 0 -y 1 2 3 -file datas/simpleDatas_2years.txt -plot -title "3 courbes" -skip -r 60 -l "2018" "2019" "2020" -save imageRef/tests/plot_graph.png')
    noseTestsImages("./imageRef/plot_graph.png", "./imageRef/tests/plot_graph.png")

def test_heatmap_graph():
    os.system("python3 main.py -file datas/randomPoints.txt -x 0 -y 1 -skip -hmap 50 -title 'Precision 50' -save imageRef/tests/heatmap_graph.png")
    noseTestsImages("./imageRef/heatmap_graph.png", "./imageRef/tests/heatmap_graph.png")

def test_boxplot_graph():
    os.system("python3 main.py -y 0 -skip -file datas/boxplot/doc1.txt datas/boxplot/doc2.txt datas/boxplot/doc3.txt -box -r 75 -save imageRef/tests/boxplot_graph.png")
    noseTestsImages("./imageRef/boxplot_graph.png", "./imageRef/tests/boxplot_graph.png")

def test_gray():
    # Bar
    os.system('python3 main.py -x 0 -y 1 2 3 -file datas/simpleDatas_2years.txt -bar -title "Gray bar graph" -skip -r 60 -l "2018" "2019" "2020" -save imageRef/tests/gray_bar.png -g')
    noseTestsImages("./imageRef/gray_bar.png", "./imageRef/tests/gray_bar.png")
    # Scatter
    os.system('python3 main.py -x 0 -y 1 2 3 -file datas/simpleDatas_2years.txt -scatter -title "Gray scatter graph" -skip -r 60 -l "2018" "2019" "2020" -save imageRef/tests/gray_scatter.png -g')
    noseTestsImages("./imageRef/gray_scatter.png", "./imageRef/tests/gray_scatter.png")
    # Plot
    os.system('python3 main.py -x 0 -y 1 2 3 -file datas/simpleDatas_2years.txt -plot -title "Gray plot graph" -skip -r 60 -l "2018" "2019" "2020" -save imageRef/tests/gray_plot.png -g')
    noseTestsImages("./imageRef/gray_plot.png", "./imageRef/tests/gray_plot.png")
    # Heatmap
    os.system("python3 main.py -file datas/randomPoints.txt -x 0 -y 1 -skip -hmap 50 -title 'Gray heatmap graph' -save imageRef/tests/gray_heatmap.png -g")
    noseTestsImages("./imageRef/gray_heatmap.png", "./imageRef/tests/gray_heatmap.png")
    # Boxplot
    os.system("python3 main.py -y 0 -skip -file datas/boxplot/doc1.txt datas/boxplot/doc2.txt datas/boxplot/doc3.txt -box -r 75 -save imageRef/tests/gray_boxplot.png -g")
    noseTestsImages("./imageRef/gray_boxplot.png", "./imageRef/tests/gray_boxplot.png")

def delete_test_dir():
    """
    Function to delete tests directory
    """
    pass # shutil.rmtree("./imageRef/tests", ignore_errors=True)


if __name__ == '__main__':
    test_yname()
    test_xname()
    test_title()
    test_rotate()
    test_logscale()
    test_externalCode()
    test_xlim()
    test_ylim()
    test_legend()
    test_xfilter()
    test_yfilter()
    test_processingDatas()
    test_movingValues()
    test_bar_graph()
    test_scatter_graph()
    test_plot_graph()
    test_heatmap_graph()
    test_boxplot_graph()
    test_gray()
    delete_test_dir()
