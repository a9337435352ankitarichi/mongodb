# first line: 346
    def get(self, ticker):
        ''' Retrieves EOD data from cache or the web.

        :param ticker: The stock symbol, such as `AAPL`.

        :returns: The data as a pandas `DataFrame`.
        '''
        start = datetime(1900, 1, 1, 0, 0, 0, 0)
        return DataReader(ticker, data_source=self.data_source, start=start)
