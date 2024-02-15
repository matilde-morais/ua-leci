Necessário fazer a instalação do módulo requests:
LINUX:
sudo apt install python3-pip
pip3 install requests
WINDOWS:
pip install requests


Necessário fazer a instalação da biblioteca timezonefinder:
LINUX:
sudo apt install python3-pip
pip3 install timezonefinder
WINDOWS:
pip install timezonefinder


Caso esteja a trabalhar no ambiente LINUX, não é necessário fazer mais nada.
Caso esteja a trabalhar no ambiente WINDOWS, é necessário ainda, na função useAgain, comentar a 1ª e descomentar a 2ª:
os.system('clear') # linha 332
# os.system('cls') # linha 334
