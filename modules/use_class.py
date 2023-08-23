import pygame 
import modules.search_path as m_path
import modules.data_base as m_data
import modules.table as m_table
pygame.init()

# Класс для создания кораблика
class Ships:
    def __init__(self, x, y,width=30,height=30,rotate=0,player=0, cell = None, level =None):
        self.WIDTH = width
        self.HEIGHT = height
        self.X = x
        self.Y = y
        self.APP = None
        self.IMG=None
        self.LEVEL = level
        self.CELL = cell
        self.ROTATE=rotate
        self.PLAYER=player
    def load_image(self, load_ship=m_path.find_path_to_file("images/ships/bship1.png")):
        image_ship = pygame.image.load(m_path.find_path_to_file(load_ship))
        self.IMG= pygame.transform.scale(image_ship,(self.WIDTH, self.HEIGHT))
        # if self.ROTATE == 1:
        #     self.IMG=pygame.transform.flip(self.IMG, 1 ,0)
        # if self.ROTATE == 2:
        #     self.IMG = pygame.transform.flip(self.IMG, 1, 1)
        # if self.ROTATE == 3:
        #     self.IMG = pygame.transform.flip(self.IMG, 0, 1)
        
        
        self.IMG = pygame.transform.rotate(self.IMG, self.ROTATE)
        return self.IMG
    
    
    def blit_sprite(self, screen_game, x=None, y=None):
        if x== None:
            x=self.X 
        if y==None:
            y=self.Y
        screen_game.blit(self.IMG, (x, y))

# ship = Ships(x = 200,y = 200)

# Класс для создания фона
class Background:
    def __init__(self, width = 1000, height = 700, x = 0, y = 0):
        self.WIDTH = width
        self.HEIGHT = height
        self.X = x
        self.Y = y
    
    
    def load_image(self):
        image_background = pygame.image.load(m_path.find_path_to_file("images/background.png"))
        img_transform = pygame.transform.scale(image_background,(self.WIDTH, self.HEIGHT))
        return img_transform
    
    
    def blit_sprite(self, screen_game):
        screen_game.blit(self.load_image(), (self.X, self.Y))

background = Background(x = 0, y = 0)
# Класс для создания кнопки
class Button:
    def __init__(self, x, y):
        self.WIDTH = 250
        self.HEIGHT = 152
        self.X = x
        self.Y = y
    

    def load_image(self):
        image_button = pygame.image.load(m_path.find_path_to_file("images/buttons/button.png"))
        img_transform = pygame.transform.scale(image_button,(self.WIDTH, self.HEIGHT))
        return img_transform
    
    def restart(self,x,y,screen_game):
        if self.X<x<self.X+self.WIDTH and self.Y<y<self.Y+self.HEIGHT:
            import modules.bot as m_bot
            pygame.display.set_caption("морський бій: розміщення")
            m_data.list_cells1 = []
            m_data.list_cells2 = []
            m_data.start_game=0
            m_data.count_ships = [[0, 4], [0, 3], [0, 2], [0, 1]]
            m_data.list_ship = []
            m_data.select_ship = 1
            m_data.turn=0
            m_data.p=0
            m_data.p1=0
            m_data.target=None
            m_data.target1=None
            m_data.win=0
            m_data.list_ship_enemy = []
            m_data.turn1 = 0
            m_data.start_attack = 0
            m_table.table1.create_cells(m_data.list_cells1)
            m_table.table2.create_cells(m_data.list_cells2)
            m_bot.place()
            background.blit_sprite(screen_game)

            ship1 = Ships(x = 0 , y = 0 ,player=1)
            ship1.load_image("images/ships/bship1.png")
            m_data.list_ship.append(ship1)


            ship2 = Ships(x = 100 , y = 0 ,width=60,player=1)
            ship2.load_image("images/ships/bship2.png")
            m_data.list_ship.append(ship2)

            ship3 = Ships(x = 300 , y = 0 ,width=90,player=1)
            ship3.load_image("images/ships/bship3.png")
            m_data.list_ship.append(ship3)

            
            ship4 = Ships(x = 500 , y = 0 ,width=120,player=1)
            ship4.load_image("images/ships/bship4.png")
            m_data.list_ship.append(ship4)
            button.blit_sprite(screen_game)
    def blit_sprite(self, screen_game):
        screen_game.blit(self.load_image(), (self.X, self.Y))

button = Button(x = 375, y = 520)

# Створюємо всі види кораблів 
for object in range (4):
    ship1 = Ships(x = 0 , y = 0 ,player=1)
    ship1.load_image("images/ships/bship1.png")
    m_data.list_ship.append(ship1)

for object in range (3):
    ship2 = Ships(x = 100 , y = 0 ,width=60,player=1)
    ship2.load_image("images/ships/bship2.png")
    m_data.list_ship.append(ship2)

for object in range (2):
    ship3 = Ships(x = 300 , y = 0 ,width=90,player=1)
    ship3.load_image("images/ships/bship3.png")
    m_data.list_ship.append(ship3)

  
ship4 = Ships(x = 500 , y = 0 ,width=120,player=1)
ship4.load_image("images/ships/bship4.png")
m_data.list_ship.append(ship4)