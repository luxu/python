''' Exemplo de PO no cultcampinas.com.br '''
from selenium import webdriver

class Cult:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://www.culturapp.com.br/index.php/noticias/'
        self.box = 'claerfix' #class
        self.type = 'typeEventBox' #class
        self.title_box = 'margem-pequena' #class
        self.date = 'data-noticia' #class
        self.place = 'placeEvent' #class
        self.hour = 'hourEvent' #class
        self.descr = 'descEventBox' #class

    def navigate(self):
        self.driver.get(self.url)

    def _get_boxes(self):
        return self.driver.find_elements_by_class_name(self.box)

    def _get_title(self, box):
        return box.find_elements_by_class_name(self.title_box)

    def get_all_data(self):
        boxes = self._get_boxes()
        for box in boxes:
            print(self._get_title(box).text)

cc = webdriver.Chrome()
c = Cult(cc)
c.navigate()
c.get_all_data()

