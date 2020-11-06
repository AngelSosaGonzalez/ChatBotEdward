#VERSION 2.0 
#Importar paquetes
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os

"""Eliminar: "No value for search_text was available on the provided input"
 de la converzacion"""
import logging
logging.basicConfig(filename='archivarlog.log', level=logging.DEBUG)

#Nombrar el Bot
ChatBot = ChatBot('Edward')

#Eliminar el entrenamiento
ChatBot.storage.drop()

#Entrenador
Entre = ChatterBotCorpusTrainer(ChatBot)
Entre.train('chatterbot.corpus.spanish')

#Funciones
#Conversacion
def conve():
    Soli = ''
    Entre = ''

    Entre = ChatterBotCorpusTrainer(ChatBot)
    Entre.train('chatterbot.corpus.spanish')

    #Inicio
    print('\nSoy Edward, tu ChatBot de cabecera\n')
    print('Para salir de nuestra conversación, solo escribe "salir" \n')

    #Conversacion (Se realiza en bucle)
    while Soli != 'salir':
        Soli = input('Yo: ')
        Soli.lower()
        Resp = ChatBot.get_response(Soli)
        print('Edward: {}'.format(Resp))
        Entre = Soli
#*************************************************************************************************************************************************************
        #Entrenamiento
        if Entre == 'entrenamiento':
            preg = input('\n¿Cual es tu pregunta? \n')
            resp = input('¿Cual es tu repuesta? \n')

            ent = open('aqui va la ruta donde tengas a conversations.yml', 'a')
            ent.write('\n- - ' + preg)
            ent.write('\n  - ' + resp.title())
            ent.close()
            
            #Reiniciar la funcion
            conve()
#*************************************************************************************************************************************************************

#Importar la funcion
conve()

#Finzalizacion
confir = input('\n¿Respondi a todas tus preguntas? S/N \n')
if confir.upper() == 'S':
    print('\n¿Sabias que puedes entrenarme?, es facil solamente escribe "entrenamiento" en nuestra conversacion')
    print('Solo ingresa la pregunta y la respuesta esperada, en un dos por tres ya me entrenaste \n')
    print('Bueno mucha explicacion ya vete...')

elif confir.upper() == 'N':
    print('\nNi modo, soy un chatbot no un genio, quedate con lo que se...')
    print('Bueno, no soy tan malo, escribe "entrenamiento" en nuestra conversacion')
    print('Solo ingresa la pregunta y la respuesta esperada, en un dos por tres ya me entrenaste \n')
    print('Bueno mucha explicacion ya vete...')

