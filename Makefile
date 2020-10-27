plot = python3 main.py
dff  = df -x"squashfs"

all : fichier1 fichier2 df externCommand simpledata example saveImage points presentation traitementDonnes sansX legend courbes dates multipleFiles filterX stackBar filterY exempleAvance

fichier1 :
	@echo "Using cat command"
	cat datas/df_test.txt | $(plot) -x 0 -y 2 -title "Test Graph" -skip -bar -xname xaxisTEST -yname yaxisTEST --rotateX 90

fichier2 :
	@echo "Using param (-file)"
	$(plot) -x 0 -y 2 -title "Test Graph" -skip -bar -xname xaxisTEST -yname yaxisTEST --rotateX 90 -file datas/df_test.txt

df:
	@echo "Using |"
	df | $(plot) -x 0 -y 2 -title "Test Graph" -skip -bar -xname xaxisTEST -yname yaxisTEST --rotateX 90

externCommand:
	@echo "Using extern Command"
	$(plot) -code "plt.figure(figsize=(10,6))" "plt.plot(['a','b','c','d'],[10,200000,3000,400000])" "plt.yscale('log')" "plt.show()"

simpledata :
	$(plot) -x 0 -y 1 -xname "Mois" -yname "Temperature Moyenne" --rotateX 90 -skip -scatter -file datas/simpleDatas.txt -title "scatter Graph"
	$(plot) -x 0 -y 1 -xname "Mois" -yname "Temperature Moyenne" --rotateX 90 -skip -plot -file datas/simpleDatas.txt -title "plot Graph"
	@echo "With sepator = ','"
	$(plot) -x 0 -y 1 -xname "Mois" -yname "Temperature Moyenne" --rotateX 90 -skip -bar -file datas/simpleDatas_virgule.txt -title "Bar Graph separator = ','" -s ","

example : 
	@echo "Example using almost all options"
	$(dff) | $(plot) -skip -x 0 -y 2 -bar -code "plt.yscale('log')" --rotateX 90 -title "Df command" -xname "Systeme de fichier" -yname "utilisé"

saveImage:
	@echo "Save png file : Gray plot"
	$(plot) -x 0 -y 1 2 3 -file datas/simpleDatas_2years.txt -plot -title "3 courbes" -skip -r 60 -l "2018" "2019" "2020" -g -save images/plot_gray.png
	exiftool images/plot_gray.png
	@echo "Save pdf file : Gray Scatter"
	$(plot) -x 0 -y 1 2 3 -file datas/simpleDatas_2years.txt -scatter -title "3 courbes" -skip -r 60 -l "2018" "2019" "2020" -g -save images/scatter_gray.pdf
	exiftool images/scatter_gray.pdf

points:
	@echo "Points sans limite"
	$(plot) -x 0 -y 1 -file datas/listes_points.txt -plot
	@echo "Points avec min max sur x"
	$(plot) -x 0 -y 1 -file datas/listes_points.txt -plot -xlim 100 200 -title "xlim 100 200"
	@echo "Points avec min max sur x"
	$(plot) -x 0 -y 1 -file datas/listes_points.txt -plot -ylim 100 200 -title "ylim 100 200"
	@echo "Points avec min max sur x et y"
	$(plot) -x 0 -y 1 -file datas/listes_points.txt -plot -xlim 100 200 -ylim 100 200 -title "xlim & ylim : min = 100 max = 200"

presentation:
	@echo "Normal"
	$(plot) -x 0 -y 1 -file datas/listes_points.txt -plot -xlim 100 200 -ylim 100 200 -title "Titre Normal" -xname "x axis" -yname "y axis"
	@echo "Presentation"
	$(plot) -x 0 -y 1 -file datas/listes_points.txt -plot -xlim 100 200 -ylim 100 200 -title "Titre Presentation" -xname "x axis" -yname "y axis" -pres

traitementDonnes:
	@echo "Sans Traitement"
	$(plot) -x 0 -y 1 -file datas/listes_points.txt -plot -title "Sans Traitement" -xname "x axis" -yname "y axis"
	@echo "Avec Traitement *10"
	$(plot) -x 0 -y 1 -file datas/listes_points.txt -plot -title "Multiplié par 10" -xname "x axis" -yname "y axis" -proc "x*10"
	@echo "Plus Complexe"
	$(plot) -x 0 -y 1 -file datas/listes_points.txt -plot -title "*100/200-40" -xname "x axis" -yname "y axis" -proc "x*100/200-40"

sansX:
	@echo "Sans argument -x"
	$(plot) -y 1 -file datas/listes_points.txt -plot -title "Sans Traitement" -xname "x axis" -yname "y axis"

