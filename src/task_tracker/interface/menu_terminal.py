import os
import time

from modelos.status_tarefa import StatusTarefa
from modelos.tarefa import Tarefa
from servico.tarefa_servico import TarefaServico


class MenuTerminal:

    def __init__(self, servico_instancia:TarefaServico):
        self.servico = servico_instancia

    def _limpar_terminal(self):
        time.sleep(0.7)
        os.system("cls" if os.name == "nt" else "clear")

    def _confirmar_volta_menu_principal(self, mensagem:str = "\nClique ENTER para voltar ao Menu Principal."):
        input(mensagem)

    def _formatar_lista_de_tarefas(self,tarefas:list[Tarefa]|None):
        if not tarefas:
            return "\nNenhuma tarefa encontrada!"

        return "\n".join(self._formatar_tarefa(item)for item in tarefas)

    def _formatar_tarefa(self, tarefa: Tarefa|None):

        return f"""{{
    'ID': {tarefa.id},
    'Status': {tarefa.status.value},
    'Descricao': '{tarefa.descricao}',
    'Data de criação': {tarefa.data_criacao.strftime("%d/%m/%Y %H:%M:%S")},
    'Última atualização': {tarefa.data_atualizacao.strftime("%d/%m/%Y %H:%M:%S")}
}}"""

    def iniciar(self):

        while True:

            opcao_escolhida = self.exibir_menu_principal()

            if opcao_escolhida == -1:
                continue
            elif opcao_escolhida == 1:
                self._limpar_terminal()
                self.fluxo_adicionar_tarefa()
                self._limpar_terminal()
            elif opcao_escolhida == 2:
                self._limpar_terminal()
                self.fluxo_listar_tarefa()
                self._limpar_terminal()
            elif opcao_escolhida == 3:
                self._limpar_terminal()
                self.fluxo_atualizar_descricao()
                self._limpar_terminal()
            elif opcao_escolhida == 4:
                self._limpar_terminal()
                self.fluxo_atualizar_status()
                self._limpar_terminal()
            elif opcao_escolhida == 5:
                self._limpar_terminal()
                self.fluxo_excluir_tarefa()
                self._limpar_terminal()
            elif opcao_escolhida == 0:
                self._limpar_terminal()
                print("Saindo do programa... Até logo!!!")
                break
            else:
                self._limpar_terminal()
                print("Opção fora do alcance de 0 a 5. Tente novamente!\n")


    def exibir_menu_principal(self):

        print("Bem Vindo ao Menu Principal do Gerenciador de Tarefas!!!")
        print("--------------------------------------------------------")
        print("1 - Criar Uma Nova Tarefa")
        print("2 - Listar Tarefas Criadas")
        print("3 - Atualizar Descrição da Tarefa")
        print("4 - Atualizar Status da Tarefa")
        print("5 - Excluir Uma Tarefa")
        print("0 - Sair do Programa")
        print("--------------------------------------------------------")

        opcao_digitada = input("Digite o número inteiro da ação que deseja fazer. \nIr para opção ")

        try:
            opcao_convertida = int(opcao_digitada)
            return opcao_convertida
        except (ValueError, TypeError):
            self._limpar_terminal()
            print(f"Erro. Opção '{opcao_digitada}' inválida! Tente novamente!\n")
            return -1

    def fluxo_adicionar_tarefa(self):
        print("----------------------------------------")
        print("Menu Criar Uma Nova Tarefa")
        print("Para voltar ao Menu Principal digite 0")
        print("----------------------------------------")

        descricao_tarefa = str(input("Descrição da Tarefa: "))

        if descricao_tarefa.strip() == "0":
            self._limpar_terminal()
            print("Operação Cancelada!")
            print("\nSaindo do Menu Criar Uma Nova Tarefa...")
            self._confirmar_volta_menu_principal()
            return

        try:
            nova_tarefa = self.servico.adicionar_tarefa(descricao_tarefa)
            self._limpar_terminal()
            print("Tarefa criada com sucesso!")
            print(self._formatar_tarefa(nova_tarefa))
        except ValueError as erro:
            print(f"\nERRO NA CRIAÇÃO DA TAREFA. {erro}")
        finally:
            self._confirmar_volta_menu_principal()

    def fluxo_listar_tarefa(self):
        continuar = True
        while continuar:
            print("----------------------------------------")
            print("Menu Listar Tarefas Criadas")
            print("1 - Listar Todas Tarefas")
            print("2 - Listar Tarefas 'A FAZER'")
            print("3 - Listar Tarefas 'EM ANDAMENTO'")
            print("4 - Listar Tarefas 'CONCLUIDA'")
            print("0 - Voltar ao Menu Principal")
            print("----------------------------------------")

            opcao_lista = input("Opção de listagem: ")

            try:
                opcao_lista_convertida = int(opcao_lista)

                if opcao_lista_convertida == 1:
                    try:
                        self._limpar_terminal()
                        print("Listando Todas as Tarefas Criadas:")
                        tarefas = self.servico.listar_tarefas()
                        print(self._formatar_lista_de_tarefas(tarefas))
                        continuar = False
                    except ValueError as erro:
                        print(f"ERRO. {erro}")
                elif opcao_lista_convertida == 2:
                    try:
                        self._limpar_terminal()
                        print("Listando Todas as Tarefas 'A FAZER':")
                        tarefas = self.servico.listar_tarefas(StatusTarefa.A_FAZER)
                        print(self._formatar_lista_de_tarefas(tarefas))
                        continuar = False
                    except ValueError as erro:
                        print(f"ERRO. {erro}")
                elif opcao_lista_convertida == 3:
                    try:
                        self._limpar_terminal()
                        print("Listando Todas as Tarefas 'EM ANDAMENTO':")
                        tarefas = self.servico.listar_tarefas(StatusTarefa.EM_ANDAMENTO)
                        print(self._formatar_lista_de_tarefas(tarefas))
                        continuar = False
                    except ValueError as erro:
                        print(f"ERRO. {erro}")
                elif opcao_lista_convertida == 4:
                    try:
                        self._limpar_terminal()
                        print("Listando Todas as Tarefas 'CONCLUIDA':")
                        tarefas = self.servico.listar_tarefas(StatusTarefa.CONCLUIDA)
                        print(self._formatar_lista_de_tarefas(tarefas))
                        continuar = False
                    except ValueError as erro:
                        print(f"ERRO. {erro}")
                elif opcao_lista_convertida == 0:
                    self._limpar_terminal()
                    print("Operação Cancelada!")
                    print("\nSaindo do Menu Listar Tarefas...")
                    continuar = False
                else:
                    self._limpar_terminal()
                    print(f"Opção '{opcao_lista_convertida}' fora do alcance de 0 a 4. Tente novamente!\n")
            except (ValueError, TypeError):
                self._limpar_terminal()
                print(f"Erro. Opção '{opcao_lista}' inválida! Tente novamente!\n")
            finally:
                if not continuar:
                    self._confirmar_volta_menu_principal()

    def fluxo_atualizar_descricao(self):
        while True:
            print("-------------------------------------------------------")
            print("Menu Atualizar Descrição de Tarefa")
            print("Todas as tarefas cadastradas: ")
            tarefas = self.servico.listar_tarefas()
            print(self._formatar_lista_de_tarefas(tarefas))
            print("0 - Voltar ao Menu Principal")
            print("-------------------------------------------------------")

            id_escolhido = input("Qual tarefa deseja atualizar? Digite apenas o ID numérico da tarefa.: \n")

            if id_escolhido.strip() == "0":
                self._limpar_terminal()
                print("Operação Cancelada!")
                print("\nSaindo do Menu Atualizar Descrição...")
                self._confirmar_volta_menu_principal()
                return

            try:
                id_escolhido_convertido = int(id_escolhido.strip())
            except ValueError:
                self._limpar_terminal()
                print(f"Opção '{id_escolhido}' não é válido! Tente novamente!\n")
                continue

            try:
                self.servico.buscar_tarefa_por_id(id_escolhido_convertido)
            except ValueError as erro:
                self._limpar_terminal()
                print(f"ERRO. {erro}\n")
                continue

            nova_descricao_tarefa = input(f"Nova Descrição da Tarefa {id_escolhido_convertido}: \n")

            try:
                tarefa_atualizada = self.servico.atualizar_descricao_tarefa(id_escolhido_convertido, nova_descricao_tarefa)
                self._limpar_terminal()
                print("Tarefa atualizada com sucesso!")
            except ValueError as erro:
                self._limpar_terminal()
                print(f"ERRO: {erro}\n")
                continue

            print(self._formatar_tarefa(tarefa_atualizada))
            self._confirmar_volta_menu_principal()
            return

    def fluxo_atualizar_status(self):
        while True:
            print("----------------------------------------")
            print("Menu Atualizar Status de Tarefa")
            print("Todas as tarefas cadastradas: ")
            tarefas = self.servico.listar_tarefas()
            print(self._formatar_lista_de_tarefas(tarefas))
            print("0 - Voltar ao Menu Principal")
            print("----------------------------------------")

            id_escolhido = input("Qual tarefa deseja atualizar? Digite apenas o ID numérico da tarefa.: \n").strip()

            if id_escolhido == "0":
                self._limpar_terminal()
                print("Operação Cancelada!")
                print("\nSaindo do Menu Atualizar Status...")
                self._confirmar_volta_menu_principal()
                return

            try:
                id_escolhido_convertido = int(id_escolhido)
            except ValueError:
                self._limpar_terminal()
                print(f"Erro. Opção '{id_escolhido}' inválida! Digite um número inteiro.\n")
                continue

            try:
                self.servico.buscar_tarefa_por_id(id_escolhido_convertido)
            except ValueError as erro:
                self._limpar_terminal()
                print(f"ERRO. {erro}\n")
                continue

            print(f"Mudar status da tarefa {id_escolhido_convertido} para:")
            print("1 - A FAZER")
            print("2 - EM ANDAMENTO")
            print("3 - CONCLUIDA")

            status_escolhido = input("Opção ")

            try:
                status_escolhido_convertido = int(status_escolhido)
            except ValueError:
                self._limpar_terminal()
                print(f"Erro. Opção '{status_escolhido}' inválida! Digite um número inteiro.\n")
                continue

            try:
                if status_escolhido_convertido == 1:
                    tarefa_atualizada = self.servico.atualizar_status_tarefa(id_escolhido_convertido, StatusTarefa.A_FAZER)
                elif status_escolhido_convertido == 2:
                    tarefa_atualizada = self.servico.atualizar_status_tarefa(id_escolhido_convertido, StatusTarefa.EM_ANDAMENTO)
                elif status_escolhido_convertido == 3:
                    tarefa_atualizada = self.servico.atualizar_status_tarefa(id_escolhido_convertido, StatusTarefa.CONCLUIDA)
                else:
                    self._limpar_terminal()
                    print(f"Opção de status '{status_escolhido_convertido}' não existe. Tente novamente!\n")
                    continue
            except ValueError as erro:
                self._limpar_terminal()
                print(f"ERRO: {erro}\n")
                continue

            self._limpar_terminal()
            print("Tarefa atualizada com sucesso!")
            print(self._formatar_tarefa(tarefa_atualizada))
            self._confirmar_volta_menu_principal()
            return

    def fluxo_excluir_tarefa(self):
        while True:
            print("----------------------------------------")
            print("Menu excluindo tarefa")
            print("Tarefas cadastradas: \n")
            tarefas = self.servico.listar_tarefas()
            print(self._formatar_lista_de_tarefas(tarefas))
            print("0 - Voltar ao Menu Principal")
            print("----------------------------------------")

            id_escolhido = input("Qual tarefa deseja excluir? PS.:Digite apenas o ID numérico da tarefa: ")

            if id_escolhido.strip() == "0":
                self._limpar_terminal()
                print("Operação Cancelada!")
                print("\nSaindo do Menu Excluir Uma Tarefa...")
                self._confirmar_volta_menu_principal()
                return

            try:
                id_escolhido_convertido = int(id_escolhido)
            except ValueError:
                self._limpar_terminal()
                print(f"Erro. Opção '{id_escolhido}' inválida! Digite um número inteiro.\n")
                continue

            try:
                self.servico.buscar_tarefa_por_id(id_escolhido_convertido)
            except ValueError as erro:
                self._limpar_terminal()
                print(f"ERRO. {erro}\n")
                continue

            confirmacao = str(input(f"\nTem certeza que deseja excluir PERMANENTEMENTE a tarefa {id_escolhido_convertido}? Responda com S para sim, e N para não.: \n"))

            if confirmacao.strip().lower() == "s":
                try:
                    self.servico.excluir_tarefa(id_escolhido_convertido)
                except ValueError as erro:
                    self._limpar_terminal()
                    print(f"ERRO: {erro}\n")
                    continue

                self._limpar_terminal()
                print(f"Tarefa {id_escolhido_convertido} excluída com sucesso!")
                print("Tarefas cadastradas depois da ação:")
                print(self._formatar_lista_de_tarefas(self.servico.listar_tarefas()))
                self._confirmar_volta_menu_principal()
                return
            elif confirmacao.strip().lower() == "n":
                self._limpar_terminal()
                print(f"Cancelando operação de excluir tarefa {id_escolhido}!")
                print("\nSaindo do Menu Excluir Uma Tarefa...")
                self._confirmar_volta_menu_principal()
                return
            else:
                self._limpar_terminal()
                print(f"Opção '{confirmacao}' inválida! Tente novamente!")