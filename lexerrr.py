import ply.lex as lex
listaInicial = [] 
listaJunto = []
with open ('pruebas.txt', 'r') as archivo:
    lineas = archivo.readlines()
    for linea in lineas:
        linea = linea.strip()
        if linea:
            print(linea)
            listaInicial.append(linea)
#print("\n")
#print(listaInicial)

for cadaLinea in listaInicial:
    textoPegado = cadaLinea.replace(" ", "")
    listaJunto.append(textoPegado)
#print("\n")
#print(listaJunto)

tokens = ["nombre", "move", "skip", "turn", "face", "put",
           "pick", "move_dir", "run_dirs", "move_face", "null", "conditional",
           "loop", "repeat", "defun", "fun_call", "left_parenth", "right_parenth", "variable", "number", "if", "defvar", "cardinal", "direction", "comma", "i_objects"]


def t_defvar(t):
    r'defvar'
    return t

def t_run_dirs(t):
    r'run-dirs'
    return t

def t_move_dir(t):
    r'move-dir'
    return t

def t_move(t):
    r'move'
    return t

def t_skip(t):
    r'skip'
    return t

def t_null(t):
    r'null'
    return t

def t_turn(t):
    r'turn'
    return t

def t_face(t):
    r'face'
    return t

def t_put(t):
    r'put'
    return t

def t_pick(t):
    r'pick'
    return t

def t_move_face(t):
    r'move-face'
    return t

def t_if(t):
    r'if'
    return t

def t_loop(t):
    r'loop'
    return t

def t_repeat(t):
    r'repeat'
    return t

def t_defun(t):
    r'defun'
    return t

def t_left_parenth(t):
    r'\('
    return t

def t_right_parenth(t):
    r'\)'
    return t

def t_number(t):
    r'\d+'
    return t

def t_conditional(t):
    r'facing\?|blocked\?|can-put\?|can-move\?|isZero\?|not'
    return t

def t_cardinal(t):
    r':north|:west|:south|:east'
    return t
    
def t_direction(t):
    r':left|:right|:around'
    return t

def t_comma(t):
    r','
    return t

def t_i_objects(t):
    r':chips|:balloons'
    return t

def t_nombre(t):
    r'[a-zA-Z_][a-zA-z0-9_]*'
    return t

def t_error(t):
    print("Carácter ilegal: '%s'" % t.value[0])
    t.lexer.skip(1)

t_ignore = ' \t'

lexer = lex.lex()
data = "(defun goend() (if (not (blocked?)) ((pick :balloons 5) (goend))(null)))"
lexer.input(data)
lista_tokens=[]
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)
    lista_tokens.append(tok)

def parser_defvar():
    #contador=0
    i=0
    if lista_tokens[i].type=="left_parenth":
        #contador+=1
        i+=1
        if lista_tokens[i].type=="nombre":
            i+=1
            if lista_tokens[i].type=="number":
                i+=1
                if lista_tokens[i].type=="right_parenth":
                    return True
            else:
                return False
        else: 
            return False
                
    else: 
        return False
parser_defvar()
def parser_name():
    i=0
    if lista_tokens[i].type=="left_parenth":
        i+=1
        if lista_tokens[i].type=="=":
            i+=1
            if lista_tokens[i].type=="number":
                i+=1
                if lista_tokens[i].type=="right_parenth":
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
print(parser_defvar())
def parser_move():
    i=0
    if lista_tokens[i].type=="left_parenth":
        i+=1
        if lista_tokens[i].type=="move":
            i+=1
            if lista_tokens[i].type=="number":
                i+=1
                if lista_tokens[i].type=="right_parenth":
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

def parser_face():
    i=0
    if lista_tokens[i].type=="left_parenth":
        i+=1
        if lista_tokens[i].type=="face":
            i+=1
            if lista_tokens[i].type=="direction":
                i+=1
                if lista_tokens[i].type=="right_parenth":
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
def skipN():
    i = 0
    if lista_tokens [i].type == "left_parenth":
        i+=1
        if lista_tokens [i].type == "skip":
            i+=1
            if lista_tokens[i].type == "number":
                i+=1
                if lista_tokens [i].type == "right_parenth":
                    return True
                else:
                    return False
            else: 
                return False
        else:
            return False
    else:
        return False
def turnD():
    i=0
    if lista_tokens [i].type == "left_parenth":
        i+=1
        if lista_tokens[i].type == "turn":
            i+=1
            if lista_tokens [i].type == "direction":
                i+=1
                if lista_tokens [i].type == "right_parenth":
                    return True
                else:
                    return False
            else:
                return False
            
        else:
            return False
    else:
        return False

def parser_move_face():
    i=0
    if lista_tokens[i].type=="left_parenth":
        i+=1
        if lista_tokens[i].type=="move_face":
            i+=1
            if lista_tokens[i].type=="direction":
                i+=1
                if lista_tokens[i].type=="right_parenth":
                    return True
                    
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
def putXn():
    i=0
    if lista_tokens [i].type == "left_parenth":
        i+=1
        if lista_tokens [i].type == "put":
            i+=1
            if lista_tokens [i].type == "i_objects":
                i+=1
                if lista_tokens[i].type == "number":
                    i+=1
                    if lista_tokens [i].type == "right_parenth":
                        return True
                    else:
                        return False
                else: return False
            else: 
                return False
        else: 
            return False
    else: return False
def pickXn():
    i=0
    if lista_tokens [i].type == "left_parenth":
        i+=1
        if lista_tokens [i].type == "pick":
            i+=1
            if lista_tokens [i].type == "i_objects":
                i+=1
                if lista_tokens[i].type == "number":
                    i+=1
                    if lista_tokens [i].type == "right_parenth":
                        return True
                    else:
                        return False
                else: return False
            else: 
                return False
        else: 
            return False
    else: return False
def moveDirND():
    i=0
    if lista_tokens [i].type == "left_parenth":
        i+=1
        if lista_tokens [i].type == "move_dir":
            i+=1
            if lista_tokens [i].type == "number":
                i+=1
                if lista_tokens[i].type == "direction":
                    i+=1
                    if lista_tokens [i].type == "right_parenth":
                        return True
                    else:
                        return False
                else: return False
            else: 
                return False
        else: 
            return False
    else: return False
def runDirsDS():
    i=0
    if lista_tokens [i].type == "left_parenth":
        i+=1
        if lista_tokens [i].type == "run_dirs":
            i+=1
            if lista_tokens [i].type == "right_parenth":
                
                return False
            else: return False
        else: 
            return False
    else: 
        return False

def null():
    i=0
    if lista_tokens [i].type == "left_parenth":
        i+=1
        if lista_tokens [i].type == "null":
            i+=1
            if lista_tokens [i].type == "right_parenth":
                return True
            else:
                return False
        else: return False
    else: 
        return False

def parser_conditionals():
    i=0
    if lista_tokens [i].type == "left_parenth":
        i+=1
        if lista_tokens [i].type == "if":
            i+=1
            if lista_tokens [i].type == "conditional":
                i+=1
            else:
                return False
        else:
            return False
    else:
        return False
