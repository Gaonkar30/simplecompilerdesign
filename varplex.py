import ply.lex as lex
# Define the tokens
tokens = (
    'VARIABLE',
    'ASSIGN',
    'SEMICOLON',
    'NUMBER'
)

# Define regular expressions for tokens
t_VARIABLE = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_ASSIGN = r'='
t_SEMICOLON = r';'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t
# Define an error handling rule
def t_error(t):
    print(f"Illegal character: ")
    t.lexer.skip(1)

def p_error(p):
    print(f"Syntax error in input")

lexer = lex.lex()
data = "x = 42;"
lexer.input(data)
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)