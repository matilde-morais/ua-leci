import requests

resp = requests.get("https://www.rfc-editor.org/rfc/rfc16.html")
print("resp.text:\n", resp.text[:300]) # neste caso, o servidor retorna os primeiros 300 caracteres do html
# .text é um atributo que retorna o conteúdo da resposta como uma string unicode