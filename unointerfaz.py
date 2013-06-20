import pygame, sys,os
from pygame.locals import *

#inicia los procesos y el motor
estado=0
screen=0
idioma=1
#carga las imagenes
#menu=pygame.image.load('imagenes/menu.png')
menuEN=pygame.image.load('imagenes/menuEN.png')
fondoAmarilo=pygame.image.load('imagenes/fondoamarillo.jpg')
fondoAzul=pygame.image.load('imagenes/fondoazul.jpg')
fondoRojo=pygame.image.load('imagenes/fondorojo.jpg')
fondoVerde=pygame.image.load('imagenes/fondoverde.jpg')
ama0=pygame.image.load('imagenes/ama0.png')
ama1=pygame.image.load('imagenes/ama1.png')
ama2=pygame.image.load('imagenes/ama2.png')
ama3=pygame.image.load('imagenes/ama3.png')
ama4=pygame.image.load('imagenes/ama4.png')
ama5=pygame.image.load('imagenes/ama5.png')
ama6=pygame.image.load('imagenes/ama6.png')
ama7=pygame.image.load('imagenes/ama7.png')
ama8=pygame.image.load('imagenes/ama8.png')
ama9=pygame.image.load('imagenes/ama9.png')
amados=pygame.image.load('imagenes/amados.png')
amano=pygame.image.load('imagenes/amano.png')
amarev=pygame.image.load('imagenes/amarev.png')
azu0=pygame.image.load('imagenes/azu0.png')
azu1=pygame.image.load('imagenes/azu1.png')
azu2=pygame.image.load('imagenes/azu2.png')
azu3=pygame.image.load('imagenes/azu3.png')
azu4=pygame.image.load('imagenes/azu4.png')
azu5=pygame.image.load('imagenes/azu5.png')
azu6=pygame.image.load('imagenes/azu6.png')
azu7=pygame.image.load('imagenes/azu7.png')
azu8=pygame.image.load('imagenes/azu8.png')
azu9=pygame.image.load('imagenes/azu9.png')
azudos=pygame.image.load('imagenes/azudos.png')
azuno=pygame.image.load('imagenes/azuno.png')
azurev=pygame.image.load('imagenes/azurev.png')
roj0=pygame.image.load('imagenes/roj0.png')
roj1=pygame.image.load('imagenes/roj1.png')
roj2=pygame.image.load('imagenes/roj2.png')
roj3=pygame.image.load('imagenes/roj3.png')
roj4=pygame.image.load('imagenes/roj4.png')
roj5=pygame.image.load('imagenes/roj5.png')
roj6=pygame.image.load('imagenes/roj6.png')
roj7=pygame.image.load('imagenes/roj7.png')
roj8=pygame.image.load('imagenes/roj8.png')
roj9=pygame.image.load('imagenes/roj9.png')
rojdos=pygame.image.load('imagenes/rojdos.png')
rojno=pygame.image.load('imagenes/rojno.png')
rojrev=pygame.image.load('imagenes/rojrev.png')
ver0=pygame.image.load('imagenes/ver0.png')
ver1=pygame.image.load('imagenes/ver1.png')
ver2=pygame.image.load('imagenes/ver2.png') 
ver3=pygame.image.load('imagenes/ver3.png')
ver4=pygame.image.load('imagenes/ver4.png')
ver5=pygame.image.load('imagenes/ver5.png')
ver6=pygame.image.load('imagenes/ver6.png')
ver7=pygame.image.load('imagenes/ver7.png')
ver8=pygame.image.load('imagenes/ver8.png')
ver9=pygame.image.load('imagenes/ver9.png')
verdos=pygame.image.load('imagenes/verdos.png')
verno=pygame.image.load('imagenes/verno.png')
verrev=pygame.image.load('imagenes/verrev.png')
atras=pygame.image.load('imagenes/atras.jpg')
comodin=pygame.image.load('imagenes/comodin.png')
comodin4=pygame.image.load('imagenes/comodin4.png')

def inicio():
	global screen, estado, idioma

	pygame.init()
	window = pygame.display.set_mode((800,600)) 
	pygame.display.set_caption('Uno League of Legends ') 
	screen = pygame.display.get_surface() 
	salir= False
	menu=pygame.image.load('imagenes/menu.png').convert_alpha()
	while salir!=True:	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				salir=True
			#selecciona el idioma

			#if event.type == MOUSEBUTTONDOWN:
			#	x, y = event.pos

			#	if x > 102 and x < 168 and y > 453 and y < 504:
			#		idioma=1
					
			#	if x > 199 and x < 267 and y > 453 and y < 504:
			#		idioma=2
		#dibujar(1)
		screen.blit(menu,(0,0)) 

#def dibujar(estados):
	#global idioma, screen, menu
	#if estados==1:
	
	#	screen.blit(menu,(0,0)) 
		

	
inicio()
