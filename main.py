import mysql.connector

from objetos import Animal, Funcionario, Demanda


def consulta_tudo():
   resultados = consulta_tabela('animal')
   print('Animal:')
   for resultado in resultados:
       print(resultado)
   print("=-" * 30)
   resultados = consulta_tabela('funcionario')
   print('Funcionario:')
   for resultado in resultados:
       print(resultado)
   print("=-" * 30)
   resultados = consulta_tabela('demanda')
   print('Demanda:')
   for resultado in resultados:
       print(resultado)
   print("=-" * 30)


def consulta_tabela(tabela):
    # Tentando conexão com o banco
    try:
        # Abrindo conexão
        conexao = mysql.connector.connect(host='localhost', database='oo', user='root', password='@nnGe624828')
        cursor = conexao.cursor()

        cursor.execute(f'SELECT * FROM {tabela}')
        resultados = cursor.fetchall()

        return resultados

        cursor.close()

    except mysql.connector.Error as erro:
        conexao.close()
        print(f'Falha ao consultar o dado no banco: {erro}')

    finally:
        if conexao.is_connected():
            conexao.close()


animais = Animal.gera_objeto(consulta_tabela('animal'))
for animal in animais:
    print(animal)
print("-*" * 50)

funcionarios = Funcionario.gera_objeto(consulta_tabela('funcionario'))
for funcionario in funcionarios:
    print(funcionario)
print("-*" * 50)

demandas = Demanda.gera_objeto(consulta_tabela('demanda'))
for demanda in demandas:
    print(demanda)
print("-*" * 50)

pause = input('Pausa para falar de update em animal(nome)')

animais[1].nome = 'Zeus'
resultados = consulta_tabela('animal')
for resultado in resultados:
    print(resultado)
print("-*" * 50)
print(animais[1])

pause = input('Pausa para falar de update em funcionário(Cargo)')

funcionarios[0].cargo = 'Analista de Dados'
resultados = consulta_tabela('funcionario')
for resultado in resultados:
    print(resultado)
print("-*" * 50)
print(funcionarios[0])

pause = input('Pausa para inserir um novo funcionário')

f = Funcionario(444, 'Lucas Gabriel', 'Aumoxarifado', False)
funcionarios.append(f)
resultados = consulta_tabela('funcionario')
for resultado in resultados:
    print(resultado)
print("-*" * 50)

pause = input('Pausa para deletar um funcionário funcionário')

sucesso = funcionarios[2].excluir_objeto_banco()
if sucesso:
    del (funcionarios[2])
else:
    print('Funcionário não apagado')

print("-*" * 50)
print('Objetos Funcionários:')
for funcionario in funcionarios:
    print(funcionario)
print("-*" * 50)

resultados = consulta_tabela('funcionario')
print("-*" * 50)
print('Funcionários no Banco:')
for resultado in resultados:
    print(resultado)
print("-*" * 50)