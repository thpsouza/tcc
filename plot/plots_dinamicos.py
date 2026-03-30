from .auxiliares_plot import (
    _plotar_perfis_separados, _plotar_perfis_conc_juntos, _plotar_perfis_juntos
    )


def plotar_perfis_din_separados(degrau:str, t:list[float], Y:tuple[tuple[list, list, list], ...], 
                                salvar:bool=False, path:str="graficos", show:bool=True):
    titulos = []
    axis_labels = []
    props = ["conc_A", "conc_B", "temp"]
    for s in (r"$C_A$"+" [mol/L]", r"$C_B$"+" [mol/L]", "T [°C]"):
        aux = s.split(" ")[0]
        titulos.append(fr"Perfil dinâmico de " + aux + "(t)")
        axis_labels.append(["t [$h$]", s])
    aux = "_"+degrau
    if degrau == "pos": y = [Y[0]]
    elif degrau == "neg": y = [Y[1]]
    else:
        y = Y 
        aux = ""
    _plotar_perfis_separados(props, t, y,  # type: ignore
                             colors = ["tab:blue", "tab:orange", "tab:red"], 
                             labels = [r"$b=+5$", r"$b=-5$"] if len(y)>1 else ["", ""], 
                             linestyles = ["-", "--"],
                             titulos = titulos, 
                             axis_labels = axis_labels, 
                             salvar=salvar, path=path, filename=f"perfil_din{aux}", show=show)

        
def plotar_perfis_din_conc_juntos(degrau:str, t:list[float], C:tuple[tuple[list, list], ...],
                                  salvar:bool=False, path:str="graficos", show:bool=True):
    aux = "_"+degrau
    if degrau == "pos": 
        c = [C[0]]
        labels = [[r"$C_A$(t) ($b=+5$)", r"$C_B$(t) ($b=+5$)"]]
    elif degrau == "neg": 
        c = [C[1]]
        labels = [[r"$C_A$(t) ($b=-5$)", r"$C_B$(t) ($b=-5$)"]]
    else:
        c = C 
        aux = ""
        labels = [[r"$C_A$(t) ($b=+5$)", r"$C_B$(t) ($b=+5$)"], 
                  [r"$C_A$(t) ($b=-5$)", r"$C_B$(t) ($b=-5$)"]]
    _plotar_perfis_conc_juntos(t, c, # type: ignore
                               colors = ["tab:blue", "tab:orange"],
                               labels = labels,
                               linestyles = ["-", "--"],
                               titulo = "Perfis dinâmicos de concentração",
                               axis_labels = ["t [$h$]", "C [mol/L]"],
                               salvar=salvar, path=path, filename=f"perfis_din_conc{aux}", show=show)


def plotar_perfis_din_juntos(degrau:str, X:list[float], Y:tuple[tuple[list, list, list], ...], 
                         salvar:bool=False, path:str="graficos", show:bool=True):
    aux = "_"+degrau
    if degrau == "pos": 
        y = [Y[0]]
        labels = [[r"$C_A$(t) ($b=+5$)", r"$C_B$(t) ($b=+5$)" , r"T(t) ($b=+5$)"]]
    elif degrau == "neg": 
        y = [Y[1]]
        labels = [[r"$C_A$(t) ($b=-5$)", r"$C_B$(t) ($b=-5$)" , r"T(t) ($b=-5$)"]]
    else:
        y = Y 
        aux = ""
        labels = [[r"$C_A$(t) ($b=+5$)", r"$C_B$(t) ($b=+5$)", r"T(t) ($b=+5$)"], 
                  [r"$C_A$(t) ($b=-5$)", r"$C_B$(t) ($b=-5$)", r"T(t) ($b=-5$)"]]   
    _plotar_perfis_juntos(X, y,  # type: ignore
                          colors = ["tab:blue", "tab:orange", "tab:red"], 
                          labels = labels,
                          linestyles = ["-", "--"],
                          titulos = ["Perfis dinâmicos de concentração", "Perfis dinâmicos de temperatura"], 
                          axis_labels = [[r"t [$h$]", "C [mol/L]"], [r"t [$h$]", "T [°C]"]],
                          salvar=salvar, path=path, filename=f"perfis_din{aux}", show=show)