legend:
	@echo "Sans légende"
	$(plot) -x 0 -y 1 -file datas/listes_points.txt -plot -title "Sans légende"
	@echo "Avec légende"
	$(plot) -x 0 -y 1 -file datas/listes_points.txt -plot -l "Points" "Legend2" -title "Avec Légende"

courbes:
	@echo "2 courbes"
	$(plot) -x 0 -y 2 3 -file datas/simpleDatas_2years.txt -plot -title "2 courbes" -skip -r 60 -l "2019" "2020"
	@echo "3 courbes"
	$(plot) -x 0 -y 1 2 3 -file datas/simpleDatas_2years.txt -plot -title "3 courbes" -skip -r 60 -l "2018" "2019" "2020"
	@echo "3 courbes"
	$(plot) -x 0 -y 1 2 3 -file datas/simpleDatas_2years.txt -plot -title "3 courbes" -skip -r 60 -l "2018" "2019" "2020" -proc "x = x + (x-1)"

dates:
	@echo "Dates"
	$(plot) -x 0 -y 1 -file datas/dates.txt -plot
	@echo "Dates2"
	$(plot) -x 0 -y 1 -file datas/dates2.txt -plot -r 90
	@echo "Dates3"
	$(plot) -x 0 -y 1 -file datas/dates3.txt -scatter -r 90 -s "|"

multipleFiles:
	@echo "Two files"
	$(plot) -x 0 -y 1 -xname "Mois" -yname "Temperature Moyenne" --rotateX 90 -skip -plot -file datas/simpleDatas.txt datas/simpleDatas2.txt -title "2 files" -l "simpledatas.txt" "simpleDatas2.txt" -r 70

density:
	@echo "Density"
	$(plot) -file datas/randomPoints.txt -x 0 -y 1 -skip -dens
	@echo "Heatmap"
	$(plot) -file datas/randomPoints.txt -x 0 -y 1 -skip -hmap -title "Précision auto"
	@echo "Heatmap 50"
	$(plot) -file datas/randomPoints.txt -x 0 -y 1 -skip -hmap 50 -title "Précision 50"

filterX:
	@echo "Avec Filtre (Mois)"
	$(plot) -file datas/simpleDatas.txt -x 0 -y 1 -skip -scatter -xf "x not in ['Mars','Janvier']" -r 90
	@echo "Sans Filtre (randomPoints)"
	$(plot) -file datas/randomPoints.txt -x 0 -y 1 -skip -scatter -r 90
	@echo "Avec Filtre (randomPoints)"
	$(plot) -file datas/randomPoints.txt -x 0 -y 1 -skip -scatter -xf "x <= 50" -r 90
	@echo "Avec Filtre (randomPoints)"
	$(plot) -file datas/randomPoints.txt -x 0 -y 1 -skip -scatter -xf "(x > 10 and x < 30) or (x > 80 and x < 100)" -r 90

stackBar:
	$(plot) -x 0 -y 2 3 -file datas/simpleDatas_2years.txt -title "2 bar" -skip -r 60 -stack
	$(plot) -x 0 -y 1 2 3 -file datas/simpleDatas_2years.txt -title "3 bar" -skip -r 60 -stack -l "1" "2" "3"

groupedBar:
	$(plot) -x 0 -y 1 -file datas/simpleDatas_2years.txt -title "1 bar" -skip -r 60 -bar
	$(plot) -x 0 -y 1 2 3 -file datas/simpleDatas_2years.txt -title "3 bar" -skip -r 60 -bar -l "1" "2" "3"

filterY :
	@echo "Avec Filtre (randomPoints)"
	$(plot) -file datas/randomPoints.txt -x 0 -y 1 -skip -scatter -yf "(y > 10 and y < 30) or (y > 50 and y < 85)" -r 90
	@echo "Plusieurs Values filtre"
	$(plot) -x 0 -y 1 -xname "Mois" -yname "Temperature Moyenne" --rotateX 90 -skip -plot -file datas/simpleDatas.txt datas/simpleDatas2.txt -title "2 files" -l "simpledatas.txt" "simpleDatas2.txt" -r 70 -yf "y < 27"

