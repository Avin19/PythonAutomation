from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
with open("proxylistall.txt","r") as f:
    PROXY = [line.strip() for line in f]
# used it only when you update the list
'''with open("proxylistall.txt", "w") as f:
    for item in PROXY:
        f.write("%s\n" % item)'''
for n in range(0,len(PROXY)):
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--proxy-server=http://%s' % PROXY[n])
        chrome = webdriver.Chrome(executable_path='D:\python\chromedriver.exe',options=chrome_options)
        pro=str(n)+". this is Proxy " + PROXY[n]
        print(pro)
        chrome.get("https://www.youtube.com/watch?v=cMM4FGlnOqw")
        time.sleep(20)
        try :
            chrome.find_element_by_id('logo-icon-container')
            with open("proxylistyoutube.txt","a+") as f:
                f.write("%s\n" % PROXY[n])
                print("writing the proxy to file")
        except NoSuchElementException:
            print("PROXY " + pro + " not connect closing the chrome")
            chrome.quit()
        else:
            pass
        finally:
            pass
    except :
        pass
    else:
        pass
    finally:
       chrome.quit()
