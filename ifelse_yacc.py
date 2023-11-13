import ply.yacc as yacc
from ifelse_lex import tokens



=
def p_statement(p):
    """
    statement : if_statement
              | if_else_statement
              | empty
    """

def p_if_statement(p):
    """
    if_statement : IF LPAREN expression RPAREN COLON expression LPAREN expression RPAREN
    """
    

def p_if_else_statement(p):
    """
    if_else_statement : IF LPAREN expression RPAREN COLON expression LPAREN expression RPAREN ELSE COLON expression LPAREN expression RPAREN
    """

def p_expression(p):
    """
    expression : IDENTIFIER
                 | NUMBER
    """
   

def p_empty(p):
    """
    empty :
    """
    pass

# Error handling
def p_error(p):
    print(f"Syntax error at '{p.value}'")

# Build the parser
parser = yacc.yacc()




while True:
    try:
        s = input('Enter if else statement: ") > ')
    except EOFError:
        break

    if not s:
        continue

    result = parser.parse(s)
    print(result)
