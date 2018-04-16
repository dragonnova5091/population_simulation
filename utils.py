

def remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list

def send_to_plot(blockArray):
    x=[]
    y=[]
    #print(blockArray)
    for block in blockArray:
        x.append(block.xecon)
        y.append(block.yauth)

#    print([x,y])

    return([x,y])







def drawGraph(blockArray, limitsarray):
    #blockArray is the population blocks in an array
    #limitsarray is the limits on the graph

    coordinate = []
    #print(blockArray)
    for block in blockArray:
        #print(block)
        coordinate.append([int(block.xecon), int(block.yauth)])

    coordinates = []
    coordinate_unique = remove(coordinate)
    for coord in coordinate_unique:
        num = 0
        for coord2 in coordinate:
            if coord == coord2:
                num += 1
        coordinates.append([coord[0], coord[1], num])
    #print(coordinates)



    xmin = limitsarray[0]
    xmax = limitsarray[1]
    ymin = limitsarray[2]
    ymax = limitsarray[3]

    grapharray = []

    for y in range(ymin, ymax):
        arr = []
        for x in range(xmin, xmax):
            append_ = True
            for coord in coordinates:
                if x == coord[0] and y == coord[1]:
                    arr.append(str(coord[2]))
                    append_ = False
            if append_ is True:
                if x == 0:
                    arr.append("|")
                elif y == 0:
                    arr.append("-")
                else:
                    arr.append(" ")

        grapharray.append(arr)

    for ylist in grapharray:
        for xchar in ylist:
            if len(xchar) < 2:
                print(xchar, end=" ")
            else:
                print(xchar, end="")
        print("")
