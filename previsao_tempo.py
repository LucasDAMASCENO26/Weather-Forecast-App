import tkinter as tk
from tkinter import messagebox
import requests
from datetime import datetime

# Função para buscar a previsão do tempo
def buscar_previsao():
    cidade = entrada_cidade.get()
    if not cidade:
        messagebox.showwarning("Input Error", "Por favor, insira o nome da cidade.")
        return
    
    API_KEY = "73779b476ce79a4493f80eb2c081d39b"
    link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

    requisicao = requests.get(link)
    requisicao_dic = requisicao.json()

    if requisicao.status_code != 200:
        messagebox.showerror("API Error", f"Erro ao buscar dados: {requisicao_dic.get('message', 'Erro desconhecido')}")
        return

    descricao = requisicao_dic['weather'][0]['description']
    temperatura = requisicao_dic['main']['temp'] - 273.15
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    cidade_nome = requisicao_dic['name']
    dia_ou_noite = "Dia" if requisicao_dic['weather'][0]['icon'].endswith('d') else "Noite"

    resultado_texto = (
        f"Data e Hora: {data_hora}\n"
        f"Cidade: {cidade_nome}\n"
        f"Período: {dia_ou_noite}\n"
        f"Temperatura: {temperatura:.1f}°C\n"
        f"Descrição: {descricao}"
    )
    label_resultado.config(text=resultado_texto)

# Função para atualizar a data e hora no layout inicial
def atualizar_data_hora():
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    label_data_hora.config(text=f"Data e Hora: {data_hora}")
    root.after(1000, atualizar_data_hora)

# Configuração da janela principal
root = tk.Tk()
root.title("Previsão do Tempo")
root.geometry("500x600")
root.configure(bg='#E0F7FA')

# Layout inicial
frame_inicio = tk.Frame(root, padx=20, pady=20, bg='#B2EBF2', bd=5, relief='raised')
frame_inicio.pack(pady=10, fill=tk.BOTH, expand=True)

label_programa = tk.Label(frame_inicio, text="Previsão do Tempo", font=("Helvetica", 24, "bold"), bg='#B2EBF2')
label_programa.pack(pady=10)

label_autor = tk.Label(frame_inicio, text="Criado por Lucas", font=("Helvetica", 16), bg='#B2EBF2')
label_autor.pack(pady=5)

label_data_hora = tk.Label(frame_inicio, font=("Helvetica", 14), bg='#B2EBF2')
label_data_hora.pack(pady=10)
atualizar_data_hora()

label_cidade = tk.Label(frame_inicio, text="Digite o nome da cidade:", font=("Helvetica", 14), bg='#B2EBF2')
label_cidade.pack(pady=5)

entrada_cidade = tk.Entry(frame_inicio, font=("Helvetica", 14), width=30)
entrada_cidade.pack(pady=5)

botao_buscar = tk.Button(frame_inicio, text="Buscar Previsão", font=("Helvetica", 14), command=buscar_previsao, bg='#00ACC1', fg='white')
botao_buscar.pack(pady=20)

# Layout de resultado
frame_resultado = tk.Frame(root, padx=20, pady=20, bg='#B2EBF2', bd=5, relief='raised')
frame_resultado.pack(pady=10, fill=tk.BOTH, expand=True)

label_resultado = tk.Label(frame_resultado, font=("Helvetica", 14), justify="left", bg='#B2EBF2')
label_resultado.pack(pady=10)

# Inicializa a interface
root.mainloop()
