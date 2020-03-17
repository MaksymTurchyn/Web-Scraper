
from selenium import webdriver
import json
from datetime import datetime
import pytz
import csv


def main():
    global_start = pytz.utc.localize(datetime.utcnow())
    # PROXY = "91.225.226.39:54198"  # IP:PORT or HOST:PORT
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--log-level=3")  # INFO = 0, WARNING = 1, LOG_ERROR = 2, LOG_FATAL = 3
    # chrome_options.add_argument("--proxy-server=%s" % PROXY)
    # chrome_options.add_argument("--window-size=1920x1080")
    # chrome_options.add_argument("--hide-scrollbars")  # Hide scrollbars from screenshots

    driver = webdriver.Chrome(options=chrome_options)

    with open('Parfumes.txt', 'r') as txtfile:
        data = json.load(txtfile)


    for d in data[37800:37900]:
        driver.get(d)
        url = d
        elem = driver.find_element_by_xpath("//*")
        html = elem.get_attribute("outerHTML")


        # Set timer
        start = pytz.utc.localize(datetime.utcnow())
        print('Start time:' + str(start))

    # Getting image url
        try:
            img = driver.find_element_by_class_name('fraginfoimage').find_element_by_tag_name('img').get_attribute('src')
            print(img)
        except:
            img = '-'
            print(img)

    #  Getting name and house
        try:
            name = driver.find_element_by_class_name('fragranceheading').find_element_by_xpath(
                '//span[@itemprop="name"]').text
            print('NAME:' + str(name))
        except:
            name = '-'
            print('NAME:' + str(name))

        try:
            house = driver.find_element_by_class_name('fragranceheading').find_element_by_xpath(
                '//span[@itemprop="brand manufacturer"]').text
            print('HOUSE:' + str(house))
        except:
            house = '-'
            print('HOUSE:' + str(house))


    # Getting:
        try:
            tds = driver.find_element_by_class_name('peoplelist').find_elements_by_xpath('//td')
            long_list_of_tds = []
            for td in tds:
                long_list_of_tds.append(td.text)
            list_of_tds = long_list_of_tds
            print(list_of_tds)
        except:
            long_list_of_tds = []

    # Year
        try:
            year_index = list_of_tds.index('Year of Launch')
            year = list_of_tds[year_index + 1]
            print('YEAR:' + str(year))
        except:
            year = '-'
            print('YEAR:' + str(year))

    # Gender
        try:
            gender_index = list_of_tds.index('Gender')
            gender = list_of_tds[gender_index + 2]
            print('GENDER:' + str(gender))
        except:
            gender = '-'
            print('GENDER:' + str(gender))

    # Availability
        try:
            availability_index = list_of_tds.index('Availability')
            availability = list_of_tds[availability_index + 1]
            print('AVAILABILITY:' + str(availability))
        except:
            availability = '-'
            print('AVAILABILITY:' + str(availability))

    # Rating
        try:
            rating = driver.find_element_by_class_name('peoplelist').find_element_by_tag_name('meta').get_attribute(
                'content')
            print('RATING:' + str(rating))
        except:
            rating = '-'
            print('RATING:' + str(rating))

    # Perfumer
        try:
            perfumer_index = list_of_tds.index('Perfumer')
            perfumer = list_of_tds[perfumer_index + 2]
            print('PERFUMER:' + str(perfumer))
        except:
            perfumer = '-'
            print('PERFUMER:' + str(perfumer))




    # Getting description
        try:
            description = driver.find_element_by_class_name('diraboutblurb').text
            print('DESCRIPTION:' + str(description))
        except:
            description = '-'
            print('DESCRIPTION:' + str(description))

    # Getting notes
        try:
            lis = driver.find_element_by_class_name('notespyramidb').text
            new_list = lis.split('\n')
            print(new_list)
        except:
            new_list = []

    # Getting notes index
        try:
            top_notes_index = new_list.index('Top Notes')
        except:
            top_notes_index = False
        try:
            heart_notes_index = new_list.index('Heart Notes')
        except:
            heart_notes_index = False
        try:
            base_notes_index = new_list.index('Base notes')
        except:
            base_notes_index = False

    # In case no notes mentioned
        if top_notes_index == False and heart_notes_index == False and base_notes_index == False:
            top_notes = new_list
            heart_notes = []
            base_notes = []
            print('3xFalse:' + str(top_notes))
    # All top notes cases
        else:
            try:
                top_notes = new_list[int(top_notes_index)+1:int(heart_notes_index)]
                print('TOP:' + str(top_notes))
            except:
                try:
                    top_notes = new_list[int(top_notes_index)+1:int(base_notes_index)]
                    print('TOP:' + str(top_notes))
                except:
                    try:
                        top_notes = new_list[int(top_notes_index)+1:]
                        print('TOP:' + str(top_notes))
                    except:
                        top_notes = []
                        print('TOP:' + str(top_notes))

    # All heart notes cases
            try:
                heart_notes = new_list[int(heart_notes_index)+1:int(base_notes_index)]
                print('HEART:' + str(heart_notes))
            except:
                try:
                    heart_notes = new_list[int(heart_notes_index)+1:]
                    print('HEART:' + str(heart_notes))
                except:
                    heart_notes = []
                    print('HEART:' + str(heart_notes))

    # All base notes cases

            try:
                base_notes = new_list[int(base_notes_index)+1:]
                print('BASE:' + str(base_notes))
            except:
                base_notes = []
                print('BASE:' + str(base_notes))

        db = {}
        db['time'] = start
        db['url'] = str(url)
        db['img'] = str(img)
        db['name'] = str(name)
        db['house'] = str(house)
        db['year'] = str(year)
        db['gender'] = str(gender)
        db['availability'] = str(availability)
        db['rating'] = str(rating)
        db['perfumer'] = str(perfumer)
        db['description'] = str(description)
        db['top_notes'] = str(top_notes)
        db['heart_notes'] = str(heart_notes)
        db['base_notes'] = str(base_notes)



        with open('mycsv(37800-.csv', 'a', encoding='utf-8') as f:
            writer = csv.writer(f)

            writer.writerow( (db['time'], db['url'], db['img'], db['name'], db['house'], db['year'], db['gender'], db['availability'], db['rating'], db['perfumer'], db['description'], db['top_notes'], db['heart_notes'], db['base_notes'] ) )

        short_url = 'C:/Users/Maksym/PycharmProjects/parfum/DB/html/' + str(url[25:(len(url)-5)])
        file_path = short_url + '.html'
        with open(file_path, 'w') as h:
           json.dump(html, h)




