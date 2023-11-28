class SistemaGerencial:
    def _init_(self):
        self.clientes = []
        self.filiais = []
        self.vendas = {}  
        self.custos = {}  

    def cadastrar_cliente(self, nome, email, telefone):
        cliente = {
            'nome': nome,
            'email': email,
            'telefone': telefone
        }
        self.clientes.append(cliente)
        print(f'Cliente {nome} cadastrado com sucesso!')

   def adicionar_filial(self, nome_filial):
        self.filiais.append(nome_filial)
        self.vendas[nome_filial] = 0 
        self.custos[nome_filial] = 0 
        print(f'Filial {nome_filial} adicionada ao sistema.')

    def adicionar_vendas_filial(self, nome_filial, valor_vendas):
        if nome_filial in self.vendas:
            self.vendas[nome_filial] += valor_vendas
            print(f'Vendas da filial {nome_filial} atualizadas com sucesso.')
        else:
            print(f'Filial {nome_filial} não encontrada.')

    def adicionar_custos_filial(self, nome_filial, valor_custos):
        if nome_filial in self.custos:
            self.custos[nome_filial] += valor_custos
            print(f'Custos da filial {nome_filial} atualizados com sucesso.')
        else:
            print(f'Filial {nome_filial} não encontrada.')

       def gerar_relatorio_vendas(self):
        print('--- Relatório de Desempenho de Vendas por Filial ---')
        for filial, venda in self.vendas.items():
            print(f'Filial: {filial} - Vendas: R${venda}')

    def gerar_relatorio_estoque(self):
        print('--- Relatório de Movimentação de Estoque por Filial ---')
        for filial, estoque in self.estoque.items():
            print(f'Filial: {filial}')
            for produto, quantidade in estoque.items():
                print(f'Produto: {produto} - Estoque: {quantidade} unidades')

     def gerar_relatorio_operacional(self):
        print('--- Relatório de Eficiência Operacional ---')
        for filial, venda in self.vendas.items():
            custo = self.custos[filial]
            eficiencia = (venda - custo) / venda * 100 if venda != 0 else 0 
            print(f'Filial: {filial} - Eficiência: {eficiencia:.2f}%')
