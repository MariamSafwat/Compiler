#import sys
def isres(st):
    if st == 'if' or st == 'then' or st == 'else' or st == 'end' or st == 'repeat' or st == 'until' or st == 'read' or st == 'write':
        result = 1
    else:
        result = 0
    return result;

def issym(st):
    if st== '<' or st== '>' or st== '+' or st== '-' or st== '*' or st== '/' or st== '(' or st== ')' or st== ';' or st== ':=' or st =='=':
        return 1
    else :
        return 0

def scanner(prog):
    #print(prog)
    prog = prog.replace('\n',' ')
    tokens = []
    
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
            elif issym(prog[ptr]):
                state = 'done'
                st += prog[ptr]
                ptr += 1
            else:
                newstr = 'Error: ' + prog[ptr] + ' is undefined'
                tokens.append(newstr)
                listTokens = '\n'.join([str(elem) for elem in tokens])
                return listTokens
                
            
        if state == 'incomment':
            while(prog[ptr] != '}'):
                ptr += 1
                if(ptr == len(prog)):
                    newstr = 'Error: comment not closed'
                    tokens.append(newstr)
                    
                    listTokens = '\n'.join([str(elem) for elem in tokens])
                    return listTokens
            if(prog[ptr] == '}'):
                state = 'start'
                ptr += 1
            

        if state == 'id':
            if(ptr < len(prog)):
                while(prog[ptr].isalpha()):
                    print(st)
                    st += prog[ptr]
                    print(st)
                    ptr += 1
                    if(ptr == len(prog)):
                        finish = 1
                        break 
                        
                if(finish == 0):
                    
                    if(prog[ptr] == ' ' ):
                        
                        state = 'done'
                        
                    elif not(issym(prog[ptr]) or prog[ptr] == ':'):
                        if(prog[ptr].isdigit()):
                            newstr = 'Error: identifiers and numbers have to be separated by space'
                            tokens.append(newstr)
                            
                        else:
                            newstr = 'Identifier Error: '+ prog[ptr] +' is undefined'
                            tokens.append(newstr)
                            
                        
                        
                        listTokens = '\n'.join([str(elem) for elem in tokens])
                        return listTokens
                        
                    
                        
            state = 'done'
            
                
        if state == 'num':
            if(ptr < len(prog)):
                while(prog[ptr].isdigit()):
                    print(st)
                    st += prog[ptr]
                    print(st)
                    ptr += 1
                    if(ptr == len(prog)):
                        finish = 1
                        break
                if(finish == 0):
                    if(prog[ptr] == ' '):
                        
                        
                        state = 'done'
                        
                    elif not(issym(prog[ptr]) or prog[ptr] == ':'):
                        if(prog[ptr].isalpha()):
                            newstr = 'Error: identifiers and numbers have to be separated by space'
                            tokens.append(newstr)
                            
                        else:
                            newstr = 'Number Error: ' + prog[ptr] + ' is undefined'
                            tokens.append(newstr)
                            
                        listTokens = '\n'.join([str(elem) for elem in tokens])
                        return listTokens    
                        
                        
            state = 'done'
            
                

        if state == 'assign':
            if(ptr < len(prog)):
                if prog[ptr] == '=':
                    st += prog[ptr]
                    state = 'done'
                    ptr += 1
                else:
                    newstr = 'Error: : is undefined'
                    tokens.append(newstr)
                    
                    listTokens = '\n'.join([str(elem) for elem in tokens])
                    return listTokens
                    
            else:
                newstr = 'Error: : is undefined'
                tokens.append(newstr)
                listTokens = '\n'.join([str(elem) for elem in tokens])
                return listTokens
        if state == 'done':
            
                
                state = 'start'
                print(st)
                
                if (isres(st)):
                    print(st)
                    print(tokens)
                    newstr = 'reseved: '+st
                    tokens.append(newstr)
                    
                elif(st.isdigit()):
                    print(st)
                    print(tokens)
                    newstr = 'number: '+st
                    tokens.append(newstr)
                    
                elif(st == ':='):
                    print(st)
                    print(tokens)
                    newstr = 'assign: '+st
                    tokens.append(newstr)
                    
                elif(issym(st)):
                    print(st)
                    print(tokens)
                    newstr = 'symbol: '+st
                    tokens.append(newstr)
                    
                elif(st.isalpha()):
                    print(st)
                    print(tokens)
                    newstr = 'identifier: '+st
                    tokens.append(newstr)
                    
                
    print(tokens)
    listTokens = '\n'.join([str(elem) for elem in tokens])
    return listTokens
   
