import ply.yacc as yacc
from varplex import tokens

# Define the parsing rules
def p_statement(p):
    '''
    statement : VARIABLE ASSIGN expression SEMICOLON
    '''
    p[0] = f"Variable declaration: {p[1]} = {p[3]}"

def p_expression(p):
    '''
    expression : VARIABLE
               | NUMBER
    '''
    p[0] = p[1]

def p_error(p):
    print(f"Syntax error in input:")

parser = yacc.yacc()

while True:
    try:
        s = input('calc > ')
    except EOFError:
        break

    if not s:
        continue
    result = parser.parse(s)
    print(result)
