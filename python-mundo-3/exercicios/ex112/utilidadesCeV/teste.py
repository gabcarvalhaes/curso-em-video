import moeda #Ou from moeda import metade, dobro, aumentar
from dado import leiadinheiro

p = leiadinheiro('Digite o preço: R$')
moeda.resumo(p, 20, 12)