# LockPass - Gerenciador de Senhas

## Descrição
LockPass é uma aplicação desktop para gerenciamento de senhas desenvolvida em Python com interface gráfica Flet. A aplicação permite armazenar, visualizar, buscar e excluir credenciais de aplicativos/sites de forma segura e organizada.

## Funcionalidades
- Armazenamento Seguro: Salve credenciais de aplicativos, sites e serviços
- **Interface Intuitiva**: Design moderno com tema escuro
- **Busca em Tempo Real**: Encontre rapidamente suas credenciais
- **Exclusão Simples**: Remova entradas com um clique
- **Navegação por Rotas**: Interface fluida entre telas principais e de adição
- **Visualização Tabular**: Dados organizados em tabela com cores alternadas

## Estrutura do projeto
```text
projeto/
├── main.py          # Aplicação principal Flet
├── database.py      # Módulo de banco de dados
└── database.db      # Banco de dados SQLite (gerado automaticamente)
```

## Tecnologias Utilizadas
- Python 3
- Flet - Framework para interface gráfica
- SQLite - Banco de dados local
- SQLite3 - Driver para operações de banco de dados

## Instalação das Dependências
```bash
pip install flet
```

## Como Executar
```bash
python main.py
```

## Uso da Aplicação
### Tela Principal
- **Buscar:** Digite no campo de busca para filtrar credenciais
- **Visualizar:** Veja todas as credenciais salvas em formato de tabela
- **Excluir:** Clique no ícone de lixeira para remover uma entrada
- **Adicionar:** Clique no ícone "+" para ir para a tela de adição

### Tela de Adição
- **Aplicativo/Site:** Nome do serviço (ex: Instagram, Gmail)
- **Usuário/Email:** Credencial de acesso
- **Senha:** Senha do serviço (campo com opção de mostrar/ocultar)
- **Salvar:** Clique para armazenar as informações

## Suporte
Para issues e contribuições, verifique o código fonte e adapte conforme necessário para seu ambiente específico.
