import pygame 
# import modules.search_path as m_path
# import modules.date_base as m_base

pygame.init()

# Создаем класс для клеточек
class Cell:
    def __init__(self, x1, x2, y1, y2, name, count=0,row=0):
        self.X1 = x1
        self.X2 = x2
        self.Y1 = y1
        self.Y2 = y2
        self.NAME = name
        self.PRESSED = False
        self.count = count 
        self.ROW=row
    def draw_cross(self,screen):
        
        color=(25,255,25)
        if self.NAME!=0 and self.NAME!=6:
            color=(255,25,25)
        pygame.draw.line(screen,color,(self.X1,self.Y1),(self.X2,self.Y2),5)
        pygame.draw.line(screen,color,(self.X2,self.Y1),(self.X1,self.Y2),5)