from scipy.integrate import solve_ivp
from scipy.optimize import fsolve


def degrau(b, t):
    return b if t>=0 else 0


def calcular_estado_estacionario(balancos, chutes_iniciais, vazao_operacao, parametros_sistema):
    return fsolve(balancos, chutes_iniciais, args=(vazao_operacao, parametros_sistema))


def calcular_dinamica(balancos, magnitude_degrau, intervalo_tempo, 
                      vazao_operacao, chutes_inciais, parametros_sistema):
    # metodo = 'RK45'
    metodo = 'BDF'
    # metodo = 'Radau'
    # metodo = 'LSODA'
    x0 = calcular_estado_estacionario(balancos, chutes_inciais, vazao_operacao, parametros_sistema)
    f = lambda t, x: balancos(x, degrau(magnitude_degrau, t)+vazao_operacao, parametros_sistema)
    solucao = solve_ivp(f, t_span=(intervalo_tempo[0],intervalo_tempo[-1]), y0=x0, method=metodo, t_eval=intervalo_tempo)
    return solucao.y