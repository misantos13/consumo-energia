# Programa de Cálculo de Consumo de Energia
# Autor: Camila Ferreira Santos

# Entrada
aparelho = input("Digite o nome do aparelho para o Cálculo: ")
potencia = float(input("Digite a potência em watts (W) do aparelho: "))
usoMedioHoras = float(input("Digite o tempo médio de uso em horas: "))

# Condições
if potencia <= 0 or usoMedioHoras <= 0:
    print("\nO valor informado não poder ser igual ou menor que zero.")
    
elif usoMedioHoras > 24:
    print("\nA quantidade de horas por dia não pode ser maior que 24.")

else:

    # Cálculo
    consumoMensal = (potencia * usoMedioHoras * 30) /1000
    custoMedioMensal = consumoMensal * 0.93

    # Apresentação dos resultados
    print("\n---")
    print(f"\nAparelho informado: {aparelho}")
    print(f"\nConsumo estimado: {consumoMensal:.2f} kWh por mês")
    print(f"\nCusto médio: R$ {custoMedioMensal:.2f} por mês")