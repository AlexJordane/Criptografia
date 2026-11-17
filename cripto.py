import string

def inverso_multiplicativo(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def codificar(mensagem: str, a: int, b: int) -> str:
    if inverso_multiplicativo(a, 26) is None:
        raise ValueError(f"O valor de 'a' ({a}) não tem inverso multiplicativo módulo 26. Escolha outro valor primo de 26.")
    alfabeto = string.ascii_uppercase
    mensagem_codificada = ""
    
    for char in mensagem.upper():
        if char in alfabeto:
            indice_original = alfabeto.index(char)
            indice_codificado = (a * indice_original + b) % 26
            mensagem_codificada += alfabeto[indice_codificado]
        else:
            mensagem_codificada += char
            
    return mensagem_codificada

def decodificar(mensagem: str, a: int, b: int) -> str:
    a_inv = inverso_multiplicativo(a, 26)
    if a_inv is None:
        raise ValueError(f"O valor de 'a' ({a}) não tem inverso multiplicativo módulo 26. Escolha outro valor primo de 26.")
    
    alfabeto = string.ascii_uppercase
    mensagem_decodificada = ""
    
    for char in mensagem.upper():
        if char in alfabeto:
            indice_codificado = alfabeto.index(char)
            indice_decodificado = (a_inv * (indice_codificado - b)) % 26
            mensagem_decodificada += alfabeto[indice_decodificado]
        else:
            mensagem_decodificada += char
            
    return mensagem_decodificada

print("Bem-vindo ao codificador e decodificador de mensagens!")
print("Escolha uma opção:")
print("1. Codificar uma mensagem")
print("2. Decodificar uma mensagem")
opcao = input("Digite 1 ou 2: ")
if opcao == "1":
    mensagem = input("Digite a mensagem a ser codificada: ")
    a = int(input("Digite o valor de 'a' (deve ser primo em relação a 26): "))
    b = int(input("Digite o valor de 'b': "))
    try:
        mensagem_codificada = codificar(mensagem, a, b)
        print(f"Mensagem codificada: {mensagem_codificada}")
    except ValueError as e:
        print(e)
elif opcao == "2":
    mensagem = input("Digite a mensagem a ser decodificada: ")
    a = int(input("Digite o valor de 'a' (deve ser primo em relação a 26): "))
    b = int(input("Digite o valor de 'b': "))
    try:
        mensagem_decodificada = decodificar(mensagem, a, b)
        print(f"Mensagem decodificada: {mensagem_decodificada}")
    except ValueError as e:
        print(e)