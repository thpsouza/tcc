import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.axes import Axes


def _plotar(axis:Axes, X:list[float]|np.ndarray, Y:list[float]|np.ndarray, 
           label:str, color:str|None=None, linestyle:str="-",
           title:str="", axis_labels:list[str]|None=None) -> None:
    axis.plot(X, Y, label=label, alpha=0.8, color=color, linestyle=linestyle)
    axis.minorticks_on()
    axis.grid(which='major', linestyle='-', linewidth=0.75, alpha=0.8)
    axis.grid(which='minor', linestyle=':', linewidth=0.75, alpha=0.8)        
    if title:
        axis.set_title(title, fontsize=13)
    if axis_labels:
        axis.set_xlabel(axis_labels[0], fontsize=12)
        axis.set_ylabel(axis_labels[1], fontsize=12)
    if label:
        axis.legend(fontsize=12, frameon=True, framealpha=0.6, loc="center right")


def _plotar_perfis_separados(props:list[str], X:list[float]|np.ndarray, Y:list[list]|list, 
                             colors:list[str], labels:list[str], linestyles:list[str]|list,
                             titulos:list[str], axis_labels:list[list[str]],
                             salvar:bool=False, path:str="graficos", filename:str="perfil", show:bool=True):   
    for j in range(len(Y[0])): #3
        fig, ax = plt.subplots(figsize=(7, 6))
        for i in range(len(Y)): #2
            _plotar(
                ax, 
                X, Y[i][j],
                label = labels[i],
                color = colors[j],
                linestyle = linestyles[i],
                title = titulos[j],
                axis_labels = axis_labels[j]
                )
    
        if salvar:
            plt.savefig(f"{path}/{filename}_{props[j]}.pdf")
            print(f"Grafico salvo em: {os.path.abspath(f"{path}/{filename}_{props[j]}.pdf")}")
        if show:
            plt.show()


def _plotar_perfis_conc_juntos(X:list[float]|np.ndarray, Y:list[list], 
                               colors:list[str], labels:list[list[str]], linestyles:list[str],
                               titulo:str, axis_labels:list[str], salvar:bool=False, 
                               path:str="graficos", filename:str="perfil", show:bool=True):
    fig, ax = plt.subplots(figsize=(7, 6))
    for j in range(len(Y[0])):
        for i in range(len(Y)):
            _plotar(
                ax, 
                X, Y[i][j],
                label = labels[i][j],
                color = colors[j],
                linestyle = linestyles[i],
                title = titulo,
                axis_labels = axis_labels
                )
    if salvar:
        plt.savefig(f"{path}/{filename}.pdf")
        print(f"Grafico salvo em: {os.path.abspath(f"{path}/{filename}.pdf")}")
    if show:
        plt.show()


def _plotar_perfis_juntos(X:list[float], Y:list[list],  
                          colors:list[str], labels:list[list[str]], linestyles:list[str],
                          titulos:list[str], axis_labels:list[list[str]],
                          salvar:bool=False, path:str="graficos", 
                          filename:str="perfil", show:bool=True):
    fig, ax = plt.subplots(ncols=2, figsize=(14, 6))
    for j in range(len(Y[0]) - 1): #3
        for i in range(len(Y)): #2
            _plotar(
                ax[0], 
                X, Y[i][j],
                label = labels[i][j],
                color = colors[j],
                linestyle = linestyles[i],
                title = titulos[0],
                axis_labels = axis_labels[0]
                )
    for k in range(len(Y)): #2
        _plotar(
            ax[1], 
            X, Y[k][2],
            label = labels[k][2],
            color = colors[2],
            linestyle = linestyles[k],
            title = titulos[1],
            axis_labels = axis_labels[1]
            )
    if salvar:
        plt.savefig(f"{path}/{filename}.pdf")
        print(f"Grafico salvo em: {os.path.abspath(f"{path}/{filename}.pdf")}")
    if show:
        plt.show()