import json

def carregar_dados(arquivo):
    try:
        with open('arquivo', 'r') as f:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}

def salvar_dados(arquivo, dados):
    with open(arquivo, 'w') as f:
        json.dump(dados, f, indent=4)

def salvar_estoque(arquivo, estoque):
    try:
        with open('estoque.json', 'r') as arquivo:
            estoque = json.load(arquivo)
    except FileNotFoundError:
        return {}
    
def salvar_servico(servicos):
    try:
        with open('servicos.json', 'r') as arquivo:
            servicos = json.load(arquivo)
    except FileNotFoundError:
        return {}
    
    
def cadastro_aparelho(dicionario):
    marca = input("Digite a marca do aparelho: ")
    codigo =input("Digite a codigo do aparelho: ")
    nome_aparelho = input("Digite o nome do aparelho: ")
    valor_tela = input("Digite o valor da troca de tela ")
    valor_bateria = input("Digite o valor da troca de bateria ")
    valor_conector = input("Digite o valor da troca de conector de carga ")

    dicionario[codigo] = {
                "marca": marca,
                "nome": nome_aparelho,
                "precos": {
                    "troca_tela": valor_tela,
                    "troca_bateria": valor_bateria,
                    "troca_conector": valor_conector
                    }
                }
    
def cadastro_cliente(clientes):
    id_cliente = input("Digite o ID do cliente ")
    nome_cliente = input("Digite o nome do cliente ")
    telefone_cliente = input("Digite o numero do cliente ")
                
    clientes[id_cliente] = {
                "identificacao": id_cliente,
                "nome": nome_cliente,
                "telefone": telefone_cliente,
            }


def cadastrar_estoque(estoque):
    codigo = input("Digite o ID do produto: ")
    nome_produto = input("Digite o nome do produto: ")
    valor = input("Digite o valor do produto: ")
    condicao = input("Digite a condição do produto: ")

    estoque[codigo] = {
        "produto": nome_produto,
        "valor": valor,
        "condicao": condicao
    }
    print("Produto cadastrado com sucesso!")


def consultar_estoque(estoque): #arrumar a função de cadastro de estoque
    id_produto = input("Digite o ID do produto a ser consultado: ")
                   
    if id_produto in estoque:
        produto = estoque[id_produto]  # Corrigido o indentação

        print(f"Produto: {produto['produto']}")
        print(f"Valor: {produto['valor']}")
        print(f"Condição: {produto['condicao']}")
    else:
        print("Produto não encontrado.")  # Mensagem de erro adicionada

    
def cadastro_servico(servicos):
    id_servico = input("Digite o ID do serviço a ser cadastradado: ")
    id_cliente = input("Digite o ID do cliente a ser cadastradado: ")
    modelo_servico = input("Digite a marca do aparelho: ")
    valor_servico = input("Digite o valor do serviço: ")
                
    servicos[id_servico] = {
            "servico": id_servico,
            "id_cliente": id_cliente,
            "modelo servico": modelo_servico,
            "valor servico": valor_servico
        }
                
#adicionar datatime
                
def consultar_clientes(clientes):
    id_cliente= input("Digite o ID do cliente para consulta: ")

    if id_cliente in clientes:
        cliente = clientes[id_cliente]
        print(f"Identificacao: {cliente['identificacao']}")
        print(f"Nome: {cliente['nome']}")
        print(f"Telefone: {cliente['telefone']}")
        
    else:
        
        print("Cliente não encontrado.")

def consultar_modelo(dicionario):
    codigo = input("Digite o código do aparelho para consulta: ")  
                   
    if codigo in dicionario:
        aparelho = dicionario[codigo]
        print(f"Marca: {aparelho['marca']}")
        print(f"Nome: {aparelho['nome']}")
        print("Preços:")
        print(f"  Troca de tela: {aparelho['precos']['troca_tela']}")
        print(f"  Troca de bateria: {aparelho['precos']['troca_bateria']}")
        print(f"  Troca de conector: {aparelho['precos']['troca_conector']}")
    else:
        print("Código não encontrado.")

