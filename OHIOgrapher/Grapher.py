import pygame as pg
import Drawer as dr
import sys
import numpy as np
width = 900
height = 900
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

    win = pg.display.set_mode((width, height))
    pg.display.set_caption("Graph")
    win.fill(GraphColors[BACKGROUND])

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
        dataprocessed.append([(d[0]*(width-100)/maxX)+50, (((d[1]*(height-100)/maxY)-((height-50)/2))*-1)+(height-50)/2])


    j = 0

    #drawBase
    pg.draw.line(win, GraphColors[GUIDE_LINE], (50,0), (50,height),guideLineThickness)
    pg.draw.line(win, GraphColors[GUIDE_LINE], (0,height-50), (width,width-50),guideLineThickness)

    ren.DrawLine((50,0), (50,height), GraphColors[GUIDE_LINE], guideLineThickness)
    ren.DrawLine((0,height-50), (width,width-50), GraphColors[GUIDE_LINE], guideLineThickness)

    pg.font.init()
    my_font = pg.font.SysFont('Arial', fontSize)
    i = 0
    while j < len(dataprocessed):
        text_surface = my_font.render(str(data[j][1]), True, GraphColors[TEXT])
        win.blit(text_surface, (0,dataprocessed[j][1]))
        ren.DrawText(str(data[j][1]), (0,dataprocessed[j][1]), GraphColors[TEXT], 1)

        text_surface = my_font.render(str(data[j][0]), True, GraphColors[TEXT])
        win.blit(text_surface, (dataprocessed[j][0],height-48))
        
        if j > 0 :
            pg.draw.line(win, GraphColors[GRAPH_LINE],dataprocessed[j-1], dataprocessed[j], graphLineThickness)
            ren.DrawLine(dataprocessed[j-1], dataprocessed[j], GraphColors[GRAPH_LINE], graphLineThickness)

        j+=1
    
    while i < len(dataprocessed):
        pg.draw.circle(win, GraphColors[POINTS], dataprocessed[i], PointThickness, 0)

        i+=1

    # now save the drawing
    # can save as .bmp .tga .png or .jpg
    fname = "graph.png"
    #pg.image.save(win, fname)
    print("file: " + fname + " has been saved!")
    ren.Save("Test.png")

    pg.display.flip()
    pg.quit()
    pass

DrawGraph([(0,0),(100,100),(200,300)])