<<<<<<< HEAD
from selenium import webdriver
import json

def main():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
    driver = webdriver.Chrome(options=chrome_options)

    list_of_houses = find_all_houses(driver)

    list_of_parfum = find_all_parfum(driver, list_of_houses)

    with open('Parfumes.txt', 'w') as txtfile:
        json.dump(list_of_parfum, txtfile)

def find_all_houses(chrome):
    url = 'http://www.basenotes.net/fragrancedirectory/'
    chrome.get(url)
    source = chrome.find_element_by_id('house')
    option = source.find_elements_by_tag_name('option')
    list_of_houses = []
    for o in option:
        house = o.get_attribute('value')
        link = url + '?house=' + str(house)
        list_of_houses.append(link)
    del list_of_houses[0]
    return list_of_houses

def find_all_parfum(chrome, houses):
    list_of_houses = houses
    list_of_parfum = []
    for house in list_of_houses:
        chrome.get(house)
        table = chrome.find_element_by_tag_name('table')
        td = table.find_elements_by_xpath('//td[@style="padding-top: 0px;"]')
        for element in td:
            a = element.find_element_by_tag_name('a')
            link = a.get_attribute('href')
            list_of_parfum.append(link)
    return list_of_parfum












if __name__ == '__main__':
    main()















=======
from selenium import webdriver
import json

def main():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
    driver = webdriver.Chrome(options=chrome_options)

    list_of_houses = find_all_houses(driver)

    list_of_parfum = find_all_parfum(driver, list_of_houses)

    with open('Parfumes1.txt', 'w') as txtfile:
        json.dump(list_of_parfum, txtfile)

def find_all_houses(chrome):
    url = 'http://www.basenotes.net/fragrancedirectory/'
    chrome.get(url)
    source = chrome.find_element_by_id('house')
    option = source.find_elements_by_tag_name('option')
    list_of_houses = []
    for o in option:
        house = o.get_attribute('value')
        link = url + '?house=' + str(house)
        list_of_houses.append(link)
    del list_of_houses[0]
    return list_of_houses

def find_all_parfum(chrome, houses):
    list_of_houses = houses
    list_of_parfum = []
    for house in list_of_houses:
        chrome.get(house)
        table = chrome.find_element_by_tag_name('table')
        td = table.find_elements_by_xpath('//td[@style="padding-top: 0px;"]')
        for element in td:
            a = element.find_element_by_tag_name('a')
            link = a.get_attribute('href')
            list_of_parfum.append(link)
    return list_of_parfum

if __name__ == '__main__':
    main()















>>>>>>> v.1.1.
