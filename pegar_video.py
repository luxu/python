#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from os.path import isdir, expanduser
from time import sleep

os.path.expanduser("~")

location_script = os.getcwd()

def youtube_dl_script():

	def repeat_script():
		print("")
		print("Deseja realizar outra operação com o script? [S/N]")
		REPEAT = input("Digite 'S' para sim ou 'N' para não: ")
		REPEAT = REPEAT.upper()
		if REPEAT == "S":
			os.system("clear")
			youtube_dl_script()
		else:
			print("")
			print("Saindo...")
			print("")
			sleep(0.3) # Time in seconds.
			os._exit(1)

	def separar_id_video(link_video):
		posicao_do_igual = link_video.find("v=")
		if posicao_do_igual<0: # quer dizer q num veio o link certo
			return posicao_do_igual
		posicao_do_igual +=2
		print(posicao_do_igual)
		return link_video[posicao_do_igual:]

	def main_function_get_id():
		print("Por favor, digite APENAS a ID do vídeo desejado (Exemplo: https://www.youtube.com/watch?v=ID_DO_VÍDEO):")
		print("=======================================================================================================")
		link_video = input("Link do vídeo: ")
		print("")
		global ID
		ID = separar_id_video(link_video)

	def video_function_path():
		os.chdir(expanduser(location_script))

	def video_function_default_mp4():
		if ID == -1:
			print("Link inválido")
		else:
			os.system("youtube-dl --format mp4 https://www.youtube.com/watch?v=" + ID)
			sleep(0.5) # Time in seconds.


	def video_function_default_mp4_conversion():
		os.system("youtube-dl --recode-video mp4 https://www.youtube.com/watch?v=" + ID)
		sleep(0.5) # Time in seconds.

	def option_function_update():
		# os.system("youtube-dl --update")
		os.system("pip install --upgrade youtube_dl")
		sleep(0.5) # Time in seconds.

	#------------------------------------------------------------
	def option_conversion_formats():
		print("Qual formato deseja que o vídeo seja convertido?")
		print("================================================")
		print("")
		print("Formatos de vídeo (conversão):")
		print("(1) Arquivo de vídeo em formato .MP4")
		print("(2) Arquivo de vídeo em formato .MKV")
		print("(3) Arquivo de vídeo em formato .WEBM")
		print("(4) Arquivo de vídeo em formato .AVI")
		print("")
		ESCOLHACONVERSAO = input("Escolha uma das opções acima: ")
		print("")
		if ESCOLHACONVERSAO == "1":
			main_function_get_id()
			video_function_path()
			video_function_default_mp4_conversion()
		else:
			print("Esta não é uma opção válida!")
			sleep(0.5)  # Time in seconds.
			# os.system("sleep 5")
	#------------------------------------------------------------
	#------------------------------------------------------------
	# Opções para o salvamento do vídeo selecionado
	#------------------------------------------------------------
	'''
	print("Como deseja salvar o vídeo?")
	print("(1) Arquivo de vídeo em formato .MP4")
	print("")
	print("Opções do script:")
	print("(7) Formatos de Conversão de Vídeo")
	print("(8) Atualizar Youtube-Dl")
	print("(9) Sair do Youtube-Dl Script")
	print("")
	ESCOLHA = input("Escolha uma das opções acima: ")
	'''
	print("")
	ESCOLHA = "1"
	if ESCOLHA == "1":
		main_function_get_id()
		video_function_path()
		video_function_default_mp4()
		repeat_script()
	elif ESCOLHA == "7":
		option_conversion_formats()
		repeat_script()
	elif ESCOLHA == "8":
		option_function_update()
		repeat_script()
	elif ESCOLHA == "9":
		print("Saindo...")
		print("")
		# os.system("sleep 3")
		sleep(0.3)  # Time in seconds.
	else:
		print("Esta não é uma opção válida!")
		# os.system("sleep 5")
		sleep(0.5)  # Time in seconds.
		repeat_script()

	# main_function_get_id()
	# video_function_path()
	# video_function_default_mp4()
	# repeat_script()
youtube_dl_script()
