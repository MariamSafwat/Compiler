import sys

def if_stmt(token,i):
    
    i += 1
    if(i>=len(token)):
             print('7aseb error len: el prog 5ls')
             sys.exit()
    i = exp(token,i)
    
    if(token[i][0] == 'THEN'):
        
        i += 1
        if(i>=len(token)):
             print('7aseb error len: el prog 5ls')
             sys.exit()
        i = stmt_seq(token,i)
    else:
        print('7aseb error')
        sys.exit()

    if(token[i][0] == 'ELSE'):
        i += 1
        if(i>=len(token)):
             print('7aseb error len: el prog 5ls')
             sys.exit()
        i = stmt_seq(token,i)
    if(token[i][0] == 'END'):
        i += 1
        if(i>=len(token)):
             print('7aseb error len: el prog 5ls')
             sys.exit()
    else:
        print('7aseb error')
        sys.exit()
    i = stmt_seq(token,i)
    return i
    
    
            

def repeat_stmt(token,i):
    i += 1
    if(i>=len(token)):
             print('7aseb error len: el prog 5ls')
             sys.exit()
    i = stmt_seq(token,i)
    if(token[i][0] == 'UNTIL'):
        i = exp(token,i)
    else:
        print('7aseb error')
        sys.exit()
    return i
    


def assign_stmt(token,i):
    i += 1
    if(i>=len(token)):
             print('7aseb error len: el prog 5ls')
             sys.exit()
    if(token[i][0] == ':='):
        i += 1
        if(i>=len(token)):
             print('7aseb error len: el prog 5ls')
             sys.exit()
        i = exp(token,i)
    else:
        print('7aseb error')
        sys.exit()
    return i
    

def read_stmt(token,i):
    print('wsl l read_stmt')
    i += 1
    if(i>=len(token)):
             print('7aseb error len: el prog 5ls')
             sys.exit()
    
    if(token[i][1] == 'IDENTIFIER'):
        print(token[i][0])
        i += 1
        if(i>=len(token)):
             print('7aseb error len: el prog 5ls')
             sys.exit()
        print('fe id i:',i)
    else:
        print('7aseb error')
        sys.exit()
        
    return i
    


def write_stmt(token,i):
    i += 1
    if(i>=len(token)):
             print('7aseb error len: el prog 5ls')
             sys.exit()
    i = exp(token,i)
    return i

def exp(token,i):
    i = simple_exp(token,i)
    while comparison_op(token[i][0]):
        i = simple_exp(token,i)
    return i

def comparison_op(token,i):
    if token == '<' or token == '>' or token == '=':
        #TODO create node fel tree 
        print(token,i)
        i += 1
        if(i>=len(token)):
             print('7aseb error len: el prog 5ls')
             sys.exit()
        return True
    else:
        print('7aseb error')
        return False
        sys.exit()

def simple_exp(token,i):
    i = term(token,i)
    while addop(token[i][0]):
        i = term(token,i)
    return i


def term(token,i):
    i = factor(token,i)
    while mulop(token[i][0]):
        i = factor(token,i)
    return i

def addop(token,i):
    if token == '+' or token == '-':
        #TODO create node fel tree 
        print(token)
        i += 1
        if(i>=len(token)):
             print('7aseb error len: el prog 5ls')
             sys.exit()
        return True
    else:
        print('7aseb error')
        return False
        sys.exit()
    return i


def mulop(token,i):
    if token == '*' or token == '/' :
        #TODO create node fel tree 
        print(token)
        i += 1
        if(i>=len(token)):
             print('7aseb error len: el prog 5ls')
             sys.exit()
        return True
    else:
        print('7aseb error')
        return False
        sys.exit()

def factor(token,i):
    #factor -> (exp) | number | identifier
    if token[i][0] == '(':
        i += 1
        if(i>=len(token)):
             print('7aseb error len: el prog 5ls')
             sys.exit()
             
        i = exp(token,i)
        i += 1
        if(i>=len(token)):
             print('7aseb error len: el prog 5ls')
             sys.exit()
             
        if token[i][0] == ')':
            i += 1
            if(i>=len(token)):
             print('7aseb error len: el prog 5ls')
             sys.exit()
             
        else:
            print('7aseb error')
            sys.exit()
    elif token[i][1] == 'NUMBER' or token[i][1] == 'INDENTIFIER':
        #TODO create node fel tree 
        print(token[i][0])
        i += 1
        if(i>=len(token)):
             print('7aseb error len: el prog 5ls')
             sys.exit()
    else:
        print('7aseb error')
        sys.exit()
    return i
        


def stmt_seq(token,i):
    print(token)
    
    i = stmt(token,i)
    print(i)
    while(1):
        print('fe while i:',i)           
        if(token[i][1]=='SEMICOLON'):
            #TODO create node fel tree 
            print(token)
            i += 1
            if(i>=len(token)):
                
                print('7aseb error len: el prog 5ls')
                sys.exit()
                     
            i = stmt(token,i)
        else:
            print('7aseb error de')
            sys.exit()
    return i
        
        

def stmt(token,i) :
    print(token)
    print(i)
    if(token[i][1] == 'IF'):
        i = if_stmt(token)
    elif(token[i][1] == 'REPEAT'):
        i = repeat_stmt(token)
    elif (token[i][1] == 'IDENTIFIER'):
        i = assign_stmt(token)
    elif(token[i][1]=='READ'):
        print('read wslt')
        i = read_stmt(token,i)
    elif(token[i][1]=='WRITE'):
        i = write_stmt(token)
    else :
        print('7aseb error')
        sys.exit()
    return i 

def parser(token):
    print(token)
    m=0
    while(m<len(token)):
        m = stmt_seq(token,m)

tokens = input("Enter list")
lo = []

token_li = tokens.split(";")#TODO lma n-create el gui nbadlha b eno y-replace \n b ; b3d kda y-split
for k in range(len(token_li)):
    token_list = token_li[k].split(",")
    lo.append(token_list)



print(lo)
parser(lo)
