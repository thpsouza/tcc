# Aprendizado por Reforço aplicado à Sintonia de Controladores Feedback

Este repositório contém os códigos desenvolvidos para meu projeto de **TCC**, que aplica técnicas de **aprendizado por reforço (reinforcement learning)** para otimizar a sintonia de controladores PID/feedback em processos químicos.

O processo utilizado como benchmark para essa aplicação será o **Reator de Van de Vusse** (sistema não-linear, composto por reações paralelas).

## ⚖️ Modelagem:
A cinética do processo é descrita pelo esquema reacional abaixo:

$$
\begin{aligned}
    &\text{A} ~ \xrightarrow{k_1} ~ \text{B} ~ \xrightarrow{k_2} ~ \text{C} 
    \\
    2~&\text{A} ~ \xrightarrow{k_3} ~ \text{D}
\end{aligned}
$$

Os balanços molares para o reagente (A) e o produto de interesse (B):

$$
\begin{align}
    \frac{dC_A}{dt} &= \frac{F}{V}\left(C_{A0} - C_A \right)- k_1(T) C_A - k_3(T) {C_A}^2
    \\
    \frac{dC_B}{dt} &= -\frac{F}{V} C_B + k_1(T)C_A - k_2(T)C_B
\end{align}
$$

O balanço de energia no reator:

$$
\begin{equation}
    \begin{aligned}
        \frac{dT}{dt} &= \dfrac{1}{\rho ~c_p} \biggl[k_1(T)C_A(-\Delta{H_{R,AB}}) \\ 
        &~~\qquad + k_2(T)C_B(-\Delta{H_{R,BC}}) \\ 
        &~~\qquad + k_3(T){C_A}^2(-\Delta{H_{R,AD}}) \biggr] \\
        &~~\qquad + \dfrac{F}{V}\left(T_0 - T\right) + \dfrac{K_W A_R}{\rho ~c_p~V} \left(T_K - T\right) 
    \end{aligned}
\end{equation}
$$


A implementação da modelagem pode ser encontrada em [modelagem](modelagem). Os dados podem ser encontrados em [modelagem/parametros_van_de_vusse.py](modelagem/parametros_van_de_vusse.py).

## 📝 Documentação:
Para informações completas sobre o processo, como parâmetros, cinética de reação e comportamento dinâmico, consulte [docs/main.pdf](docs/main.pdf).


## 📁 Estrutura do Repositório
```bash
├── main.py                # Script principal
├── docs/                  # Documentação técnica e PDFs
├── modelagem/             # Modelos matemáticos e parâmetros
├── simulador/             # Pequeno simulador do processo
├── plot/                  # Funções para geração de gráficos
└── utils/                 # Utilitários
    └── SistemaUnidades\     # Análise dimensional
```

## 👤 Autor:
**Thiago Pacheco de Souza**

*Este projeto foi desenvolvido como Trabalho de Conclusão de Curso da minha Graduação em Engenharia Química.*

---

*Último atualizado: Março de 2026*
