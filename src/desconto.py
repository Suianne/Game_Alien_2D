from abc import ABC, abstractmethod

class Desconto(ABC):
    @abstractmethod
    def calcular(self, valor: float) -> float:
        pass

class IDesconto:
    def calcular(self, valor):
        raise NotImplementedError

class ICupom:
    def aplicar_cupom(self, codigo):
        raise NotImplementedError

class IVIP:
    def validar_usuario_vip(self, usuario):
        raise NotImplementedError

class Desconto_normal(Desconto):
    def calcular(self, valor) -> float:
        return valor * 0.1

class Desconto_vip(IDesconto, ICupom, IVIP):
    def calcular(self, valor) -> float:
        return valor * 0.2
    
    def aplicar_cupom(self, codigo):
        return True

    def validar_usuario_vip(self, usuario):
        return usuario == "vip"

class Desconto_premium(Desconto):
    def calcular(self, valor) -> float:
        return valor * 0.3

def aplicar_desconto(desconto: Desconto, valor:float) -> float:
    return desconto.calcular(valor)

def aplicar_cupom(desconto: Desconto, cupom: str) -> bool:
    return desconto.aplicar_cupom(cupom)

class Pedido:
    def __init__(self, desconto: IDesconto):
        self.desconto = desconto

    def total(self, valor):
        return valor - self.desconto.calcular(valor)

if __name__ == "__main__":
    valor = 100

    pedido_normal = Pedido(Desconto_normal())
    pedido_vip = Pedido(Desconto_vip())

    print("Normal:", pedido_normal.total(valor))
    print("VIP:", pedido_vip.total(valor))

