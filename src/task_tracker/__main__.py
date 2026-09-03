from src.task_tracker.modelos.status_tarefa import StatusTarefa
from src.task_tracker.modelos.tarefa import Tarefa
from rich import inspect

from src.task_tracker.repositorio.tarefa_repositorio import TarefaRepositorio


def main():
    tr = TarefaRepositorio("dados/tarefas.json")

    tr.carregar_tarefas_do_json()


if __name__ == "__main__":
    main()