import smtplib

class GerenteSystem:
    def __init__(self):
        self.fornecedores = []
        self.niveis_estoque = {}

    def cadastrar_fornecedor(self):
        nome = input("Nome do fornecedor: ")
        email = input("E-mail do fornecedor: ")
        produto_fornecido = input("Produto fornecido pelo fornecedor: ")
        
        novo_fornecedor = {"nome": nome, "email": email, "produto": produto_fornecido}
        self.fornecedores.append(novo_fornecedor)
        
        print(f"Fornecedor '{nome}' cadastrado com sucesso!")

    def verificar_niveis_estoque(self, produto):
        # Lógica para verificar níveis de estoque
        # Retorna True se o nível estiver abaixo do ponto de reposição
        pass

    def enviar_alerta_email(self):
        # Lógica para enviar alerta por e-mail
        server = smtplib.SMTP('smtp.gmail.com', 587)
        # Configurar o servidor SMTP e enviar e-mail
        server.starttls()
        # Lógica de autenticação no e-mail
        server.login("seu_email@gmail.com", "sua_senha")
        # Construir e enviar e-mail
        subject = "Alerta de Reabastecimento"
        body = "Níveis de estoque estão baixos. Favor providenciar reabastecimento."
        message = f"Subject: {subject}\n\n{body}"
        server.sendmail("seu_email@gmail.com", "gerente_email@gmail.com", message)
        print("Alerta de reabastecimento enviado com sucesso!")

    def gerar_pedido_fornecedor(self, fornecedor):
        # Lógica para gerar pedido ao fornecedor
        print(f"Pedido gerado para {fornecedor['nome']} - {fornecedor['produto']}")

    def pedidos_automaticos(self):
        produto = input("Nome do produto: ")
        if self.verificar_niveis_estoque(produto):
            print("Gerando pedidos automáticos...")
            for fornecedor in self.fornecedores:
                self.gerar_pedido_fornecedor(fornecedor)
                self.enviar_alerta_email()
            print("Pedidos automáticos enviados com sucesso!")

    def menu_gerente(self):
        while True:
            print("\nMenu Gerente:")
            print("1. Cadastrar Fornecedor")
            print("2. Pedidos Automáticos")
            print("3. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.cadastrar_fornecedor()
            elif opcao == '2':
                self.pedidos_automaticos()
            elif opcao == '3':
                print("Saindo do sistema. Até mais!")
                break
            else:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    sistema_gerente = GerenteSystem()
    sistema_gerente.menu_gerente()