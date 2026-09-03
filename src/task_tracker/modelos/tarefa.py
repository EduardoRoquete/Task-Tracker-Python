from datetime import datetime

from src.task_tracker.modelos.status_tarefa import StatusTarefa


class Tarefa:

    def __init__(self, id:int, descricao:str):
        self.__id = id
        self.__descricao = None
        self.data_criacao = datetime.now()
        self.data_atualizacao = datetime.now()
        self.status = StatusTarefa.A_FAZER

        self.descricao = descricao

    @property
    def id(self):
        return self.__id

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, valor_descricao:str):

        if len(valor_descricao.strip()) > 0:
            self.__descricao = valor_descricao.strip()
        else:
            self.__descricao = None
            raise ValueError("Não foi possível criar uma tarefa, pois não são aceitas descrições vazias.")

    def atualizar_descricao(self, nova_descricao:str):

        self.descricao = nova_descricao
        self.data_atualizacao = datetime.now()

    def atualizar_status(self, novo_status:StatusTarefa):

        if not isinstance(novo_status, StatusTarefa):
            raise ValueError(f"Não é possível mudar o status da tarefa por meio de um texto. Operação cancelada!")

        self.status = novo_status
        self.data_atualizacao = datetime.now()

    def para_dicionario(self) -> dict:

        return{
            "id": self.id,
            "status": self.status.value,
            "descricao": self.descricao,
            "data_criacao": self.data_criacao.isoformat(),
            "data_atualizacao": self.data_atualizacao.isoformat()
        }

    @classmethod
    def de_dicionario(cls, dados:dict):

        tarefa = cls(dados["id"], dados["descricao"])
        tarefa.status = StatusTarefa(dados["status"])
        tarefa.data_criacao = datetime.fromisoformat(dados["data_criacao"])
        tarefa.data_atualizacao = datetime.fromisoformat(dados["data_atualizacao"])

        return tarefa