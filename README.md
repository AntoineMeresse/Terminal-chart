# Terminal chart using Matplotlib

This is a project that I started on my university's gitlab. 

The goal of this project is to generate chart from the terminal using Matplotlib (python).

# Install everything you need

- Python3
- Pip3 : ```sudo apt install python3-pip```
- Numpy : ```pip3 install numpy```
- Matplotlib : ```pip3 install matplotlib```
- piexif : ```pip3 install piexif```
- Nose : ```pip3 install nose```
- Scipy : ```pip3 install scipy```

There is also a file called  ```./setup.sh``` for ubuntu users to install everything with pip.

# Add it to your bash/zsh for unix users

vim ```~/.(bash|zsh)rc``` 

Add the following line : ```alias plot="python3 pathToGitlabClone/main.py"```

source ```~/.(bash|zsh)rc```

# Want to see examples ?

## Makefile

Check the file ```Makefile```. There are a lot of examples but they are in french now.

## Example with pipe

Let's use the command ```df``` to see disk usage.

There are 2 ways of buildings chart :
- using pipe
- using file(s)

We're going to display disk usage (column 3) for each file system (column 1).
We assume plot stands for "python3 /.../main.py"

```df | plot -x 0 -y 2 -bar```

-x 0 : column for x axis on graph

-y 2 : column for y axxis on graph

-bar to display a bar graph

```df | plot -x 0 -y 2 -bar -skip```

-skip : skip the first line of data

```df | plot -x 0 -y 2 -bar -skip -r 90```

-r 90 : rotate labels of 90°

```df | plot -x 0 -y 2 -bar -skip -r 90 -log y```

-log y : log scale on y axis

```df | plot -x 0 -y 2 -bar -skip -r 90 -log y -title "Title example" -xname "file system" -yname "usage"```

-title : set title to the chart

-xname : change x-axis label name

-yname : change y-axis label name

```df | plot -x 0 -y 2 -bar -skip -r 90 -log y -title "Title example" -xname "file system" -yname "usage" -xf "'loop' not in x"```

Example of filter on string :

-xf : we want to filter x values, here I want to delete all elements that contains loop (I want to delete every snap install showed in df command) 

```df | plot -x 0 -y 2 -bar -skip -r 90 -log y -title "Title example" -xname "file system" -yname "usage" -xf "'loop' not in x" -yf "y > 100"```

Example of filter on num:

-yf : Keep only values above 100 on y axis

```df | plot -x 0 -y 2 -bar -skip -r 90 -log y -title "Title example" -xname "file system" -yname "usage" -xf "'loop' not in x" -yf "y > 100" -save Bureau/df-example.png```

-save path : save your image with metadata (only for png, pdf) Usefull if you want to see the command you used to generate the chart.

# All options

Use this command : ```plot -h```

Doc is in french for now, I will translate is as soon as possible



