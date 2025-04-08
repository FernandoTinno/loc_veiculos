import uuid


class Cliente:
    def __init__(self,nome =str,sexo = str,cpf =str,email =str,renda = float):
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
        
          
class Funcionario:
    def __init__(self,nome =str,sexo = str,cpf =str,email =str,salario = float, cargo = str):
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


class Locadora:
    def __init__(self,funcionario = Funcionario(),cliente = Cliente(),qtd_veiculos = int, cnpj = str, endereco = str, telefone = str, email = str):     
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
         
            
class Veiculo:
    def __init__(self, marca = str, cor = str, ano = int, modelo = str):
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
        

class Pagamento:
    def __init__(self, entrada = float):
        self.__id_pagamento = uuid.uuid4()
        self.__entrada = entrada
        self.__pag_metodo = ['debito', 'credito', 'pix', 'boleto', 'credito_parcelado', 'dinheiro']
        
        
    
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
        
        
class Seguro:
    def __init__(self,tipo_seguro = str, valor_seguro = float):
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
    def valor__seguro(self):
        return self.__valor_seguro

    @valor__seguro.setter
    def valor__seguro(self, valor__seguro):
        self.__valor_seguro = valor__seguro


class Contrato: 
    def __init__(self, data_inicio = str, data_fim =str, mediador = Funcionario(), cliente = Cliente(), mtd_pagamento = Pagamento(), seguro = Seguro(), val_total = float):
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
        
        
fernando = Cliente(nome = 'Fernando',sexo = 'masculino',cpf = '54984814896',email = 'fernando.venceslau@estudante.ifms.edu.br',renda = 1500.50)
larissa = Funcionario(nome = 'Larissa' ,sexo = 'feminino',cpf = '841651515',email ='lalarissamoura51@gmail.com',salario = 3000, cargo = 'gerente')
localiza = Locadora(funcionario = larissa.nome,cliente = fernando.nome,qtd_veiculos = 10, cnpj = '40028922', endereco = 'rua j', telefone = '189974632542', email = 'localiza@gmail.com')
gol = Veiculo(marca = 'volksvagen', cor = 'vermelho', ano = '2012', modelo = 'gol')
pag = Pagamento(500)
seg = Seguro('completo', 200)
cont = Contrato(data_inicio = '07/04/2025', data_fim = '07/05/2025', mediador = larissa.nome, cliente = fernando.nome, mtd_pagamento = [pag.entrada,pag.pag_metodo[5]] , seguro = seg.valor__seguro, val_total= 1000)

print(f'o cliente {fernando.nome} está realizando um contrato de aluguel, tendo como mediadora a gerente {larissa.nome}.\n O veiculo em especifico é um {gol.modelo}, da marca {gol.marca}, fabricado no ano de {gol.ano}.\n')

ver_contrato = input('Você deseja ver o contrato?(digite s ou n)')

if ver_contrato == 's':
    print('Aqui estão os dados do contrato:\n')
    print(f'Inicio do contrato: {cont.data_inicio}\nFim do contrato: {cont.data_fim}\n\nCliente: {fernando.nome}\nCPF: {fernando.cpf}\nEmail: {fernando.email}.\n\nFuncionaria responsavel: {larissa.nome}\nCPF: {larissa.cpf}\nEmail: {larissa.email}.\n\nModelo do carro: {gol.modelo}\nMarca: {gol.marca}\nAno: {gol.ano}\nCor: {gol.cor}\n\nValor total: {cont.val_total}\nEntrada: {pag.entrada}\nTipo do seguro: {seg.tipo_seguro}\nValor do seguro: {seg.valor__seguro}\nValor restante: {cont.val_total - seg.valor__seguro - pag.entrada}\nMetodo de pagamento do valor restante: {pag.pag_metodo[5]}\n')
else:
    print('OK')