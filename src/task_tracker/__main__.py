from interface.menu_terminal import MenuTerminal
from modelos.status_tarefa import StatusTarefa
from modelos.tarefa import Tarefa

from repositorio.tarefa_repositorio import TarefaRepositorio
from servico.tarefa_servico import TarefaServico


def main():

    repositorio = TarefaRepositorio("dados/tarefas.json")

    servico = TarefaServico(repositorio)

    menu = MenuTerminal(servico)
    menu.iniciar()


if __name__ == "__main__":
    main()