def escolha():
    print("Escolha uma opção")
    
    modelo = []
    telas = []
    
    opcao =-1
    
    while opcao != 0:
        opcao = int(input("\n [1] Consulta \n [2] Serviços \n [3] Venda \n [0] Sair \n\n"))
        
        if opcao == 0:
            print("Saindo... ")
            break
            
        if opcao == 1:
            print(""" 
            ========== Escolha uma opção ========== 
            [1] Consultar um modelo 
            [2] Adicionar um modelo 
            [3] Tabela de Preços
            [4] consulta de preços
            """)
            
            modelo_opcao = int(input("Escolha o serviço desejado: ")) 
            
            if modelo_opcao == 1:
                print("Digite o código do aparelho: ")
                codigo = input()  # Captura o código do aparelho
                print("Digite a marca do aparelho")
                print(f"Consultando o modelo com código {codigo}...")
                print(f" Esse aparelho e o {nome}")
                
            elif modelo_opcao == 2:                                                                     
                modelo = []  # Lista para armazenar os modelos
                print("Digite o código do aparelho: ")
                codigo = input().strip()  # Captura o código do novo modelo
                print("Digite o modelo do aparelho" )
                nome = input().strip()
                modelo.append(codigo)  # Adiciona o código à lista
                modelo.append(nome)
                print(f"{nome} adicionado com sucesso!")
                
            if modelo_opcao == 3:
                telas = []
                print("Digite o código do aparelho: ")
                codigo = input().strip()
                print("Digite o valor do serviço")
                valor = input().strip()
                telas. append(valor)
                print("valor salvo com sucesso")
                
            elif modelo_opcao == 4:
                print("Digite o código do aparelho: ")
                codigo = input()  # Captura o código do aparelho
                print(f" Esse aparelho fica {valor}")
                
                #para melhorar o codigo devo implemetar um dicinario

        if opcao == 2:
            print(
                """
                ==========Escolha uma opção==========
                
                [1] Troca de telas
                [2] Troca de baterias
                [3] Troca de conectores de carga
                    
            """   
            )
            
            opcao_servico = int(input("\n [1] Troca de telas \n [2] Troca de baterias \n [3] Troca de conectores de carga \n\n"))
            
            if opcao_servico == 1:
                print("digite o modelo do aparelho")
                           
            elif opcao_servico == 2:  
                print("b")

            if opcao_servico == 3:
                print("c")
            
        if opcao == 3:
            
            opcao_venda = int(input("\n [1] Celulares a venda \n [2] Notebooks a venda \n\n" )) #organizar como imolementar e retirar aparelhos da lista (algo parecido com a operação de saque)
            
            if opcao_venda == 1:
                print("Celulares")
            elif opcao_venda == 2:
                print("Notebooks")
        
escolha()

