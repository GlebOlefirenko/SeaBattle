import random
import modules.data_base as m_data
import modules.table as m_table
import modules.use_class as m_class
import modules.search_path as m_path
def place():
    m_data.list_ship_enemy = []
    end=1
    r=random.randint
    while end:
        end=0
        test=0
        count=0
        m_data.select_ship=1
        while test<4:
            print(1)
            target=random.randint(0,99)
            cell=m_data.list_cells2[target]

            if m_data.list_cells2[target].NAME==0:
                
                ship=m_class.Ships(x=cell.X1,y=cell.Y1, width= 30,rotate=r(0,3) * 90, cell = target, level=1)
                ship.load_image(m_path.find_path_to_file(f"images/ships/bship1.png"))
                m_data.list_cells2[target].NAME=1
                m_data.list_ship_enemy.append(ship)
                test+=1
                m_table.table2.set1(target,m_data.list_cells2)
            if count > 99:
                end=1
                break
        test=0
        m_data.select_ship=2
        while test<3:
            rotate=random.randint(0,3)
            print(2)
            target=random.randint(0,99)
            cell=m_data.list_cells2[target]
            if m_table.table2.check(target,m_data.list_cells2, rotate):
                if rotate < 2:
                    ship=m_class.Ships(x=cell.X1,y=cell.Y1, width= 60,rotate=r(0,1) * 180, cell = target, level = 2)
                    ship.load_image(m_path.find_path_to_file(f"images/ships/bship2.png"))
                    m_data.list_cells2[target].NAME=2
                    m_data.list_cells2[target+1].NAME=2
                    m_data.list_ship_enemy.append(ship)
                    test+=1
                    m_table.table2.set1(target,m_data.list_cells2)
                    m_table.table2.set1(target+1,m_data.list_cells2)
                else:
                    ship=m_class.Ships(x=cell.X1,y=cell.Y1, width= 60,rotate=r(0,1) * 180 + 90, cell = target, level= 2)
                    ship.load_image(m_path.find_path_to_file(f"images/ships/bship2.png"))
                    m_data.list_cells2[target].NAME=2
                    m_data.list_cells2[target+10].NAME=2
                    m_data.list_ship_enemy.append(ship)
                    test+=1
                    m_table.table2.set1(target,m_data.list_cells2)
                    m_table.table2.set1(target+10,m_data.list_cells2)
            if count > 99:
                end=1
                break
        test=0
        m_data.select_ship=3
        while test<2:
            print(3)
            count+=1
            rotate = random.randint(0, 3)
            target=random.randint(0,99)
            cell=m_data.list_cells2[target]
            if m_table.table2.check(target,m_data.list_cells2, rotate):
                if rotate < 2:

                    ship=m_class.Ships(x=cell.X1,y=cell.Y1, width= 90,rotate=r(0,1)* 180, cell = target, level=3)
                    ship.load_image(m_path.find_path_to_file(f"images/ships/bship3.png"))
                    m_data.list_cells2[target].NAME=3
                    m_data.list_cells2[target+1].NAME=3
                    m_data.list_cells2[target+2].NAME=3
                    m_data.list_ship_enemy.append(ship)
                    test+=1
                    m_table.table2.set1(target,m_data.list_cells2)
                    m_table.table2.set1(target+1,m_data.list_cells2)
                    m_table.table2.set1(target+2,m_data.list_cells2)
                else:

                    ship=m_class.Ships(x=cell.X1,y=cell.Y1, width= 90,rotate=r(0,1)* 180 + 90, cell = target, level = 3)
                    ship.load_image(m_path.find_path_to_file(f"images/ships/bship3.png"))
                    m_data.list_cells2[target].NAME=3
                    m_data.list_cells2[target+10].NAME=3
                    m_data.list_cells2[target+20].NAME=3
                    m_data.list_ship_enemy.append(ship)
                    test+=1
                    m_table.table2.set1(target,m_data.list_cells2)
                    m_table.table2.set1(target+10, m_data.list_cells2)
                    m_table.table2.set1(target+20, m_data.list_cells2)                  
            if count > 99:
                end=1
                break
        test=0
        m_data.select_ship=4
        while test<1:
            print(4)
            count+=1
            rotate = random.randint(0, 3)
            target=random.randint(0,99)
            cell=m_data.list_cells2[target]
            if m_table.table2.check(target,m_data.list_cells2, rotate):
                if rotate < 2:
                    ship=m_class.Ships(x=cell.X1,y=cell.Y1, width= 120,rotate=r(0,1) * 180, cell = target, level = 4)
                    ship.load_image(m_path.find_path_to_file(f"images/ships/bship4.png"))
                    m_data.list_cells2[target].NAME=4
                    m_data.list_cells2[target+1].NAME=4
                    m_data.list_cells2[target+2].NAME=4
                    m_data.list_cells2[target+3].NAME=4
                    m_data.list_ship_enemy.append(ship)
                    test+=1
                    m_table.table2.set1(target,m_data.list_cells2)
                    m_table.table2.set1(target+1,m_data.list_cells2)
                    m_table.table2.set1(target+2,m_data.list_cells2)
                    m_table.table2.set1(target+3,m_data.list_cells2)
                else:
                    ship=m_class.Ships(x=cell.X1,y=cell.Y1, width= 120,rotate=r(0,1) * 180 + 90, cell = target, level = 4)
                    ship.load_image(m_path.find_path_to_file(f"images/ships/bship4.png"))
                    m_data.list_cells2[target].NAME=4
                    m_data.list_cells2[target+10].NAME=4
                    m_data.list_cells2[target+20].NAME=4
                    m_data.list_cells2[target+30].NAME=4
                    m_data.list_ship_enemy.append(ship)
                    test+=1
                    m_table.table2.set1(target,m_data.list_cells2)
                    m_table.table2.set1(target+10,m_data.list_cells2)
                    m_table.table2.set1(target+20,m_data.list_cells2)
                    m_table.table2.set1(target+30,m_data.list_cells2)
            if count > 99:
                end=1
                break
        if end:
            m_data.list_cells2=[]
            m_data.list_ship_enemy=[]
            m_table.table2.create_cells(m_data.list_cells2)
        m_data.select_ship=1
