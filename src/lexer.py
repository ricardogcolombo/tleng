import ply.lex as lex

# Lista de tokens
tokens = (
    'STRING',
    'INT',
    'FLOAT64',
    'BOOL',
    'LBRACKET',
    'RBRACKET',
    'ARRAY',
    'TYPE',
    'STRUCT',
    'ATT_TYPE_NAME'
)

# Expresiones regulares para tokens simples
t_STRING = r'string'
t_INT = r'int'
t_FLOAT64 = r'float64'
t_BOOL = r'bool'
t_LBRACKET = r'\{'
t_RBRACKET = r'\}'
t_ARRAY = r'\[\]'
t_TYPE = r'type'
t_STRUCT = r'struct'
t_ATT_TYPE_NAME = r'(?!string|int|float64|bool|type|struct)[a-z]+'

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
