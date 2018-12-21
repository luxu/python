from time import sleep
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
import getpass

class Instagram(object):

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.browser = webdriver.Chrome()

    def login(self):
        self.browser.get('https://www.instagram.com/')
        sleep(2)
        connect = self.browser.find_element_by_link_text('Conecte-se').click()
        sleep(3)
        user = self.browser.find_element_by_name('username')
        user.send_keys(self.email)
        passw = self.browser.find_element_by_name('password')
        passw.send_keys(self.password)
        passw.submit()

    def like(self):
        # Botão de baixar app
        sleep(5)
        self.browser.find_element_by_link_text('Agora não').click()
        # Botão de notificação
        sleep(3)
        btn_ativar = self.browser.find_element_by_class_name('aOOlW')
        btn_ativar.click()
        #procura pelo 'explore'
        sleep(10)
        explore = self.browser.find_element_by_class_name(
            '''glyphsSpriteSafari__outline__24__grey_9''')
            # '''glyphsSpriteSafari__outline__24__grey_9.u-__7''')
        #clica no 'explore'
        explore.click()
        #procura pela img
        sleep(3)
        a = self.browser.find_elements_by_tag_name('a')
        href = [h.get_attribute('href') for h in a]
        imgs = [img for img in href if img[26:30] == 'p/Br']
        for i in imgs:
            try:
                #abri a imagem
                self.browser.get(i)
                #botão curtir
                dá_like = self.browser.find_element_by_class_name(
                    '''coreSpriteHeartOpen''')
                    # '''dCJp8.afkep.coreSpriteHeartOpen._0mzm-''')
                #curti a imagem
                dá_like.click()
            except ElementClickInterceptedException:
                print("Falhou")



# user = str(input('Email: '))
senha = getpass.getpass('Senha: ')
user = u"zicadopv@gmail.com"
insta = Instagram(user, senha)
insta.login()
insta.like()
