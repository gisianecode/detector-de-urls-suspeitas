import tkinter as tk

def analisar_url():

    url = entrada.get().lower().strip()

    if not url:
        texto_resultado.config(
            text="⚠ Digite uma URL para analisar."
        )
        return

    score = 0
    motivos = []

    palavras_suspeitas = [
        "login",
        "verify",
        "secure",
        "bank",
        "update",
        "free",
        "bonus",
        "pix",
        "paypal",
        "facebook",
        "instagram",
        "senha",
        "account",
        "support"
    ]

    # HTTPS
    if not url.startswith("https://"):
        score += 30
        motivos.append("Não utiliza HTTPS")

    # Palavras suspeitas
    for palavra in palavras_suspeitas:
        if palavra in url:
            score += 10
            motivos.append(f"Contém palavra suspeita: {palavra}")

    # URL muito longa
    if len(url) > 40:
        score += 20
        motivos.append("URL muito longa")

    # Caracteres suspeitos
    if "@" in url:
        score += 20
        motivos.append("Possui caractere @")

    # Muitos hífens
    if url.count("-") >= 3:
        score += 10
        motivos.append("Possui muitos hífens")

    # Classificação
    if score >= 60:
        resultado = "🚨 ALTO RISCO"

    elif score >= 30:
        resultado = "⚠ URL SUSPEITA"

    else:
        resultado = "✅ URL APARENTEMENTE SEGURA"

    if not motivos:
        motivos.append("Nenhum indício suspeito encontrado")

    texto_resultado.config(
        text=
        f"{resultado}\n\n"
        f"Pontuação de risco: {score}\n\n"
        f"Motivos:\n" +
        "\n".join(motivos)
    )


# Janela principal
janela = tk.Tk()
janela.title("Detector de URLs Suspeitas")
janela.geometry("700x500")

# Título
titulo = tk.Label(
    janela,
    text="🔐 Detector de URLs Suspeitas",
    font=("Arial", 18, "bold")
)

titulo.pack(pady=15)

# Descrição
descricao = tk.Label(
    janela,
    text="Digite uma URL para verificar possíveis indícios de phishing.",
    font=("Arial", 10)
)

descricao.pack()

# Campo de entrada
entrada = tk.Entry(
    janela,
    width=70,
    font=("Arial", 12)
)

entrada.pack(pady=15)

# Botão
botao = tk.Button(
    janela,
    text="Analisar URL",
    command=analisar_url,
    font=("Arial", 12)
)

botao.pack(pady=10)

# Resultado
texto_resultado = tk.Label(
    janela,
    text="",
    justify="left",
    font=("Arial", 11),
    wraplength=650
)

texto_resultado.pack(pady=20)

# Executar aplicação
janela.mainloop()