def fingerprint_tecnologias(resp):
    tec=[]

    server = resp.headers.get("Server", "" )
    powered = resp.headers.get("x-Powered-By", "")
    html = resp.text

    if "PHP" in powered:
        tec.append("PHP")
    if "WordPress" in html:
        tec.append("WordPress")
    if "Laravel" in html:
        tec.append("Larave")
    if "Django" in html:
        tec.append("Django")
    if "Node" in html:
        tec.append("Node")
    if "Apache" in html:
        tec.append("Apache")
    if "nginx" in html:
        tec.append("NGINX")
    return tec
    