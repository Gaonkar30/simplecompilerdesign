import ply.yacc as yacc
from func_decllex import tokens

def p_function_declaration(p):
    '''
    function_declaration : FUNCTION IDENTIFIER LPAREN parameters RPAREN COLON statements
    '''
    p[0] = f"Function: {p[1]}({p[4]}): {p[7]}"

def p_parameters(p):
    '''
    parameters : IDENTIFIER
               | parameters COMMA IDENTIFIER
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1] + ', ' + p[3]

def p_statements(p):
    '''
    statements : statement
              | statements statement
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1] + '\n' + p[2]

def p_statement(p):
    '''
    statement : IDENTIFIER
    '''
    p[0] = p[1]


parser = yacc.yacc()

while True:
    try:
        s = input('Enter a function > ')
    except EOFError:
        break

    if not s:
        continue

    result = parser.parse(s)
    print(result)