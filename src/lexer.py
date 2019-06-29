import ply.lex as lex

# Lista de tokens
tokens = (
    'LBRACKET',
    'RBRACKET',
    'ARRAY',
    'STRING'
)

# Expresiones regulares para tokens simples
t_LBRACKET = r'\{'
t_RBRACKET = r'\}'
t_ARRAY = r'\[\]'
t_STRING = r'[a-z]+'

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Caracteres ignorados (spaces and tabs)
t_ignore  = ' \t'

# Error handling de caracteres invalidos
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
