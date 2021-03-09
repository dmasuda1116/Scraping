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
fi


echo "Enter the line access token: "
while True ; do
  read access_token
  length=${#access_token}
  echo ${length}
  if [ $length -gt 30 ]; then
    break;
  else
    echo "Enter the line access token: "
  fi
done

echo ${access_token}
path='../chromedrive'

# keyを代入
keyName='"access_token":'
driver_path='"driver_path":'

# keyとパラメータを変数に代入
nameJson="${keyName} \"$access_token\""
ageJson="${driver_path} \"$path\""

# printfでJSON形式でファイルにリダイレクトする
printf '{
  %s,
  %s
}' "${nameJson}" "${ageJson}"  > ../json/config.json 
