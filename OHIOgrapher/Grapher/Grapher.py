# ## REMENDO DE MERDA VOU TENTAR RESOLVER DEPOIS
# import png
# import math

# Letters = {
#     "0": [
#         [0,0,1,1,1,1,0,0],
#         [0,1,0,0,0,0,1,0],
#         [0,1,0,0,0,0,1,0],
#         [0,1,0,0,0,0,1,0],
#         [0,1,0,0,0,0,1,0],
#         [0,1,0,0,0,0,1,0],
#         [0,1,0,0,0,0,1,0],
#         [0,0,1,1,1,1,0,0],
#             ]
#     ,"1": [
#         [0,0,0,0,1,0,0,0],
#         [0,0,0,1,1,0,0,0],
#         [0,0,1,0,1,0,0,0],
#         [0,0,0,0,1,0,0,0],
#         [0,0,0,0,1,0,0,0],
#         [0,0,0,0,1,0,0,0],
#         [0,0,0,0,1,0,0,0],
#         [0,1,1,1,1,1,1,0],
#             ]
#     ,"2": [
#         [0,0,1,1,1,1,0,0],
#         [0,1,0,0,0,0,1,0],
#         [0,0,0,0,0,0,1,0],
#         [0,0,0,0,0,1,0,0],
#         [0,0,0,0,1,0,0,0],
#         [0,0,0,1,0,0,0,0],
#         [0,0,1,0,0,0,0,0],
#         [0,1,1,1,1,1,1,0],
#             ]
#     ,"3": [
#         [0,0,1,1,1,1,0,0],
#         [0,1,0,0,0,0,1,0],
#         [0,0,0,0,0,0,1,0],
#         [0,0,0,1,1,1,0,0],
#         [0,0,0,0,0,0,1,0],
#         [0,0,0,0,0,0,1,0],
#         [0,1,0,0,0,0,1,0],
#         [0,0,1,1,1,1,0,0],
#             ]
#     ,"4": [
#         [0,0,0,0,0,1,0,0],
#         [0,0,0,0,1,1,0,0],
#         [0,0,0,1,0,1,0,0],
#         [0,0,1,0,0,1,0,0],
#         [0,1,1,1,1,1,1,0],
#         [0,0,0,0,0,1,0,0],
#         [0,0,0,0,0,1,0,0],
#         [0,0,0,0,0,1,0,0],
#             ]
#     ,"5": [
#         [0,1,1,1,1,1,1,0],
#         [0,1,0,0,0,0,0,0],
#         [0,1,0,0,0,0,0,0],
#         [0,1,1,1,1,1,1,0],
#         [0,0,0,0,0,0,1,0],
#         [0,0,0,0,0,0,1,0],
#         [0,0,0,0,0,0,1,0],
#         [0,1,1,1,1,1,0,0],
#             ]
#     ,"6": [
#         [0,0,1,1,1,1,1,0],
#         [0,1,0,0,0,0,0,0],
#         [0,1,0,0,0,0,0,0],
#         [0,1,1,1,1,1,0,0],
#         [0,1,0,0,0,0,1,0],
#         [0,1,0,0,0,0,1,0],
#         [0,1,0,0,0,0,1,0],
#         [0,0,1,1,1,1,0,0],
#             ]
#     ,"7": [
#         [0,1,1,1,1,1,1,0],
#         [0,0,0,0,0,0,1,0],
#         [0,0,0,0,0,1,0,0],
#         [0,0,0,0,0,1,0,0],
#         [0,0,0,0,1,0,0,0],
#         [0,0,0,0,1,0,0,0],
#         [0,0,0,0,1,0,0,0],
#         [0,0,0,0,1,0,0,0],
#             ]
#     ,"8": [
#         [0,0,1,1,1,1,0,0],
#         [0,1,0,0,0,0,1,0],
#         [0,1,0,0,0,0,1,0],
#         [0,0,1,1,1,1,0,0],
#         [0,1,0,0,0,0,1,0],
#         [0,1,0,0,0,0,1,0],
#         [0,1,0,0,0,0,1,0],
#         [0,0,1,1,1,1,0,0],
#             ]
#     ,"9": [
#         [0,0,1,1,1,1,0,0],
#         [0,1,0,0,0,0,1,0],
#         [0,1,0,0,0,0,1,0],
#         [0,1,0,0,0,0,1,0],
#         [0,0,1,1,1,1,1,0],
#         [0,0,0,0,0,0,1,0],
#         [0,0,0,0,0,0,1,0],
#         [0,1,1,1,1,1,0,0],
#             ]
#     ," ": [
#         [0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0],
#             ]
#     ,".": [
#         [0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0],
#         [0,0,0,1,1,0,0,0],
#         [0,0,0,1,1,0,0,0],
#             ]
# }

