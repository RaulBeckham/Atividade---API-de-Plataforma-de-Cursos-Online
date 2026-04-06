from fastapi import APIRouter, HTTPException
from services.services import criar_aluno as service_criar_aluno, criar_curso as service_criar_curso, listar_alunos as service_listar_alunos, listar_cursos as service_listar_cursos, buscar_curso as service_buscar_curso, atualizar_preco as service_atualizar_preco
from schemas.schemas import AlunoSchema, CursoSchema

router = APIRouter()

@router.post("/alunos")
def criar_aluno(aluno: AlunoSchema):
    return service_criar_aluno(aluno.nome, aluno.email)

@router.get("/alunos")
def listar_alunos():
    return service_listar_alunos()

@router.post("/cursos")
def criar_curso(curso: CursoSchema):
    return service_criar_curso(curso.codigo, curso.titulo, curso.preco, curso.tipo, curso.desconto_percentual)

@router.get("/cursos")
def listar_cursos():
    return service_listar_cursos()

@router.get("/cursos/{codigo}")
def buscar_curso(codigo: int):
    curso = service_buscar_curso(codigo)
    if not curso:
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    return curso

@router.put("/cursos/{codigo}/preco")
def atualizar_preco(codigo: int, novo_preco: float):
    curso = service_atualizar_preco(codigo, novo_preco)
    if not curso:
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    return curso

@router.get("/cursos/{codigo}/preco_final")
def preco_final(codigo: int):
    curso = buscar_curso(codigo)
    if not curso:
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    return {"preco_final": curso.preco_final()}