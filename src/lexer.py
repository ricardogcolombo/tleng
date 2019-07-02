import ply.lex as lex

# Palabras reservadas
reserved = {
    'type' : 'TYPE',
    'struct' : 'STRUCT',
    'string' : 'STRING',
    'float64' : 'FLOAT64',
    'bool' : 'BOOL',
    'int' : 'INT'
}

# Lista de tokens
tokens = [
    'LBRACKET',
    'RBRACKET',
    'ARRAY',
    'WORD'
] + list(reserved.values())

# Expresiones regulares para tokens simples
t_LBRACKET = r'\{'
t_RBRACKET = r'\}'
t_ARRAY = r'\[\]'

def t_WORD(t):
    r'[a-zA-Z0-9]+'
    if t.value in reserved.keys():
        t.type = reserved[t.value]
    return t

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
