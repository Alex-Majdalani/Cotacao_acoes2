import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import yfinance as yf


# Função que será chamada quando o botão "Enviar" for pressionado
def submit():
    ticker = entry_ticker.get()
    data_inic = entry_data_inic.get()
    data_term = entry_data_term.get()

    # Validação dos dados (opcional)
    if not ticker:
        messagebox.showerror("Erro", "Por favor, insira o código da ação.")
        return
    if not data_inic or not data_term:
        messagebox.showerror("Erro", "Por favor, insira ambas as datas.")
        return

    try:
        # Obter dados históricos da ação
        dados = yf.download(ticker, start=data_inic, end=data_term)
        if dados.empty:
            messagebox.showerror("Erro", "Nenhum dado encontrado para o período especificado.")
            return

        # Cálculo dos preços máximo, mínimo e médio
        preco_max = dados['High'].max()
        preco_min = dados['Low'].min()
        preco_medio = dados['Close'].mean()

        # Exibir os resultados
        label_resultado.config(text=f"Preço Máximo: {preco_max:.2f}\nPreço Mínimo: {preco_min:.2f}\nPreço Médio: {preco_medio:.2f}")

    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao obter os dados: {e}")

# Criação da janela principal
root = tk.Tk()
root.title("Mercado Financeiro")
root.geometry("500x700")
root.configure(bg='#2e2e2e')

# Título
label_titulo = tk.Label(root, text="Bolsa de Valores BR", bg='#2e2e2e', fg='white', font=("Helvetica", 16))
label_titulo.pack(pady=10)

# Imagem de fundo
canvas = tk.Canvas(root, width=200, height=100)
canvas.pack()

# Carregar a imagem de fundo
imagem_fundo = Image.open("D:/Python/Projetos/MERCADO FINANCEIRO/Cotacao_acoes/obybox.png")
imagem_fundo = imagem_fundo.resize((200, 100), Image.LANCZOS)
bg_image = ImageTk.PhotoImage(imagem_fundo)

# Adicionar a imagem de fundo ao canvas
canvas.create_image(0, 0, anchor=tk.NW, image=bg_image)

# Frame para os campos de entrada
frame = tk.Frame(root, bg='#2e2e2e')
frame.pack(pady=20)

label_ticker = tk.Label(frame, text="Código da Ação:", bg='#2e2e2e', fg='white')
label_ticker.grid(row=0, column=0, padx=10, pady=10)

entry_ticker = tk.Entry(frame, bg='#4d4d4d', fg='white')
entry_ticker.grid(row=0, column=1, padx=10, pady=10)

label_data_inic = tk.Label(frame, text="Início do Período (aaaa-mm-dd):", bg='#2e2e2e', fg='white')
label_data_inic.grid(row=1, column=0, padx=10, pady=10)

entry_data_inic = tk.Entry(frame, bg='#4d4d4d', fg='white')
entry_data_inic.grid(row=1, column=1, padx=10, pady=10)

label_data_term = tk.Label(frame, text="Término do Período (aaaa-mm-dd):", bg='#2e2e2e', fg='white')
label_data_term.grid(row=2, column=0, padx=10, pady=10)

entry_data_term = tk.Entry(frame, bg='#4d4d4d', fg='white')
entry_data_term.grid(row=2, column=1, padx=10, pady=10)

# Criação do botão "Enviar"
button_submit = tk.Button(frame, text="Enviar", command=submit, bg='#4d4d4d', fg='white')
button_submit.grid(row=3, columnspan=2, pady=20)

# Criação do rótulo para exibir os resultados
label_resultado = tk.Label(root, text="", bg='#2e2e2e', fg='white')
label_resultado.pack(pady=10)

# Execução da janela principal
root.mainloop()