
import sys
import networkx as nx
import matplotlib.pyplot as plt
import random
def hierarchy_pos(G, root=None, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5):

    if not nx.is_tree(G):
        raise TypeError('cannot use hierarchy_pos on a graph that is not a tree')

    if root is None:
        if isinstance(G, nx.DiGraph):
            root = next(iter(nx.topological_sort(G)))  #allows back compatibility with nx version 1.11
        else:
            root = random.choice(list(G.nodes))

    def _hierarchy_pos(G, root, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5, pos = None, parent = None):
        
        if pos is None:
            pos = {root:(xcenter,vert_loc)}
        else:
            pos[root] = (xcenter, vert_loc)
        children = list(G.neighbors(root))
        if not isinstance(G, nx.DiGraph) and parent is not None:
            children.remove(parent)  
        if len(children)!=0:
            dx = width/len(children) 
            nextx = xcenter - width/2 - dx/2
            for child in children:
                nextx += dx
                pos = _hierarchy_pos(G,child, width = dx, vert_gap = vert_gap, 
                                    vert_loc = vert_loc-vert_gap, xcenter=nextx,
                                    pos=pos, parent = root)
        return pos


    return _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)
index = 0
G = nx.Graph()
output=[]
G1 = nx.Graph()
def drawing (output):
    for k in range(len(output)):
        if(output[k][1]=='READ'):
            G1.add_edges_from([(output[k][0],output[k+1][0])])
            pos = hierarchy_pos(G1,output[0][0])    
            nx.draw(G1, pos=pos, with_labels=True)
            plt.draw()
            plt.show()
def if_stmt(token,i):
    
    i += 1
    if(i>=len(token)):
             print('7aseb error len: el prog 5ls')
             parser(token,i)
    i = exp(token,i)
    
    if(token[i][1] == 'THEN'):
        output.append(['then',token[i][1]])
        G.add_node('then')
        i += 1
        if(i>=len(token)):
             print('7aseb error len: el prog 5ls')
             parser(token,i)
             
        i = stmt_seq(token,i)
    else:
        print('7aseb error')
        sys.exit()

    if(token[i][1] == 'ELSE'):
        output.append(['else',token[i][1]])
        G.add_node('else')
        i += 1
        if(i>=len(token)):
             print('7aseb error len: el prog 5ls')
             parser(token,i)
             
        i = stmt_seq(token,i)
    if(token[i][1] == 'END'):
        G.add_node('end')
        output.append(['end',token[i][1]])
        i += 1
        if(i>=len(token)):
             print('7aseb error len: el prog 5ls')
             parser(token,i)
    else:
        print('7aseb error')
        sys.exit()
    i = stmt_seq(token,i)
    return i
    
    
            

def repeat_stmt(token,i):
    i += 1
    if(i>=len(token)):
             print('7aseb error len: el prog 5ls')
             parser(token,i)
             
    i = stmt_seq(token,i)
    if(token[i][1] == 'UNTIL'):
        G.add_node(['until',token[i][1]])
        output.append('until')
        i = exp(token,i)
    else:
        print('7aseb error')
        sys.exit()
    return i
    


def assign_stmt(token,i):
    print('assign_stmt')
    i += 1
    print('i=',i)
    if(i>=len(token)):
             print('7aseb error len: el prog 5ls')
             parser(token,i)
             
    if(token[i][0] == ':='):
        
        node = str('assign ('+ token[i-1][0] + ')')
        G.add_node(node)
        output.append([node,'ASSIGN'])
        
        i += 1
        if(i>=len(token)):
             print('7aseb error len: el prog 5ls')
             parser(token,i)
             
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
             parser(token,i)
    
    if(token[i][1] == 'IDENTIFIER'):
        
        node = str('read ('+ token[i][0] + ')')
        G.add_node(node)
        output.append([node,'READ'])
        
        print(token[i][0])
        i += 1
        if(i>=len(token)):
             print('7aseb error len: el prog 5ls')
             parser(token,i)
        print('fe id i:',i)
    else:
        print('7aseb error')
        sys.exit()
        
    return i
    


def write_stmt(token,i):
    
    G.add_node('write')
    output.append(['write','WRITE'])
    i += 1
    if(i>=len(token)):
        print('7aseb error len: el prog 5ls')
        parser(token,i)
         
    i = exp(token,i)
    return i

def exp(token,i):
    i = simple_exp(token,i)
    flag,i = comparison_op(token,i)
    while flag:
        print('d5l comp',i)
        i = simple_exp(token,i)
        flag,i = comparison_op(token,i)
    return i

def comparison_op(token,i):
    if token[i][1] == 'LESSTHAN' or token[i][0] == '>' or token[i][0] == '=':
        #TODO create node fel tree
        node = str('op ('+ token[i][0] + ')')
        G.add_node(node)
        output.append([node,'OP'])
        
        print(token,i)
        i += 1
        if(i>=len(token)):
             print('7aseb error len: el prog 5ls')
             parser(token,i)
        return True,i
    else:
        print('7aseb error')
        return False,i
        #sys.exit()