def consultar_estoque(estoque):
    id_produto = input("Digite o ID do produto a ser consultado: ")
                   
    if id_produto in estoque:
                
        produto = estoque[id_produto]
    
    print(f"Produto: {produto['produto']}")
    print(f"Valor: {produto['valor']}")
    print(f"Condição: {produto['condicao']}")
                                
def consulta_servico(servicos, clientes):
    id_servico = input("Digite o ID do serviço a ser consultado: ")

    if id_servico in servicos:
        servico = servicos[id_servico]
        id_cliente = servico["id_cliente"]  # Acessando corretamente o ID do cliente

        # Exibindo informações do serviço
        print(f"Cliente ID: {id_cliente}")
        print(f"Modelo do aparelho: {servico['modelo servico']}")
        print(f"Valor do serviço: {servico['valor servico']}")

        # Consultando dados do cliente
        if id_cliente in clientes:
            cliente = clientes[id_cliente]
            print(f"Nome do cliente: {cliente['nome']}")
            print(f"Telefone do cliente: {cliente['telefone']}")
        else:
            print("Cliente não encontrado.")
    else:
        print("Serviço não encontrado.")

     
def main():
              
    dicionario = carregar_dados('dados.json')
    clientes = carregar_dados('clientes.json')
    estoque = carregar_dados('estoque.json')
    servicos = carregar_dados('servicos.json')
                   
    while True:
        
        opcao = int(input("\n [1] Cadasto \n [2] Consulta \n [3] Serviços \n [4] Vendas \n [0] Sair \n\n"))
        
        if opcao == 0:
            break
        
        if opcao == 1:
            print("""
                [1] Cadastrar aparelhos
                [2] Cadastar clientes
                [3] Cadastrar Estoque 
                [4] Cadastrar serviços
            """) # arrumar o cadastro de estoque
                 # arrumar a função de salvar os arquivos

            opcao_cadastro = int(input("Escolha uma opção: "))
        
            if opcao_cadastro == 1:
                cadastro_aparelho(dicionario)
                salvar_dados('dados.json', dicionario)  # Salvar após o cadastro
            elif opcao_cadastro == 2:
                cadastro_cliente(clientes)
                salvar_dados('clientes.json', clientes)  # Salvar após o cadastro
            elif opcao_cadastro == 3:
                cadastrar_estoque(estoque)
                salvar_dados('estoque.json', estoque)  # Salvar após o cadastro
            elif opcao_cadastro == 4:
                cadastro_servico(servicos)
                salvar_dados('servicos.json', servicos)  # Salvar após o cadastro
             
        if opcao == 2:     
            print("""
                  [1] Clientes
                  [2] Modelos
                  [3] Estoque
                  """)
            
            opcao_consulta = int(input("Escolha uma opção "))   
            
            if  opcao_consulta == 1:
                consultar_clientes(clientes)
            elif  opcao_consulta == 2:
                consultar_modelo(dicionario)
            elif  opcao_consulta == 3:
                consultar_estoque(estoque)
#adcionar o input de nome do produto  
        if opcao == 3:
            print("""
                [1] Celulares
                [2] Notebooks
                    """)
                
            opcao_consulta = int(input("Escolha uma opção: "))

            if opcao_consulta == 1:
                 consulta_servico(servicos, clientes)
            elif opcao_consulta == 2:
                print(2)

        if opcao == 4:
            
            print("""
                  [1] Celulares
                  [2] Notebooks
                  [3] Peças
                  """)
            
            opcao_vendas = int(input("Escolha uma opção "))
            
            if opcao_vendas == 1:
                print("Celulares")

            elif opcao_vendas == 2:
                print("Notebooks")

            elif opcao_vendas == 3:
                print("Peças")
    
if __name__ == "__main__":
    main()