place()
def bot_attack3(target1, c=1):

    check=0
    check1 = 1
    target = 0
    target += target1
    if m_data.p1 and c:
        bot_attack3(m_data.target1,0)
    else:

        map=m_data.list_cells1
        print(target / 10, map[target-10].PRESSED, m_data.turn1,998)
        if target>0 and map[target-1].PRESSED==0 and m_data.turn1 == 0 and map[target - 1].ROW == map[target].ROW:
            target-=1
        elif target<99 and map[target+1].PRESSED==0 and m_data.turn1 == 1 and map[target + 1].ROW == map[target].ROW:
            target+=1
        elif target > 10 and map[target-10].PRESSED == 0 and m_data.turn1 == 2 and map[target - 10].ROW == map[target].ROW - 1:
            target -= 10
        elif target < 90 and map[target + 10].PRESSED == 0 and m_data.turn1 == 3 and map[target + 10].ROW == map[target].ROW + 1:
            target += 10
        else:
                #print(target, m_data.target, m_data.target1)
                if m_data.p1:
                    m_data.p1=0
                    m_data.p=0
                    m_data.target1=None
                    m_data.target=None
                    m_data.turn1 = 0
                    m_data.start_attack = 0                
                else:
                    m_data.p1=1
                    check=1
                    if m_data.turn1 == 3:
                        m_data.turn1 = 2
                    elif m_data.turn1 == 2:
                        m_data.turn1 = 3
                    else: 
                        m_data.turn1 = not m_data.turn1
                                        
        if m_data.p and check1:
            if map[target].NAME==0 or map[target].NAME==6:
                m_data.turn=0
                #print(random.randint(-1000, 0))
                if m_data.p1 and not check:
                    m_data.target=None
                    m_data.target1=None
                    m_data.p1=0
                    m_data.p=0
                    m_data.turn1 = 0
                    m_data.start_attack = 0
                else:
                    m_data.p1=1
                
                    if m_data.turn1 == 3:
                        m_data.turn1 = 2
                    elif m_data.turn1 == 2:
                        m_data.turn1 = 3
                    else: 
                        m_data.turn1 = not m_data.turn1

                    
            

            elif c:m_data.target=target
            else:m_data.target1=target
            map[target].PRESSED=1
            # if not map[target].NAME == 0 and not map[target].NAME == 6:
            #     m_data.start_attack = 1
