import ply.yacc as yacc
from for_loopplex import tokens
def p_for_loop(p):
    '''
    for_loop : FOR IDENTIFIER IN RANGE LPAREN expression RPAREN COLON statements
    '''
    p[0] = f"For loop: for {p[2]} in range({p[6]}): {p[8]}"

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
        s = input('for i in range(200): print(i)')
    except EOFError:
        break

    if not s:
        continue
    result = parser.parse(s)
    print(result)
