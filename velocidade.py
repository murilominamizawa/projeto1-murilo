'''1-quais são os dados de entrada necessários? 
velocidade inicial, normal, final
2-o que devo fazer com estes dados? 
calcular se a velocidade é maior/menor que 80km/h
3-quais são as restrições deste problema? 
a velocidade deve ser um número positivo
4-qual é o resultado esperado? 
mensagem indicando se a velocidade está dentro do limite ou se houve excesso de velocidade

5-qual é sequência de passos a serem feitas para chegar ao resultado esperado?
- Ler a velocidade do usuário
- Verificar se a velocidade é um número positivo
- Comparar a velocidade com 80km/h
- Exibir a mensagem correspondente
se é menor ou igual a 80km/h ou se houve excesso de velocidade muito alto ou leve'''
km = 80
print("================verificador de velocidade================")
velo = float(input("digite a velocidade do seu veiculo em km/h: "))
if velo <= 80:
    print("velocidade dentro do limite permitido, dirija com segurança!")
elif velo > 80 and velo <= 90:
    print("excesso de velocidade leve, recebera uma multa leve!")
else:
    print("excesso de velocidade muito alto, recebera uma multa alta se fudeu!")
