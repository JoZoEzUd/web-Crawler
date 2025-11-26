from src.crawler.finder_links import extrair_links
from src.crawler.finder_forms import detectar_formularios
from src.crawler.fingerprint import fingerprint_tecnologias
from src.crawler.directory_scanner import buscar_endpoints
from src.crawler.email_extractor import extrair_emails
from src.utils.requests_wrapper import get_request
from src.utils.file_manager import salvar_relatorio

URL = input("Digite a URL alvo para varredura (LAB SEGURO): ")

print("\n[+] Requisitando página...")
resp = get_request(URL)

print("[+] Extraindo links...")
links = extrair_links(URL, resp.text)

print("[+] Detectando formulários...")
forms = detectar_formularios(resp.text)

print("[+] Fingerprint de tecnologias...")
tec = fingerprint_tecnologias(resp)

print("[+] Buscando endpoints comuns...")
endpoints = buscar_endpoints(URL)

print("[+] Procurando e-mails...")
emails = extrair_emails(resp.text)

print("[+] Salvando relatório...")
dados = {
    "url": URL,
    "links": links,
    "formularios": forms,
    "tecnologias": tec,
    "endpoints": endpoints,
    "emails": emails
}

salvar_relatorio(dados)
print("\nRelatório gerado: relatorio.html")