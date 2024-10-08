import OHIOgrapher.Drawer as dr
import sys
import numpy as np
width = 1200
height = 1200
fontSize = 20
guideLineThickness = 3
graphLineThickness = 3
PointThickness = 5
GraphColors = [(255,255,255), (125, 125, 125), (255,0,0), (0,0,0), (0,0,0)]
###### COLOR CHANGERHELPER #######################
BACKGROUND = 0
GUIDE_LINE = 1
GRAPH_LINE = 2
POINTS = 3
TEXT = 4



def DrawGraph(data:list):
    ren = dr.Renderer(width, height)

    ren.Fill(GraphColors[BACKGROUND])

    dataprocessed = []
    i = 0
    maxY = -sys.float_info.max
    maxX = -sys.float_info.max
    while i < len(data):
        if data[i][0] > maxX:
            maxX = data[i][0]
        if data[i][1] > maxY:
            maxY = data[i][1]

        i+=1
    for d in data:
        dataprocessed.append([(d[0]*(width-200)/maxX)+100, (((d[1]*(height-100)/maxY)-((height-50)/2))*-1)+(height-50)/2])


    j = 0

    #drawBase
    ren.DrawLine((100,0), (100,height), GraphColors[GUIDE_LINE], guideLineThickness)
    ren.DrawLine((0,height-50), (width,width-50), GraphColors[GUIDE_LINE], guideLineThickness)
    i = 0
    while j < len(dataprocessed):
        ren.DrawText(str(data[j][1]), (0,dataprocessed[j][1]), GraphColors[TEXT], 2)

        ren.DrawText(str(data[j][1]), (dataprocessed[j][0],height-45), GraphColors[TEXT], 2)
        
        if j > 0 :
            ren.DrawLine(dataprocessed[j-1], dataprocessed[j], GraphColors[GRAPH_LINE], graphLineThickness)

        j+=1
    
    while i < len(dataprocessed):
        #draw a circle

        i+=1

    # now save the drawing
    # can save as .bmp .tga .png or .jpg
    fname = "graph.png"
    print("file: " + fname + " has been saved!")
    ren.Save(fname)
    pass

DrawGraph([(0,0),(100,100),(200,300)])
