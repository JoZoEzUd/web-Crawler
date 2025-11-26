import requests

COMMON_PATHS = [
    "admin", "login", "dashboard", "api",
    "uploads", "backup", "private", "config"
]

def buscar_endpoints(base_url):
    encontrados = []

    for p in COMMON_PATHS:
        url = base_url.rstrip("/") + "/" + p
        try:
            r = requests.get(url, timeout=4)
            if r.status_code == 200:
                encontrados.append(url)
        except:
            pass

    return encontrados