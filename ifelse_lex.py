import ply.lex as lex

# List of token names
tokens = (
    'IF',
    'ELSE',
    'IDENTIFIER',
'LPAREN', 'RPAREN',
    'COLON',
    'NUMBER',
)

# Regular expressions for simple tokens


t_COLON = r':'
t_LPAREN = r'\('
t_RPAREN = r'\)'
def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t
# Regular expression for identifiers (variable names)
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    reserved_words = {'if', 'else'}
    if t.value not in reserved_words:
        t.type = 'IDENTIFIER'
    return t

# Define a rule to track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t
# Ignore whitespace and tabs
t_ignore = ' \t'

# Error handling
def t_error(t):

    t.lexer.skip(1)

lexer = lex.lex()
# Build the lexer
data = """if x:
    y = 5
else:
    y = 10"""
lexer.input(data)
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)