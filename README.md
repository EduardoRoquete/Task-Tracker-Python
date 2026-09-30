# 📋 Task Tracker Python

> Um gerenciador de tarefas construído do zero em Python com Programação Orientada a Objetos — projeto de estudo baseado no desafio [Task Tracker](https://roadmap.sh/projects/task-tracker) do roadmap.sh, evoluído em versões incrementais.

![Python](https://img.shields.io/badge/Python-3.12.6-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Versão](https://img.shields.io/badge/Versão-v1.0.0-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

**Navegação:** [Sobre](#-sobre-o-projeto) · [Funcionalidades](#-funcionalidades-principais) · [Tecnologias](#️-tecnologias-utilizadas) · [Metodologia](#-metodologia-de-desenvolvimento) · [Versões](#️-versões) · [Melhorias Futuras](#-melhorias-futuras) · [v1.0.0](#-v100--gerenciador-de-tarefas-no-terminal-poo--json) · [Autor](#-Autor)

---

## 🧠 Sobre o Projeto

O **Task Tracker Python** é um gerenciador de tarefas para criar, listar, atualizar e excluir tarefas, com os dados persistidos localmente.

Diferente da proposta original do roadmap.sh — que usa argumentos posicionais de linha de comando (`task-cli add "..."`) — a versão atual foi construída para funcionar através de um **menu interativo**, onde o usuário navega e insere os dados diretamente pelo `input()` do terminal, tornando a experiência mais acessível e amigável.

O projeto nasceu como exercício prático de **Orientação a Objetos**, com foco em arquitetura de software limpa, separação de responsabilidades entre camadas e boas práticas de desenvolvimento — do planejamento à implementação. A partir daí, evolui em **passos pequenos e contínuos**: cada versão adiciona uma nova capacidade (API, banco de dados) sem descartar o que já foi construído, e o histórico de versões abaixo registra essa evolução.

---

## ✨ Funcionalidades Principais

> Estado atual do projeto (**v1.0.0**). Esta lista cresce a cada nova versão.

- ✅ Criar novas tarefas, com ID único gerado automaticamente pelo sistema
- ✅ Listar todas as tarefas ou filtrar por status (`A FAZER`, `EM ANDAMENTO`, `CONCLUIDA`)
- ✅ Atualizar a descrição de uma tarefa existente
- ✅ Atualizar o status de uma tarefa
- ✅ Excluir uma tarefa (com confirmação antes da exclusão)
- ✅ Persistência automática dos dados em arquivo JSON
- ✅ Tratamento de erros de entrada, sem quebrar a aplicação

---

## 🛠️ Tecnologias Utilizadas

> Stack do estado atual (**v1.0.0**). O detalhamento de cada versão está na [seção da própria versão](#-v100--gerenciador-de-tarefas-no-terminal-poo--json).

- **Python 3.12.6**
- Somente biblioteca padrão do Python — nenhuma dependência externa é necessária para executar a v1.0.0
- **Git e GitHub** para versionamento
- **Notion** para o planejamento das sprints

---

## 📌 Metodologia de Desenvolvimento

O projeto é planejado e construído com uma abordagem inspirada em **Scrum**: cada versão é dividida em sprints incrementais, com tarefas e critérios de aceitação definidos antes da implementação.

| Versão | Sprint | Entrega |
|---|---|---|
| **v1.0.0** | Sprint 1 | Modelagem do domínio (`Tarefa`, `StatusTarefa`) e camada de persistência (`TarefaRepositorio`) |
| **v1.0.0** | Sprint 2 | Implementação das regras de negócio (`TarefaServico`) |
| **v1.0.0** | Sprint 3 | Interface interativa de terminal (`MenuTerminal`) e tratamento de erros |

O planejamento detalhado de cada sprint, com as tasks e critérios de aceitação, está disponível no board do Notion:

🔗 **Notion:** <https://app.notion.com/p/76e18612db3848cbb3b2bc130807c95a?v=5876eaeb0a264336b255c9332c986686&source=copy_link>

---

## 🏷️ Versões

| Versão | Nome | Status | O que entrega |
|---|---|---|---|
| **v1.0.0** | [Gerenciador de Tarefas no Terminal (POO + JSON)](#-v100--gerenciador-de-tarefas-no-terminal-poo--json) | ✅ Lançada | Aplicação completa de terminal com menu interativo, arquitetura em camadas e persistência em arquivo JSON. |
| **v2.0.0** | API REST com FastAPI | 🚧 Em planejamento | Expõe as mesmas regras de negócio por uma API HTTP, mantendo a versão de terminal funcionando. |

---

## 🧩 Melhorias Futuras

- [ ] API REST com FastAPI (v2.0.0)
- [ ] Testes automatizados (unitários e de integração)
- [ ] Persistência em banco de dados relacional

---

---

# 📦 v1.0.0 — Gerenciador de Tarefas no Terminal (POO + JSON)

> Primeira versão do projeto: uma aplicação de terminal completa, com menu interativo, arquitetura em camadas e dados salvos em JSON.

## 🎯 O que foi entregue

Ao iniciar, o programa exibe um menu principal com as ações abaixo. Em todos os submenus, digitar `0` cancela a operação e volta ao menu principal.

| Opção | Ação | Comportamento |
|---|---|---|
| **1** | Criar tarefa | Pede a descrição, gera o ID automaticamente, define o status inicial como `A FAZER` e registra as datas de criação e de atualização. |
| **2** | Listar tarefas | Lista todas ou filtra por status (`A FAZER`, `EM ANDAMENTO`, `CONCLUIDA`). |
| **3** | Atualizar descrição | Mostra as tarefas, pede o ID, valida se ele existe, recebe a nova descrição e atualiza a data de atualização. |
| **4** | Atualizar status | Mostra as tarefas, pede o ID e oferece os três status disponíveis para escolha. |
| **5** | Excluir tarefa | Pede o ID e uma confirmação (`S`/`N`) antes de remover definitivamente; depois exibe a lista atualizada. |
| **0** | Sair | Encerra o programa. |

**Regras de negócio implementadas:**

- O ID é gerado pelo sistema: o usuário nunca o digita ao criar uma tarefa.
- A descrição é obrigatória. Descrições vazias (ou só com espaços) são recusadas, e espaços nas pontas são removidos.
- O status pertence a um conjunto fechado: `A FAZER`, `EM ANDAMENTO` ou `CONCLUIDA`.
- Toda alteração de descrição ou de status atualiza a data de atualização; a data de criação nunca muda.
- Entradas inválidas (texto no lugar de número, ID inexistente, opção fora do menu) geram mensagens amigáveis, sem interromper o programa.

## 🏗️ Arquitetura

O projeto segue uma arquitetura em camadas, cada uma com uma responsabilidade única e bem definida:

```
Task-Tracker-Python/
├── src/
│   └── task_tracker/
│       ├── __main__.py                 # Ponto de entrada: monta as camadas e inicia o menu
│       ├── modelos/
│       │   ├── tarefa.py               # Entidade de domínio: Tarefa
│       │   └── status_tarefa.py        # Enum com os status possíveis
│       ├── repositorio/
│       │   └── tarefa_repositorio.py   # Persistência (leitura e escrita em JSON)
│       ├── servico/
│       │   └── tarefa_servico.py       # Regras de negócio e orquestração
│       ├── interface/
│       │   └── menu_terminal.py        # Interação com o usuário via terminal
│       └── dados/
│           └── tarefas.json            # Dados das tarefas (criado automaticamente na 1ª execução)
├── .gitignore
├── requirements.txt
└── README.md
```

**Fluxo de dependência:** `MenuTerminal` → `TarefaServico` → `TarefaRepositorio` → `Tarefa` / `StatusTarefa`. Cada camada só conhece a camada logo abaixo.

**Princípios aplicados:**

- 🔹 **Injeção de dependência** — o ponto de entrada cria o repositório, entrega-o ao serviço e entrega o serviço ao menu; nenhuma camada cria suas próprias dependências.
- 🔹 **Fonte única de verdade** — a entidade `Tarefa` garante a própria integridade (por exemplo, a validação da descrição), sem duplicar regras em outras camadas.
- 🔹 **Separação de camadas** — a interface nunca acessa o arquivo diretamente, e o repositório apenas lê e grava dados.
- 🔹 **Domínio sem entrada e saída** — `Tarefa` não imprime nem lê nada do usuário; toda interação fica em `MenuTerminal`.
- 🔹 **Tratamento de erros consistente** — as exceções sobem de forma controlada até a interface, onde viram mensagens amigáveis. Falhas técnicas de leitura do arquivo são convertidas em erro de negócio com mensagem clara.

## 🧰 Stack de tecnologias da versão

| Tecnologia | Uso |
|---|---|
| **Python 3.12.6** | Linguagem principal |
| `json` | Serialização e leitura dos dados |
| `pathlib` | Manipulação de caminhos de arquivo, independente do sistema operacional |
| `datetime` | Datas de criação e de atualização (formato ISO 8601 no arquivo) |
| `enum` | Conjunto fechado de status da tarefa |
| `os` e `time` | Limpeza de tela e pequenas pausas na interface |

Nenhuma dependência externa é necessária.

## 🧠 Fundamentos e skills abordados

| Fundamento / Skill | Onde aparece no projeto |
|---|---|
| **Classes e objetos** | `Tarefa`, `TarefaRepositorio`, `TarefaServico`, `MenuTerminal` |
| **Encapsulamento** | Atributos privados em `Tarefa` com acesso por `property` e validação no `setter` |
| **Enumerações** | `StatusTarefa` |
| **Métodos de fábrica (`classmethod`)** | Reconstrução de uma `Tarefa` a partir dos dados do arquivo |
| **Serialização e desserialização** | Conversão entre objeto `Tarefa` e dicionário/JSON |
| **Arquitetura em camadas** | Separação em modelos, repositório, serviço e interface |
| **Padrão Repository** | `TarefaRepositorio` isola o acesso ao arquivo |
| **Camada de serviço** | `TarefaServico` concentra a orquestração das regras de negócio |
| **Injeção de dependência** | Montagem das camadas em `__main__.py` |
| **Tratamento de exceções** | Captura granular na interface e exceção unificada na persistência |
| **Anotações de tipo (type hints)** | Assinaturas de métodos ao longo do código |
| **Manipulação de arquivos** | Leitura e escrita com codificação UTF-8 e criação automática do arquivo |
| **Modelagem de dados** | Estrutura da tarefa e formato do JSON |
| **Git, GitHub e Scrum** | Versionamento, sprints e critérios de aceitação planejados no Notion |

## ▶️ Como executar sem erros

**Pré-requisitos:** Python 3.12 ou superior e Git. Nenhuma biblioteca precisa ser instalada.

```bash
# 1. Clone o repositório
git clone https://github.com/EduardoRoquete/Task-Tracker-Python.git

# 2. Acesse a pasta do projeto
cd Task-Tracker-Python

# 3. (Recomendado) Se o repositório já tiver versões mais novas, volte para esta versão
git checkout v1.0.0

# 4. (Opcional) Crie e ative um ambiente virtual
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

# 5. Execute a partir da RAIZ do projeto, apontando para a pasta do pacote
python src/task_tracker
```

> 💡 No Linux e no Mac, use `python3` no lugar de `python` caso o primeiro comando não seja encontrado. No Windows, `py` também funciona.

> ⚠️ **Atenção:** nesta versão, execute exatamente `python src/task_tracker`. O comando `python -m task_tracker` **não funciona** na v1.0.0, porque os módulos são importados a partir da pasta do pacote (a transformação em pacote instalável está nas [melhorias futuras](#-melhorias-futuras)).

**Problemas comuns**

| Sintoma | Causa provável | Solução |
|---|---|---|
| `ModuleNotFoundError: No module named 'interface'` | O programa foi iniciado com `python -m task_tracker` ou de outro jeito | Na raiz do projeto, execute `python src/task_tracker` |
| `python` não é reconhecido | Python não está no PATH, ou o comando tem outro nome | Use `python3` (Linux/Mac) ou `py` (Windows), ou reinstale marcando "Add Python to PATH" |
| Caracteres estranhos ao limpar a tela | O programa está rodando em um console de IDE que não interpreta comandos de terminal | Execute em um terminal de verdade (Prompt de Comando, PowerShell, Terminal do Linux/Mac ou terminal integrado do editor) |
| Mensagem de arquivo de dados corrompido | O `tarefas.json` foi editado manualmente ou ficou incompleto | Corrija o arquivo ou apague-o; ele é recriado vazio na próxima execução |

**Onde ficam os dados:** em `src/task_tracker/dados/tarefas.json`, criado automaticamente na primeira execução. Apagar esse arquivo reinicia o sistema sem nenhuma tarefa.

## 🚧 Limitações conhecidas (base para as próximas versões)

- **Uso por uma pessoa por vez:** não há controle de acesso simultâneo ao arquivo JSON.
- **IDs podem ser reaproveitados:** o novo ID é o maior ID existente somado a 1; se a tarefa de maior ID for excluída, seu número pode ser usado por uma tarefa nova.
- **Sem testes automatizados:** a validação foi feita manualmente ao final de cada sprint.
- **Execução por pasta:** o projeto ainda não é um pacote instalável.

---

## 👤 Autor

**Eduardo Aguiar Roquete**

- 💼 LinkedIn: <https://www.linkedin.com/in/eduardo-aguiar-roquete/>
- 🐙 GitHub: [@EduardoRoquete](https://github.com/EduardoRoquete)

---

<p align="center">Desenvolvido com 🐍 como projeto de estudo de Orientação a Objetos em Python</p>