import ply.lex as lex

class Lexer():
    def __init__(self):
        tokens = [
           'CORREO',
           'VARIABLE',
           'NUMERO',
           'CADENACARACTER',
           'SUMA',
           'RESTA',
           'MULTIPLICACION',
           'DIVISION',
           'APARENTESIS',
           'CPARENTESIS',
           'INCREMENTO',
           'ASIGNACION',
           'MAYORQUE',
           'MENORQUE'
        ]
        reserved = {
           'if' : 'IF',
           'then' : 'THEN',
           'else' : 'ELSE',
           'while' : 'WHILE',
        }
        tokens = tokens  + list(reserved.values())
        
        t_SUMA    = r'\+'
        t_RESTA   = r'-'
        t_MULTIPLICACION   = r'\*'
        t_DIVISION  = r'/'
        t_APARENTESIS  = r'\('
        t_CPARENTESIS  = r'\)'
        t_ASIGNACION = r'='
        t_MAYORQUE = r'>'
        t_MENORQUE = r'<'
        
        def t_CORREO(t):
            r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}'
            return t
        
        def t_CADENACARACTER(t):
            r'".*"'
            return t
        
        def t_VARIABLE(t):
            r'_[a-zA-Z0-9]+'
            return t
        
        def t_NUMERO(t):
            r'\d+'
            t.value = int(t.value)
            return t
        
        def t_nuevaLinea(t):
            r'\n+'
            t.lexer.lineno += len(t.value)        
        
        t_ignore  = ' \t'        
        
        def t_error(t):
            print("Illegal character '%s'" % t.value[0])
            t.lexer.skip(1)       
        
        self.lexer = lex.lex()
        

    def leerCodigo(self,data):
        self.lexer.input(data)
        
    
    def obteneToken(self):
        return self.lexer.token()
        

