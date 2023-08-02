import requests
import numpy as np
import pandas as pn
import csv
import os
from dotenv import load_dotenv



def getData(symbol):

	load_dotenv()
	api_key = os.getenv("API_KEY")

	url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={api_key}"

	r = requests.get(url)
	data = r.json()

	print(data)




getData('NVDA')

