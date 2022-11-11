"""
LF (Line Feed) (Unix - MAC/Linux) -> \n
CRLF (Carriage Return Line Feed) (Windows) -> \r\n
\r\n -> Caracteres especiais
\r -> Move o cursor para o inicio da linha sem pular a mesma
\n -> Move o cursor para a próxima linha sem mover para o inicio
"""

print(12, 34, 1011, sep="-", end="\r\n")  # (12, 34) -> Argumentos não nomeados
print(12, 34, 1011, sep="-", end="\n##\n")
print(56, 78, sep='-', end='\n')  # sep -> Argumento nomeado
print(9, 10, sep='-', end='\n')
