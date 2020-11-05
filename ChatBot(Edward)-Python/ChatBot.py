#Importar paquetes
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

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

#Conversacion
while True:
    Soli = input('Yo: ')
    Resp = ChatBot.get_response(Soli)
    print('Edward: {}'.format(Resp))
