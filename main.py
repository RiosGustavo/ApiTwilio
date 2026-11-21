import os

import requests
#from twilio.rest import Client

#url ="https://api.openweathermap.org/data/2.5/weather?lat=5.0668907&lon=-75.5066661&appid=f33a46f2dad8124e607432d454c824e3"

api_key = os.environ.get("OWM_API_KEY")

auth_token = os.environ.get("AUTH_TOKEN")



parameters = {
    'lat':5.0668907,
    'lon':-75.5066661,
    'appid': "f33a46f2dad8124e607432d454c824e3",
    'cnt':4,
    'units':'metric',

}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
clima_datos = response.json()

print(clima_datos)
#print(response.status_code)
weather_id = clima_datos["list"][0]["weather"][0]["id"]
print(weather_id)

condition_list =[]

for condition in clima_datos["list"]:
    condition_list.append(condition["weather"][0]["id"])

print(condition_list)
# llovera = False
# for hora_data in clima_datos["list"]:
#     condicion_code = hora_data["weather"][0]["id"]
#     if int(condicion_code) < 700:
#         llovera = True

# if llovera:
#     client = Client(account_sid, auth_token)
#     message = client.messages.create(
#         body = "Va a llover hoy no olvides traer paraguas",
#         from ="TUNUMERO",
#         to="NUMEROCLIENTE",
#     )




    #print("traiga paraguas")