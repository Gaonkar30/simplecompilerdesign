import ply.lex as lex
# Define the tokens
tokens = (
    'FOR',
    'IDENTIFIER',
    'IN',
    'RANGE',
    'COLON',
    'NUMBER',
'LPAREN', 'RPAREN',
)

# Define regular expressions for tokens
t_FOR = r'for'
t_IN = r'in'
t_RANGE = r'range'
t_COLON = r':'
t_LPAREN = r'\('
t_RPAREN = r'\)'

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

# Define rules for handling whitespace and comments
t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Define an error handling rule
def t_error(t):
    print(f"Illegal character: {t.value[0]}")
    t.lexer.skip(1)
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

lexer = lex.lex()

# Test the lexer with input data
data = "for i in range(10): print(i)"
lexer.input(data)
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)