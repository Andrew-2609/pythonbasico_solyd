import json


class ApiKey:
    def __init__(self):
        pass

    @staticmethod
    def return_api_key_file():
        try:
            api_key = json.load(open("apiKey.json"))
            return api_key
        except Exception as err:
            print("Ocorreu um erro ao abrir o arquivo:", err)
            exit()
