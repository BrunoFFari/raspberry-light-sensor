#!/usr/bin/env python3
import paho.mqtt.client as mqtt

# Funçao a ser chamada quando chegar um pacote do tipo CONNACK .
def conectou(client, userdata, flags, rc):
	print("Conectado! Código recebido:"+str(rc))
	client.subscribe("dev_iot_impacta/grupo/89/sensor/02")

# Função chamada quando uma nova mensagem do tópico é recebida.
def chegou_mensagem(client, userdata, msg):
	dado = msg.payload.decode()
	print("Nivel de iluminacao : " + dado + " lx")

client = mqtt.Client()
client.on_connect = conectou
client.on_message = chegou_mensagem
client.connect ("mqtt.eclipse.org",1883, 60)

# Permanece em loop, recebendo mensagens
# e manipulando a conexão.
client.loop_forever()