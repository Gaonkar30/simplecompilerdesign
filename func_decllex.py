import ply.lex as lex

# Define the tokens
tokens = (
    'FUNCTION',
    'IDENTIFIER',
    'LPAREN',
    'RPAREN',
    'COLON',
    'COMMA',
)

# Define regular expressions for tokens
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COLON = r':'
t_COMMA= r','
def t_IDENTIFIER(t):
    r'(?!def\b)[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_FUNCTION(t):
    r'def'
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

lexer = lex.lex()
