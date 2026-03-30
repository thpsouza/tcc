from utils.SistemaUnidades import Dado, Unidade

k10 = Dado(1.287e12, Unidade({"h":-1})) #h^-1
k20 = Dado(1.287e12, Unidade({"h":-1})) #h^-1
k30 = Dado(9.043e9, Unidade({"L":1, "mol":-1, "h":-1})) #L / mol A . h
E1_R = Dado(9758.3, Unidade("K")) #K
E2_R = Dado(9758.3, Unidade("K")) #K
E3_R = Dado(8560.0, Unidade("K")) #K
deltaH_RAB = Dado(4.20, Unidade({"kJ":1, "mol":-1})) #kJ / mol A
deltaH_RBC = Dado(-11.00, Unidade({"kJ":1, "mol":-1})) #kJ / mol A
deltaH_RAD = Dado(-41.85, Unidade({"kJ":1, "mol":-1})) #kJ / mol A
rho = Dado(0.9342, Unidade({"kg":1, "L":-1})) #kg / L
cp = Dado(3.01, Unidade({"kJ":1, "kg":-1, "K":-1})) #kJ / kg.K
Kw = Dado(4032, Unidade({"kJ":1, "h":-1, "K":-1, "m":-2})) #kJ / h.K.m^2
A_R = Dado(0.215, Unidade("m", 2)) #m^2
V = Dado(10, Unidade("L")) #L
Tk = Dado(128.95+273.15, Unidade("K")) #K
T0 = Dado(130+273.15, Unidade("K")) #K
Ca0 = Dado(5.10, Unidade({"mol":1, "L":-1})) #mol A / L

parametros_reator_unidade = [
    Ca0, rho, cp, T0, Tk, Kw, A_R, V, 
    k10, k20, k30, 
    E1_R, E2_R, E3_R, 
    deltaH_RAB, deltaH_RBC, deltaH_RAD
    ]

parametros_reator = [float(p) for p in parametros_reator_unidade]