def simple_exp(token,i):
    i = term(token,i)
    while addop(token,i):
        i = term(token,i)
    return i


def term(token,i):
    i = factor(token,i)
    while mulop(token,i):
        i = factor(token,i)
    return i

def addop(token,i):
    if token[i][0] == '+' or token[i][0] == '-':
        #TODO create node fel tree
        node = str('op ('+ token[i][0] + ')')
        G.add_node(node)
        output.append([node,'OP'])
        print(token)
        i += 1
        if(i>=len(token)):
             print('7aseb error len: el prog 5ls')
             parser(token,i)
        return True
    else:
        print('7aseb error')
        return False
        sys.exit()
    return i


def mulop(token,i):
    if token[i][0] == '*' or token[i][0] == '/' :
        #TODO create node fel tree
        node = str('op ('+ token[i][0] + ')')
        G.add_node(node)
        output.append([node,'OP'])
        print(token)
        i += 1
        if(i>=len(token)):
             print('7aseb error len: el prog 5ls')
             parser(token,i)
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
             parser(token,i)
             
        i = exp(token,i)
        i += 1
        if(i>=len(token)):
             print('7aseb error len: el prog 5ls')
             parser(token,i)
             
        if token[i][0] == ')':
            i += 1
            if(i>=len(token)):
             print('7aseb error len: el prog 5ls')
             parser(token,i)
             
        else:
            print('7aseb error')
            sys.exit()
            
    elif token[i][1] == 'NUMBER' or token[i][1] == 'IDENTIFIER':
        print('fh')
        #TODO create node fel tree
        if(token[i][1] == 'NUMBER'):
            node = str('const ('+ token[i][0] + ')')
            output.append([node,'CONST'])
        elif(token[i][1] == 'IDENTIFIER'):
            node = str('id ('+ token[i][0] + ')')
            output.append([node,'ID'])
        
        G.add_node(node)
        
        print(token[i][0])
        i += 1
        if(i>=len(token)):
             print('7aseb error len: el prog 5ls')
             parser(token,i)
    else:
        print('7aseb error')
        sys.exit()
    return i
        


def stmt_seq(token,i):
    print('stmt_seq')
    
    i = stmt(token,i)
    print('i=',i)
    print('hna')
    while(token[i][1]=='SEMICOLON'):
        i += 1
        if(i>=len(token)):
                print('7aseb error len: el prog 5ls')
                parser(token,i)
        i = stmt(token,i)

        
    '''
    while(1):
        print('fe while i:',i)
        print('hna brdo')
        if(token[i][1]=='SEMICOLON'):
            #TODO create node fel tree 
            print(token)
            i += 1
            if(i>=len(token)):
                print('7aseb error len: el prog 5ls')
                parser(token,i)
                     
            i = stmt(token,i)
        else:
            print('msh semicolon')
            sys.exit()
    '''
    return i
        
        

def stmt(token,i) :
    print('stmt')
    print('i=',i)
    if(token[i][1] == 'IF'):
        print('d5l if')
        G.add_node('if')
        output.append(['if','IF'])
        i = if_stmt(token,i)
        if(i>=len(token)):
            print('7aseb error len: el prog 5ls HNAA')
            parser(token,i)
        
    elif(token[i][1] == 'REPEAT'):
        G.add_node('repeat')
        output.append(['repeat',token[i][1]])
        i = repeat_stmt(token,i)
        if(i>=len(token)):
            print('7aseb error len: el prog 5ls HNAA')
            parser(token,i)
        
    elif (token[i][1] == 'IDENTIFIER'):
        i = assign_stmt(token,i)
        if(i>=len(token)):
            print('7aseb error len: el prog 5ls HNAA')
            parser(token,i)
        
    elif(token[i][1]=='READ'):
        print('read wslt')
        i = read_stmt(token,i)
        if(i>=len(token)):
            print('7aseb error len: el prog 5ls HNAA')
            parser(token,i)
            
        
    elif(token[i][1]=='WRITE'):
        i = write_stmt(token,i)
        if(i>=len(token)):
            print('7aseb error len: el prog 5ls HNAA')
            parser(token,i)
        
    else :
        print('7aseb error')
        sys.exit()
    return i 

def parser(token,m):
    print(token)
    if(m>=len(token)):
        drawing(output)
        ##return
        ##nx.draw(G, with_labels=True)
        ##plt.draw()
        ##plt.show()
        sys.exit()
    else:
        while(m<len(token)):
            print('hiii ',m)
            m = stmt_seq(token,m)

tokens = input("Enter list")
lo = []

token_li = tokens.split("$")#TODO lma n-create el gui nbadlha b eno y-replace \n b ; b3d kda y-split
for k in range(len(token_li)):
    token_list = token_li[k].split(",")
    token_list = [x.strip(' ') for x in token_list]
    lo.append(token_list)



print(lo)
parser(lo,0)

nx.draw(G, with_labels=True)
plt.draw()
plt.show()


