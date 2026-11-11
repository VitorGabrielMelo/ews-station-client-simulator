# Cliente de nível da água (interface gráfica)
# Python v3.6.3
# Por Shelby LeBlac e Sagun Pandey
# Comentários em português adicionados por Vitor Gabriel

from tkinter import *
import requests
import json
import datetime
import random
import time as Time
import os
import multiprocessing

def client(clientId):

    # cria a janela principal e as variáveis que guardam os valores exibidos
    root = Tk()
    entry = []
    label = []
    entryText1 = StringVar()
    entryText2 = StringVar()
    entryText3 = StringVar()
    number_of_labels = 3
    id = clientId
    time = ""
    level = ""
    # endereço do servidor que recebe as leituras (IP de rede local)
    url2 = 'http://10.30.41.115:8080/reading'


    def display():

        # cria os campos de texto onde aparecem hora, nível da água e ID da estação
        entry.append(Entry(root,text=entryText1,width=30))
        entry.append(Entry(root,text=entryText2,width=30))
        entry.append(Entry(root,text=entryText3,width=30))

        # cria os rótulos (textos) de cada campo
        label.append(Label(root, text="Read Time",fg="black",font=14))
        label.append(Label(root, text="Water Level",fg="black",font=14))
        label.append(Label(root, text="Station ID",fg="black",font=14))

        # posiciona campos e rótulos na janela, um por linha
        for i in range(number_of_labels):
            entry[i].grid(row=i, column=1)
            label[i].grid(row=i,sticky=W)

        #submitButton.grid(columnspan=2)

        # título e tamanho da janela
        root.title("Water Client")
        root.geometry("300x150")

    def update():

        # define a hora atual e um nível de água aleatório entre 10 e 49
        time=datetime.datetime.now().isoformat()
        level=random.randrange(10,50)

        # atualiza os valores mostrados na tela
        entryText1.set(time)
        entryText2.set(level)
        entryText3.set(id)


        # envia a leitura para o servidor
        exportJson(time,level)
        Time.sleep(1)

        # agenda a próxima atualização para daqui a 6 a 10 segundos
        root.after(random.randrange(6000,10000,1000),update)

        # mantém a janela aberta até ser fechada
        root.mainloop()


    def exportJson(time,level):
        # monta o JSON com hora, nível e ID da estação
        data = {"readTime": time,"waterLevel": level,"station":{ "id": id}}
        headers = {"Content-Type": "application/json"}
        # envia os dados ao servidor por requisição PUT
        response = requests.put(url2,data=json.dumps(data), headers=headers)
    display()
    update()


# programa principal: cria um processo para cada estação simulada
if __name__ == '__main__':
    number_process = 6
    p = []

    # cria e inicia os 6 processos
    for i in range(number_process):
        p.append(multiprocessing.Process(target=client, args=(i+1,)))
        p[i].start()

    # espera todos os processos terminarem
    for i in range(number_process):
        p[i].join()
