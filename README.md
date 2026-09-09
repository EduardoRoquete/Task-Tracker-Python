# 📋 Task Tracker Python

> Um gerenciador de tarefas via terminal, construído do zero em Python com Programação Orientada a Objetos — projeto de estudo baseado no desafio [Task Tracker](https://roadmap.sh/projects/task-tracker) do roadmap.sh, adaptado para uma experiência 100% interativa.

![Python](https://img.shields.io/badge/Python-3.12.6-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

---

## 🧠 Sobre o Projeto

O **Task Tracker Python** é uma aplicação de linha de comando para criar, listar, atualizar e excluir tarefas, com todos os dados persistidos localmente em um arquivo JSON.

Diferente da proposta original do roadmap.sh — que usa argumentos posicionais de linha de comando (`task-cli add "..."`) — esta versão foi construída para funcionar através de um **menu interativo**, onde o usuário navega e insere os dados diretamente pelo `input()` do terminal, tornando a experiência mais acessível e amigável.

O projeto foi desenvolvido como exercício prático de **Orientação a Objetos**, com foco em arquitetura de software limpa, separação de responsabilidades entre camadas e boas práticas de desenvolvimento — do planejamento à implementação.

---

## ✨ Funcionalidades

- ✅ Criar novas tarefas, com ID único gerado automaticamente pelo sistema
- ✅ Listar todas as tarefas ou filtrar por status (`A Fazer`, `Em Andamento`, `Concluída`)
- ✅ Atualizar a descrição de uma tarefa existente
- ✅ Atualizar o status de uma tarefa
- ✅ Excluir uma tarefa (com confirmação antes da exclusão)
- ✅ Persistência automática dos dados em arquivo JSON
- ✅ Tratamento de erros de entrada, sem quebrar a aplicação

---

## 🏗️ Arquitetura

O projeto segue uma arquitetura em camadas, cada uma com uma responsabilidade única e bem definida:

```
task_tracker/
├── main.py                        # Ponto de entrada da aplicação
├── modelos/
│   ├── tarefa.py                  # Entidade de domínio: Tarefa
│   └── status_tarefa.py           # Enum com os status possíveis de uma tarefa
├── repositorio/
│   └── tarefa_repositorio.py      # Persistência dos dados (leitura/escrita em JSON)
├── servico/
│   └── tarefa_servico.py          # Regras de negócio e orquestração
├── interface/
│   └── menu_terminal.py           # Interação com o usuário via terminal
└── dados/
    └── tarefas.json                # Arquivo de dados (gerado em tempo de execução)
```

**Princípios aplicados:**
- 🔹 **Injeção de dependência** — cada camada recebe suas dependências prontas, ao invés de criá-las internamente.
- 🔹 **Fonte única de verdade** — cada regra de validação vive em um único lugar (ex.: a entidade `Tarefa` garante sua própria integridade, sem duplicar validações em outras camadas).
- 🔹 **Separação de camadas** — a interface nunca acessa o arquivo diretamente, e o repositório nunca decide regra de negócio.
- 🔹 **Tratamento de erros consistente** — exceções de negócio sobem de forma controlada até a interface, onde são convertidas em mensagens amigáveis ao usuário.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.12.6**
- Bibliotecas 100% da biblioteca padrão do Python — nenhuma dependência externa foi necessária:
  - `json` — serialização e leitura dos dados
  - `pathlib` — manipulação de caminhos de arquivo
  - `datetime` — controle de datas de criação/atualização
  - `os` — limpeza de tela do terminal

---

## 🚀 Como Executar

```bash
# 1. Clone o repositório
git clone https://github.com/EduardoRoquete/Task-Tracker-Python.git

# 2. Acesse a pasta do projeto
cd Task-Tracker-Python

# 3. Crie um ambiente virtual
python -m venv .venv

# 4. Ative o ambiente virtual
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

# 5. Execute a aplicação
python main.py
```

> 💡 Não há dependências externas a instalar — o projeto roda apenas com a biblioteca padrão do Python (veja `requirements.txt`).

---

## 📌 Metodologia de Desenvolvimento

O projeto foi planejado e construído seguindo uma abordagem inspirada em **Scrum**, dividido em 3 sprints incrementais:

| Sprint | Entrega |
|---|---|
| **Sprint 1** | Modelagem do domínio (`Tarefa`, `StatusTarefa`) e camada de persistência (`TarefaRepositorio`) |
| **Sprint 2** | Implementação das regras de negócio (`TarefaServico`) |
| **Sprint 3** | Interface interativa de terminal (`MenuTerminal`) e tratamento de erros |

O planejamento detalhado de cada sprint, com as tasks e critérios de aceitação, está disponível no board do Notion:

🔗 **Notion:** https://app.notion.com/p/76e18612db3848cbb3b2bc130807c95a?v=5876eaeb0a264336b255c9332c986686&source=copy_link

---

## 🧩 Possíveis Melhorias Futuras

- [ ] Testes automatizados (unitários e de integração)
- [ ] Persistência em banco de dados relacional
- [ ] Exportação de tarefas em outros formatos (CSV, TXT)

---

## 👤 Autor

**Eduardo Aguiar Roquete**

- 💼 LinkedIn: https://www.linkedin.com/in/eduardo-aguiar-roquete/
- 🐙 GitHub: [@EduardoRoquete](https://github.com/EduardoRoquete)


---

<p align="center">Desenvolvido com 🐍 como projeto de estudo de Orientação a Objetos em Python</p>