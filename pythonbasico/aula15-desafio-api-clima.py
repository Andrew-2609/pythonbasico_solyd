import requests
import json
import datetime as dt
from apikey import ApiKey

api_key = ApiKey.return_api_key_file().get("api-clima")


def buscar_informacoes_climaticas(cidade):
    try:
        req = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric&lang=pt_br")
        return json.loads(req.text)
    except Exception as err:
        print(f"Falha na requisição. Erro: {err}")
        exit()


def organizar_e_mostrar_resposta(res):
    print("\n###")
    if not res.get("message"):
        horario_nascer_sol = dt.datetime.utcfromtimestamp(int(res['sys']['sunrise'])).strftime('%H:%M:%S')
        horario_por_sol = dt.datetime.utcfromtimestamp(int(res['sys']['sunset'])).strftime('%H:%M:%S')
        print("Nome oficial da cidade:", res['name'])
        print("País:", res['sys']['country'])
        print("Clima:", str.capitalize(res['weather'][0]['description']))
        print("Temperatura estimada:", str(res['main']['temp']) + "°C")
        print("Sensação térmica:", str(res['main']['feels_like']) + "°C")
        print("Horário do nascer do Sol (UTC):", horario_nascer_sol)
        print("Horário do pôr do Sol (UTC):", horario_por_sol)
    else:
        print(f"Erro {res['cod']}:", str.capitalize(res['message']))
    print("###\n")


if __name__ == '__main__':
    opcao = input("De qual cidade você deseja saber informações climáticas? Digite: ")
    resposta = buscar_informacoes_climaticas(opcao)
    organizar_e_mostrar_resposta(resposta)
