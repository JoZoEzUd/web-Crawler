import re

def extrair_emails(text):
    return list(set(re.findall(r"[A-Za-z0-9.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)))
