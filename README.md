# Автотесты для Selenium на языке Python сайта Home.Mephi.ru
К нашему большому счастью сайт решил долго жить, потому стоит использовать VPN:
<p> <a href="https://it.mephi.ru/vpn" target="_blank">Ссылка на VPN</a></p>


###Установить зависимости:
```bash
pip install -r requirements.txt
```

###Так же нужно установить Chromium:
<h4> Для установки откройте сайт <a href="https://sites.google.com/chromium.org/driver/" target="_blank"> Chromium </a>и скачайте ту версию ChromeDriver, которая соответствует версии вашего браузера. Чтобы узнать версию браузера, откройте новое окно в Chrome, в поисковой строке наберите: chrome://version/ и нажмите Enter. В верхней строчке вы увидите информацию про версию браузера. </h4>


###Вставить свой логин и пароль от сайта home.mephi.ru
Пример лежит в env_example.py, потому копируем и изменяем там значения:
``` bash
cp .\env_example.py env.py
```

##И приятной работы, запустив главный файл