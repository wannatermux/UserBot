## Единственный юзербот который не имеет скам модулей

## Для Termux (Android)

### Установка
```
 apt-get update -y ; apt-get install python -y ; apt-get install git -y ; curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py ; python3 get-pip.py ; rm get-pip.py ; git clone https://github.com/wannatermux/UserBot ; cd UserBot ; termux-wake-lock ; python3 main.py
```

### При запуске
```
cd UserBot && termux-wake-lock && python main.py
```

---

## Для Linux [Debian/Kali]

### Установка
Открываем терминал, и устанавливаем Python и также Git
```
apt install python3 git
```

Теперь мы клонируем репозиторий коммандой
```
git clone https://github.com/wannatermux/UserBot.git
```

Переходим в директерию с юзерботом
```
cd UserBot
```

И запускаем файл через Python
```
python3 main.py
```

Готово)

### Запуск

Запускаем терминал и пишем такие комманды
```
cd UserBot && python3 main.py
```
---
