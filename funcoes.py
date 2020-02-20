'''
def retornar_nome(nome, sobrenome):
    resultado = 'seu nome é ' +nome+' '+sobrenome
    return resultado

nome_input = input('digite seu nome:')
sobrenome_input=input('digite sobrenome')

meu_nome = retornar_nome(sobrenome= sobrenome_input, nome=nome_input)
print(meu_nome)
'''

def somar (a,b):
    resultado = a + b
    if resultado <=40:
        return(print("ops só retorno maiores que 40"))
    else:
        return resultado

a_input = int(input('digite o primeiro numero: '))
b_input = int(input('digite o segundo numero: '))
soma = somar(a_input,b_input)
print(soma)
