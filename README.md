# gestao-estoque-comercio-local
Sistema em Python para gestão de estoque voltado a microempreendedores do bairro Jardim Ana Estela, Carapicuíba

# 📦 Sistema de Gestão de Estoque - Jardim Ana Estela

Um sistema digital simples, acessível e executado via terminal, desenvolvido em Python para auxiliar microempreendedores locais do bairro Jardim Ana Estela (Carapicuíba – SP) na organização e controle eficiente de seus estoques.

O projeto tem como foco principal promover a inclusão digital e a sustentabilidade financeira para pequenos lojistas, oferecendo uma interface amigável e à prova de falhas para usuários com ou sem familiaridade com ferramentas tecnológicas.

## ✨ Funcionalidades

- **Cadastro de Produtos:** Adição rápida de novos itens informando quantidade inicial e preço.
- **Registro de Vendas (Saída):** Baixa automática no inventário, com trava de segurança que impede a venda de uma quantidade maior do que a disponível em estoque.
- **Monitoramento e Alertas:** Painel de visualização com tags visuais (`⚠️ BAIXO ESTOQUE`) para produtos que atingem menos de 5 unidades, facilitando o planejamento de reposição.
- **Persistência de Dados (Anti-falhas):** Salvamento instantâneo e automático das informações em um arquivo local `.json`. Os dados do comerciante permanecem seguros mesmo em caso de quedas de energia ou fechamento acidental do sistema.

## 🚀 Como Executar o Projeto

### Pré-requisitos
Para rodar a aplicação, é necessário ter o [Python](https://www.python.org/downloads/) instalado no seu computador.

### Passo a Passo

1. Faça o clone deste repositório no seu terminal:
   ```bash
   git clone [https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git](https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git)
(Ou simplesmente baixe o arquivo estoque.py e coloque em uma pasta de sua preferência).

Pelo terminal, navegue até a pasta onde o arquivo foi salvo:

Bash
cd caminho/para/a/pasta
Inicie o sistema executando o comando:

Bash
python estoque.py
🛠️ Tecnologias Utilizadas
Python 3: Lógica central e construção dos menus interativos via terminal.

Módulo JSON: Estruturação do banco de dados local para armazenamento das mercadorias.

Módulo OS: Limpeza dinâmica da tela para garantir uma interface de usuário sem distrações.
