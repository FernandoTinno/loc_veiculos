import uuid


class Cliente:
    def __init__(self, nome: str, sexo: str, cpf: str, email: str, renda: float):
        self.__id_cliente = uuid.uuid4()
        self.__nome = nome
        self.__sexo = sexo
        self.__cpf = cpf
        self.__email = email
        self.__renda = renda

    @property
    def id_cliente(self):
        return self.__id_cliente

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def sexo(self):
        return self.__sexo

    @sexo.setter
    def sexo(self, sexo):
        self.__sexo = sexo

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def renda(self):
        return self.__renda

    @renda.setter
    def renda(self, renda):
        self.__renda = renda

    def mostrar(self):
        print(f'Cliente: {self.nome}\nSexo: {self.sexo}\nCPF: {self.cpf}\nEmail: {self.email}\n Renda mensal: {self.renda}\n')


class Funcionario:
    def __init__(self, nome: str, sexo: str, cpf: str, email: str, salario: float, cargo: str):
        self.__id_funcionario = uuid.uuid4()
        self.__nome = nome
        self.__sexo = sexo
        self.__cpf = cpf
        self.__email = email
        self.__salario = salario
        self.__cargo = cargo

    @property
    def id_funcionario(self):
        return self.__id_funcionario

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def sexo(self):
        return self.__sexo

    @sexo.setter
    def sexo(self, sexo):
        self.__sexo = sexo

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, salario):
        self.__salario = salario

    @property
    def cargo(self):
        return self.__cargo

    @cargo.setter
    def cargo(self, cargo):
        self.__cargo = cargo

    def mostrar(self):
        print(f'Funcionaria responsavel: {self.nome}\nSexo: {self.sexo}\nCPF: {self.cpf}\nEmail: {self.email}\nSalario: {self.salario}\nCargo: {self.cargo}\n')


class Locadora:
    def __init__(self, funcionario, cliente, qtd_veiculos: int, cnpj: str, endereco: str, telefone: str, email: str):
        self.__id_locadora = uuid.uuid4()
        self.__funcionarios = funcionario
        self.__clientes = cliente
        self.__qtd_veiculos = qtd_veiculos
        self.__cnpj = cnpj
        self.__endereco = endereco
        self.__telefone = telefone
        self.__email = email

    @property
    def id_locadora(self):
        return self.__id_locadora

    @property
    def funcionarios(self):
        return self.__funcionarios

    @funcionarios.setter
    def funcionarios(self, funcionarios):
        self.__funcionarios = funcionarios

    @property
    def clientes(self):
        return self.__clientes

    @clientes.setter
    def clientes(self, clientes):
        self.__clientes = clientes

    @property
    def qtd_veiculos(self):
        return self.__qtd_veiculos

    @qtd_veiculos.setter
    def qtd_veiculos(self, qtd_veiculos):
        self.__qtd_veiculos = qtd_veiculos

    @property
    def cnpj(self):
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, cnpj):
        self.__cnpj = cnpj

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    def mostrar(self):
        print(f'Funcionarios: {self.funcionarios.nome}\nClientes: {self.clientes.nome}\nQuantidade de veiculos: {self.qtd_veiculos}\nCNPJ: {self.cnpj}\nEndereço: {self.endereco}\nTelefone: {self.telefone}\nEmail: {self.email}\n')


class Veiculo:
    def __init__(self, marca: str, cor: str, ano: int, modelo: str):
        self.__id_veiculo = uuid.uuid4()
        self.__marca = marca
        self.__cor = cor
        self.__ano = ano
        self.__modelo = modelo

    @property
    def id_veiculo(self):
        return self.__id_veiculo

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    @property
    def cor(self):
        return self.__cor

    @cor.setter
    def cor(self, cor):
        self.__cor = cor

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

    def mostrar(self):
        print(f'Modelo do carro: {self.modelo}\nMarca: {self.marca}\nAno: {self.ano}\nCor: {self.cor}\n')


