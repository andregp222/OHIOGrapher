import pygame as pg
def DrawGraph(data:list):
    # pygame uses (r, g, b) color tuples
    white = (255, 255, 255)
    gray = (125, 125, 125)

    width = 900
    height = 900
    RUNNING = True

    # create the display window
    win = pg.display.set_mode((width, height))
    # optional title bar caption
    pg.display.set_caption("Graph")
    # default background is black, so make it white
    win.fill(white)

    dataprocessed = []
    i = 0
    maxY = 0
    maxX = 0
    while i < len(data):
        if data[i][0] > maxX:
            maxX = data[i][0]
        if data[i][1] > maxY:
            maxY = data[i][1]

        i+=1

    for d in data:
        dataprocessed.append([(d[0]*800/maxX)+50, (((d[1]*800/maxY)-425)*-1)+425])


    j = 0

    #drawBase
    pg.draw.line(win, gray, (50,0), (50,900),3)
    pg.draw.line(win, gray, (0,850), (900,850),3)

    pg.font.init()
    my_font = pg.font.SysFont('Arial', 20)
    i = 0
    while j < len(dataprocessed):
        text_surface = my_font.render(str(data[j][1]), True, (0, 0, 0))
        win.blit(text_surface, (0,dataprocessed[j][1]))

        text_surface = my_font.render(str(data[j][0]), True, (0, 0, 0))
        win.blit(text_surface, (dataprocessed[j][0],852))
        
        if j > 0 :
            pg.draw.line(win, (255,0,0),dataprocessed[j-1], dataprocessed[j], 3)
        j+=1

    # now save the drawing
    # can save as .bmp .tga .png or .jpg
    fname = "graph.png"
    pg.image.save(win, fname)
    print("file" + fname + " has been saved!")

    pg.display.flip()
    pg.quit()
    pass