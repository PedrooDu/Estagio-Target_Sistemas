import json

def calcular_faturamento(faturamento):

    faturamento_com_faturamento = [dia['valor'] for dia in faturamento if dia['valor'] > 0]

    menor_faturamento = min(faturamento_com_faturamento)
    maior_faturamento = max(faturamento_com_faturamento)
    media_faturamento = sum(faturamento_com_faturamento) / len(faturamento_com_faturamento)
    dias_acima_da_media = len([dia for dia in faturamento_com_faturamento if dia > media_faturamento])

    return menor_faturamento, maior_faturamento, dias_acima_da_media

with open('Target_Sistemas/src/faturamento.json', 'r') as file:
    dados_faturamento = json.load(file)

menor_faturamento, maior_faturamento, dias_acima_da_media = calcular_faturamento(dados_faturamento)

print(f"Menor valor de faturamento: {menor_faturamento}")
print(f"Maior valor de faturamento: {maior_faturamento}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")
