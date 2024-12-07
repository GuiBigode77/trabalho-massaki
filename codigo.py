class GerenciadorDeDespesas:
    def __init__(self):
        self.salario = 0
        self.despesas = []

    def definir_salario(self):
        self.salario = float(input("Digite seu salário: R$ "))
        print(f"Salário definido: R$ {self.salario:.2f}")

    def adicionar_despesa(self):
        nome_despesa = input("Digite o nome da despesa: ")
        valor_despesa = float(input("Digite o valor da despesa: R$ "))
        self.despesas.append({'nome': nome_despesa, 'valor': valor_despesa})
        print(f"Despesa '{nome_despesa}' de R$ {valor_despesa:.2f} adicionada.")

    def calcular_total_despesas(self):
        return sum(despesa['valor'] for despesa in self.despesas)

    def verificar_alerta(self):
        total_despesas = self.calcular_total_despesas()
        saldo = self.salario - total_despesas
        if saldo < 500:
            print(f"ALERTA VERMELHO! Seu saldo é de R$ {saldo:.2f}.")
        else:
            print(f"Seu saldo atual é de R$ {saldo:.2f}.")

    def listar_despesas(self):
        print("Despesas cadastradas:")
        for despesa in self.despesas:
            print(f"{despesa['nome']}: R$ {despesa['valor']:.2f}")

    def executar(self):
        self.definir_salario()
        while True:
            self.adicionar_despesa()
            self.verificar_alerta()
            self.listar_despesas()  # Exibe as despesas após cada adição
            continuar = input("Deseja adicionar outra despesa? (s/n): ").lower()
            if continuar != 's':
                break
        print("Gerenciador de despesas encerrado.")


if __name__ == "__main__":
    gerenciador = GerenciadorDeDespesas()
    gerenciador.executar()
