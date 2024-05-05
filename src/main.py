import pandas as pd
import requests

url = 'https://us.kabutan.jp/disclosures/0000320193-24-000005?lang=en'

# ユーザーエージェントの設定
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

response = requests.get(url, headers=headers)

# pandasにHTMLコンテンツを直接渡す
dataframes = pd.read_html(response.text)
dataframe = dataframes[0]
dataframe.to_csv('data.csv', encoding="shift-jis")