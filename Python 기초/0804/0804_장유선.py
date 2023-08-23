class Region:

    def __init__(self, MinX=0, MinY=0, MaxX=0, MaxY=0):
        if MinX > MaxX:
            MinX, MaxX = MaxX, MinX
        
        self.MinX = MinX
        self.MinY = MinY
        self.MaxX = MaxX
        self.MaxY = MaxY


    def getWidth(self):
        return self.MaxX-self.MinX
        
    def getHeight(self):
        return self.MaxY-self.MinY
       
    def getCenterPoint(self):
        return ((self.MinX + self.MaxX)/2, (self.MinY + self.MaxY)/2)
        

    def getLeftBottomPoint(self):
        return (self.MinX, self.MinY)
    
    def getRightTopPoint(self):
        return (self.MaxX, self.MaxY)
    
    def ptInRect(self,x,y):
        return self.MinX<= x <= self.MaxX and self.MinY <= y <= self.MaxY
     
        

r1 = Region(0, 0, 100, 100)
print(r1.getWidth())
print(r1.getHeight())
print(r1.getCenterPoint())
print(r1.getLeftBottomPoint())
print(r1.getRightTopPoint())
print(r1.ptInRect(1, 1))
print(r1.ptInRect(200, 1))
print('\n')

r2 = Region(100, 0, 0, 100)
print(r2.getWidth())
print(r2.getHeight())
print(r2.getCenterPoint())
print(r2.getLeftBottomPoint())
print(r2.getRightTopPoint())
print(r2.ptInRect(1, 1))
print(r2.ptInRect(200, 1))