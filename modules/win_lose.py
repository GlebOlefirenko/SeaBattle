def win_lose(map):
    test=1
    for cell in map:
        if cell.NAME!=0 and 6!=cell.NAME and cell.PRESSED==0:
            test=0
    return test