def salvar_relatorio(dados, arquivo="relatorio.html"):
    html = f"""
    <html>
    <head>
        <title>Relatório do Crawler</title>
        <style>
            body {{ font-family: Arial; background: #111; color: #eee; padding: 20px; }}
            h1 {{ color: #4CAF50; }}
            pre {{ background: #222; padding: 15px; border-radius: 10px; }}
        </style>
    </head>
    <body>
        <h1>Relatório de Varredura</h1>
        <pre>{dados}</pre>
    </body>
    </html>
    """

    with open(arquivo, "w", encoding="utf-8") as f:
        f.write(html)