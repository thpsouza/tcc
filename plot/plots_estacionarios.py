from .auxiliares_plot import (
    _plotar_perfis_separados, _plotar_perfis_conc_juntos, _plotar_perfis_juntos
    )


def plotar_perfis_est_separados(FV:list[float], Y:tuple[list, list, list], 
                                salvar:bool=False, path:str="graficos", show:bool=True):
    titulos = []
    axis_labels = []
    props = ["conc_A", "conc_B", "temp"]
    for s in (r"$C_A$"+" [mol/L]", r"$C_B$"+" [mol/L]", "T [°C]"):
        titulos.append("Perfil estacionário de " + s.split(" ")[0] + "(F/V)")
        axis_labels.append(["F/V [" + r"$h^{-1}$" + "]", s])
    _plotar_perfis_separados(props, FV, [Y],
                             colors = ["tab:blue", "tab:orange", "tab:red"], 
                             labels = [""],
                             linestyles = ["-"],
                             titulos = titulos, 
                             axis_labels = axis_labels, 
                             salvar=salvar, path=path, filename="perfil_est", show=show)
           
        
def plotar_perfis_est_conc_juntos(FV:list[float], C:tuple[list, list], 
                                  salvar:bool=False, path:str="graficos", show:bool=True):
    _plotar_perfis_conc_juntos(FV, [C],  # type: ignore
                               colors = ["tab:blue", "tab:orange"],
                               linestyles = ["-"],
                               labels = [[r"$C_{A}$(F/V)", r"$C_{B}$(F/V)"]],
                               titulo = "Perfis estacionários de concentração", 
                               axis_labels = ["F/V [" + r"$h^{-1}$" + "]", "C [mol/L]"],
                               salvar=salvar, path=path, filename="perfis_est_conc", show=show)


def plotar_perfis_est_juntos(X:list[float], Y:tuple[list, list, list], 
                         salvar:bool=False, path:str="graficos", show:bool=True):
    _plotar_perfis_juntos(X, [Y],  # type: ignore
                          colors = ["tab:blue", "tab:orange", "tab:red"],
                          labels = [[r"$C_A$(F/V)", r"$C_B$(F/V)", "T(F/V)"]],
                          linestyles = ["-"],
                          titulos = ["Perfis estacionários de concentração", "Perfis estacionários de temperatura"],
                          axis_labels = [["F/V [" + r"$h^{-1}$" + "]", "C [mol/L]"], ["F/V [" + r"$h^{-1}$" + "]", "T [°C]"]],
                          salvar=salvar, path=path, filename="perfis_estacionarios", show=show)
