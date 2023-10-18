from Lexer import Lexer


data = '''
lcerrada@automatismoslau.cl
_id = 5
_Nombre = "texto"
3 + 4 * 10
  + -20 *2
'''

analisSemantico = Lexer()
analisSemantico.leerCodigo(data)
while True:
    tok = analisSemantico.obteneToken()
    if not tok:
        break      
    print(tok)
    

