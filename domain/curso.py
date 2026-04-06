class Curso:
    def __init__(self, codigo, titulo, preco, tipo, desconto_percentual=0):
        self.codigo = codigo
        self.titulo = titulo
        self.preco = preco
        self.tipo = tipo
        self.desconto_percentual = desconto_percentual

    def preco_final(self) -> float:
        if self.tipo == 1:
            return 0
        
        desconto = self.preco * (self.desconto_percentual / 100)
        final = self.preco - desconto

        if final < 0:
            return 0
        return final