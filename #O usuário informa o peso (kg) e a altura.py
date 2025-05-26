#O usuário informa o peso (kg) e a altura (m).
#O programa calcula o IMC:
#IMC = peso / (altura ** 2)
#O IMC é exibido junto com uma mensagem personalizada:
#IMC ≥ 30.0 → Cuidado com a Saúde
#IMC < 30.0 → Tudo ok

nome = input("digite o nome do pacientema :")
peso = float(input("Informe o peso em kg: "))
altura = float(input("Informe a altura em metros: "))

imc = peso / (altura * 2)
imc, porcentagem = (peso, altura, )

#< 18.5	Abaixo do peso
#18.5 – 24.9	Peso normal
#25.0 – 29.9	Sobrepeso
#30.0 – 34.9	Obesidade Grau I
#35.0 – 39.9	Obesidade Grau II
#≥ 40.0	Obesidade Grau III (mórbida)

if peso < 18.5:
    classificacao = "Abaixo do peso "
elif 18.5 <= peso < 24.9:
    classificacao = "Peso normal"
elif 25.0 <= peso < 29.9:
    classificacao = "Sobre peso 😳"
elif 30.0 <= peso < 34.9:
    classificacao = "Obesidade Grau I 🤦‍♂️🚫"
elif 35.0 <= peso < 39.0:
    classificacao = "Obesidade Grau II 🫥"
elif peso >= 40.0:
    classificacao = "Obesidade Grau III (mórbida)😔"

else:
    classificacao = "⚰️"
print("---------------------")

print(f"Agente {nome}, sua classificação é: {classificacao} (altura: {altura})")
print(f"O seu IMC é: {imc:}")

print("---------------------")
