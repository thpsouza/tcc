class Unidade:
    def __init__(self, valor:str|dict[str, int], expoente:int=1, nome:str="") -> None:
        if isinstance(valor, str):
            self.valor = {valor: expoente} if valor else {}
        else:
            self.valor = {u: e for u, e in valor.items() if e != 0}
        self.nome = nome
        
    def __mul__(self, other:'Unidade') -> 'Unidade':
        if isinstance(other, Unidade):
            d = {}
            for unidade in self.valor.keys() | other.valor.keys():
                d[unidade] = self.valor.get(unidade, 0) + other.valor.get(unidade, 0)
            return Unidade(d)
        return NotImplemented

    def __truediv__(self, other: 'Unidade') -> 'Unidade':
        if isinstance(other, Unidade):
            d = {}
            for unidade in self.valor.keys() | other.valor.keys():
                d[unidade] = self.valor.get(unidade, 0) - other.valor.get(unidade, 0)
            return Unidade(d)
        return NotImplemented
    
    def __rtruediv__(self, value:int=1) -> 'Unidade':
        if value == 1:
            d = {}
            for unidade, expoente in self.valor.items():
                d[unidade] = -expoente
            return Unidade(d)
        return NotImplemented
    
    def __pow__(self, value):
        if isinstance(value, (int, float)):
            d = {}
            for unidade, expoente in self.valor.items():
                d[unidade] = expoente * value
            return Unidade(d)
        return NotImplemented
    
    def __eq__(self, other:object):
        if isinstance(other, Unidade):
            return self.valor == other.valor
        return NotImplemented
    def __ne__(self, other:object): return not self.__eq__(other)

    def __str__(self) -> str:         
        # Ordenando numerador e denominador, e depois em ordem alfabética
        if self.valor:
            s = ""
            for u in sorted(self.valor.keys(), key=lambda u: (self.valor[u] < 0, u)):
                e = self.valor[u]
                s += f"{u} " if e == 1 else f"{u}^{e} "
            return s[:-1]
        return "1"
    
        ## Separando em numerador e denominador
        # num = {}
        # den = {}
        # str_num = ""
        # str_den = ""
        # for u, e in self.valor.items():
        #     if e > 0: num[u] = e
        #     elif e<0: den[u] = -e
        # for u in sorted(num.keys()):
        #     e = num[u]
        #     str_num += f"{u} " if e == 1 else f"{u}^{e} "
        # for u in sorted(den.keys()):
        #     e = den[u]
        #     str_den += f"{u} " if e == 1 else f"{u}^{e} "
    
        # s = ""
        # if str_num and str_den:
        #     s = f"{str_num[:-1]} / {str_den[:-1]}"
        # elif str_num:
        #     s = str_num[:-1]
        # elif str_den:
        #     s = f"1/({str_den[:-1]})"
        # return s
        
class UnidadesDiferentesError(ValueError):
    def __init__(self, operacao:str, u1:Unidade, u2:Unidade) -> None:
        self.message = f"Só é possível {operacao} dados com a mesma unidade!\n" + \
                    f"Unidade à esquerda: [ {u1} ]\n" + \
                    f"Unidade à direita [ {u2} ]"
        super().__init__(self.message)