import undetected_chromedriver.v2 as uc
import time

def lauchingbrowser():
    driver= uc.Chrome()
    value=input('Enter wait ever you want to download')
    url='https://www.youtube.com/results?search_query='+value
    driver.get(url)
    return driver
def goingtoyotube(dr):
    filter_btn= dr.find_element_by_xpath('//*[@id="container"]/ytd-toggle-button-renderer')
    filter_btn.click()
    dr.find_element_by_xpath('//*[@id="collapse-content"]/ytd-search-filter-group-renderer[4]/ytd-search-filter-renderer[5]').click()
    return_url=dr.current_url
    listofvideo=dr.find_elements_by_id('dismissible')
def caluatingnumberofvideo(dr):
    for i in range(len(listofvideo)):
        listofvideo=dr.find_elements_by_id('dismissible')
        listofvideo[i].click()
        time.sleep(2)
        dr.find_element_by_xpath('//*[@id="movie_player"]').click()
        vurl=dr.current_url
        index=vurl.find('yo')
        videourl =vurl[:index]+'ss'+vurl[index:]
        time.sleep(5)
        title=dr.find_element_by_xpath('//*[@id="container"]/h1/yt-formatted-string').get_attribute('innerHTML')
        dr.get(videourl)
        parenttab=dr.window_handles[0]
        time.sleep(10)
        dr.find_element_by_xpath('//*[@id="sf_result"]/div/div[1]/div[2]/div[2]/div[1]/a').click()
        childtab=dr.window_handles[1]
        dr.switch_to.window(childtab)
        time.sleep(1)
        dr.close()
        dr.switch_to.window(parenttab)
        time.sleep(1)
        dr.get(return_url)
        time.sleep(1)
dr=lauchingbrowser()
goingtoyotube(dr)
caluatingnumberofvideo(dr)