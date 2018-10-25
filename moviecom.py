from selenium import webdriver

class Moviecom:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://moviecom.com.br'
        self.btn_yes = 'botao bt-left f-canaro'
        self.btn_no = 'troca-praca' #id
        self.praca_direita = 'direita' #class
        self.praca_esquerda = 'esquerda' #class
        self.city = 'f-azul'

    def navigate(self):
        self.driver.get(self.url)

    def search(self):
            self.driver.find_element_by_id(self.btn_no).click()
    
    def escolha_cidade(self):
            self.driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/div[4]/a[contains(@onclick, 'trocaPraca')]").click()
            # self.driver.find_element_by_xpath("//a[contains(@onclick, 'trocaPraca')]").click()
            # self.driver.find_element_by_xpath("//span[contains(text(),'PrudenShopping')]").click()
            # self.driver.find_element_by_xpath("//span[contains(@class, 'f-azul')]").click()
            # self.driver.find_element_by_xpath('.//span[@class="f-azul"]')
            # find_element_by_xpath('.//a[@class="single_like_button btn3-wrap"]')
            self.programacao()
    
    def programacao(self):
            # self.driver.find_element_by_xpath(
            #     "/html/body/div[3]/div[3]/div/div[3]/div[2]/div/a"
            #     ).href
            print(self.driver.find_element_by_xpath("//div[@class='botao bt-center f-canaro']"))
            # return self.driver.find_element_by_partial_link_text('COMPLETA')
    
    def _get_pracas(self,lado):
        if lado == 'direita':
            return self.driver.find_elements_by_class_name(self.praca_direita)
        else :
            return self.driver.find_elements_by_class_name(self.praca_esquerda)

    def _get_title(self, p):
        return p.find_elements_by_class_name(self.city)

    def get_all_data(self):
        lados = []
        pracas = self._get_pracas('direita')
        for p in pracas:
            lados.append(p)
        pracas = self._get_pracas('esquerdo')
        for p in pracas:
            lados.append(p)
            # print(self._get_title(p).text)
        return lados

cc = webdriver.Chrome()
c = Moviecom(cc)
c.navigate()
c.search()
# pracas = c.get_all_data()
c.escolha_cidade()
# c.programacao()
# cc.findElement(By.linkText(self.city)).click();
# for x in pracas:
    # print(x.findAll('span',{'class':'f-azul'}))
    # print(x.find_elements_by_class_name('f-azul'))
    # print(c._get_title(x))