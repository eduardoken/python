from math import radians, sin, cos, tan
an = float(input('Digite o valor do angulo: '))
seno = sin(radians(an))
cosseno = cos(radians(an))
tangente = tan(radians(an))
print(' O ângulo de {} tem o Seno de {:.2f}, o Cosseno de {:.2f} e a Tangente de {:.2f}'.format(an, seno, cosseno, tangente))