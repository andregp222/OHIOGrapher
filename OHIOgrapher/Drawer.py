import png
import math

Letters = {
    "0": [
        [0,0,1,1,1,1,0,0],
        [0,1,0,0,0,0,1,0],
        [0,1,0,0,0,0,1,0],
        [0,1,0,0,0,0,1,0],
        [0,1,0,0,0,0,1,0],
        [0,1,0,0,0,0,1,0],
        [0,1,0,0,0,0,1,0],
        [0,0,1,1,1,1,0,0],
            ]
    ,"1": [
        [0,0,0,0,1,0,0,0],
        [0,0,0,1,1,0,0,0],
        [0,0,1,0,1,0,0,0],
        [0,0,0,0,1,0,0,0],
        [0,0,0,0,1,0,0,0],
        [0,0,0,0,1,0,0,0],
        [0,0,0,0,1,0,0,0],
        [0,1,1,1,1,1,1,0],
            ]
    ,"2": [
        [0,0,1,1,1,1,0,0],
        [0,1,0,0,0,0,1,0],
        [0,0,0,0,0,0,1,0],
        [0,0,0,0,0,1,0,0],
        [0,0,0,0,1,0,0,0],
        [0,0,0,1,0,0,0,0],
        [0,0,1,0,0,0,0,0],
        [0,1,1,1,1,1,1,0],
            ]
    ,"3": [
        [0,0,1,1,1,1,0,0],
        [0,1,0,0,0,0,1,0],
        [0,0,0,0,0,0,1,0],
        [0,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,1,0],
        [0,0,0,0,0,0,1,0],
        [0,1,0,0,0,0,1,0],
        [0,0,1,1,1,1,0,0],
            ]
    ,"4": [
        [0,0,0,0,0,1,0,0],
        [0,0,0,0,1,1,0,0],
        [0,0,0,1,0,1,0,0],
        [0,0,1,0,0,1,0,0],
        [0,1,1,1,1,1,1,0],
        [0,0,0,0,0,1,0,0],
        [0,0,0,0,0,1,0,0],
        [0,0,0,0,0,1,0,0],
            ]
    ,"5": [
        [0,1,1,1,1,1,1,0],
        [0,1,0,0,0,0,0,0],
        [0,1,0,0,0,0,0,0],
        [0,1,1,1,1,1,1,0],
        [0,0,0,0,0,0,1,0],
        [0,0,0,0,0,0,1,0],
        [0,0,0,0,0,0,1,0],
        [0,1,1,1,1,1,0,0],
            ]
    ,"6": [
        [0,0,1,1,1,1,1,0],
        [0,1,0,0,0,0,0,0],
        [0,1,0,0,0,0,0,0],
        [0,1,1,1,1,1,0,0],
        [0,1,0,0,0,0,1,0],
        [0,1,0,0,0,0,1,0],
        [0,1,0,0,0,0,1,0],
        [0,0,1,1,1,1,0,0],
            ]
    ,"7": [
        [0,1,1,1,1,1,1,0],
        [0,0,0,0,0,0,1,0],
        [0,0,0,0,0,1,0,0],
        [0,0,0,0,0,1,0,0],
        [0,0,0,0,1,0,0,0],
        [0,0,0,0,1,0,0,0],
        [0,0,0,0,1,0,0,0],
        [0,0,0,0,1,0,0,0],
            ]
    ,"8": [
        [0,0,1,1,1,1,0,0],
        [0,1,0,0,0,0,1,0],
        [0,1,0,0,0,0,1,0],
        [0,0,1,1,1,1,0,0],
        [0,1,0,0,0,0,1,0],
        [0,1,0,0,0,0,1,0],
        [0,1,0,0,0,0,1,0],
        [0,0,1,1,1,1,0,0],
            ]
    ,"9": [
        [0,0,1,1,1,1,0,0],
        [0,1,0,0,0,0,1,0],
        [0,1,0,0,0,0,1,0],
        [0,1,0,0,0,0,1,0],
        [0,0,1,1,1,1,1,0],
        [0,0,0,0,0,0,1,0],
        [0,0,0,0,0,0,1,0],
        [0,1,1,1,1,1,0,0],
            ]
    ," ": [
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
            ]
    ,".": [
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,1,1,0,0,0],
        [0,0,0,1,1,0,0,0],
            ]
}

def lerp(v0, v1,t):
  return (1 - t) * v0 + t * v1

class Renderer:
    def __init__(self, width, height) -> None:
        self.data = []
        i = 0
        while i < height:
            j = 0
            row = []
            while j < width:
                row.append((0,0,0))
                j+=1 
            self.data.append(row)
            i+=1
        pass

    def Fill(self, fillColor:tuple):
        i = 0
        while i < len(self.data):
            j = 0
            while j < len(self.data[i]):
                self.data[i][j] = fillColor
                j+=1
            i +=1

    def DrawLine(self,startPos:tuple, endPos:tuple, lineColor:tuple, lineThickness = 1):
        distX = endPos[0] - startPos[0]
        distY = endPos[1] - startPos[1]
        i = 0
        if distX  >= distY:
            while i < distX:
                iY = lerp(startPos[1], endPos[1], i/distX)
                print(iY)
                print("\n")
                self.data[math.floor(iY)][math.floor(startPos[0] + i)] = lineColor
                if lineThickness >1:
                    j = math.floor(-lineThickness/2)
                    while j < lineThickness:
                        self.data[math.floor(iY) + j][math.floor(startPos[0] + i)] = lineColor
                        j+=1
                i+=1
        else:
            while i < distY:
                iX = lerp(startPos[0], endPos[0], i/distY)
                print(iX)
                print("\n")
                self.data[math.floor(startPos[1] + i)][math.floor(iX)] = lineColor
                if lineThickness >1:
                    j = math.floor(-lineThickness/2)
                    while j < lineThickness:
                        self.data[math.floor(startPos[1] + i)][math.floor(iX)+j] = lineColor
                        j+=1
                i+=1
        pass
    
    def DrawText(self, text:str, Pos:tuple, textColor:tuple, textSize = 1):
        i = 0
        while i < len(text):
            c = Letters[text[i]]
            j = 0
            while j < len(c):
                k = 0
                while k < len(c[j]):
                    if c[j][k] == 1:
                        self.data[math.floor(Pos[1]+j)][math.floor(Pos[0] +k+ (i*len(c[j])))] = textColor 
                    k+=1
                j+=1
            i+=1
        pass

    def Save(self, fileName):
        d = []
        for row in self.data:
            r = []
            for j in row:
                for i in j:
                    r.append(i)
            d.append(r)
        image = png.from_array(d, "RGB")
        image.save(fileName)

r = Renderer(100,100)
r.DrawText("0123456789 .",(0,0), (255,255,255))
r.DrawText("2.5", (0,8), (255,0,0), 1)
r.Save("TESTTEXT.png")