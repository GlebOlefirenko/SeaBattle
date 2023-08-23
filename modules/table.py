import pygame
import modules.data_base as m_data
import modules.search_path as m_path

import modules.cell as m_cell
import modules.use_class as m_class

pygame.init()
# Создаем класс для таблицы
check = lambda rotate: 1 if rotate %180 == 0 else 10
class Table:
    def __init__(self, x1 = 0, y1 = 0):
        self.X = x1
        self.Y = y1
    def create_cells(self, list_cells):
        x = self.X
        y = self.Y
        count_cell = 0
        for row in range(10):
            for cell in range(10):
                count_cell += 1
                cell1 = m_cell.Cell(x1 = x, x2 = x + 35, y1 = y, y2 = y + 35, name = 0,row=row)
                list_cells.append(cell1)
                
                x = x + 32
            y = y + 31.7
            x = self.X
    def check(self,count,map, rotate = 0):
        yes_no=1
        if rotate < 2:

            for cell1 in range(m_data.select_ship):
                # print(count+cell1-1)
                if count+cell1>99 or (count+cell1)%10==0 and cell1!=0 or map[count+cell1].NAME!=0:
                    yes_no=0
        else:
            for cell1 in range(m_data.select_ship):
                if count + cell1 * 10 > 99 and cell1 != 0 or map[count + cell1 * 10].NAME != 0:
                    yes_no = 0

        return yes_no
    def start_game(self,x,y):
        if self.X<x<self.X+352 and self.Y<y<self.Y+352:
            return 1
        return 0
    def set1(self,count,map, attack = 0):
        if attack == True:
            row=map[count].ROW
            if count>0 and map[count - 1].PRESSED == 0 and map[count - 1].ROW == row:
                map[count-1].PRESSED = 1
            if count+1<100 and map[count + 1].ROW == row and map[count + 1].PRESSED == 0:
                map[count+1].PRESSED = 1
            for count2 in range(3):
                if count - 11 + count2 > -1 and map[count - 11 + count2].PRESSED == 0 and map[count - 11 + count2].ROW == row - 1:
                    map[count-11+count2].PRESSED = 1
            for count2 in range(3):
                if count + 9 + count2 < 100 and map[count + 9 + count2].PRESSED == 0 and map[count + 9 + count2].ROW == row + 1:
                   map[count+9+count2].PRESSED = 1

                   
        else:
            row=map[count].ROW
            if count>0 and map[count-1].NAME==0 and map[count-1].ROW==row:
                map[count-1].NAME=6
            if count+1<100 and map[count+1].ROW==row and map[count+1].NAME==0:
                map[count+1].NAME=6
            for count2 in range(3):
                if count-11+count2>-1 and map[count-11+count2].NAME==0 and map[count-11+count2].ROW==row-1:
                    map[count-11+count2].NAME=6
            for count2 in range(3):
                if count+9+count2<100 and map[count+9+count2].NAME==0 and map[count+9+count2].ROW==row+1:
                    map[count+9+count2].NAME=6
        return map
    def attack_ship(self, list_cells, list_ships, screen_game):
        for ship in list_ships:
            # print(ship.LEVEL, list_cells[ship.CELL].PRESSED)
            
            c = check(ship.ROTATE)
            l = list_cells
            if ship.LEVEL == 1 and l[ship.CELL].PRESSED == 1:
                ship.blit_sprite(screen_game)
                self.set1(ship.CELL, l, attack = 1)
            if ship.CELL+ c<100 and ship.LEVEL == 2 and l[ship.CELL].PRESSED == 1 and l[ship.CELL+ c].PRESSED==1:
                ship.blit_sprite(screen_game)
                self.set1(ship.CELL, l, attack = 1)
                self.set1(ship.CELL+ c, l, attack = 1)
            if ship.CELL+ c<100 and ship.LEVEL == 3 and l[ship.CELL].PRESSED == 1 == l[ship.CELL+ c].PRESSED==1 == l[ship.CELL + c * 2].PRESSED:
                ship.blit_sprite(screen_game)
                self.set1(ship.CELL, l, attack = 1)
                self.set1(ship.CELL+ c, l, attack = 1)
                self.set1(ship.CELL + c * 2, l, attack= 1)
            if ship.CELL+ c<100 and ship.LEVEL == 4 and l[ship.CELL].PRESSED == 1 == l[ship.CELL+ c].PRESSED==1 == l[ship.CELL + c * 2].PRESSED == 1 == l[ship.CELL + c * 3].PRESSED:
                ship.blit_sprite(screen_game)
                self.set1(ship.CELL, l, attack = 1)
                self.set1(ship.CELL+ c, l, attack = 1)
                self.set1(ship.CELL + c * 2, l, attack= 1)  
                self.set1(ship.CELL + c * 3, l, attack= 1)
    def get_pressed(self, x, y, list_cells,attack=0):
        keys = pygame.key.get_pressed()
        rotate = 0
        if keys[pygame.K_RIGHT]:
            rotate = 1
        elif keys[pygame.K_UP]:
            rotate = 3
        elif keys[pygame.K_DOWN]:
            rotate = 2
        
        count=-1
        for cell in list_cells:
            count+=1
            if cell.X1 < x and cell.X2 > x and attack:
                if cell.Y1 < y and cell.Y2 > y and not m_data.turn and not cell.PRESSED:
                    # print(cell.NAME)
                    # m_class.ship.blit_sprit(screen_game, cell.X1, cell.Y1)
                    cell.PRESSED = True
                    # m_class.ship1.app
                    if cell.NAME == 0 or cell.NAME == 6:

                        m_data.turn=1

            
            if x<100 and y<50:
                m_data.select_ship = 1
            elif 100<x<165 and y<50:
                m_data.select_ship = 2
            elif 300<x<390 and y<50:
                m_data.select_ship = 3
            elif 500<x<620 and y<50:
                m_data.select_ship = 4
            if cell.X1<x<cell.X2 and cell.Y1<y<cell.Y2 and m_data.count_ships[m_data.select_ship-1][0]<m_data.count_ships[m_data.select_ship-1][1] and self.check(count,list_cells, rotate):
                
                # cell.NAME=m_data.select_ship
                if rotate < 2:
                    ship=m_class.Ships(x=cell.X1,y=cell.Y1, width= m_data.select_ship * 30, rotate = rotate*180)

                    for count1 in range(m_data.select_ship):
                        list_cells[count+count1].NAME=m_data.select_ship
                    m_data.count_ships[m_data.select_ship-1][0]+=1
                    for count3 in range(m_data.select_ship):
                        self.set1(count+count3,map=list_cells)
                else:
                    ship=m_class.Ships(x=cell.X1,y=cell.Y1, width= m_data.select_ship * 30, rotate = rotate * 180 + 90)
                    for count1 in range(m_data.select_ship):
                        list_cells[count+count1 * 10].NAME=m_data.select_ship
                    m_data.count_ships[m_data.select_ship-1][0]+=1
                    for count3 in range(m_data.select_ship):
                        self.set1(count+count3 * 10 ,map=list_cells)   
                m_data.list_ship.append(ship)
                ship.load_image(m_path.find_path_to_file(f"images/ships/bship{m_data.select_ship}.png"))
table1 = Table(x1 = 112, y1 = 164)
table2 = Table(x1 = 573, y1 = 164)
