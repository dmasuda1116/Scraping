# Scraping

Scraping is done using google chrome, chrome driver and selenium.
The acquisition result will be notified on LINE.

# Environment

ProductName:	Mac OS X
ProductVersion:	10.14.6
BuildVersion:	18G7016

# Requirement

* Python 3.7.4
* pip 19.3.1
* selenium 3.141.0
* requests 2.24.0

# How to set up

### Acquire LINE access code

1. Add LINE Notify to your friends.
2. Access LINE Notify (https://notify-bot.line.me/ja/)
4. Log in from the upper right
5. Click the same place as login to go to My Page
6. Get access token

Make a copy of the access token as it will be used for set up.

### Install Python3

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
brew install python3
python3 -V
```

### Install modules

```
pip3 install selenium requests
```

### Get souce code
```
git clone https://github.com/dmasuda1116/Scraping.git
```

### set up chromedriver

```
chmod 755 get_driver.sh
sh get_driver.sh
```

### make config for LINE notify

```
chmod 755 setting_line.sh
sh setting_line.sh
```

When "Enter the line access token: " is displayed, enter the access token

# Let's scraping
```
python3 main.py
```


