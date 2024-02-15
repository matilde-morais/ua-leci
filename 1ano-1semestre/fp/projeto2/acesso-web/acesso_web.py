import requests

resp = requests.get("https://www.rfc-editor.org/rfc/rfc16.txt")
print("resp.status_code:", resp.status_code)  # deve ser 200
print("resp.text:\n", resp.text)