exempleAvance :
	$(plot) -x 0 -y 1 -xname "Mois" -yname "Temperature Moyenne" --rotateX 90 -skip -bar -file datas/simpleDatas.txt datas/simpleDatas2.txt -title "Bar Graph : 2 files, all datas" -l "simpledatas.txt" "simpleDatas2.txt" -r 70
	$(plot) -x 0 -y 1 -xname "Mois" -yname "Temperature Moyenne" --rotateX 90 -skip -bar -file datas/simpleDatas.txt datas/simpleDatas2.txt -title "Bar Graph : 2 files, 2 filters" -l "simpledatas.txt" "simpleDatas2.txt" -r 70 -xf "x not in ['Janvier', 'Fevrier']" -yf "y < 27 and y > 10"
	$(plot) -x 0 -y 1 -xname "Mois" -yname "Temperature Moyenne" --rotateX 90 -skip -scatter -file datas/simpleDatas.txt datas/simpleDatas2.txt -title "Scatter Graph : 2 files, 2 filters" -l "simpledatas.txt" "simpleDatas2.txt" -r 70 -xf "x not in ['Janvier', 'Fevrier']" -yf "y < 27 and y > 10"
	$(plot) -x 0 -y 1 -xname "Mois" -yname "Temperature Moyenne" --rotateX 90 -skip -plot -file datas/simpleDatas.txt datas/simpleDatas2.txt -title "Plot Graph : 2 files, 2 filters" -l "simpledatas.txt" "simpleDatas2.txt" -r 70 -xf "x not in ['Janvier', 'Fevrier']" -yf "y < 27 and y > 10"

log :
	$(plot) -file datas/randomPoints.txt -x 0 -y 1 -skip -scatter -r 90 -title "Normal"
	$(plot) -file datas/randomPoints.txt -x 0 -y 1 -skip -scatter -r 90 -log x -title "X log"
	$(plot) -file datas/randomPoints.txt -x 0 -y 1 -skip -scatter -r 90 -log y -title "Y log"
	$(plot) -file datas/randomPoints.txt -x 0 -y 1 -skip -scatter -r 90 -log xy -title "X & Y log"

gray:
	$(plot) -x 0 -y 1 -g -xname "Mois" -yname "Temperature Moyenne" --rotateX 90 -skip -bar -file datas/simpleDatas.txt datas/simpleDatas2.txt -title "Bar Graph : 2 files, all datas" -l "simpledatas.txt" "simpleDatas2.txt" -r 70
	$(plot) -x 0 -y 1 -g -xname "Mois" -yname "Temperature Moyenne" --rotateX 90 -skip -bar -file datas/simpleDatas.txt datas/simpleDatas2.txt -title "Bar Graph : 2 files, 2 filters" -l "simpledatas.txt" "simpleDatas2.txt" -r 70 -xf "x not in ['Janvier', 'Fevrier']" -yf "y < 27 and y > 10"
	$(plot) -x 0 -y 1 -g -xname "Mois" -yname "Temperature Moyenne" --rotateX 90 -skip -scatter -file datas/simpleDatas.txt datas/simpleDatas2.txt -title "Scatter Graph : 2 files, 2 filters" -l "simpledatas.txt" "simpleDatas2.txt" -r 70 -xf "x not in ['Janvier', 'Fevrier']" -yf "y < 27 and y > 10"
	$(plot) -x 0 -y 1 -g -xname "Mois" -yname "Temperature Moyenne" --rotateX 90 -skip -plot -file datas/simpleDatas.txt datas/simpleDatas2.txt -title "Plot Graph : 2 files, 2 filters" -l "simpledatas.txt" "simpleDatas2.txt" -r 70 -xf "x not in ['Janvier', 'Fevrier']" -yf "y < 27 and y > 10"
	$(plot) -g -file datas/randomPoints.txt -x 0 -y 1 -skip -dens
	$(plot) -g -file datas/randomPoints.txt -x 0 -y 1 -skip -hmap -title "Précision auto"
	$(plot) -g -file datas/randomPoints.txt -x 0 -y 1 -skip -hmap 50 -title "Précision 50"

gray_plot :
	@echo "2 courbes Gris"
	$(plot) -x 0 -y 2 3 -file datas/simpleDatas_2years.txt -plot -title "2 courbes" -skip -r 60 -l "2019" "2020" -g
	@echo "3 courbes Gris"
	$(plot) -x 0 -y 1 2 3 -file datas/simpleDatas_2years.txt -plot -title "3 courbes" -skip -r 60 -l "2018" "2019" "2020" -g

gray_scatter :
	@echo "2 courbes Gris"
	$(plot) -x 0 -y 2 3 -file datas/simpleDatas_2years.txt -scatter -title "2 courbes" -skip -r 60 -l "2019" "2020" -g
	@echo "3 courbes Gris"
	$(plot) -x 0 -y 1 2 3 -file datas/simpleDatas_2years.txt -scatter -title "3 courbes" -skip -r 60 -l "2018" "2019" "2020" -g

gray_bar :
	@echo "3 barres Gris"
	$(plot) -x 0 -y 1 2 3 -file datas/simpleDatas_2years.txt -bar -title "3 courbes" -skip -r 60 -l "2018" "2019" "2020" -g
	@echo "3 barres Gris"
	$(plot) -x 0 -y 1 2 3 -file datas/simpleDatas_2years.txt -stack -title "3 courbes" -skip -r 60 -l "2018" "2019" "2020" -g

