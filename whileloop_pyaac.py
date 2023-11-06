import ply.yacc as yacc
from whileloop_plex import tokens  # Make sure you have defined the 'tokens' in the 'whileloop_plex' module

# Define the parsing rules
def p_while_loop(p):
    '''
    while_loop : WHILE expression COLON statements
    '''
    p[0] = f'while {p[2]}:\n{p[4]}'  # Corrected the formatting

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

# Create the parser
parser = yacc.yacc()

while True:
    try:
        s = input('Enter a while loop (e.g., "while x < 10: print(x): ") > ')
    except EOFError:
        break

    if not s:
        continue

    result = parser.parse(s)
    print(result)
