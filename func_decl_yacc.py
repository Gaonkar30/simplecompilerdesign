import ply.yacc as yacc
from func_decllex import tokens

def p_program(p):
    '''
    program : function_declaration
           | program function_declaration
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_function_declaration(p):
    '''
    function_declaration : FUNCTION IDENTIFIER LPAREN parameters RPAREN SEMICOLON
    '''
    p[0] = f"Function: {p[2]}({p[4]}) {p[6]}"

def p_parameters(p):
    '''
    parameters : IDENTIFIER
               | parameters COMMA IDENTIFIER
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

parser = yacc.yacc()
while True:
    try:
        s = input('Enter a function > ')
    except EOFError:
        break

    if not s:
        continue

    result = parser.parse(s)
    if isinstance(result, list):
        for declaration in result:
            print(declaration)
    else:
        print(result)