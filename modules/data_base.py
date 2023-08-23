import modules.cell as m_cell
# Поле для гравця
list_cells1 = []
# list=[0,0,0,
#       0,0,0,
#       0,0,0]

# list=[[0,0,0],
#       [0,0,0],
#       [0,0,0]]
# x,y=110-30,134
# for cell in range(100):
#     x+=30
#     if cell%10==0:
#         y+=30
#         x=0
#     list_cells1.append(m_cell.Cell(x1 = x, y1 = y, y2 = y+30,x2=x+30,name=cell))
# Поле для бота
start_game=0
list_cells2 = []
count_ships = [[0, 4], [0, 3], [0, 2], [0, 1]]
list_ship = []
select_ship = 1
turn=0
p=0
p1=0
target=None
target1=None
win=0
list_ship_enemy = []
turn1 = 0
start_attack = 0