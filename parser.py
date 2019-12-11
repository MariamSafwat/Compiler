import sys

def if_stmt(token,i):
    
    i += 1
    exp(token,i)
    if(token[i][0] == 'THEN'):
        i += 1
        stmt_seq(token,i)
    else:
        print('7aseb error')
        sys.exit()

    if(token[i][0] == 'ELSE'):
        i += 1
        stmt_seq(token,i)
    if(token[i][0] == 'END'):
        i += 1
    else:
        print('7aseb error')
        sys.exit()
    stmt_seq(token,i)
    
    
            

def repeat_stmt(token,i):
    i += 1
    stmt_seq(token,i)
    if(token[i][0] == 'UNTIL'):
        exp(token,i)
    else:
        print('7aseb error')
        sys.exit()
    


def assign_stmt(token,i):
    i += 1
    if(token[i][0] == ':='):
        i += 1
        exp(token,i)
    else:
        print('7aseb error')
        sys.exit()
    

def read_stmt(token,i):
    print('wsl l read_stmt')
    i += 1
    if(i> len(token)):
        print('7aseb error len')
        sys.exit
    
    if(token[i][1] == 'IDENTIFIER'):
        print(token[i][0])
        i += 1
    else:
        print('7aseb error')
        sys.exit()
    


def write_stmt(token,i):
    i += 1
    exp(token,i)


def exp(token,i):
    simple_exp(token,i)
    while comparison_op(token[i][0]):
        simple_exp(token,i)


def comparison_op(token,i):
    if token == '<' or token == '>' or token == '=':
        #TODO create node fel tree 
        print(token,i)
        i += 1
        return True
    else:
        print('7aseb error')
        return False
        sys.exit()

def simple_exp(token,i):
    term(token,i)
    while addop(token[i][0]):
        term(token,i)



def term(token,i):
    factor(token,i)
    while mulop(token[i][0]):
        factor(token,i)
    

def addop(token,i):
    if token == '+' or token == '-':
        #TODO create node fel tree 
        print(token)
        i += 1
        return True
    else:
        print('7aseb error')
        return False
        sys.exit()


def mulop(token,i):
    if token == '*' or token == '/' :
        #TODO create node fel tree 
        print(token)
        i += 1
        return True
    else:
        print('7aseb error')
        return False
        sys.exit()

def factor(token,i):
    #factor -> (exp) | number | identifier
    if token[i][0] == '(':
        i += 1
        exp(token,i)
        i += 1
        if token[i][0] == ')':
            i += 1
        else:
            print('7aseb error')
            sys.exit()
    elif token[i][1] == 'NUMBER' or token[i][1] == 'INDENTIFIER':
        #TODO create node fel tree 
        print(token[i][0])
        i += 1
    else:
        print('7aseb error')
        sys.exit()
        


def stmt_seq(token,i):
    print(token)
    stmt(token,i)
    while(1):
        if(token[i][1]=='SEMICOLON'):
            #TODO create node fel tree 
            print(token)
            i += 1
            stmt(token,i)
        else:
            print('7aseb error de')
            sys.exit()  
        
        

def stmt(token,i) :
    print(token)
    print(i)
    if(token[i][1] == 'IF'):
        if_stmt(token)
    elif(token[i][1] == 'REPEAT'):
        repeat_stmt(token)
    elif (token[i][1] == 'IDENTIFIER'):
        assign_stmt(token)
    elif(token[i][1]=='READ'):
        print('read wslt')
        read_stmt(token,i)
    elif(token[i][1]=='WRITE'):
        write_stmt(token)
    else :
        print('7aseb error')
        sys.exit()

def parser(token):
    print(token)
    for i in range(len(token)):
        stmt_seq(token,i)

tokens = input("Enter list")
lo = []

token_li = tokens.split(";")#TODO lma n-create el gui nbadlha b eno y-replace \n b ; b3d kda y-split
for k in range(len(token_li)):
    token_list = token_li[k].split(",")
    lo.append(token_list)



print(lo)
parser(lo)
