# Atividade---API-de-Plataforma-de-Cursos-Online
No terminal dentro da pasta do projeto escreva:
 
 pip install fastapi uvicorn
 uvicorn main:app --reload

Depois abra o navegador e escreva
http://123.0.0.1:8000/docs

Para criar um aluno clique em POST /alunos, dps em "Try it out" e substitua os parametros e finalize clicando no botão de executar.
Para criar um curso clique em Post /cursos, dps em "try it out" e substitua os parametros r finalize clicando no botão de executar.

Para listar os alunos clique em get /alunos, dps em "Try it out" e substitua os parametros e finalize clicando no botão de executar.
Para listar os cursos clique em get /cursos, dps em "Try it out" e substitua os parametros e finalize clicando no botão de executar.

Para atualizar o preço de um curso clique em put /cursos, dps em "Try it out", digite o codigo do curso, digite o novo preço e finalize clicando no botão de executar.
Para consultar o preço final de um curso clique em get /curso/{codigo}/preco, dps em "Try it out", digite o codigo do curso e finalize clicando no botão de executar.
