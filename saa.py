#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyfiglet import Figlet
from random import randint
from clint.textui import colored
from pyfiglet import Figlet
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import ElementNotInteractableException
import os, sys, platform, time, random

class SeleniumAliAutomation:

	def __init__(self, url):
		try:
			firefox_options = Options()
			firefox_options.set_headless()

			user_agent = "Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16"
			profile = webdriver.FirefoxProfile() 
			profile.set_preference("general.useragent.override", user_agent)

			self.browser = webdriver.Firefox(profile, options=firefox_options)
			self.browser.set_window_size(360,640)
			self.browser.get(url)

			WebDriverWait(self.browser, 30).until(
			EC.presence_of_element_located((By.XPATH, r"//span[contains(text(), 'Help your friend slash the price！')]"))).click()

			#print(self.tipo_mensagem("alerta", u"Criando uma conta no Aliexpress"))

			WebDriverWait(self.browser, 30).until(
			EC.presence_of_element_located((By.XPATH, r"/html/body/div[1]/div/div[2]/div[1]/div/ul/li[1]/div"))).click()

			WebDriverWait(self.browser, 30).until(
			EC.presence_of_element_located((By.XPATH, r"/html/body/div[1]/div/div[2]/div[2]/div[1]/div/div/div/div[4]/div[1]/input"))).send_keys(str(random.randint(111111111111,999999999999))+"@gmail.com")
			
			WebDriverWait(self.browser, 30).until(

			EC.presence_of_element_located((By.XPATH, r"/html/body/div[1]/div/div[2]/div[2]/div[1]/div/div/div/div[4]/div[2]/input"))).send_keys("Ali"+str(random.randint(11111, 99999))+"Conta"+str(random.randint(11111, 99999)))
			
			WebDriverWait(self.browser, 30).until(
			EC.presence_of_element_located((By.XPATH, r"/html/body/div[1]/div/div[2]/div[2]/div[1]/div/div/div/div[4]/div[5]/a"))).click()

			try:
				WebDriverWait(self.browser, 30).until(
				EC.presence_of_element_located((By.XPATH, r"//a[contains(text(), 'CONFIRA!')]")))

				WebDriverWait(self.browser, 30).until(
				EC.presence_of_element_located((By.XPATH, r"//span[@id='ms-back']"))).click()
				#print(self.tipo_mensagem("sucesso", u"Conta criada com sucesso."))

				try:
					WebDriverWait(self.browser, 30).until(
					EC.presence_of_element_located((By.XPATH, r"//span[contains(text(), 'Ajude seu amigo a pechinchar')]"))).click()

					try:
						WebDriverWait(self.browser, 30).until(
						EC.presence_of_element_located((By.XPATH, r"//div[contains(text(), 'Você acabou de cortar')]")))
						print(self.tipo_mensagem("sucesso", u"Ajudado com sucesso."))
						
						time.sleep(2)
						self.browser.close()
						self.finalizar()

					except NoSuchElementException:
						print(self.tipo_mensagem("erro", u"Não foi possivel Ajudar."))
						self.browser.close()
						self.finalizar()

					except ElementClickInterceptedException:
						print(self.tipo_mensagem("erro", u"Não foi possivel Ajudar."))
						self.browser.close()
						self.finalizar()

					except ElementNotInteractableException:
						print(self.tipo_mensagem("erro", u"Não foi possivel Ajudar."))
						self.browser.close()
						self.finalizar()

				except NoSuchElementException:
					print(self.tipo_mensagem("erro", u"Não foi possivel Ajudar."))
					self.browser.close()
					self.finalizar()

				except ElementClickInterceptedException:
					print(self.tipo_mensagem("erro", u"Não foi possivel Ajudar."))
					self.browser.close()
					self.finalizar()

				except ElementNotInteractableException:
					print(self.tipo_mensagem("erro", u"Não foi possivel Ajudar."))
					self.browser.close()
					self.finalizar()

			except NoSuchElementException:
				print(self.tipo_mensagem("erro", u"Não foi possivel encontrar os elementos na página."))
				self.browser.close()
				self.finalizar()

			except ElementClickInterceptedException:
				print(self.tipo_mensagem("erro", u"Não foi possivel encontrar os elementos na página."))
				self.browser.close()
				self.finalizar()

			except ElementNotInteractableException:
				print(self.tipo_mensagem("erro", u"Não foi possivel encontrar os elementos na página."))
				self.browser.close()
				self.finalizar()

		except NoSuchElementException:
			print(self.tipo_mensagem("erro", u"Não foi possivel encontrar os elementos na página."))
			self.browser.close()
			self.finalizar()

		except ElementClickInterceptedException:
			print(self.tipo_mensagem("erro", u"Não foi possivel Ajudar."))
			self.browser.close()
			self.finalizar()

		except ElementNotInteractableException:
			print(self.tipo_mensagem("erro", u"Não foi possivel encontrar os elementos na página."))
			self.browser.close()
			self.finalizar()

		except TimeoutException:
			print(self.tipo_mensagem("erro", u"Não foi possivel carregar a página de login."))
			self.browser.close()
			self.finalizar()


	def tipo_mensagem(self, tipo, mensagem):
		if tipo == "sucesso":
			return colored.green("[+] Sucesso: "+mensagem)
		elif tipo == "alerta":
			return colored.yellow("[!] Alerta: "+mensagem)
		elif tipo == "erro":
			return colored.red("[-] Erro: "+mensagem)

	def finalizar(self):
		self.browser.quit()
		#print(self.tipo_mensagem("sucesso", u"Script foi finalizado."))