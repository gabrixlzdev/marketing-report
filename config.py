import json

def save_config(config):
    with open("config.json","w") as f:
        json.dump(config,f) #converte um dicionário Python para texto no formato JSON e escreve no arquivo.
    
def load_config():
    try:
        with open("config.json","r") as f:
            config = json.load(f) # lê o texto JSON do arquivo e converte de volta para um dicionário Python.
            return config
    except FileNotFoundError:
        return None
    

