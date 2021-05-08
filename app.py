#!/usr/bin/env python
# -*- coding: utf-8 -*-
from saa import SeleniumAliAutomation
from pyfiglet import Figlet
from clint.textui import colored
import random, os


Graph = Figlet(font="slant")
GraphRender = Graph.renderText("PechinhaBot")
os.system("cls")
print("%s" % (colored.cyan(GraphRender)))
print(colored.cyan("Automatização de pechinha Aliexpress.\nNão me responsabilizo por possíveis Bloqueios.\nBy Nícolas Pastorello\n"))

url = input(colored.yellow('Insira a url do pechinha: '))

while True:
    quantidade = input(colored.yellow('Insira a quantidade de vezes que deve ser ajudado: '))
    try:
        quantidade = int(quantidade)
    except:
        continue
    if quantidade < 1:
        continue
    break
print("\n")

count = 0
while count <= quantidade:
    count += 1
    saa = SeleniumAliAutomation(url)
    print(saa.tipo_mensagem("alerta", u"Ajudado "+str(count)+" vezes."))