import pygame 
import modules.use_class as m_class
import modules.table as m_table
import modules.data_base as m_data
import modules.win_lose as m_win
pygame.init()

width = 1000
height = 700

screen_game = pygame.display.set_mode((width, height))

FPS = pygame.time.Clock()
m_class.background.blit_sprite(screen_game)

m_class.button.blit_sprite(screen_game)

m_table.table1.create_cells(m_data.list_cells1)

pygame.display.set_caption("морський бій: розміщення")
m_table.table2.create_cells(m_data.list_cells2)
print(132824)
import modules.bot as m_bot
game = True

# m_data.list_ship=[]
while game:

    if m_data.start_game and not m_data.win:
            m_bot.bot_attck()
    for event in pygame.event.get():
        m_table.table2.attack_ship(m_data.list_cells2, m_data.list_ship_enemy, screen_game)
        if m_data.start_game:
            w=m_win.win_lose(m_data.list_cells1)
            l=m_win.win_lose(m_data.list_cells2)
            if w:
                m_data.win=1
                pygame.display.set_caption(f"морський бій: ви програли")
            if l:
                m_data.win=1
                pygame.display.set_caption(f"морський бій: ви виграли")
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.MOUSEBUTTONDOWN :
            x, y = event.pos
            # print(x, y)
            m_class.button.restart(x,y, screen_game)
            
            if not m_data.start_game and not m_data.win:
                m_table.table1.get_pressed(x, y, m_data.list_cells1)
            elif not m_data.win:
                m_table.table2.get_pressed(x, y, m_data.list_cells2,attack=1)
            # if m_class.button.start_game(x,y) and m_data.start_game==0:
            if m_table.table2.start_game(x,y) and m_data.start_game==0:
                pygame.display.set_caption(f"морський бій: не вистачає однопалубних кораблів у кількості {4-m_data.count_ships[0][0]}")
                if m_data.count_ships[0]==[4,4]:
                    pygame.display.set_caption(f"морський бій: не вистачає двопалубних кораблів у кількості {3-m_data.count_ships[1][0]}")
                    if m_data.count_ships[1]==[3,3]:
                        pygame.display.set_caption(f"морський бій: не вистачає трипалубних кораблів у кількості {2-m_data.count_ships[2][0]}")
                        if m_data.count_ships[2]==[2,2]:
                            pygame.display.set_caption(f"морський бій: не вистачає чотирьох кораблів у кількості 1")
                            if m_data.count_ships[3]==[1,1]:
                                m_data.start_game=1
                                pygame.display.set_caption("морський бій: початок гри")
                # print(1039456)
            # 
    # ship.blit_sprite(screen_game)
    # ship.blit_sprite(screen_game)
    # ship.blit_sprite(screen_game)
    # ship.blit_sprite(screen_game)
    if m_data.win:
        for ship in  m_data.list_ship_enemy:
            ship.blit_sprite(screen_game)
    for ship in m_data.list_ship:
        ship.blit_sprite(screen_game)
    for cell in m_data.list_cells2:
        if cell.PRESSED:
            cell.draw_cross(screen_game)
        
    for cell in m_data.list_cells1:
        if cell.PRESSED:
            cell.draw_cross(screen_game)
    FPS.tick(60)
    
    pygame.display.flip()