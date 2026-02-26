import json
from funcionarios import Funcionarios 

def salvar_dados(lista, arquivo="empresa.json"):
    # convertemos todos os objetos para dict usando a função to_dict da class funcionarios
    dados_dict = [funcionario.to_dict() for funcionario in lista]
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados_dict, f, indent=4, ensure_ascii=False)
    print(f"\ndados salvos com sucesso em {arquivo}!")

lista_funcionarios = []

while True:
    print("\n" + "="*30)
    print("SISTEMA DE CADASTRO")
    print("="*30)
    try:
      nome = input("nome: ")
      setor = input("setor: ")
      cargo = input("cargo: ")
        
      # erro de tipo costuma acontecer aqui ou no setter
      salario_input = input("salario : ")
      salario = float(salario_input) # se vier letra, o ValueError pula direto pro except

      novo = Funcionarios(nome, setor, cargo, salario)

      lista_funcionarios.append(novo)
      print("\nfuncionario adicionado a lista")

    except ValueError as e:
        # aqui pegamos erros de conversão (letras no float/int) 
        # e erros dos seus Setters (salário negativo, bônus > 100, etc)
        print(f"\nERRO DE INPUT: {e}")
        print("insira valores validos.")
        continue # reinicia o loop para tentar novamente

    except Exception as e:
        # para qualquer outro erro inesperado
        print(f"\nocorreu um erro inesperado: {e}")
        continue

    sair = input("\ndeseja cadastrar outro? (s/n): ").lower()
    if sair == 'n':
        break

# no final do loop, salvamos tudo
if lista_funcionarios:
    salvar_dados(lista_funcionarios)
else:
    print("\nnenhum dado foi cadastrado para salvar.")
