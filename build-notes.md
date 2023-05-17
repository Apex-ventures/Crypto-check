# Things to do before building the image

Write Python code to download the daily market data for tickers BTCUSDT and ETHUSDT from the website : "https://data.binance.vision/?prefix=data/futures/um/daily/klines/" + "TICKER_VARIABLE". You might need requests and pandas.

Check if the files for the last 30 days are already present or not. If they are not, download for the missing days.
Make sure you delete any files that are older than 30 days. Do this via a cron job.

Additional information:
Store the data in a suitable format such as parquet for good compression and fast read/write. You might need to install pyarrow or fastparquet.
The data should be stored in a folder called "data" in the root directory of the cloud. What are my cloud storage options?

