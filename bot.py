#Bot Whatsapp#
from selenium import webdriver
import time
import PySimpleGUI as sg

class Whatsapp:
    def __init__(self):

        sg.theme('Reddit')
        #Layout    
        layout = [
            [sg.Text("Para quem voce quer mandar a mensagem?")],
            [sg.Input(key='contact')],
            [sg.Text("Digite sua mensagem abaixo")],
            [sg.Input(key='mensage')],
            [sg.Button('Enviar')]
        ]
        #Janela        
        window = sg.Window("Robo Whatsapp").layout(layout)
        #Extracao
        self.button, self.values = window.Read()
        self.contact = self.values['contact']
        self.mensage = self.values['mensage']

        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver')
    
    def sendMensage(self):
        #<span dir="auto" title="Cambada de doentes" class="_35k-1 _1adfa _3-8er">Cambada de doentes</span>d copyable-text selectable-text" contenteditable="true" data-tab="6" dir="ltr" spellcheck="true"></div></div></div>
        #<div tabindex="-1" class="_2A8P4">
        #<span data-testid="send" data-icon="send" class="">
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(8)
        contato = self.driver.find_element_by_xpath("//span[@title='{}']".format(self.contact))
        time.sleep(2)
        contato.click()
        chat_box = self.driver.find_element_by_class_name('_2A8P4')
        time.sleep(2)
        chat_box.click()
        chat_box.send_keys(self.mensage)
        button_send = self.driver.find_element_by_xpath("//span[@data-icon='send']")
        time.sleep(2)
        button_send.click()
        time.sleep(5)

bot = Whatsapp()
bot.sendMensage()