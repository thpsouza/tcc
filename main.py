import numpy as np

from modelagem.parametros_van_de_vusse import *
from modelagem import balancos_reator
from simulador import *
from plot import *
from utils.SistemaUnidades import *


def verificar_unidades_balancos():
    mol = Unidade("mol")
    litro = Unidade("L")
    kelvin = Unidade("K")
    hora = Unidade("h")
    mol_L = mol/litro
    K_h = kelvin/hora  
    
    Ca = Dado(3, mol_L)
    Cb = Dado(3, mol_L)
    T = Dado(393, kelvin)
    FV = Dado(45, 1/hora)
    dCa_dt, dCb_dt, dT_dt = balancos_reator([Ca, Cb, T], FV, parametros_reator_unidade)
    
    expressoes = [dCa_dt, dCb_dt, dT_dt]
    unidades_esperadas = [mol_L/hora, mol_L/hora, K_h]
    bools = verificar_consistencia_dimensional(expressoes, unidades_esperadas)
    print("Consistência dimensional das expressões: ", 
          f"Balanço molar A: {bools[0]} ({unidades_esperadas[0]})",     # type: ignore
          f"Balanço molar B: {bools[1]} ({unidades_esperadas[1]})",     # type: ignore
          f"Balanço de energia: {bools[2]} ({unidades_esperadas[2]})",  # type: ignore
          sep="\n")
    

def calcular_perfis_estacionarios():
    ## Chutes iniciais
    Cae = 3
    Cbe = 3 
    T0e = 120 + 273.15
    ## Solução do sistema de equações não lineares para cada F/V
    CA = []
    CB = []
    T = []
    F_V = np.linspace(10, 80)
    for fv in F_V:
        sol = calcular_estado_estacionario(balancos_reator, (Cae, Cbe, T0e), fv, parametros_reator)
        Cae, Cbe, Te = sol[0], sol[1], sol[2]
        CA.append(Cae)
        CB.append(Cbe)
        T.append(Te-273.15) #Converter novamente para Celsius
    
    ## Plot
    show = True
    salvar = False
    path = "../docs/src/fig/est"
    # plotar_perfis_est_separados(F_V, (CA, CB, T), salvar, path, show) # type: ignore
    # plotar_perfis_est_conc_juntos(F_V, (CA, CB), salvar, path, show) # type: ignore
    plotar_perfis_est_juntos(F_V, (CA, CB, T), salvar, path, show) # type: ignore


def calcular_perfis_dinamicos():
    ## Chutes iniciais
    Ca0 = 3
    Cb0 = 3 
    T0 = 120 + 273.15
    b = 5
    Fe_V = 45
    tempo = np.linspace(0, 0.5, 500)
    CA1, CB1, T1 = calcular_dinamica(balancos_reator, b, tempo, Fe_V, (Ca0, Cb0, T0), parametros_reator)
    CA2, CB2, T2 = calcular_dinamica(balancos_reator, -b, tempo, Fe_V, (Ca0, Cb0, T0), parametros_reator)
    
    show = True
    salvar = False
    path = "../docs/src/fig/din"
    degrau = "ambos" #"ambos", "pos" ou "neg"
    # plotar_perfis_din_separados(degrau, tempo, ((CA1, CB1, T1), (CA2, CB2, T2)), salvar, path, show) # type: ignore
    # plotar_perfis_din_conc_juntos(degrau, tempo, ((CA1, CB1), (CA2, CB2)), salvar, path, show) # type: ignore
    plotar_perfis_din_juntos(degrau, tempo, ((CA1, CB1, T1), (CA2, CB2, T2)), salvar, path, show) # type: ignore
    

def main():   
    verificar_unidades_balancos()
    calcular_perfis_estacionarios()
    calcular_perfis_dinamicos()
    

if __name__ == "__main__":
    main()
