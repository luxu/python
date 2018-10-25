import requests

url = "http://www.ferendum.com/pt/votarpost3.php"

def proxy():
    url = "http://gimmeproxy.com/api/getProxy?protocol=http"
    r = requests.get(url).json()
    return {
        r['protocol']:r['curl']
    }

while True:
    proxies = proxy()
    data = {
        "record3":"",
        "record4":"",
        "pregunta_ID":169927,
        "sec_digit":75613,
        "config_anonimo":1,
        "config_aut_req":0,
        "titulo":"PRA+QUEM+VOCÊ+VOTARIA+HOJE?",
        "votos_array":873398,
        "submit_votacion":"Enviar"
    }
    try:
        r = requests.post(url,data=data,proxies=proxies)
        print(r.status_code)
        if "Obrigado por participar desta enquente de Ferendum.com!" in r.content:
            print("Voto realizado com sucesso!")
    except Exception as e:
        print("Deu ruim!{}".format(e))
        False
