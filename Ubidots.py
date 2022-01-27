import time
import requests
from tkinter import * 
def funcTemp():
    getTemp=vTemp.get()
    printTemp=Label(app,text="Temperatura:                    ")
    printTemp.place(x=160,y=105)
    textTemp="Temperatura: "+getTemp
    printTemp=Label(app,text=textTemp)
    printTemp.place(x=160,y=105)
    app.update()
    chamar()
    vTemp.delete(0,END)
def funcUmidade():
    getUmidade=vUmidade.get()
    printUmidade=Label(app,text="Umidade:                    ")
    printUmidade.place(x=160,y=122)
    textUmidade="Umidade: "+getUmidade
    printUmidade=Label(app,text=textUmidade)
    printUmidade.place(x=160,y=122)
    app.update()
    chamar()
    vUmidade.delete(0,END)
def funcVel():
    getVelocidade=getDado("velocidade")
    printVelocidade=Label(app,text="Velocidade:                    ")
    printVelocidade.place(x=160,y=139)
    textVelocidade="Velocidade: "+getVelocidade
    printVelocidade=Label(app,text=textVelocidade)
    printVelocidade.place(x=160,y=139)
    app.update()
def funcAceleracao():
    getAceleracao=getDado("aceleracao")
    printAceleracao=Label(app,text="Aceleração:                    ")
    printAceleracao.place(x=160,y=156)
    textAceleracao="Aceleração: "+getAceleracao
    printAceleracao=Label(app,text=textAceleracao)
    printAceleracao.place(x=160,y=156)
    app.update()
def getDado():
    headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}
    getVelocidade=requests.get(url="https://industrial.api.ubidots.com/api/v1.6/devices/teste2/velocidade/lv",headers=headers)
    printVelocidade=Label(app,text="Velocidade:                    ")
    printVelocidade.place(x=160,y=139)
    textVelocidade="Velocidade: "+str(getVelocidade.text)
    printVelocidade=Label(app,text=textVelocidade)
    printVelocidade.place(x=160,y=139)
    print("Velocidade: "+getVelocidade.text)
    getAceleracao=requests.get(url="https://industrial.api.ubidots.com/api/v1.6/devices/teste2/aceleracao/lv",headers=headers)
    printAceleracao=Label(app,text="Aceleração:                    ")
    printAceleracao.place(x=160,y=156)
    textAceleracao="Aceleração: "+str(getAceleracao.text)
    printAceleracao=Label(app,text=textAceleracao)
    printAceleracao.place(x=160,y=156)
    print("Aceleração: "+getAceleracao.text)
def build_payload(temperatura,umidade,valorTemp,valorUmidade):
    payload = {temperatura: valorTemp,
               umidade: valorUmidade}
    return payload
def post_request(payload):
    # Creates the headers for the HTTP requests
    url = "http://industrial.api.ubidots.com"
    url = "{}/api/v1.6/devices/{}".format(url, DEVICE_LABEL)
    headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}
    # Makes the HTTP requests
    status = 400
    attempts = 0
    while status >= 400 and attempts <= 5:
        req = requests.post(url=url, headers=headers, json=payload)
        status = req.status_code
        attempts += 1
        time.sleep(1)
    # Processes results
    print(req.status_code, req.json())
    if status >= 400:
        print("[ERROR] Não foi possível enviar dados após 5 tentativas, verifique \
             suas credenciais de token e conexão com a Internet")
        return False
    print("[INFO] Solicitação feita corretamente, seu device está atualizado")
    return True
def chamar():
    payload = build_payload(
        VARIABLE_LABEL_1, VARIABLE_LABEL_2,vTemp.get(),vUmidade.get())
    print("[INFO] Tentando enviar dados")
    post_request(payload)
    print("[INFO] Concluido")
TOKEN="*********************************"  # Put your TOKEN here
DEVICE_LABEL="teste2"  # Put your device label here 
VARIABLE_LABEL_1="temperatura"  # Put your first variable label here
VARIABLE_LABEL_2="umidade"  # Put your second variable label here
VARIABLE_LABEL_3="velocidade"  # Put your second variable label here
VARIABLE_LABEL_4="aceleracao"
app = Tk()
app.title("Ubidots")
app.geometry("320x250")
getTemp=StringVar()
getUmidade=StringVar()
quadroEnviar = LabelFrame(app, text = "Enviar informações")
quadroEnviar.place(x=5,y=0,width=150,height=210)
lbTemp = Label(quadroEnviar, text = "Temperatura")
lbTemp.place(x = 0, y = 0)
vTemp = Entry(quadroEnviar)
vTemp.place(x = 10, y = 25)
lbUmidade = Label(quadroEnviar, text = "Umidade")
lbUmidade.place(x = 0,y = 95)
vUmidade = Entry(quadroEnviar)
vUmidade.place(x = 10,y = 115)
btnEnviar1 = Button(quadroEnviar, text = "Enviar", fg="blue",command=funcTemp)
btnEnviar2 = Button(quadroEnviar, text  = "Enviar", fg="blue",command=funcUmidade)
btnEnviar1.place(x = 5,y = 55)
btnEnviar2.place(x=5,y=145)
quadroPegar = LabelFrame(app, text = "Pegar informações")
quadroPegar.place(x=160,y=0,width=150,height=100)
btnPegar1 = Button(quadroPegar, text = "Pegar", fg="blue",command=getDado)
btnPegar1.place(x = 50, y = 15)
textUmidade="Temperatura: "
printUmidade=Label(app,text=textUmidade)
printUmidade.place(x=160,y=105)
textUmidade="Umidade: "
printUmidade=Label(app,text=textUmidade)
printUmidade.place(x=160,y=122)
textVel="Velocidade: "
printVelocidade=Label(app,text=textVel)
printVelocidade.place(x=160,y=139)
textAcelerecao="Aceleração: "
printAceleracao=Label(app,text=textAcelerecao)
printAceleracao.place(x=160,y=156)
app.mainloop()