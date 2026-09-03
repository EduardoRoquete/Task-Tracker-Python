from src.task_tracker.modelos.status_tarefa import StatusTarefa
from src.task_tracker.modelos.tarefa import Tarefa
from src.task_tracker.repositorio.tarefa_repositorio import TarefaRepositorio


class TarefaServico:

    def __init__(self, repositorio_instancia:TarefaRepositorio):
        self.repositorio = repositorio_instancia

    def buscar_tarefa_por_id(self, id_buscar:int, todas_tarefas:list[Tarefa]):
        for tarefa in todas_tarefas:
            if tarefa.id == id_buscar:
                return tarefa
        raise ValueError(f"ID {id_buscar} não encontrado em lista de tarefas. Operação cancelada!")

    def adicionar_tarefa(self, descricao: str):
        todas_tarefas = self.repositorio.carregar_tarefas()

        novo_id = self.repositorio.gerar_proximo_id(todas_tarefas)
        tarefa = Tarefa(novo_id, descricao)

        todas_tarefas.append(tarefa)
        self.repositorio.salvar_tarefas(todas_tarefas)

        return tarefa

    def listar_tarefas(self, filtro_status:StatusTarefa | None = None):
        todas_tarefas = self.repositorio.carregar_tarefas()

        if filtro_status is None:
            return todas_tarefas

        if isinstance(filtro_status, StatusTarefa):
            return [tarefa  # O QUE ENTRA NO RETURN DE LISTA SERÁ 'tarefa'
                    for tarefa in todas_tarefas  # DE ONDE VEM OS ELEMENTOS
                    if tarefa.status == filtro_status  # FILTRO
            ]

        raise ValueError("Status não compatível com os possíveis")

    def atualizar_descricao_tarefa(self, id_digitado:int, nova_descricao:str):
        todas_tarefas = self.repositorio.carregar_tarefas()

        tarefa_econtrada = self.buscar_tarefa_por_id(id_digitado, todas_tarefas)
        
        tarefa_econtrada.atualizar_descricao(nova_descricao)
        self.repositorio.salvar_tarefas(todas_tarefas)
        
        return True

    def atualizar_status_tarefa(self, id_digitado:int, novo_status:StatusTarefa):
        todas_tarefas = self.repositorio.carregar_tarefas()

        tarefa_econtrada = self.buscar_tarefa_por_id(id_digitado, todas_tarefas)

        tarefa_econtrada.atualizar_status(novo_status)
        self.repositorio.salvar_tarefas(todas_tarefas)
        
        return True

    def excluir_tarefa(self, id_digitado:int):
        todas_tarefas = self.repositorio.carregar_tarefas()

        tarefa_econtrada = self.buscar_tarefa_por_id(id_digitado, todas_tarefas)

        todas_tarefas.remove(tarefa_econtrada)
        self.repositorio.salvar_tarefas(todas_tarefas)

        return True

