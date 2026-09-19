import json
import os

# Arquivo onde os dados serão salvos para não perder nada ao fechar
ARQUIVO_ESTOQUE = 'estoque_ana_estela.json'

def carregar_estoque():
    """Carrega os dados do arquivo JSON, se existir."""
    if os.path.exists(ARQUIVO_ESTOQUE):
        with open(ARQUIVO_ESTOQUE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def salvar_estoque(estoque):
    """Salva os dados no arquivo JSON."""
    with open(ARQUIVO_ESTOQUE, 'w', encoding='utf-8') as f:
        json.dump(estoque, f, indent=4, ensure_ascii=False)

def adicionar_produto(estoque):
    print("\n--- Adicionar Novo Produto ---")
    nome = input("Nome do produto: ").strip().title()
    
    try:
        quantidade = int(input("Quantidade inicial: "))
        preco = float(input("Preço unitário (ex: 15.50): ").replace(',', '.'))
        
        if nome in estoque:
            estoque[nome]['quantidade'] += quantidade
            estoque[nome]['preco'] = preco # Atualiza o preço
            print(f"\n✅ Produto '{nome}' atualizado com sucesso!")
        else:
            estoque[nome] = {'quantidade': quantidade, 'preco': preco}
            print(f"\n✅ Produto '{nome}' cadastrado com sucesso!")
            
        salvar_estoque(estoque)
    except ValueError:
        print("\n❌ Erro: Digite apenas números para quantidade e preço.")

def visualizar_estoque(estoque):
    print("\n--- Estoque Atual ---")
    if not estoque:
        print("O estoque está vazio.")
        return

    print(f"{'Produto':<20} | {'Qtd':<5} | {'Preço (R$)'}")
    print("-" * 45)
    for nome, dados in estoque.items():
        print(f"{nome:<20} | {dados['quantidade']:<5} | R$ {dados['preco']:.2f}")
    print("-" * 45)

def registrar_venda(estoque):
    print("\n--- Registrar Venda ---")
    nome = input("Nome do produto vendido: ").strip().title()
    
    if nome not in estoque:
        print(f"\n❌ Produto '{nome}' não encontrado no estoque.")
        return
        
    try:
        qtd_vendida = int(input("Quantidade vendida: "))
        
        if qtd_vendida > estoque[nome]['quantidade']:
            print(f"\n❌ Estoque insuficiente! Você só tem {estoque[nome]['quantidade']} unidades.")
        else:
            estoque[nome]['quantidade'] -= qtd_vendida
            total_venda = qtd_vendida * estoque[nome]['preco']
            print(f"\n✅ Venda registrada! Total: R$ {total_venda:.2f}")
            
            # Remove o produto se zerar o estoque (opcional, mas mantém limpo)
            # if estoque[nome]['quantidade'] == 0:
            #     del estoque[nome]
                
            salvar_estoque(estoque)
    except ValueError:
        print("\n❌ Erro: Digite apenas números para a quantidade.")

def menu():
    estoque = carregar_estoque()
    
    while True:
        print("\n" + "="*30)
        print("📦 SISTEMA DE ESTOQUE - ANA ESTELA")
        print("="*30)
        print("1. Adicionar/Atualizar Produto")
        print("2. Visualizar Estoque")
        print("3. Registrar Venda (Baixa no estoque)")
        print("4. Sair")
        
        opcao = input("\nEscolha uma opção (1-4): ")
        
        if opcao == '1':
            adicionar_produto(estoque)
        elif opcao == '2':
            visualizar_estoque(estoque)
        elif opcao == '3':
            registrar_venda(estoque)
        elif opcao == '4':
            print("\nSaindo do sistema... Até logo!")
            break
        else:
            print("\n❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()