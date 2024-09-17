
def inverter_string(texto):
    string_invertida = ""
    for i in range(len(texto) - 1, -1, -1):
        string_invertida += texto[i]
    return string_invertida

texto_exemplo = "Teste do teste"
print(inverter_string(texto_exemplo))