class Pagamento:
    def __init__(self, entrada: float, pag_metodo: str):
        self.__id_pagamento = uuid.uuid4()
        self.__entrada = entrada
        self.__pag_metodo = pag_metodo

    @property
    def id_pagamento(self):
        return self.__id_pagamento

    @property
    def pag_metodo(self):
        return self.__pag_metodo

    @pag_metodo.setter
    def pag_metodo(self, pag_metodo):
        self.__pag_metodo = pag_metodo

    @property
    def entrada(self):
        return self.__entrada

    @entrada.setter
    def entrada(self, entrada):
        self.__entrada = entrada

    def mostrar(self):
        print(f'Entrada: {self.entrada}\nMetodo de pagamento: {self.pag_metodo}\n')


class Seguro:
    def __init__(self, tipo_seguro: str, valor_seguro: float):
        self.__id_seguro = uuid.uuid4()
        self.__tipo_seguro = tipo_seguro
        self.__valor_seguro = valor_seguro

    @property
    def id_seguro(self):
        return self.__id_seguro

    @property
    def tipo_seguro(self):
        return self.__tipo_seguro

    @tipo_seguro.setter
    def tipo_seguro(self, tipo_seguro):
        self.__tipo_seguro = tipo_seguro

    @property
    def valor_seguro(self):
        return self.__valor_seguro

    @valor_seguro.setter
    def valor_seguro(self, valor_seguro):
        self.__valor_seguro = valor_seguro

    def mostrar(self):
        print(f'Tipo do seguro: {self.tipo_seguro}\nValor do seguro: {self.valor_seguro}\n')


class Contrato:
    def __init__(self, mediador, cliente, mtd_pagamento, seguro, data_inicio: str, data_fim: str, val_total: float):
        self.__id_contrato = uuid.uuid4()
        self.__data_inicio = data_inicio
        self.__data_fim = data_fim
        self.__mediador = mediador
        self.__cliente = cliente
        self.__mtd_pagamento = mtd_pagamento
        self.__seguro = seguro
        self.__val_total = val_total

    @property
    def id_contrato(self):
        return self.__id_contrato

    @property
    def data_inicio(self):
        return self.__data_inicio

    @data_inicio.setter
    def data_inicio(self, data_inicio):
        self.__data_inicio = data_inicio

    @property
    def data_fim(self):
        return self.__data_fim

    @data_fim.setter
    def data_fim(self, data_fim):
        self.__data_fim = data_fim

    @property
    def mediador(self):
        return self.__mediador

    @mediador.setter
    def mediador(self, mediador):
        self.__mediador = mediador

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @property
    def mtd_pagamento(self):
        return self.__mtd_pagamento

    @mtd_pagamento.setter
    def mtd_pagamento(self, mtd_pagamento):
        self.__mtd_pagamento = mtd_pagamento

    @property
    def seguro(self):
        return self.__seguro

    @seguro.setter
    def seguro(self, seguro):
        self.__seguro = seguro

    @property
    def val_total(self):
        return self.__val_total

    @val_total.setter
    def val_total(self, val_total):
        self.__val_total = val_total

    def mostrar(self):
        print(f'Inicio do contrato: {self.data_inicio}\nFim do contrato: {self.data_fim}\nValor total: {self.val_total}\nEntrada: {self.mtd_pagamento.entrada}\nValor restante: {self.val_total - self.seguro.valor_seguro - self.mtd_pagamento.entrada}\nMetodo de pagamento do valor restante: {self.mtd_pagamento.pag_metodo}')
        


fernando = Cliente(nome='Fernando', sexo='masculino', cpf='54984814896', email='fernando.venceslau@estudante.ifms.edu.br', renda=1500.50)
larissa = Funcionario(nome='Larissa', sexo='feminino', cpf='841651515', email='lalarissamoura51@gmail.com', salario=3000, cargo='gerente')
localiza = Locadora(funcionario=larissa, cliente=fernando, qtd_veiculos=10, cnpj='40028922', endereco='rua j', telefone='189974632542', email='localiza@gmail.com')
gol = Veiculo(marca='volksvagen', cor='vermelho', ano=2012, modelo='gol')
pag = Pagamento(entrada=500, pag_metodo='dinheiro')
seg = Seguro(tipo_seguro='completo', valor_seguro=200)
cont = Contrato(data_inicio='07/04/2025', data_fim='07/05/2025', mediador=larissa, cliente=fernando, mtd_pagamento=pag, seguro=seg, val_total=1000)

fernando.mostrar()
larissa.mostrar()
localiza.mostrar()
gol.mostrar()
pag.mostrar()
seg.mostrar()
cont.mostrar()