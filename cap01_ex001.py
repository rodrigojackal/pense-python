""" Exercício 1.1 """
# 1) Em uma instrução print, o que acontece se você omitir um dos parênteses ou ambos?
# R: O comando não é executado corretamente gerando erro:
# Missing parentheses in call to 'print'. Did you mean print(...)?
# print 'Hello, World'

# 2) Se estiver tentando imprimir uma string, o que acontece se omitir uma das aspas ou ambas?
# R: Ocorre erro pois o Python não reconhece a intrução
# print(Hello, World) > NameError: name 'Hello' is not defined

# 3) Você pode usar um sinal de menos para fazer um número negativo como -2.
# O que acontece se puser um sinal de mais antes de um número? E se escrever assim: 2++2?
# R: Será feita a soma dos valores.
print(2++2)

# 4) Na notação matemática, zeros à esquerda são aceitáveis, como em 02.
# O que acontece se você tentar usar isso no Python?
# R: SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers.
print(02)

# 5) O que acontece se você tiver dois valores sem nenhum operador entre eles?
# O Python concatena os valores ao invés de utilizar as regras da matemática.
print(22)