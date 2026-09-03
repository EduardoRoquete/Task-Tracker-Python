import json
from pathlib import Path

from src.task_tracker.modelos.tarefa import Tarefa


class TarefaRepositorio:

    def __init__(self, caminho_arquivo: str):
        raiz_src = Path(__file__).resolve().parent.parent
        self._caminho_arquivo = raiz_src / caminho_arquivo

    def _garantir_arquivo(self):
        #garantindo a criação do arquivo em src\task_tracker\"caminho_arquivo"
        if not self._caminho_arquivo.exists():
            self._caminho_arquivo.parent.mkdir(parents=True, exist_ok=True)
            self._caminho_arquivo.write_text("[]", encoding="utf-8")

    def carregar_tarefas(self):
        self._garantir_arquivo()

        try:
            with open(self._caminho_arquivo, "r", encoding="utf-8") as arquivo:
                if arquivo.read().strip() == "":
                    return []

                arquivo.seek(0)
                dados_tarefas = json.load(arquivo)

                return [
                    Tarefa.de_dicionario(dado)
                    for dado in dados_tarefas
                ]
        except (json.JSONDecodeError, OSError, KeyError, ValueError) as erro:
                raise ValueError(f"Não foi possível carregar as tarefas: arquivo de dados corrompido ou incompatíveis ({erro}).")

    def salvar_tarefas(self, tarefas: list[Tarefa]):
        self._garantir_arquivo()

        dados_tarefas = []
        for tarefa in tarefas:
            dados_tarefas.append(tarefa.para_dicionario())

        with open(self._caminho_arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(dados_tarefas, arquivo, ensure_ascii=False, indent=4)


    def gerar_proximo_id(self, tarefas:list[Tarefa]):
        if not tarefas:
            return 1

        maior_id = max(tarefa.id for tarefa in tarefas)

        return maior_id + 1

