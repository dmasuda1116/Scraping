# Scraping

Scraping is done using google chrome, chrome driver and selenium.
The acquisition result will be notified on LINE.

# Environment

ProductName:	Mac OS X
ProductVersion:	10.14.6
BuildVersion:	18G7016

# Requirement

* Python3 3.7.4
* pip3 19.3.1
* selenium 3.141.0
* requests 2.24.0

# How to set up

### Acquire LINE access code

1. Add LINE Notify to your friends.
2. Access LINE Notify (https://notify-bot.line.me/ja/)
4. Login from the upper right
5. Click the same place as login to go to My Page
6. Get access token
Make a copy of the access token as it will be used for set up.

### Set up
```
git clone https://github.com/dmasuda1116/Scraping.git
cd Scraping/src/
chmod 755 set_up.sh
./set_up.sh
```
When "Enter the line access token: " is displayed, enter the access token

# Let's scraping
```
python3 main.py
```


