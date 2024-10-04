import pygame as pg
import sys
import numpy as np
width = 900
height = 900
fontSize = 20
guideLineThickness = 3
graphLineThickness = 3
PointThickness = 5
GraphColors = [(255,255,255), (125, 125, 125), (255,0,0), (0,0,0)]
###### COLOR CHANGERHELPER #######################
BACKGROUND = 0
GUIDE_LINE = 1
GRAPH_LINE = 2
POINTS = 3



def DrawGraph(data:list):

    win = pg.display.set_mode((width, height))
    pg.display.set_caption("Graph")
    win.fill(GraphColors[BACKGROUND])

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
        dataprocessed.append([(d[0]*(width-100)/maxX)+50, (((d[1]*(height-100)/maxY)-((height-50)/2))*-1)+(height-50)/2])


    j = 0

    #drawBase
    pg.draw.line(win, GraphColors[GUIDE_LINE], (50,0), (50,height),guideLineThickness)
    pg.draw.line(win, GraphColors[GUIDE_LINE], (0,height-50), (width,width-50),guideLineThickness)

    pg.font.init()
    my_font = pg.font.SysFont('Arial', fontSize)
    i = 0
    psSurface = pg.Surface((width, height))
    while j < len(dataprocessed):
        text_surface = my_font.render(str(data[j][1]), True, (0, 0, 0))
        win.blit(text_surface, (0,dataprocessed[j][1]))

        text_surface = my_font.render(str(data[j][0]), True, (0, 0, 0))
        win.blit(text_surface, (dataprocessed[j][0],height-48))
        
        if j > 0 :
            pg.draw.line(win, GraphColors[GRAPH_LINE],dataprocessed[j-1], dataprocessed[j], graphLineThickness)

        pg.draw.circle(psSurface, GraphColors[POINTS], dataprocessed[j], PointThickness, 0)
        j+=1
    
    win.blit(psSurface, (0,0), (width,height))

    # now save the drawing
    # can save as .bmp .tga .png or .jpg
    fname = "graph.png"
    pg.image.save(win, fname)
    print("file" + fname + " has been saved!")

    pg.display.flip()
    pg.quit()
    pass