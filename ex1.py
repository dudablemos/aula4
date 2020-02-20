
import datetime as dt

def vida(hoje,nasc):
    dias_vida= hoje - nasc
    return dias_vida


dia_nasc = int(input('dia nascimento: '))
mes_nasc = int(input('mes nascimento: '))
ano_nasc = int(input('ano nascimento: '))

hoje = dt.date.today()
nasc = dt.date(year = ano_nasc, month = mes_nasc, day=dia_nasc)

dias = vida(hoje,nasc)
print(dias)