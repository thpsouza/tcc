from .dado import Dado
from .unidade import Unidade


def verificar_consistencia_dimensional(expressao:Dado|list[Dado], 
                       unidade:Unidade|list[Unidade]
                       ) -> bool|list[bool]:
    if isinstance(expressao, Dado) and isinstance(unidade, Unidade):
        return expressao.unidade == unidade
    elif isinstance(expressao, (list, tuple)) and isinstance(unidade, (list, tuple)):
        return list(
            map(lambda x: verificar_consistencia_dimensional(x[0], x[1]), 
                zip(expressao, unidade)
                )
            ) # type: ignore
    else:
        raise ValueError(
            f"A expressão deve ser do tipo 'Dado', ou uma lista de 'Dados'. Foi passado '{type(expressao)}'.\n" 
            + f"A unidade deve ser do tipo 'Unidade', ou uma lista de 'Unidades'. Foi passado '{type(unidade)}'.")