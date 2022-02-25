""" Exercício 1.2 """

# Quantos segundos há em 42 minutos e 42 segundos?
s = 60
m = 42
t = (m * s) + m
print('Em 42 minutos e 42 segundos, existem {} segundos.' .format(t))

# Quantas milhas há em 10 quilômetros? Dica: uma milha equivale a 1,61 quilômetro.
mi = 1.61
km = 10
mt = mi * km
print('Em 10 quilômetros existem {:.2f} milhas.'.format(mt))

# Se você correr 10 quilômetros em 42 minutos e 42 segundos, qual é o seu passo médio
# (tempo por milha em minutos e segundos)? Qual é a sua velocidade média em milhas por hora?
s = 42
m = 42
st = (m * 60) + s
h = st / 3600
vm = mt / h
print('A velocidade média é de {:.2f} milhas/h.'.format(vm))
