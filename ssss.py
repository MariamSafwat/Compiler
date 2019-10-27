import sys
def isres(st):
    if st == 'if' or st == 'then' or st == 'else' or st == 'end' or st == 'repeat' or st == 'until' or st == 'read' or st == 'write':
        result = 1
        
    #TODO check return true
    else:
        result = 0
    return result;

def issym(st):
    if st== '<' or st== '>' or st== '+' or st== '-' or st== '*' or st== '/' or st== '(' or st== ')' or st== ';' or st== ':=':
        return 1
    else :
        return 0
#TODO put strings in list of list containing value and name of each
def scanner(prog):
    ptr = 0
    finish = 0
    state = 'start' #start
    while(ptr <= len(prog)-1):
        
        
        st = ''
        if state == 'start':
            if prog[ptr] == '{':
                state = 'incomment'
                ptr += 1
            elif prog[ptr] == ' ':
                ptr += 1
            elif prog[ptr].isalpha():
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
                if(ptr == len(prog)):
                    print('7aseb error: comment not closed')
                    sys.exit()
            if(prog[ptr] == '}'):
                state = 'start'
                ptr += 1
            

        if state == 'id':
            if(ptr < len(prog)):
                while(prog[ptr].isalpha()):
                    st += prog[ptr]
                    ptr += 1
                    if(ptr == len(prog)):
                        finish = 1
                        break 
                        
                if(finish == 0):
                    ######t2rebn lw geh num aw 7aga msh symbol f nos el id error###
                    if(prog[ptr] == ' ' ):
                        #el id 5ls ro7 le done
                        #TODO check space wa7da wla eh
                        state = 'done'
                        ptr += 1
                    elif not(issym(prog[ptr])):
                        print('7aseb identifier error')
                        sys.exit()
                    
                        
            state = 'done'
            """   
                if prog[ptr] != ' ':
                    #error
                    #TODO ynf3 yb2o laz2en f b3d?
                    print('7aseb identifier error')
            """   
                
        if state == 'num':
            if(ptr < len(prog)):
                while(prog[ptr].isdigit()):
                    st += prog[ptr]
                    ptr += 1
                    if(ptr == len(prog)):
                        finish = 1
                        break
                if(finish == 0):
                    if(prog[ptr] == ' ' ):
                        #el num 5ls ro7 le done
                        #TODO check space wa7da wla eh
                        state = 'done'
                        ptr += 1
                    elif not(issym(prog[ptr])):
                        print('7aseb number error')
                        sys.exit()
                        
            state = 'done'
            
                

        if state == 'assign':
            if prog[ptr] == '=':
                st += prog[ptr]
                state = 'done'
                ptr += 1
            else:
                print('7aseb assign error')
                sys.exit()
            
        if state == 'done':
            #TODO reseverd, symbol, number, identifier
                #TODO put output in double list
                state = 'start'
                #result = isres(st);
                if (isres(st)):
                    print('reseved:', st)
                elif(st.isdigit()):
                    print('number:', st)
                elif(st == ':='):
                    print('assign:', st)
                elif(issym(st)):
                    print('symbol:' , st)
                elif(st.isalpha()):
                    print('identifier:', st)
                else:
                    print('7aseb error w 5las')
                    sys.exit()
                    


prog = input('ektb:')
scanner(prog)
