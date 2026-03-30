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


def balancos_reator(X:list, F_V:float, parametros_sistema:list):
    Ca0, rho, cp, T0, Tk, Kw, A_R, V, \
        k10, k20, k30, E1_R, E2_R, E3_R, \
            deltaH1, deltaH2, deltaH3 = parametros_sistema
    Ca, Cb, T = X
    k1 = arrhenius(T, k10, E1_R)
    k2 = arrhenius(T, k20, E2_R)
    k3 = arrhenius(T, k30, E3_R)
    dCa_dt = F_V*(Ca0 - Ca) -  k1*Ca - k3*Ca**2
    dCb_dt = -F_V*Cb +  k1*Ca - k2*Cb
    dT_dt = (1/(rho*cp))*((-deltaH1)*k1*Ca + 
                          (-deltaH2)*k2*Cb + 
                          (-deltaH3)*k3*Ca**2) \
          + F_V*(T0 - T) + (Kw*A_R/(rho*cp*V))*(Tk - T)
    return [dCa_dt, dCb_dt, dT_dt]