moyenneGlissante :
	@echo "Données"
	$(plot) -x 0 -y 1 2 -file datas/moyenneGlissante.txt -plot -skip -title "Données du fichier moyenneGlissante.txt" -xname "Date" -yname "Prix" -r 75
	@echo "Données avec moyenne glissante par Trimestre"
	$(plot) -x 0 -y 1 2 -file datas/moyenneGlissante.txt -plot -skip -title "Données avec moyenne glissante par Trimestre" -xname "Date" -yname "Prix" -r 75 -mg 3
	@echo "Données avec moyenne glissante par Semestre"
	$(plot) -x 0 -y 1 2 -file datas/moyenneGlissante.txt -plot -skip -title "Données avec moyenne glissante par Semestre" -xname "Date" -yname "Prix" -r 75 -mg 6

minGlissante :
	@echo "Données"
	$(plot) -x 0 -y 1 2 -file datas/moyenneGlissante.txt -plot -skip -title "Données du fichier moyenneGlissante.txt" -xname "Date" -yname "Prix" -r 75
	@echo "Données avec min glissant par Trimestre"
	$(plot) -x 0 -y 1 2 -file datas/moyenneGlissante.txt -plot -skip -title "Données avec min par Trimestre" -xname "Date" -yname "Prix" -r 75 -ming 3
	@echo "Données avec min glissant par Semestre"
	$(plot) -x 0 -y 1 2 -file datas/moyenneGlissante.txt -plot -skip -title "Données avec min par Semestre" -xname "Date" -yname "Prix" -r 75 -ming 6

maxGlissante :
	@echo "Données"
	$(plot) -x 0 -y 1 2 -file datas/moyenneGlissante.txt -plot -skip -title "Données du fichier moyenneGlissante.txt" -xname "Date" -yname "Prix" -r 75
	@echo "Données avec max glissant par Trimestre"
	$(plot) -x 0 -y 1 2 -file datas/moyenneGlissante.txt -plot -skip -title "Données avec max  par Trimestre" -xname "Date" -yname "Prix" -r 75 -maxg 3
	@echo "Données avec max glissant par Semestre"
	$(plot) -x 0 -y 1 2 -file datas/moyenneGlissante.txt -plot -skip -title "Données avec max  par Semestre" -xname "Date" -yname "Prix" -r 75 -maxg 6

medianeGlissante :
	@echo "Données"
	$(plot) -x 0 -y 1 2 -file datas/moyenneGlissante.txt -plot -skip -title "Données du fichier moyenne Glissante.txt" -xname "Date" -yname "Prix" -r 75
	@echo "Données avec mediane glissante par Trimestre"
	$(plot) -x 0 -y 1 2 -file datas/moyenneGlissante.txt -plot -skip -title "Données avec mediane par Trimestre" -xname "Date" -yname "Prix" -r 75 -medg 3
	@echo "Données avec mediane glissante par Semestre"
	$(plot) -x 0 -y 1 2 -file datas/moyenneGlissante.txt -plot -skip -title "Données avec mediane par Semestre" -xname "Date" -yname "Prix" -r 75 -medg 6

titre:
	@echo "Données"
	$(plot) -x 0 -y 1 2 -file datas/moyenneGlissante.txt -plot -skip -title "This is a very long title This \n is a very long title This is a very long title \n This is a very long title" -xname "Date" -yname "Prix" -r 75

figureSize:
	@echo "Normal"
	$(plot) -x 0 -y 1 2 3 -file datas/simpleDatas_2years.txt -plot -title "3 courbes" -skip -r 60 -l "2018" "2019" "2020"
	@echo "Figure size"
	$(plot) -x 0 -y 1 2 3 -file datas/simpleDatas_2years.txt -plot -title "3 courbes" -skip -r 60 -l "2018" "2019" "2020" -fs 10 20
	$(plot) -x 0 -y 1 2 3 -file datas/simpleDatas_2years.txt -plot -title "3 courbes" -skip -r 60 -l "2018" "2019" "2020" -fs 30 50

symlog:
	@echo "Log"
	$(plot) -x 0 -y 1 -file datas/log.txt -plot -skip -log y

boxplot:
	@echo "Box"
	$(plot) -y 0 -skip -file datas/boxplot/doc1.txt datas/boxplot/doc2.txt datas/boxplot/doc3.txt -box -r 75
	@echo "Box Short Name"
	$(plot) -y 0 -skip -file datas/boxplot/doc1.txt datas/boxplot/doc2.txt datas/boxplot/doc3.txt -box short -r 75

tests :
	python3 -m doctest src/*.py


testsVerbose :
	python3 -m doctest -v src/*.py
	python3 -m nose graphTest.py

clean : 
	rm -rf images/