from math import exp


def arrhenius(T:float, k0:float, E_R:float) -> float:
    """Calcula a constante de velocidade de uma reação pela Lei de Arrhenius.

    Args:
        T (float): Temperatura, em Kelvin.
        k0 (float): Constante de velocidade da reação independente da temperatura, em h^-1.
        E_R (float): Energia de ativação normalizada pela cte dos gases, em K.

    Returns:
        float: Constante de velocidade da reação para uma dada temperatura, em h^-1.
    """
    return k0 * exp(-E_R / T)