# def lerp(v0, v1,t):
#   return (1 - t) * v0 + t * v1

# class Renderer:
#     def __init__(self, width, height) -> None:
#         self.data = []
#         i = 0
#         while i < height:
#             j = 0
#             row = []
#             while j < width:
#                 row.append((0,0,0))
#                 j+=1 
#             self.data.append(row)
#             i+=1
#         pass

#     def Fill(self, fillColor:tuple):
#         i = 0
#         while i < len(self.data):
#             j = 0
#             while j < len(self.data[i]):
#                 self.data[i][j] = fillColor
#                 j+=1
#             i +=1

#     def DrawLine(self,startPos:tuple, endPos:tuple, lineColor:tuple, lineThickness = 1):
#         distX = endPos[0] - startPos[0]
#         distY = endPos[1] - startPos[1]
#         i = 0
#         if distX  >= distY:
#             while i < distX:
#                 iY = lerp(startPos[1], endPos[1], i/distX)
#                 print(iY)
#                 print("\n")
#                 self.data[math.floor(iY)][math.floor(startPos[0] + i)] = lineColor
#                 if lineThickness >1:
#                     j = math.floor(-lineThickness/2)
#                     while j < lineThickness:
#                         self.data[math.floor(iY) + j][math.floor(startPos[0] + i)] = lineColor
#                         j+=1
#                 i+=1
#         else:
#             while i < distY:
#                 iX = lerp(startPos[0], endPos[0], i/distY)
#                 print(iX)
#                 print("\n")
#                 self.data[math.floor(startPos[1] + i)][math.floor(iX)] = lineColor
#                 if lineThickness >1:
#                     j = math.floor(-lineThickness/2)
#                     while j < lineThickness:
#                         self.data[math.floor(startPos[1] + i)][math.floor(iX)+j] = lineColor
#                         j+=1
#                 i+=1
#         pass
    
#     def DrawText(self, text:str, Pos:tuple, textColor:tuple, textSize = 1):
#         i = 0
#         while i < len(text):
#             c = Letters[text[i]]
#             j = 0
#             while j < len(c)*textSize:
#                 k = 0
#                 while k < len(c[math.floor(j/textSize)])*textSize:
#                     if c[math.floor(j/textSize)][math.floor(k/textSize)] == 1:
#                         self.data[math.floor(Pos[1]+j)][math.floor(Pos[0] +k+ (i*len(c[math.floor(j/textSize)])*textSize))] = textColor 
#                     k+=1
#                 j+=1
#             i+=1
#         pass

#     def Save(self, fileName):
#         d = []
#         for row in self.data:
#             r = []
#             for j in row:
#                 for i in j:
#                     r.append(i)
#             d.append(r)
#         image = png.from_array(d, "RGB")
#         image.save(fileName)
#         print("saved: " + fileName + " to disk")



import pygame as pg
import Drawer as dr
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
    ren = Renderer(width, height)

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
        dataprocessed.append([(d[0]*(width-200)/maxX)+100, (((d[1]*(height-100)/maxY)-((height-50)/2))*-1)+(height-50)/2])


    j = 0

    #drawBase
    pg.draw.line(win, GraphColors[GUIDE_LINE], (50,0), (50,height),guideLineThickness)
    pg.draw.line(win, GraphColors[GUIDE_LINE], (0,height-50), (width,width-50),guideLineThickness)

    ren.DrawLine((100,0), (100,height), GraphColors[GUIDE_LINE], guideLineThickness)
    ren.DrawLine((0,height-50), (width,width-50), GraphColors[GUIDE_LINE], guideLineThickness)

    pg.font.init()
    my_font = pg.font.SysFont('Arial', fontSize)
    i = 0
    while j < len(dataprocessed):
        text_surface = my_font.render(str(data[j][1]), True, GraphColors[TEXT])
        win.blit(text_surface, (0,dataprocessed[j][1]))
        ren.DrawText(str(data[j][1]), (0,dataprocessed[j][1]), GraphColors[TEXT], 3)

        text_surface = my_font.render(str(data[j][0]), True, GraphColors[TEXT])
        win.blit(text_surface, (dataprocessed[j][0],height-48))
        ren.DrawText(str(data[j][1]), (dataprocessed[j][0],height-45), GraphColors[TEXT], 3)
        
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
    pg.image.save(win, fname)
    print("file: " + fname + " has been saved!")
    ren.Save("graph2.png")

    pg.display.flip()
    pg.quit()
    pass

DrawGraph([(0,0),(100,100),(200,300)])
