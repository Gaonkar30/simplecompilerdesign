import ply.lex as lex
tokens = (
    'WHILE',
    'IDENTIFIER',
    'COLON',
'NUMBER',
'LPAREN', 'RPAREN',
)

t_LPAREN = r'\('
t_RPAREN = r'\)'

t_COLON = r':'

def t_WHILE(t):
    r'while'
    return t
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_IDENTIFIER(t):
    r'(?!while\b)[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):

    t.lexer.skip(1)

lexer = lex.lex()

# Test the lexer with input data
data = "while x < 10: print(x)"
lexer.input(data)
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)