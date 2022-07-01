import mysql


class Animal:
    def __init__(self, id, nome, raca, nascimento):
        self._id = id
        self._nome = nome
        self._raca = raca
        self._nascimento = nascimento

    @staticmethod
    def gera_objeto(lista_animal):
        animais = []
        for animal in lista_animal:
            animais.append(Animal(animal[0], animal[1], animal[2], f'{animal[3].year}-{animal[3].month}-{animal[3].day}'))
        return animais

    def __str__(self):
        return f'Id: {self._id} - Nome: {self._nome} - Raça: {self._raca} - Nascimento: {self._nascimento}'

    @property
    def id(self):
        return self._id

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        # Tentando conexão com o banco
        try:
            # Abrindo conexão
            conexao = mysql.connector.connect(host='localhost', database='oo', user='root', password='@nnGe624828')
            cursor = conexao.cursor()

            sql = f'UPDATE animal SET nome = %s WHERE id = %s'
            val = (novo_nome, self._id)
            cursor.execute(sql, val)
            conexao.commit()
            print(cursor.rowcount, 'alteradas com sucesso.')

            cursor.close()
            self._nome = novo_nome
        except mysql.connector.Error as erro:
            conexao.close()
            print(f'Falha ao alterar o dado no banco: {erro}')
        finally:
            if conexao.is_connected():
                conexao.close()

    @property
    def raca(self):
        return self._raca

    @property
    def nascimento(self):
        return self._nascimento


class Funcionario:
    def __init__(self, id, nome, cargo, isBanco):
        if not isBanco:
            # Tentando conexão com o banco
            try:
                # Abrindo conexão
                conexao = mysql.connector.connect(host='localhost', database='oo', user='root', password='@nnGe624828')
                cursor = conexao.cursor()

                sql = f'INSERT INTO funcionario (id, nome, cargo) VALUES (%s, %s, %s)'
                val = (f'{id}', f'{nome}', f'{cargo}')
                cursor.execute(sql, val)
                conexao.commit()
                print(cursor.rowcount, 'inserida com sucesso.')

                cursor.close()
                self._id = id
                self._nome = nome
                self._cargo = cargo
            except mysql.connector.Error as erro:
                conexao.close()
                print(f'Falha ao inserir o dado no banco: {erro}')
            finally:
                if conexao.is_connected():
                    conexao.close()
        else:
            self._id = id
            self._nome = nome
            self._cargo = cargo

    @staticmethod
    def gera_objeto(lista_funcionario):
        funcionarios = []
        for funcionario in lista_funcionario:
            funcionarios.append(
               Funcionario(funcionario[0], funcionario[1], funcionario[2], True))
        return funcionarios

    def excluir_objeto_banco(self):
        # Tentando conexão com o banco
        sucesso = False
        try:
            # Abrindo conexão
            conexao = mysql.connector.connect(host='localhost', database='oo', user='root', password='@nnGe624828')
            cursor = conexao.cursor()

            sql = f'DELETE FROM funcionario WHERE id = {self._id}'
            cursor.execute(sql)
            conexao.commit()
            print(cursor.rowcount, 'deletada com sucesso.')

            cursor.close()
            sucesso = True
        except mysql.connector.Error as erro:
            conexao.close()
            print(f'Falha ao alterar o dado no banco: {erro}')
        finally:
            if conexao.is_connected():
                conexao.close()
            return sucesso

    def __str__(self):
        return f'Id: {self._id} - Nome: {self._nome} - Cargo: {self._cargo}'

    @property
    def id(self):
        return self._id

    @property
    def nome(self):
        return self._nome

    @property
    def cargo(self):
        return self._cargo

    @cargo.setter
    def cargo(self, novo_cargo):
        # Tentando conexão com o banco
        try:
            # Abrindo conexão
            conexao = mysql.connector.connect(host='localhost', database='oo', user='root', password='@nnGe624828')
            cursor = conexao.cursor()

            sql = f'UPDATE funcionario SET cargo = %s WHERE id = %s'
            val = (novo_cargo, self._id)
            cursor.execute(sql, val)
            conexao.commit()
            print(cursor.rowcount, 'alteradas com sucesso.')

            cursor.close()
            self._cargo = novo_cargo
        except mysql.connector.Error as erro:
            conexao.close()
            print(f'Falha ao alterar o dado no banco: {erro}')
        finally:
            if conexao.is_connected():
                conexao.close()

class Demanda:
    def __init__(self, id, id_animal, id_funcionario, data, descricao):
        self._id = id
        self._id_animal = id_animal
        self._id_funcionario = id_funcionario
        self._data = data
        self._descricao = descricao

    @staticmethod
    def gera_objeto(lista_demanda):
        demandas = []
        for demanda in lista_demanda:
            demandas.append(
                Demanda(
                demanda[0], demanda[1], demanda[2], f'{demanda[3].year}-{demanda[3].month}-{demanda[3].day}', demanda[4]
                )
            )
        return demandas

    @staticmethod
    def consulta_nome_por_id(tabela, id):
        # Tentando conexão com o banco
        try:
            # Abrindo conexão
            conexao = mysql.connector.connect(host='localhost', database='oo', user='root', password='@nnGe624828')
            cursor = conexao.cursor()

            cursor.execute(f'SELECT nome FROM {tabela} WHERE id = {id}')
            resultados = cursor.fetchall()
            return resultados

            cursor.close()
        except mysql.connector.Error as erro:
            conexao.close()
            print(f'Falha ao consultar o dado no banco: {erro}')
        finally:
            if conexao.is_connected():
                conexao.close()

    def __str__(self):
        return f'Id: {self._id} - Animal: {self.consulta_nome_por_id("animal", self._id_animal)[0][0]} - ' \
               f'Responsável: {self.consulta_nome_por_id("funcionario", self._id_funcionario)[0][0]} - ' \
               f'Data: {self._data} - Descrição: {self._descricao}'

    @property
    def id(self):
        return self._id

    @property
    def id_animal(self):
        return self._id_animal

    def id_funcionario(self):
        return self._id_funcionario

    def data(self):
        return self._data

    def descricao(self):
        return self._descricao

