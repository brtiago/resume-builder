class LerCurriculoCommand:
    def execute(self):
        print("Lendo Curriculo Vitae")

class LerDescricaoVagaCommand:
    def execute(self):
        print("Lendo descrição da vaga")

class ListarHabilidadesCommand:
    def execute(self):
        print("Listando habilidades técnicas da vaga")

class CriarSecaoSobreCommand:
    def execute(self):
        print("Criando a seção SOBRE para Linkedin")

class ObterCompatibilidadeCommand:
    def execute(self):
        print("Obtendo compatibilidade com a vaga")

class CriarResumoProfissionalCommand:
    def execute(self):
        print("Criando RESUMO PROFISSIONAL para o Currículo")

class Menu:
    def __init__(self):
        self.comandos = {
            1: LerCurriculoCommand(),
            2: LerDescricaoVagaCommand(),
            3: ListarHabilidadesCommand(),
            4: CriarSecaoSobreCommand(),
            5: ObterCompatibilidadeCommand(),
            6: CriarResumoProfissionalCommand()
        }

    def mostrar_opcoes(self):
        print("\nDIGITE O NÚMERO DA OPERAÇÃO DESEJADA:")
        print("1 -> Ler Curriculo Vitae")
        print("2 -> Ler descrição da vaga")
        print("3 -> Listar habilidades técnicas da vaga")
        print("4 -> Criar a seção SOBRE para Linkedin")
        print("5 -> Obter compatibilidade com a vaga")
        print("6 -> Criar RESUMO PROFISSIONAL para o Currículo")
        print("0 -> Sair")

    def executar_opcao(self, opcao):
        comando = self.comandos.get(opcao)
        if comando:
            comando.execute()
        else:
            print("Opção inválida")

def main():
    menu_principal = Menu()
    opcao = -1
    while opcao != 0:
        menu_principal.mostrar_opcoes()
        opcao = int(input("Opção escolhida: "))
        menu_principal.executar_opcao(opcao)

if __name__ == "__main__":
    main()