# Set timer
    finish = datetime.now()
    print('global start time:' + str(global_start))
    print('finish time:' + str(finish))






if __name__ == '__main__':
    main()



























=======
from selenium import webdriver
import json
from datetime import datetime
import pytz
import csv


def main():
    global_start = pytz.utc.localize(datetime.utcnow())
    # PROXY = "91.225.226.39:54198"  # IP:PORT or HOST:PORT
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--log-level=3")  # INFO = 0, WARNING = 1, LOG_ERROR = 2, LOG_FATAL = 3
    # chrome_options.add_argument("--proxy-server=%s" % PROXY)
    # chrome_options.add_argument("--window-size=1920x1080")
    # chrome_options.add_argument("--hide-scrollbars")  # Hide scrollbars from screenshots

    driver = webdriver.Chrome(options=chrome_options)

    with open('URL.txt', 'r') as txtfile:
        data = json.load(txtfile)


    for d in data[:10]:
        driver.get(d)
        url = d
        elem = driver.find_element_by_xpath("//*")
        html = elem.get_attribute("outerHTML")


        # Set timer
        start = pytz.utc.localize(datetime.utcnow())
        print('Start time:' + str(start))

    # Getting image url
        try:
            img = driver.find_element_by_class_name('fraginfoimage').find_element_by_tag_name('img').get_attribute('src')
            print(img)
        except:
            img = '-'
            print(img)

    #  Getting name and house
        try:
            name = driver.find_element_by_class_name('fragranceheading').find_element_by_xpath(
                '//span[@itemprop="name"]').text
            print('NAME:' + str(name))
        except:
            name = '-'
            print('NAME:' + str(name))

        try:
            house = driver.find_element_by_class_name('fragranceheading').find_element_by_xpath(
                '//span[@itemprop="brand manufacturer"]').text
            print('HOUSE:' + str(house))
        except:
            house = '-'
            print('HOUSE:' + str(house))


    # Getting:
        try:
            tds = driver.find_element_by_class_name('peoplelist').find_elements_by_xpath('//td')
            long_list_of_tds = []
            for td in tds:
                long_list_of_tds.append(td.text)
            list_of_tds = long_list_of_tds
            print(list_of_tds)
        except:
            long_list_of_tds = []

    # Year
        try:
            year_index = list_of_tds.index('Year of Launch')
            year = list_of_tds[year_index + 1]
            print('YEAR:' + str(year))
        except:
            year = '-'
            print('YEAR:' + str(year))

    # Gender
        try:
            gender_index = list_of_tds.index('Gender')
            gender = list_of_tds[gender_index + 2]
            print('GENDER:' + str(gender))
        except:
            gender = '-'
            print('GENDER:' + str(gender))

    # Availability
        try:
            availability_index = list_of_tds.index('Availability')
            availability = list_of_tds[availability_index + 1]
            print('AVAILABILITY:' + str(availability))
        except:
            availability = '-'
            print('AVAILABILITY:' + str(availability))

    # Rating
        try:
            rating = driver.find_element_by_class_name('peoplelist').find_element_by_tag_name('meta').get_attribute(
                'content')
            print('RATING:' + str(rating))
        except:
            rating = '-'
            print('RATING:' + str(rating))

    # Perfumer
        try:
            perfumer_index = list_of_tds.index('Perfumer')
            perfumer = list_of_tds[perfumer_index + 2]
            print('PERFUMER:' + str(perfumer))
        except:
            perfumer = '-'
            print('PERFUMER:' + str(perfumer))




    # Getting description
        try:
            description = driver.find_element_by_class_name('diraboutblurb').text
            print('DESCRIPTION:' + str(description))
        except:
            description = '-'
            print('DESCRIPTION:' + str(description))

    # Getting notes
        try:
            lis = driver.find_element_by_class_name('notespyramidb').text
            new_list = lis.split('\n')
            print(new_list)
        except:
            new_list = []

    # Getting notes index
        try:
            top_notes_index = new_list.index('Top Notes')
        except:
            top_notes_index = False
        try:
            heart_notes_index = new_list.index('Heart Notes')
        except:
            heart_notes_index = False
        try:
            base_notes_index = new_list.index('Base notes')
        except:
            base_notes_index = False

    # In case no notes mentioned
        if top_notes_index == False and heart_notes_index == False and base_notes_index == False:
            top_notes = new_list
            heart_notes = []
            base_notes = []
            print('3xFalse:' + str(top_notes))
    # All top notes cases
        else:
            try:
                top_notes = new_list[int(top_notes_index)+1:int(heart_notes_index)]
                print('TOP:' + str(top_notes))
            except:
                try:
                    top_notes = new_list[int(top_notes_index)+1:int(base_notes_index)]
                    print('TOP:' + str(top_notes))
                except:
                    try:
                        top_notes = new_list[int(top_notes_index)+1:]
                        print('TOP:' + str(top_notes))
                    except:
                        top_notes = []
                        print('TOP:' + str(top_notes))

    # All heart notes cases
            try:
                heart_notes = new_list[int(heart_notes_index)+1:int(base_notes_index)]
                print('HEART:' + str(heart_notes))
            except:
                try:
                    heart_notes = new_list[int(heart_notes_index)+1:]
                    print('HEART:' + str(heart_notes))
                except:
                    heart_notes = []
                    print('HEART:' + str(heart_notes))

    # All base notes cases

            try:
                base_notes = new_list[int(base_notes_index)+1:]
                print('BASE:' + str(base_notes))
            except:
                base_notes = []
                print('BASE:' + str(base_notes))

        db = {}
        db['time'] = start
        db['url'] = str(url)
        db['img'] = str(img)
        db['name'] = str(name)
        db['house'] = str(house)
        db['year'] = str(year)
        db['gender'] = str(gender)
        db['availability'] = str(availability)
        db['rating'] = str(rating)
        db['perfumer'] = str(perfumer)
        db['description'] = str(description)
        db['top_notes'] = str(top_notes)
        db['heart_notes'] = str(heart_notes)
        db['base_notes'] = str(base_notes)



        with open('mycsv.csv', 'a', encoding='utf-8') as f:
            writer = csv.writer(f)

            writer.writerow( (db['time'], db['url'], db['img'], db['name'], db['house'], db['year'], db['gender'], db['availability'], db['rating'], db['perfumer'], db['description'], db['top_notes'], db['heart_notes'], db['base_notes'] ) )

# Set timer
    finish = datetime.now()
    print('global start time:' + str(global_start))
    print('finish time:' + str(finish))






if __name__ == '__main__':
    main()



























>>>>>>> v.1.1.
