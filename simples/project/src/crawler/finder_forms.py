from bs4 import BeautifulSoup

def detectar_formularios(html):
    soup = BeautifulSoup(html,"html.parser")
    forms= soup.find_all("form")

    dados=[]
    for f in forms:
        metodo= f.get("method", "get").upper()
        acao = f.get("action", "")
        inputs= [i.get("name") for i in f.find_all("input")if i.get("name")]

        dados.append({
            "method": metodo,
            "action" : acao,
            "inputs": inputs
        })
        
