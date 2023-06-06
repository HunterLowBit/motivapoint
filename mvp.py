import tkinter as tk

# Variáveis de vendas de cada vendedor e pontuação
vendas_vendedores = {
    1: 0,
    2: 0,
    3: 0
}

pontuacao_vendedores = {
    1: 0,
    2: 0,
    3: 0
}

# Variáveis de compras de cada cliente e pontuação
compras_clientes = {
    1: 0,
    2: 0,
    3: 0
}

pontuacao_clientes = {
    1: 0,
    2: 0,
    3: 0
}

# Função para abrir a janela de vendedores
def abrir_janela_vendedores():
    vendedores_window = tk.Toplevel(root)
    vendedores_window.title("Vendedores")

    # Função para registrar venda do vendedor
    def registrar_venda(vendedor):
        valor_venda = float(venda_entry.get())
        vendas_vendedores[vendedor] += valor_venda
        pontos = int(valor_venda / 100)  # Calcula a quantidade de pontos
        pontuacao_vendedores[vendedor] += pontos
        resultado_label.config(text="Venda registrada com sucesso.")

    # Função para exibir o total de vendas e pontuação dos vendedores
    def exibir_total_vendas():
        total_vendas = sum(vendas_vendedores.values())
        resultado_label.config(text=f"Total de vendas:\n")
        for vendedor, vendas in vendas_vendedores.items():
            resultado_label.config(text=resultado_label.cget("text") + f"Vendedor {vendedor}: R${vendas:.2f}\n")
        resultado_label.config(text=resultado_label.cget("text") + f"Total: R${total_vendas:.2f}")

        resultado_label.config(text=resultado_label.cget("text") + "\n\nPontuação dos vendedores:\n")
        for pontos_vend, pontuacao in pontuacao_vendedores.items():
            resultado_label.config(text=resultado_label.cget("text") + f"Vendedor {pontos_vend}: {pontuacao} pontos\n")

    # Função para sair da janela de vendedores
    def sair_janela_vendedores():
        vendedores_window.destroy()

    # Cria os widgets da interface gráfica da janela de vendedores
    menu_label = tk.Label(vendedores_window, text="Escolha uma opção:")
    menu_label.pack()

    vendedor_var = tk.StringVar()

    opcao_radio1 = tk.Radiobutton(vendedores_window, text="Registrar venda do vendedor 1", variable=vendedor_var, value="1")
    opcao_radio1.pack()

    opcao_radio2 = tk.Radiobutton(vendedores_window, text="Registrar venda do vendedor 2", variable=vendedor_var, value="2")
    opcao_radio2.pack()

    opcao_radio3 = tk.Radiobutton(vendedores_window, text="Registrar venda do vendedor 3", variable=vendedor_var, value="3")
    opcao_radio3.pack()

    venda_label = tk.Label(vendedores_window, text="Valor da venda:")
    venda_label.pack()

    venda_entry = tk.Entry(vendedores_window)
    venda_entry.pack()

    registrar_button = tk.Button(vendedores_window, text="Registrar", command=lambda: registrar_venda(int(vendedor_var.get())) if vendedor_var.get() in ["1", "2", "3"] else None)
    registrar_button.pack()

    exibir_button = tk.Button(vendedores_window, text="Exibir Total", command=exibir_total_vendas)
    exibir_button.pack()

    resultado_label = tk.Label(vendedores_window, text="")
    resultado_label.pack()

    sair_button = tk.Button(vendedores_window, text="Sair", command=sair_janela_vendedores)
    sair_button.pack()


# Função para abrir a janela de clientes
def abrir_janela_clientes():
    clientes_window = tk.Toplevel(root)
    clientes_window.title("Clientes")

    # Função para registrar compra do cliente
    def registrar_compra(cliente):
        valor_compra = float(compra_entry.get())
        compras_clientes[cliente] += valor_compra
        pontos = int(valor_compra / 100)  # Calcula a quantidade de pontos
        pontuacao_clientes[cliente] += pontos
        resultado_label.config(text="Compra registrada com sucesso.")

    # Função para exibir o total de compras e pontuação dos clientes
    def exibir_total_compras():
        total_compras = sum(compras_clientes.values())
        resultado_label.config(text=f"Total de compras:\n")
        for cliente, compras in compras_clientes.items():
            resultado_label.config(text=resultado_label.cget("text") + f"Cliente {cliente}: R${compras:.2f}\n")
        resultado_label.config(text=resultado_label.cget("text") + f"Total: R${total_compras:.2f}")

        resultado_label.config(text=resultado_label.cget("text") + "\n\nPontuação dos clientes:\n")
        for cliente, pontos in pontuacao_clientes.items():
            resultado_label.config(text=resultado_label.cget("text") + f"Cliente {cliente}: {pontos} pontos\n")

    # Função para sair da janela de clientes
    def sair_janela_clientes():
        clientes_window.destroy()

    # Cria os widgets da interface gráfica da janela de clientes
    menu_label = tk.Label(clientes_window, text="Escolha uma opção:")
    menu_label.pack()

    cliente_var = tk.StringVar()

    opcao_radio1 = tk.Radiobutton(clientes_window, text="Registrar compra do cliente 1", variable=cliente_var, value="1")
    opcao_radio1.pack()

    opcao_radio2 = tk.Radiobutton(clientes_window, text="Registrar compra do cliente 2", variable=cliente_var, value="2")
    opcao_radio2.pack()

    opcao_radio3 = tk.Radiobutton(clientes_window, text="Registrar compra do cliente 3", variable=cliente_var, value="3")
    opcao_radio3.pack()

    compra_label = tk.Label(clientes_window, text="Valor da compra:")
    compra_label.pack()

    compra_entry = tk.Entry(clientes_window)
    compra_entry.pack()

    registrar_button = tk.Button(clientes_window, text="Registrar", command=lambda: registrar_compra(int(cliente_var.get())) if cliente_var.get() in ["1", "2", "3"] else None)
    registrar_button.pack()

    exibir_button = tk.Button(clientes_window, text="Exibir Total", command=exibir_total_compras)
    exibir_button.pack()

    resultado_label = tk.Label(clientes_window, text="")
    resultado_label.pack()

    sair_button = tk.Button(clientes_window, text="Sair", command=sair_janela_clientes)
    sair_button.pack()


# Cria a janela principal
root = tk.Tk()
root.title("MOTIVAPOINT")
root.geometry("400x400")

# Cria os widgets da interface gráfica da janela principal
titulo_label = tk.Label(root, text="MOTIVAPOINT")
titulo_label.pack()

vendedores_button = tk.Button(root, text="Vendedores", command=abrir_janela_vendedores)
vendedores_button.pack()

clientes_button = tk.Button(root, text="Clientes", command=abrir_janela_clientes)
clientes_button.pack()

sair_button = tk.Button(root, text="Sair", command=root.destroy)
sair_button.pack()

# Inicia o loop principal da interface gráfica
root.mainloop()
