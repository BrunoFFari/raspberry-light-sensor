#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import smbus
import time

ENDERECO = 0x23 # Endereco I2C padrao
CANAL = 1 # Canal onde o sensor esta.

# Uma medicao com resolucao de 1 lx a cada
# 120 ms.
ONE_TIME_HIGH_RES_MODE_1 = 0x20

TOPICO = "dev_iot_impacta/grupo/89/sensor/02"

# Inicia um canal.
i2c = smbus.SMBus(CANAL)

# Cria Client MQTT
client = mqtt.Client()
client.connect("mqtt.eclipse.org", 1883, 60)

# Esta funcao converte um valor dividido em 2 bytes
# em um valor decimal.
def converteParaNumero(dado):
	resultado = (dado[1] + (256 * dado[0])) / 1.2
	return (resultado)

# Le os dados da interface I2C
def leLuz(endereco):
	dado = i2c.read_i2c_block_data(endereco,ONE_TIME_HIGH_RES_MODE_1)
	return converteParaNumero(dado)


def main():
	while True:
		nivelLuz = leLuz(ENDERECO)
		client.publish(TOPICO, str(nivelLuz).encode(), qos=0)
		
		time.sleep (0.5)

if __name__ == "__main__":
	main()


