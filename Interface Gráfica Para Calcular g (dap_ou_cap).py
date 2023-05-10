## Interface Gráfica Para Calcular a área seccional à altura do peito (g) 
###com base no valor do diâmetro à altura do peito (DAP) 
###com base no valor da circunferência à altura do peito (CAP)

##Importando as bibliotecas
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import math

##Definindo as formulas 
def dap_to_cap(dap):
    cap = dap * math.pi
    return cap

def cap_to_dap(cap):
    dap = cap / math.pi
    return dap

def calculate_g():
    value = float(value_entry.get())
    unit = unit_variable.get()
    calculation_type = calculation_variable.get()

    try:
        if calculation_type == "dap_to_g":
            if unit == "cm":
                value /= 100  # Converter para metros se estiver em centímetros
            g = (math.pi * value**2) / 4
        else:  # calculation_type == "cap_to_g"
            if unit == "cm":
                value /= 100  # Converter para metros se estiver em centímetros
            dap = cap_to_dap(value)
            g = (math.pi * dap**2) / 4

        result_label.config(text=" Resultado da Área seccional à altura do Peito: {:.4f} m²".format(round(g, 4)))
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor numérico válido.")

def switch_calculation():
    current_calculation_type = calculation_variable.get()

    if current_calculation_type == "dap_to_g":
        calculation_variable.set("cap_to_g")
        value_label.config(text="CAP:")
        instructions_label.config(text="Insira o valor do CAP em metros ou centímetros:")
    else:  # current_calculation_type == "cap_to_g"
        calculation_variable.set("dap_to_g")
        value_label.config(text="DAP:")
        instructions_label.config(text="Insira o valor do DAP em metros ou centímetros:")

# Criação da janela principal
window = tk.Tk()
window.title("calculadora de área seccional à altura do peito")

# Criação do Notebook
notebook = ttk.Notebook(window)
notebook.grid(row=0, column=0, columnspan=2, sticky="nswe", padx=10, pady=10)


# Criação da aba de instruções
instructions_frame = ttk.Frame(notebook)
notebook.add(instructions_frame, text="Instruções")

instructions_text = """
1. Bem-vindo à calculadora de área seccional à altura do peito (g)!
2. Na interface, você encontrará os seguintes elementos:
   - Um botão chamado "Alternar Cálculo": este botão permite alternar entre os tipos de cálculo disponíveis.
   - Um rótulo indicando "DAP": este rótulo mostra o tipo de valor que você deve inserir.
   - Uma caixa de entrada: aqui você pode digitar o valor do DAP ou CAP da árvore.
   - Um rótulo chamado "Unidade": você pode selecionar a unidade de medida desejada (metros ou centímetros).
   - Um botão "Calcular": clique neste botão para obter o resultado da área seccional à altura do peito.
   - Uma etiqueta de resultado: aqui será exibido o resultado do cálculo.
3. Antes de realizar qualquer cálculo, certifique-se de inserir valores numéricos válidos.
   - Atenção: Utilize ponto(.) como separador decimal. Ex: 1.2 ou 0.5
4. Para começar, insira o valor do DAP (diâmetro à altura do peito) ou CAP (circunferência à altura do peito) na caixa de entrada.
5. Escolha a unidade de medida desejada (metros ou centímetros) no menu suspenso "Unidade".
6. Se você quiser calcular a área seccional à altura do peito com base no DAP, basta deixar a opção selecionada como "DAP" e digitar o valor correspondente na caixa de entrada.
7. Se preferir calcular a área seccional à altura do peito com base no CAP, clique no botão "Alternar Cálculo". O rótulo mudará para "CAP" e você poderá inserir o valor correspondente.
8. Após inserir o valor e selecionar a unidade correta, clique no botão "Calcular".
9. O resultado da área seccional à altura do peito será exibido na etiqueta de resultado.
10. Se você cometer algum erro ao inserir os valores, uma mensagem de erro será exibida para ajudá-lo a corrigir a entrada.
11. Divirta-se usando a calculadora de área seccional à altura do peito e aproveite os cálculos!

Certifique-se de seguir as instruções cuidadosamente para obter resultados precisos.
"""

instructions_label = tk.Label(instructions_frame, text=instructions_text, justify='left')
instructions_label.pack(padx=5, pady=5)

# Criação dos widgets da interface

calculation_switch_button = tk.Button(window, text="Alternar Cálculo", command=switch_calculation)
calculation_switch_button.grid(row=1, column=0, sticky="nswe", padx=10, pady=10)

instructions_label = tk.Label(window, text="Insira o valor do DAP em metros ou centímetros:")
instructions_label.grid(row=1, column=1, sticky="nswe", padx=10, pady=10)

value_label = tk.Label(window, text="DAP:")
value_label.grid(row=2, column=0,sticky="nswe", padx=10, pady=5)

value_entry = tk.Entry(window, justify="center")
value_entry.grid(row=2, column=1,sticky="nswe", padx=10, pady=5)

unit_label = tk.Label(window, text="Unidade:")
unit_label.grid(row=3, column=0,sticky="nswe", padx=10, pady=5)

unit_variable = tk.StringVar(window)
unit_variable.set("m")  # Valor padrão

unit_optionmenu = tk.OptionMenu(window, unit_variable, "m", "cm")
unit_optionmenu.grid(row=3, column=1,sticky="nswe", padx=10, pady=10)

calculation_variable = tk.StringVar(window)
calculation_variable.set("dap_to_g")  # Valor padrão

calculate_button = tk.Button(window, text="Calcular", command=calculate_g)
calculate_button.grid(row=4, column=0,columnspan=2,sticky="nswe", padx=10, pady=5)

result_label = tk.Label(window, text="")
result_label.grid(row=5, column=0, columnspan=2,sticky="nswe", padx=10, pady=10)

referenc_label = tk.Label(window, text="""Autor: Eng. Florestal Luis Henrique de Araújo Gouvêa""",justify='center')
referenc_label.grid(row=6, column=1,sticky="nswe", padx=10, pady=5)

# Inicialização da janela principal
window.mainloop()
