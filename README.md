# Sistema de Inventário Doméstico

Aplicação de desktop desenvolvida em Python para gerenciar um inventário de itens domésticos. Permite cadastrar, visualizar, atualizar e deletar itens, além de associar uma imagem a cada um.

 
*(Substitua o link acima por um screenshot real da sua aplicação)*

---

## ✨ Funcionalidades

- **Adicionar Itens:** Cadastro de novos itens com informações detalhadas como nome, local, descrição, marca/modelo, data e valor da compra, e número de série.
- **Anexar Imagem:** Possibilidade de carregar e associar uma imagem a cada item do inventário.
- **Visualização em Tabela:** Todos os itens são exibidos em uma tabela clara e organizada com barras de rolagem.
- **Atualizar Itens:** Selecione um item na tabela para carregar seus dados nos campos de formulário e realizar atualizações.
- **Deletar Itens:** Remoção de itens do inventário.
- **Visualização de Imagem:** Exibe a imagem do item selecionado na tabela.
- **Dashboard Simples:** Mostra o valor total e a quantidade de itens cadastrados em tempo real.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Tkinter:** Para a construção da interface gráfica (GUI).
- **Pillow (PIL Fork):** Para manipulação e exibição de imagens.
- **Tkcalendar:** Para o widget de seleção de data.
- **SQLite3:** Para o armazenamento de dados em um banco de dados local.

---

## 🚀 Como Executar o Projeto

Siga os passos abaixo para rodar a aplicação em sua máquina local.

### Pré-requisitos

- [Python 3.8+](https://www.python.org/downloads/) instalado.
- `pip` (gerenciador de pacotes do Python).

### Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/sistema_cadastro_python.git
   cd sistema_cadastro_python
   ```

2. **Crie e ative um ambiente virtual (recomendado):**
   ```bash
   python -m venv venv
   # No Windows:
   .\venv\Scripts\activate
   # No macOS/Linux:
   source venv/bin/activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install Pillow tkcalendar
   ```

4. **Crie o banco de dados:**
   Se o arquivo `dados.db` não existir, execute o script para criá-lo.
   ```bash
   python criarbd.py
   ```

5. **Inicie a aplicação:**
   ```bash
   python main.py
   ```

---

## 📂 Estrutura do Projeto

```
sistema_cadastro_python/
├── assets/
│   └── img/            # Ícones e imagens da UI
├── criarbd.py          # Script para criação inicial do banco de dados
├── main.py             # Arquivo principal da aplicação (GUI e lógica)
├── view.py             # Módulo de acesso ao banco de dados (CRUD)
└── README.md           # Este arquivo
```
