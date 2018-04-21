def phoneCheck(pnum):
    pnum = str.strip(pnum)
    numDigits = 0
    ignore = ['(',')','.','-',' ']

    if pnum[0:1] == '+1' :
        pnum = pnum[2:]
    elif (not pnum[0].isdigit()) or (not pnum[0] == '('):
        return False
        



    for char in pnum:
        if(char == ignore[0] or 
            char == ignore[1] or
            char == ignore[2] or 
            char == ignore[3] or
            char == ignore[4]):
            continue
        
        

