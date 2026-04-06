from domain.curso import Curso
from repositories.repo import alunos, cursos

def criar_curso(codigo:int, titulo:str, preco:float, tipo:int, desconto_percentual:float=0):
    curso_novo = Curso(codigo, titulo, preco, tipo, desconto_percentual)
    cursos.append(curso_novo)
    return curso_novo

def listar_cursos():
    return cursos

def buscar_curso(codigo:int):
    for curso in cursos:
        if curso.codigo == codigo:
            return curso
    return None

def atualizar_preco(codigo:int, novo_preco:float):
    curso = buscar_curso(codigo)
    if curso:
        curso.preco = novo_preco
        return curso
    return None

def criar_aluno(nome:str, email:str):
    aluno_novo = {"nome": nome, "email": email}
    alunos.append(aluno_novo)
    return aluno_novo

def listar_alunos():
    return alunos

