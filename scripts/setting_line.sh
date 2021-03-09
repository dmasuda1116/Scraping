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
