import ply.yacc as yacc
from ifelse_lex import tokens



# Start symbol for the grammar
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
    # Implement your handling of if statements here

def p_if_else_statement(p):
    """
    if_else_statement : IF expression COLON statement LPAREN statement RPAREN ELSE COLON statement LPAREN statement RPAREN
    """
    # Implement your handling of if-else statements here

def p_expression(p):
    """
    expression : IDENTIFIER
                 | NUMBER
    """
    # Implement your handling of expressions here

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