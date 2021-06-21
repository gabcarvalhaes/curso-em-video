# Programa com função voto() que vai receber a data de nascimento de uma pessoa como parâmetro
# Retorna um valor literal indicando se uma pessoa te voto NEGADO, OPCIONAL ou OBRIGATÓRIO
from datetime import datetime


def voto(data_nasc):
    idade = datetime.now().year - data_nasc
    if idade >= 18 and idade < 65:
        return f"Com idade {idade}: VOTO OBRIGATÓRIO!"
    elif idade >= 16 or idade >= 65:
        return f"Com idade {idade}: VOTO OPCIONAL"
    else:
        return f"Com idade {idade}: VOTO NEGADO"


n = int(input('Digite o ano que você nasceu: '))
print(voto(n))

# Na solução do professor Guanabara, ele importou a biblioteca dentro do escopo da função apenas
# Isso economiza memória!!!