def bot_attack2(target1,c=1):
    print(20000, target1)
    check=0
    check1 = 1
    target = 0
    rotate = None
    target += target1
    if m_data.start_attack:
        bot_attack3(m_data.target,1)
    else:

        map=m_data.list_cells1
        print(target / 10, map[target-10].PRESSED, m_data.turn1,998)
        if target>0 and map[target-1].PRESSED==0 and map[target -1].ROW ==  map[target].ROW :
            target-=1
            rotate = 0
        elif target<99 and map[target+1].PRESSED==0 and map[target +1].ROW ==  map[target].ROW:
            target+=1
            rotate = 1
        elif target > 10 and map[target-10].PRESSED == 0 and map[target -10].ROW  ==  map[target].ROW -1:
            target -= 10
            rotate = 2
        elif target < 90 and map[target + 10].PRESSED == 0 and map[target +10].ROW  ==  map[target].ROW +1:
            target += 10
            rotate = 3
        else:
            #check1 = 0
            #print(m_data.start_attack)
            # if not m_data.start_attack and m_data.turn1<3:
            #m_data.turn1 += 1
            #if m_data.turn1>4 :
            m_data.p1=0
            print(m_data.p, 19000)
            m_data.p=0
            m_data.target1=None
            m_data.target=None
            m_data.turn1 = 0
            m_data.start_attack = 0  
            # else:
                
            
            #     if m_data.p1:
            #         m_data.p1=0
            #         m_data.p=0
            #         m_data.target1=None
            #         m_data.target=None
            #         m_data.turn1 = 0
            #         m_data.start_attack = 0                
            #     else:
            #         m_data.p1=1
            #         check=1
            #         if m_data.turn1 == 3:
            #             m_data.turn1 = 2
            #         elif m_data.turn1 == 2:
            #             m_data.turn1 = 3
            #         else: 
            #             m_data.turn1 = not m_data.turn1
                                        
        if m_data.p and check1:
            if map[target].NAME==0 or map[target].NAME==6:
                m_data.turn=0
                # if m_data.p1 and not check:
                #     m_data.target=None
                #     m_data.target1=None
                #     m_data.p1=0
                #     m_data.p=0
                #     m_data.turn1 = 0
                #     m_data.start_attack = 0
                # else:
                #     m_data.p1=1
                
                #     if m_data.turn1 == 3:
                #         m_data.turn1 = 2
                #     elif m_data.turn1 == 2:
                #         m_data.turn1 = 3
                #     else: 
                #         m_data.turn1 = not m_data.turn1

                    
            

            else:
                m_data.target=target
                m_data.start_attack = 1
                m_data.turn1 = rotate
            # else:m_data.target1=target
            map[target].PRESSED=1
            #if not map[target].NAME == 0 and not map[target].NAME == 6:
                
                
def bot_attck():
    if m_data.turn:
        
        if m_data.target != None:
            m_data.p = 1
            bot_attack2(m_data.target)
        else:
            
            map=m_data.list_cells1
            while True:
                target=random.randint(0,99)
                if not map[target].PRESSED:
                    map[target].PRESSED=1
                    if map[target].NAME==0 or map[target].NAME==6:
                        m_data.turn=0
                        break
                    else:
                        print(9999999999999999, 713)
                        m_data.target=target
                        m_data.p=1
                        m_data.target1=target                 
                        m_data.p1=0
                    #  m_data.p=0
                    #  m_data.target1=None
                    #  m_data.target=None
                        m_data.turn1 = 0
                        m_data.start_attack = 0  
                        #while m_data.p:
                        #    
#                       
                        break
                        #    bot_attack2(m_data.target)
