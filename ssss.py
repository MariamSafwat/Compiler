def isres(st):
    print('gwa el fn')
    if st == 'if' or st == 'then' or st == 'else' or st == 'end' or st == 'repeat' or st == 'until' or st == 'read' or st == 'write':
        result = 1
        
    #TODO check return true
    else:
        result = 0
    return result;

def issym(st):
    print('gwa func symbol')
    if st== '<' or st== '>' or st== '+' or st== '-' or st== '*' or st== '/' or st== '(' or st== ')' or st== ';' or st== ':=':
        return 1
    else :
        return 0

def scanner(prog):
    ptr = 0
    while(ptr < len(prog)-1):
        state = 'start' #start
        
        st = ''
        if state == 'start':
            if prog[ptr] == '{':
                state = 'incomment'
                ptr += 1
            elif prog[ptr] == ' ':
                ptr += 1
            elif prog[ptr].isalpha():
                print('wslt hna')
                state = 'id'
                st += prog[ptr]
                ptr += 1
            elif prog[ptr].isdigit():
                state = 'num'
                st += prog[ptr]
                ptr += 1
            elif prog[ptr] == ':':
                state = 'assign'
                st += prog[ptr]
                ptr += 1
            else:
                state = 'done'
                st += prog[ptr]
                ptr += 1
            
        if state == 'incomment':
            while(prog[ptr] != '}'):
                ptr += 1
            if(prog[ptr] == '}'):
                state = 'start'
                ptr += 1

        if state == 'id':
            while(prog[ptr].isalpha()):
                print('wslt id')
                st += prog[ptr]
                ptr += 1
            if(prog[ptr] == ' ' or prog[ptr] == ';'):
                #el id 5ls ro7 le done
                #TODO check space wa7da wla eh
                print(state)
                state = 'done'
                print(state)
                ptr += 1
                print(ptr)
            """   
            if prog[ptr] != ' ':
                #error
                #TODO ynf3 yb2o laz2en f b3d?
                print('7aseb identifier error')
             """   
                
        if state == 'num':
            while(prog[ptr].isdigit()):
                print('wslt num')
                st += prog[ptr]
                ptr += 1
            if(prog[ptr] == ' ' or prog[ptr] == ';'):
                #el num 5ls ro7 le done
                #TODO check space wa7da wla eh
                print(state)
                state = 'done'
                print(state)
                ptr += 1
                print(ptr)

        if state == 'assign':
            if prog[ptr] == '=':
                st += prog[ptr]
                state = 'done'
                ptr += 1
            else:
                print('7aseb assign error')
            
        if state == 'done':
            #TODO reseverd, symbol, number, identifier
            #TODO put output in double list
            print('wslt done')
            state = 'start'
            #result = isres(st);
            if (isres(st)):
                print('reseved:', st)
            elif(st.isdigit()):
                print('number:', st)
            elif(st == ':='):
                print('assign:', st)
            elif(issym(st)):
                print('symbol' , st)


prog = input('ektb:')
scanner(prog)
            
                


        
        
                
