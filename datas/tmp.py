with open("listes_points.txt","w+") as f:
    i = 0
    j = 2
    while(i < 1001):
             f.write(str(i) + " " + str(j) + "\n")
             i+=1
             j+=1