from .unidade import Unidade, UnidadesDiferentesError


class Dado(float):
    def __new__(cls, valor:float, unidade:Unidade|None=None):
        return super().__new__(cls, valor)
    
    def __init__(self, valor:float, unidade:Unidade|None=None):
        if unidade:
            self.unidade = unidade
        else:
            self.unidade = Unidade("")
    
    def __neg__(self) -> 'Dado':
        return Dado(super().__neg__(), self.unidade)

    def __pos__(self) -> 'Dado':
        return Dado(super().__pos__(), self.unidade)

    def __abs__(self) -> 'Dado':
        return Dado(super().__abs__(), self.unidade)
    
    def __bool__(self) -> bool:
        return super().__bool__()
    
    def __add__(self, other:'Dado|float') -> 'Dado':
        if isinstance(other, Dado):
            if self.unidade == other.unidade:
                return Dado(super().__add__(other), self.unidade)
            else:
                raise UnidadesDiferentesError("somar", self.unidade, other.unidade)
        else:
            return Dado(super().__add__(other), self.unidade)
    def __radd__(self, value: float) -> 'Dado': return Dado(super().__radd__(value), self.unidade)
    
    def __sub__(self, other:'Dado|float') -> 'Dado':
        if isinstance(other, Dado):
            if self.unidade == other.unidade:
                return Dado(super().__sub__(other), self.unidade)
            else:
                raise UnidadesDiferentesError("subtrair", self.unidade, other.unidade)
        else:
            return Dado(super().__sub__(other), self.unidade)
    def __rsub__(self, value: float) -> 'Dado': return Dado(super().__rsub__(value), self.unidade)
    
    def __mul__(self, other:'Dado|float') -> 'Dado':
        if isinstance(other, Dado):
            nova_unidade = self.unidade * other.unidade
        else:
            nova_unidade = self.unidade
        return Dado(super().__mul__(other), nova_unidade)
    def __rmul__(self, value: float) -> 'Dado': return Dado(super().__rmul__(value), self.unidade)
    
    def __truediv__(self, other: 'Dado|float') -> 'Dado':
        if isinstance(other, Dado):
            nova_unidade = self.unidade / other.unidade
        else:
            nova_unidade = self.unidade
        return Dado(super().__truediv__(other), nova_unidade) 
    def __rtruediv__(self, value: float) -> 'Dado': 
        return Dado(super().__rtruediv__(value), Unidade({u:-e for u, e in self.unidade.valor.items()}))
    
    def __pow__(self, value:float, mod:None=None) -> 'Dado':
        return Dado(super().__pow__(value, mod), self.unidade**value)
    
    def __lt__(self, other: 'Dado|float') -> bool:
        if isinstance(other, Dado) and (self.unidade != other.unidade):
            raise UnidadesDiferentesError("comparar", self.unidade, other.unidade)
        return super().__lt__(other)

    def __le__(self, other: 'Dado|float') -> bool:
        if isinstance(other, Dado) and (self.unidade != other.unidade):
            raise UnidadesDiferentesError("comparar", self.unidade, other.unidade)
        return super().__le__(other)

    def __gt__(self, other: 'Dado|float') -> bool:
        if isinstance(other, Dado) and (self.unidade != other.unidade):
            raise UnidadesDiferentesError("comparar", self.unidade, other.unidade)
        return super().__gt__(other)

    def __ge__(self, other: 'Dado|float') -> bool:
        if isinstance(other, Dado) and (self.unidade != other.unidade):
            raise UnidadesDiferentesError("comparar", self.unidade, other.unidade)
        return super().__ge__(other)
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, Dado) and (self.unidade != other.unidade):
            return False
        return super().__eq__(other)
    def __ne__(self, other: object) -> bool: return not self.__eq__(other)
    
    def __round__(self, n:int=0) -> 'Dado': # type: ignore
        return Dado(super().__round__(n), self.unidade)
    
    def __str__(self) -> str:
        return f"{float(self):.7g}  [{self.unidade}]"
