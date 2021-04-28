chrome=$(/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --version)
array=( `echo $chrome | tr -s '/' ' '`)
echo ${chrome}
echo ${array[2]}
split=(${array[2]//./ })
number=$split
echo ${number}

if [ ${number} = "88"  ]; then
  wget https://chromedriver.storage.googleapis.com/87.0.4280.88/chromedriver_mac64.zip
  unzip chromedriver_mac64.zip
  rm chromedriver_mac64.zip
elif [ ${number} = "88"  ]; then
  wget https://chromedriver.storage.googleapis.com/88.0.4324.96/chromedriver_mac64.zip
  unzip chromedriver_mac64.zip
  rm chromedriver_mac64.zip
elif [ ${number} = "89"  ]; then
  wget https://chromedriver.storage.googleapis.com/89.0.4389.23/chromedriver_mac64.zip
  unzip chromedriver_mac64.zip
  rm chromedriver_mac64.zip
elif [ ${number} = "90"  ]; then
  wget https://chromedriver.storage.googleapis.com/90.0.4430.24/chromedriver_mac64.zip
  unzip chromedriver_mac64.zip
  rm chromedriver_mac64.zip
elif [ ${number} = "91"  ]; then
  wget https://chromedriver.storage.googleapis.com/91.0.4472.19/chromedriver_mac64.zip
  unzip chromedriver_mac64.zip
  rm chromedriver_mac64.zip
fi

mv chromedriver ..
