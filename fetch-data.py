import os
import sys
import time
import requests

# Base website URL
base_url = "https://data.binance.vision/?prefix=data/futures/um/daily/klines/"
# Set the time frame, update this later
time_frame = "15m"
# Set the tickers
tickers = ["BTCUSDT", "ETHUSDT", "BNBUSDT"]

