from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests

class SocialBlade:

    def __init__(self,driver):
        self.driver = driver
        self.url = "https://socialblade.com/"
        self.caixa_search = 'q'  #name

    def navigate(self):
        self.driver.get(self.url)

    def get_all_data(self):
        boxes = self.destrinchar_url()
        print(type(boxes))
        return
        for box in boxes:
            print(box)

    def destrinchar_url(self):
        prices = self.driver.find_elements_by_xpath("/html/body/div[15]/div[2]/div[1]/div[2]/div[3]")
        prices = self.driver.find_elements_by_tag_name('div')
        for price in prices:
            print(price)
        # return self.driver.find_elements_by_xpath("/html/body/div[15]/div[2]/div[1]/div[2]/div[3]")
        # print(c)

    def search(self, word='None'):
        self.driver.find_element_by_name(self.caixa_search).send_keys(word)
        self.driver.find_element_by_xpath("//*[@id='topSearchForm']/div[1]/button").click()
        if self.driver.find_element_by_xpath("/html/body/div[10]/div[1]/a"):
            self.driver.find_element_by_xpath("/html/body/div[10]/div[1]/a").click()
        return self.driver.current_url

url = "https://socialblade.com/"
cc = webdriver.Chrome()
c = SocialBlade(cc)
c.navigate()
# url = c.search('andarilho')
url = c.search('Canal VGames')
# url = c.search('Clash com Nery')
c.destrinchar_url()
# cc.close()
# cc.quit()

'''
#
# found = soup.find('span', text='Rok produkcji').find_next_sibling('div')
info_youtuber = 'YouTubeUserTopInfoWrap'  #id
# url_veio_do_selenium = 'https://socialblade.com/youtube/channel/UCBUPPrMmr9TIhEo849cQm-w' #Andarilho
url_veio_do_selenium = 'https://socialblade.com/youtube/channel/UCRCODdRFa5G2r3jkBCw9J7Q' #CanalVGames

# c.destrinchar_url(url_veio_do_selenium)
page = requests.get(url_veio_do_selenium)
soup = BeautifulSoup(page.content, 'html.parser')
info_youtuber = soup.find(id='YouTubeUserTopInfoWrap')
link_avatar = soup.find(id='YouTubeUserTopInfoAvatar').get('src')
caixas = soup.find_all(id='YouTubeUserTopInfoBlock')
# infos = soup.find_all(class_="hint--top")
# print(infos)
for caixa in caixas:
    nv = caixa.find_all(class_="YouTubeUserTopInfo")
    # nv = caixa.find("span", string=["Uploads", "Subscribers", "Video Views"])
    # nv = caixa.find("span", string=["Uploads"])
    # for n in nv:
    #     n = n.find_next("span")
    #     print(n.find_next("span").find_next("span").text)
    #     # print(n.find(id='youtube-stats-header-uploads').text)
    #     # print(n.find(id='youtube-stats-header-subs'))
    #     # print(n.find(id='youtube-stats-header-views'))
    #     # print(n.find(id='youtube-stats-header-views'))
    # print(nv[0].find_next("span").find_next("span").find_next("span").text)

    # print('-'*10)
UPLOADS = nv[0].find_next("span").find_next("span").find_next("span").text
SUBSCRIBERS = nv[1].find_next("span").find_next("span").find_next("span").text
VIDEO_VIEWS = nv[2].find_next("span").find_next("span").find_next("span").text
# USER_CREATED = n[5].text
print('UPLOADS.:{}\nSUBSCRIBERS.:{}\nVIDEO VIEWS.:{}'.format(UPLOADS,SUBSCRIBERS,VIDEO_VIEWS))
'''