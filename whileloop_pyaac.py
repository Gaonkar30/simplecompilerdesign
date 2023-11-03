import ply.yacc as yacc
from whileloop_plex import tokens
# Define the parsing rules
def p_while_loop(p):
    '''
    while_loop : WHILE expression COLON statements
    '''
    p[0] = f"While loop: while {p[2]}: {p[4]}"

def p_expression(p):
    '''
    expression : NUMBER
    '''
    p[0] = p[1]

def p_statements(p):
    '''
    statements : statement
              | statements statement
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1] + p[2]

def p_statement(p):
    '''
    statement : IDENTIFIER
              | NUMBER
    '''
    p[0] = str(p[1])

def p_error(p):
    print(f"Syntax error in input: {p.value}")

parser = yacc.yacc()

while True:
    try:
        s = input('while x < 10: print(x)')
    except EOFError:
        break

    if not s:
        continue
    result = parser.parse(s)
    print(result)
