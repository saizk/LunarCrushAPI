import time
import datetime
import requests
import urllib.parse
from lunarcrush.base import LunarCrushABC


class LunarCrushV3(LunarCrushABC):
    _BASE_URL = 'https://lunarcrush.com/api3'

    def __init__(self, api_key):
        super().__init__(api_key)
        self.coin_ids = {coin.get('symbol'): coin.get('id') for coin in self.get_coins_list()['data']}
        self.nft_ids = {nft.get('name'): nft.get('id') for nft in self.get_nfts_list()['data']}

    @staticmethod
    def _parse_kwargs(kwargs):
        req_params = {}
        for param, value in kwargs.items():
            if isinstance(value, list):
                req_params[param] = ','.join(value)
            if isinstance(value, datetime.datetime):
                req_params[param] = str(int(time.mktime(value.timetuple())))
            if isinstance(value, bool):
                req_params[param] = str(value.real)
            elif value is not None:
                req_params[param] = value
        return req_params

    def _gen_url(self, endpoint, **kwargs):
        url = self._BASE_URL + endpoint
        url += '&' + urllib.parse.urlencode(kwargs) if kwargs else ''
        return url

    def _request(self, endpoint, **kwargs):
        kwargs = self._parse_kwargs(kwargs)
        url = self._gen_url(endpoint, **kwargs)
        headers = {'Authorization': f'Bearer {self._api_key}'}
        return requests.get(url, headers=headers).json()

    def get_coin_id(self, coin):
        return str(self.coin_ids.get(coin))

    def get_nft_id(self, nft):
        return str(self.nft_ids.get(nft))

    def get_coin_of_the_day(self) -> dict:
        """
        Get the current LunarCrush Coin of the Day. Coin of the Day is the coin with the highest combination of
        Galaxy Score™ and AltRank™.
        """
        return self._request('/coinoftheday')

    def get_coin_of_the_day_info(self) -> dict:
        """
        Get the previous history of Coin of the Day and when it was last updated.
        """
        return self._request('/coinoftheday/info')

    def get_coins(self, sort: str = 'alt_rank', limit: int = None, desc: bool = False) -> dict:
        """
        Get a general snapshot of LunarCrush metrics on the entire list of tracked coins. It is designed as a
        lightweight mechanism for monitoring the universe of available assets, either in aggregate or relative to each
        other. Metrics include Galaxy Score™, AltRank™, price, volatility, 24h percent change, market cap, social
        mentions, social engagements, average sentiment, social contributors, social dominance, and categories. A more
        comprehensive and granular range of metrics on any specific coin can be found by calling the /coins/:coin endpoint.

        :param str sort: Sort the output by metric. Options: 'galaxy_score', 'nft_score', 'alt_rank', 'nft_rank',
                         'close', 'floor_price', 'percent_change_24h', 'social_volume', 'social_score',
                         'social_dominance', 'social_contributors', 'average_sentiment', 'market_cap', 'market_cap',
                         'volume', 'volume', 'market_dominance', 'market_cap_rank', 'holders', 'nfts', 'crypto_usd'.
        :param int limit: Limit the number of results.
        :param bool desc: Pass any value as desc and the output will be reversed (descending).
        """
        return self._request('/coins', sort=sort, limit=limit, desc=desc)

    def get_coin(self, coin: str | int) -> dict:
        """
        Get a robust and detailed snapshot of a specific coin's metrics. This endpoint was designed to provide a
        granular look at the coin at the timestamp that the call is made. Depending on the call frequency, can be used
        as a time-series or pseudo real-time stream of all LunarCrush metrics as it pertains to a specific asset. Each
        call returns a current time-stamp of 60+ metrics related to the coin and includes the full suite of social
        metrics available on LunarCrush. Specify the coin to be queried by providing the numeric ID or the symbol of the
        coin in the input parameter, which can be found by calling the FREE /coins/list endpoint.

        :param str coin: Pass any value as desc and the output will be reversed (descending).
        """
        return self._request(f'/coins/{coin}')

    def get_coin_change(self, coin: str | int, interval: str = '1w') -> dict:
        """
        Get percentage change metrics for provided coin id or symbol. The endpoint returns all the same metrics as the
        /coins/:coin endpoint, but relative to a specified interval prior to the time of call. For example, calling the
        endpoint with a 1 week interval will provide the difference in either the sum or the average of the metric from
        the previous time period until the current time period, e.g. most recent 1 week vs. the 1 week prior to that.

        :param str | int coin: Provide the numeric id or symbol of the coin or token.
        :param str interval: The % change since time interval to use. Options: '1d', '1w', '1m', '3m', '6m', '1y', '2y'.
        """
        return self._request(f'/coins/{coin}/change', interval=interval)

    def get_coin_historical(self, coin: str | int) -> dict:
        """
        Get a full hourly time series data dump for all metrics provided by /coins/:coin/time-series endpoint. It is
        designed to be a cheaper alternative for grabbing full historical data (as opposed to a specified interval) for
        back-testing and modeling. This is usually a > 30mb download and only includes data up to the most recently
        completed day.

        :param str | int coin: Provide the numeric id or symbol of the coin or token.
        """
        return self._request(f'/coins/{coin}/historical')

    def get_coin_influencers(self, coin: str | int, interval: str = '1w', order: str = 'influential',
                             limit: int = 100, page: int = None) -> dict:
        """
        Get a list a crypto influencers for a specified coin or token. It is sorted on influencer_rank (influential)
        by default but can be sorted by engagement, follower, or social media volume by specifying the sort criteria
        in the input parameters. Returns an influencers social media volume, volume rank, followers, followers rank,
        engagement, engagement rank, influencer rank, and weighted average rank. Also includes metadata like twitter
        handle, display name, profile and banner image.

        :param str | int coin: Provide the numeric id or symbol of the coin or token.
        :param str interval: The time interval to use. Options: '1d', '1w', '1m', '3m', '6m', '1y', '2y', 'all'.
        :param str order: Order results. Options: 'influential', 'engagement', 'followers', 'volume'.
        :param int limit: Limit the number of results.
        :param int page: Page number starting at 0.
        """
        return self._request(f'/coins/{coin}/influencers', interval=interval, order=order, limit=limit, page=page)

    def get_coin_insights(self, coin: str | int, metrics: str = None, limit: int = 10) -> dict:
        """
        Get a list of LunarCrush insights for a specific coin or token. Insights are generated for any anomalies in the
        data or for any significant deviations from the moving average on a specific metric e.g. bullish sentiment
        spikes 50% from the 90-day moving average. Useful for providing notifications or triggering trading or
        application functions based on “out of the ordinary” movements of a coin metric. The return data for insights
        can also be filtered by specific metric (galaxy_score, alt_rank, close, social_volume, social_score,
        social_dominance, social_contributors, market_cap, volume, market_dominance) by specifying in the "metrics"
        query parameter.

        :param str | int coin: Provide the numeric id or symbol of the coin or token.
        :param str metrics: Filter insights to specific metrics. Options: 'galaxy_score', 'alt_rank', 'close',
                            'social_volume', 'social_score', 'social_dominance', 'social_contributors', 'market_cap',
                            'volume', 'market_dominance'.
        :param int limit: Limit the number of results.
        """
        return self._request(f'/coins/{coin}/insights', metrics=metrics, limit=limit)

    def get_coin_meta(self, coin: str | int) -> dict:
        """
        Get all of a coin's basic descriptive data. This includes a coin's description, official social media links,
        white paper, etc.

        :param str | int coin: Provide the numeric id or symbol of the coin or token.
        """
        return self._request(f'/coins/{coin}/meta')

    def get_coin_time_series(self, coin: str | int, interval: str = '1w', start: datetime.datetime = None,
                             bucket: str = 'hour', data_points: int = None) -> dict:
        """
        Get the same metrics available on the /coins/:coin endpoint in a series of discrete, memorialized time buckets
        (hourly or daily) over a certain time interval beginning at a specified start time. This time series endpoint
        differs from /coins/:coin in that the latter provides real-time flexibility while the former provides the data
        at pre-specified hourly or daily timestamps, capped at 1000 data points. This endpoint was designed to provide
        historical data for research or backtesting purposes.

        :param str | int coin: Provide the numeric id or symbol of the coin or token.
        :param str interval: The time interval to use. Options: '1d', '1w', '1m', '3m', '6m', '1y', '2y', 'a'.
        :param datetime.datetime start: The start time (datetime.datetime) to go back to.
        :param str bucket: Use hour or day time buckets / aggregates. Options: 'hour', 'day'.
        :param int data_points: The number of data points to fetch from the start time.

        """
        return self._request(f'/coins/{coin}/time-series',
                             interval=interval, start=start, bucket=bucket, data_points=data_points)

    def get_coins_global(self) -> dict:
        """
        Get aggregated metrics across all coins tracked on the LunarCrush platform at the time of call. This is designed
        to be a global snapshot of the entire market, and tracks the same social metrics - e.g. url shares, reddit
        volumes, twitter, twitter sentiment, social score, social volume, average sentiment - as well a few metrics only
        applicable to the global schema like btc dominance, altcoin market cap, altcoin dominance.
        """
        return self._request('/coins/global')

    def get_coins_global_change(self, interval: str = '1w') -> dict:
        """
        Get percentage change metrics for aggregated metrics across all coins tracked on the LunarCrush platform. The
        endpoint returns all the same metrics as the /coins/global endpoint, but relative to a specified interval prior
        to the time of call. For example, calling the endpoint with a 1 week interval will provide the difference in
        either the sum or the average of the metric from the previous time period until the current time period, e.g.
        most recent 1 week vs. the 1 week prior to that.

        :param str interval: The time interval to use. Options: '1d', '1w', '1m', '3m', '6m', '1y', '2y', 'a'.
        """
        return self._request('/coins/global/change', interval=interval)

    def get_coins_global_historical(self) -> dict:
        """
        The full historical hourly time series data for cryptocurrency global metrics. This is usually a > 30mb download
        and only includes data up to the most recently completed day.
        """
        return self._request('/coins/global/historical')

    def get_coins_global_insights(self, metrics: str = None, limit: int = 10) -> dict:
        """
        Get a list of global cryptocurrency insights.

        :param str metrics: Filter insights to specific metrics. Options: 'social_volume', 'social_score',
                            'social_contributors', 'market_cap', 'volume'.
        :param int limit: Limit the number of results.
        """
        return self._request('/coins/global/insights', metrics=metrics, limit=limit)

    def get_coins_global_time_series(self, interval: str = '1w', start: datetime.datetime = None,
                                     bucket: str = 'hour', data_points: int = None) -> dict:
        """
        Get the same metrics available on the /coins/global endpoint in a series of discrete, memorialized time buckets
        (hourly or daily) over a certain time interval beginning at a specified start time. This time series endpoint
        differs from /coins/global in that the latter provides real-time flexibility while the former provides the data
        at pre-specified hourly or daily timestamps, capped at 1000 data points. This endpoint was designed to provide
        historical data for research or back-testing purposes.

        :param str interval: The time interval to use. Options: '1d', '1w', '1m', '3m', '6m', '1y', '2y', 'a'.
        :param datetime.datetime start: The start time (datetime.datetime) to go back to.
        :param str bucket: Use hour or day time buckets / aggregates. Options: 'hour', 'day'.
        :param int data_points: The number of data points to fetch from the start time.

        """
        return self._request('/coins/global/time-series',
                             interval=interval, start=start, bucket=bucket, data_points=data_points)

    def get_coins_influencers(self, interval: str = '1w', order: str = 'influential',
                              limit: int = 100, page: int = None) -> dict:
        """
        Get a list of overall crypto influencers across all coins. It is sorted on influencer_rank (influential) by
        default but can be sorted by engagement, follower, or social media volume by specifying the sort criteria in the
        input parameters. Returns an influencers social media volume, volume rank, followers, followers rank, engagement,
        engagement rank, influencer rank, and weighted average rank. Also includes metadata like twitter handle, display
        name, profile and banner image.

        :param str interval: The time interval to use. Options: '1d', '1w', '1m', '3m', '6m', '1y', '2y', 'all'.
        :param str order: Order results. Options: 'influential', 'engagement', 'followers', 'volume'.
        :param int limit: Limit the number of results.
        :param int page: Page number starting at 0.
        """
        return self._request('/coins/influencers', interval=interval, order=order, limit=limit, page=page)

    def get_coins_insights(self, metrics: str = None, limit: int = 10,
                           volume: float = None, market_cap: float = None, alt_rank: int = None) -> dict:
        """
        Get a list of LunarCrush insights over all coins tracked on the LunarCrush platform. Insights are generated for
        any anomalies in the data or for any significant deviations from the moving average on a specific metric e.g.
        bullish sentiment spikes 50% from the 90-day moving average. The return data for insights can also be filtered
        by specific metric (galaxy_score, alt_rank, close, social_volume, social_score, social_dominance,
        social_contributors, market_cap, volume, market_dominance) by specifying in the "metrics" query parameter. This
        is useful for monitoring the entire universe of coins, and includes additional filters.

        :param str metrics: Filter insights to specific metrics. Options: 'galaxy_score', 'alt_rank', 'close',
                            'social_volume', 'social_score', 'social_dominance', 'social_contributors', 'market_cap',
                            'volume', 'market_dominance'.
        :param int limit: Limit the number of results.
        :param float volume: Minimum 24h volume on the coin to filter by.
        :param float market_cap: Minimum market cap on the coin to filter by.
        :param int alt_rank: Maximum alt rank on the coin to filter by.
        """
        return self._request('/coins/insights',
                             metrics=metrics, limit=limit, volume=volume, market_cap=market_cap, alt_rank=alt_rank)

    def get_coins_list(self) -> dict:
        """
        Get a list of all supported coins in one output. Includes a coin's LunarCrush id, name, symbol
        and link to the coin's logo.
        """
        return self._request('/coins/list')

    def get_exchanges(self, order: str = '1m', limit: int = 10) -> dict:
        """
        Get a list of all exchanges along with global exchange metrics.

        :param str order: The metric to order the results by. Options: 'trust_rank', '1d_volume', '1d_volume_percent',
                          '1d_trades', '30d_volume', '30d_volume_percent', '30d_trades', 'num_pairs'
        :param int limit: Limit the number of results.
        """
        return self._request('/exchanges', order=order, limit=limit)

    def get_exchange(self, exchange: int) -> dict:
        """
        Gets detail for a provided exchange including metrics and market pairs.

        :param exchange: The id or lunar id of the exchange.
        """
        return self._request(f'/exchanges/{exchange}')

    def get_feeds(self, limit: int = 10, since: str = '1m', hours: int = None, days: int = None, sources: str = None,
                  coin_id: int = None, symbol: str = None, lunar_id: int = None, market: str = 'coins') -> dict:
        """
        Get a list of relevant, highly-engaged social media posts  with the ability to filter by a specific coin or
        NFT asset, as well as a general category (coin or NFT). Additional filters include selected time intervals
        and sources (Twitter, news, Medium, YouTube, Reddit). This was designed for applications who plan to curate
        their own news or social media feeds for themselves or for their users.

        :param int limit: Limit the number of results (max = 1000).
        :param str since: Top feeds from the selected time interval looking back. Options: '1d', '1w', '1m', '3m', '6m',
                      '1y', '2y', 'all'.
        :param int hours: Optionally specify the number of hours to look back.
        :param int days: Optionally specify the number of days to look back.
        :param str sources: Select one or multiple sources to display feeds from. Default/blank selects all sources.
                        Options: 'twitter', 'news', 'medium', 'urls', 'youtube', 'reddit'.
        :param int coin_id: An id of a coin or nft to filter feeds by.
        :param str symbol: The symbol of a coin to filter feeds by.
        :param int lunar_id: The lunar_id of an nft to filter feeds by.
        :param str market: Choose an asset market. Options: 'coins', 'nfts'.
        """
        return self._request('/feeds', limit=limit, since=since, hours=hours, days=days, sources=sources,
                             coin_id=coin_id, symbol=symbol, lunar_id=lunar_id, market=market)

    def get_feed(self, feed: str) -> dict:
        """
        Get high-detail metrics for a specific feed post.

        :param str feed: Provide the lunar id of the feed item to get details for, i.e. 'tweets-1559564427413729287'.
        """
        return self._request(f'/feeds/{feed}')

    def get_influencer(self, influencer: str, fast: bool = False, interval: str = None, sort: str = None) -> dict:
        """
        Get high-detail metrics for a specific influencer. Includes profile information, social volume and engagement
        rank, stats, influence ranks on a list of tokens, and a list of tweets or content data from the influencer.
        Filter by time interval or pass True into the fast query parameter to receive faster output by omitting the
        list of tweets/content.

        :param str influencer: Provide the numeric id or twitter screen name of an influencer, i.e. 'lunarcrush'.
        :param bool fast: Pass True here for the fast output without list of tweets.
        :param str interval: The time interval to get data for. Options: '1d', '1w', '1m', '3m', '6m', '1y', '2y', 'all'.
        :param str sort: Metric to sort the tweets by. Options: 'time'.
        """
        return self._request(f'/influencers/{influencer}', fast=fast, interval=interval, sort=sort)

    def get_insight(self, insight: str, type: str = 'coins') -> dict:
        """
        Get details on a specific insight (specified by insight ID).

        :param str type: The type of insight to fetch. Options: 'coins', 'nfts', 'global', 'nfts-global', 'influencers'.
        :param str insight: The ID of the insight to fetch details for, i.e. 'D1l133'.
        """
        return self._request(f'/insights/{insight}', type=type)

    def get_market_pairs(self, coin: str | int, limit: int = 100, page: int = 100, sort: str = None) -> dict:
        """
        Get a full list of market pairs across all available exchanges, and the data pertaining to the specific market
        exchange pair for any coin id or symbol. Data on each pair includes the exchange id, 1-day trading metrics,
        30-day trading metrics, price on the specific pairing, pairing URL, and timestamp of last update. You can sort
        the output by specifying a sort metric in the query parameters (name, market_sort, price, 1d_volume, 30d_volume,
        type, last_updated). This is a useful design to help monitor a coin's trading activity across available metrics.

        :param coin: ID or symbol of a coin/token to get market pairs for.
        :param limit: Limit the number of results.
        :param page: Page number starting at 0.
        :param sort: Sort the output by a metric. Options: 'name', 'market_sort', 'price', '1d_volume', '30d_volume',
                     'type', 'last_updated'.
        """
        return self._request(f'/market-pairs/{coin}', limit=limit, page=page, sort=sort)

    def get_nft_of_the_day(self) -> dict:
        """
        Get current LunarCrush NFT of the Day. The NFT of the Day is selected based on the collection with the
        highest combination of NFT Score™ and NFTRank™
        """
        return self._request('/nftoftheday')

    def get_nft_of_the_day_info(self) -> dict:
        """
        Get the previous history of NFT of the Day and when it was last updated.
        """
        return self._request('/nftoftheday/info')

    def get_nfts(self, sort: str = 'alt_rank', limit: int = None, desc: bool = False) -> dict:
        """
        Get a general snapshot of LunarCrush metrics on the entire list of tracked NFTs. It is designed as a lightweight
        mechanism for monitoring the universe of available NFT collections, either in aggregate or relative to each
        other. Metrics include NFT Score™, NFTRank™, floor price, volatility, 24h percent change, market cap, social
        mentions, social engagements, average sentiment, social contributors, social dominance, and categories. A more
        comprehensive and granular range of metrics on any specific collection can be found by calling the /nfts/:nft
        endpoint.

        :param sort: Sort the output by metric. Options: 'galaxy_score', 'nft_score', 'alt_rank', 'nft_rank', 'close',
                     'floor_price', 'percent_change_24h', 'social_volume', 'social_score', 'social_dominance',
                     'social_contributors', 'average_sentiment', 'market_cap', 'market_cap', 'volume', 'volume',
                     'market_dominance', 'market_cap_rank', 'holders', 'nfts', 'crypto_usd'.
        :param limit: Limit the number of results.
        :param desc: Pass any value as desc and the output will be reversed (descending).
        """
        return self._request('/nfts', sort=sort, limit=limit, desc=desc)

    def get_nft(self, nft: str | int) -> dict:
        """
        Get a robust and detailed snapshot of a specific NFT collection's metrics. This endpoint was designed to provide
        a granular look at the collection at the timestamp that the call is made. Depending on the call frequency, can
        be used as a time-series or pseudo real-time stream of all LunarCrush metrics as it pertains to a specific
        asset. Each call returns a current time-stamp of 60+ metrics related to the coin and includes the full suite of
        social metrics available on LunarCrush. Specify the coin to be queried by providing the numeric ID or the symbol
        of the coin in the input parameter, which can be found by calling the FREE /coins/list endpoint.

        :param nft: Provide the numeric id or lunar id of the NFT collection.
        """
        return self._request(f'/nft/{nft}')

    def get_nft_change(self, nft: str | int, interval: str = '1w') -> dict:
        """
        Get percentage change metrics for provided nft id or lunar id. The endpoint returns all the same metrics as the
        /nfts/:nft endpoint, but relative to a specified interval prior to the time of call. For example, calling the
        endpoint with a 1 week interval will provide the difference in either the sum or the average of the metric from
        the previous time period until the current time period, e.g. most recent 1 week vs. the 1 week prior to that.

        :param nft: Provide the numeric id or lunar id of the NFT.
        :param str interval: The % change since time interval to use. Options: '1d', '1w', '1m', '3m', '6m', '1y', '2y'.
        """
        return self._request(f'/nfts/{nft}/change', interval=interval)

    def get_nft_historical(self, nft: str | int) -> dict:
        """
        Get a full hourly time series data dump for all metrics provided by /nfts/:nft/time-series endpoint. It is
        designed to be a cheaper alternative for grabbing full historical data (as opposed to a specified interval) for
        back-testing and modeling. This is usually a > 10mb download and only includes data up to the most recently
        completed day.

        :param str | int nft: Provide the numeric id or symbol of the NFT or token.
        """
        return self._request(f'/nfts/{nft}/historical')

    def get_nft_influencers(self, nft: str | int, interval: str = '1w', order: str = 'influential',
                            limit: int = 100, page: int = None) -> dict:
        """
        Get a list of crypto influencers for a specified nft collection. It is sorted on influencer_rank (influential)
        by default but can be sorted by engagement, follower, or social media volume by specifying the sort criteria in
        the input parameters. Returns an influencers social media volume, volume rank, followers, followers rank,
        engagement, engagement rank, influencer rank, and weighted average rank. Also includes metadata like twitter
        handle, display name, profile and banner image.

        :param str | int nft: Provide the numeric id or symbol of the NFT or token.
        :param str interval: The time interval to use. Options: '1d', '1w', '1m', '3m', '6m', '1y', '2y', 'all'.
        :param str order: Order results. Options: 'influential', 'engagement', 'followers', 'volume'.
        :param int limit: Limit the number of results.
        :param int page: Page number starting at 0.
        """
        return self._request(f'/nfts/{nft}/influencers', interval=interval, order=order, limit=limit, page=page)

    def get_nft_insights(self, nft: str | int, metrics: str = None, limit: int = 10) -> dict:
        """
        Get a list of LunarCrush insights for a specific NFT collection. Insights are generated for any anomalies in the
        data or for any significant deviations from the moving average on a specific metric e.g. social contributors
        spikes 50% from the 90-day moving average. Useful for providing notifications or triggering trading or
        application functions based on “out of the ordinary” movements of an NFT collection metric. The return data for
        insights can also be filtered by specific metric  (social_volume, social_score, social_dominance,
        social_contributors, market_cap) by specifying in the "metrics" query parameter.

        :param str | int nft: Provide the numeric id or symbol of the NFT or token.
        :param str metrics: Filter insights to specific metrics. Options: 'social_volume', 'social_score',
                            'social_dominance', 'social_contributors', 'market_cap'.
        :param int limit: Limit the number of results.
        """
        return self._request(f'/nfts/{nft}/insights', metrics=metrics, limit=limit)

    def get_nft_time_series(self, nft: str | int, interval: str = '1w', start: datetime.datetime = None,
                            bucket: str = 'hour', data_points: int = None) -> dict:
        """
        Get the same metrics available on the /nfts/:nft endpoint in a series of discrete, memorialized time buckets
        (hourly or daily) over a certain time interval beginning at a specified start time. This time series endpoint
        differs from /nfts/:nft in that the latter provides real-time flexibility while the former provides the data at
        pre-specified hourly or daily timestamps, capped at 1000 data points. This endpoint was designed to provide
        historical data for research or back-testing purposes.

        :param str | int nft: Provide the numeric id or symbol of the NFT or token.
        :param str interval: The time interval to use. Options: '1d', '1w', '1m', '3m', '6m', '1y', '2y', 'a'.
        :param datetime.datetime start: The start time (datetime.datetime) to go back to.
        :param str bucket: Use hour or day time buckets / aggregates. Options: 'hour', 'day'.
        :param int data_points: The number of data points to fetch from the start time.

        """
        return self._request(f'/nfts/{nft}/time-series',
                             interval=interval, start=start, bucket=bucket, data_points=data_points)

    def get_nft_tokens(self, nft: str | int, sort: str = 'last_sold_amount',
                       limit: int = 100, desc: bool = False) -> dict:
        """
        Get details on all tokens within an NFT collection. An NFT collection more than often consists of a few discrete
        non-fungible tokens within the collection, provisioned by the same smart contract. The data returned here is a
        list of each available non-fungible token and it's within the collection, including token id, token url,
        description, image, last sold time, last sold amount, and lunar_id.

        :param nft: the numeric id or lunar_id of the NFT collection.
        :param sort: sort the output by metric. Options: 'last_sold_amount', 'last_sold_time', 'name'.
        :param limit: limit the number of results.
        :param desc: "True" to reverse the sorted order.
        :return:
        """
        return self._request(f'/nfts/{nft}/tokens', sort=sort, limit=limit, desc=desc)

    def get_nfts_global(self) -> dict:
        """
        Get aggregated metrics across all NFT collections tracked on the LunarCrush platform at the time of call. This
        is designed to be a global snapshot of the entire NFT market, and tracks the same social metrics - e.g. url
        shares, reddit volumes, twitter, twitter sentiment, social score, social volume, average sentiment.
        """
        return self._request('/nfts/global')

    def get_nfts_global_change(self, interval: str = '1w') -> dict:
        """
        Get percentage change metrics for aggregated metrics across all NFT collections tracked on the LunarCrush
        platform. The endpoint returns all the same metrics as the /nfts/global endpoint, but relative to a specified
        interval prior to the time of call. For example, calling the endpoint with a 1 week interval will provide the
        difference in either the sum or the average of the metric from the previous time period until the current time
        period, e.g. most recent 1 week vs. the 1 week prior to that.

        :param str interval: The time interval to use. Options: '1d', '1w', '1m', '3m', '6m', '1y', '2y', 'a'.
        """
        return self._request('/nfts/global/change', interval=interval)

    def get_nfts_global_historical(self) -> dict:
        """
        The full historical hourly time series data for nft global metrics. This is usually a > 10mb download and only
        includes data up to the most recently completed day.
        """
        return self._request('/nfts/global/historical')

    def get_nfts_global_insights(self, metrics: str = None, limit: int = 10) -> dict:
        """
        Get a list of LunarCrush insights for the global aggregated metrics across all NFT collections. Insights are
        generated for any anomalies in the data or for any significant deviations from the moving average on a specific
        metric e.g. bullish sentiment spikes 50% from the 90-day moving average. The return data for insights can also
        be filtered by specific metric (social_volume, social_score, social_contributors, market_cap) by specifying in
        the "metrics" query parameter.

        :param str metrics: Get a list of LunarCrush insights for the global aggregated metrics across all coins.
                            Insights are generated for any anomalies in the data or for any significant deviations from
                            the moving average on a specific metric e.g. bullish sentiment spikes 50% from the 90-day
                            moving average. Options: 'social_volume', 'social_score', 'social_contributors',
                            'market_cap', 'volume'.
        :param int limit: Limit the number of results.
        """
        return self._request('/nfts/global/insights', metrics=metrics, limit=limit)

    def get_nfts_global_time_series(self, interval: str = '1w', start: datetime.datetime = None,
                                    bucket: str = 'hour', data_points: int = None) -> dict:
        """
        Get the same metrics available on the /nfts/global endpoint in a series of discrete, memorialized time buckets
        (hourly or daily) over a certain time interval beginning at a specified start time. This time series endpoint
        differs from /nfts/global in that the latter provides real-time flexibility while the former provides the data
        at pre-specified hourly or daily timestamps, capped at 1000 data points. This endpoint was designed to provide
        historical data for research or back-testing purposes.

        :param str interval: The time interval to use. Options: '1d', '1w', '1m', '3m', '6m', '1y', '2y', 'a'.
        :param datetime.datetime start: The start time (datetime.datetime) to go back to.
        :param str bucket: Use hour or day time buckets / aggregates. Options: 'hour', 'day'.
        :param int data_points: The number of data points to fetch from the start time.

        """
        return self._request('/nfts/global/time-series',
                             interval=interval, start=start, bucket=bucket, data_points=data_points)

    def get_nfts_influencers(self, interval: str = '1w', order: str = 'influential',
                             limit: int = 100, page: int = None) -> dict:
        """
        Get a list of overall crypto influencers across all NFTs. It is sorted on influencer_rank (influential) by
        default but can be sorted by engagement, follower, or social media volume by specifying the sort criteria in
        the input parameters. Returns an influencers social media volume, volume rank, followers, followers rank,
        engagement, engagement rank, influencer rank, and weighted average rank. Also includes metadata like twitter
        handle, display name, profile and banner image.

        :param str interval: The time interval to use. Options: '1d', '1w', '1m', '3m', '6m', '1y', '2y', 'all'.
        :param str order: Order results. Options: 'influential', 'engagement', 'followers', 'volume'.
        :param int limit: Limit the number of results.
        :param int page: Page number starting at 0.
        """
        return self._request('/nfts/influencers', interval=interval, order=order, limit=limit, page=page)

    def get_nfts_insights(self, metrics: str = None, limit: int = 10,
                          volume: float = None, market_cap: float = None, alt_rank: int = None) -> dict:
        """
        Get a list of LunarCrush insights across all NFT collections. Insights are generated for any anomalies in the
        data or for any significant deviations from the moving average on a specific metric e.g. bullish sentiment
        spikes 50% from the 90-day moving average. The amount of deviation is provided in the response objects under
        the 'z-score' field. Useful for providing notifications or triggering trading or application functions based
        on “out of the ordinary” movements of a coin metric. The return data for insights can also be filtered by
        specific metric (galaxy_score, alt_rank, close, social_volume, social_score, social_dominance,
        social_contributors, market_cap, volume, market_dominance) by specifying in the "metrics" query parameter.

        :param str metrics: Filter insights to specific metrics. Options: 'social_volume', 'social_score',
                            'social_dominance', 'social_contributors', 'market_cap'.
        :param int limit: Limit the number of results.
        :param float volume: Minimum 24h volume on the NFT to filter by.
        :param float market_cap: Minimum market cap on the NFT to filter by.
        :param int alt_rank: Maximum alt rank on the NFT to filter by.
        """
        return self._request(f'/nfts/insights',
                             metrics=metrics, limit=limit, volume=volume, market_cap=market_cap, alt_rank=alt_rank)

    def get_nfts_list(self) -> dict:
        """
        Get a list of all supported NFTs in one output.
        """
        return self._request('/nfts/list')

    def get_opinions(self, context: str = None, sort: str = None) -> dict:
        """
        Get index of opinions for the main opinions screen. LunarCrush opinions are surveyed across all coin,
        NFT collection, influencer, social media content assets for bullish/bearish, quality, and other points of
        view. In addition, questions are proposed ad hoc by the LunarCrush team on a variety of topics and answered
        by users across the platform.

        :param context: Select the context. Options: 'all', 'global', 'coin', 'nft', 'feed', 'exchange', 'influencer'.
        :param sort: Sort the results by. Options: 'all', 'positive', 'negative', 'split'.
        """
        return self._request('/opinions', context=context, sort=sort)

    def get_opinions_summary(self) -> dict:
        """
        Get summary stats for opinions.
        """
        return self._request('/opinions/summary')

    def get_spark(self, spark_id: str) -> dict:
        """
        Get the sparks information for a single identifier.

        :param spark_id: The unique identifier for the spark which is formatted as {context_type}-{context_id}
                         as a single string, i.e. 'feeds-twitter-1544881801687994369'.
        """
        return self._request(f'/sparks/{spark_id}')

    def get_stats_lunrfi(self) -> dict:
        """
        Get global LunrFi stats.
        """
        return self._request('/stats/lunrfi')

    def get_top_mentions(self, interval: str = 'all', type: str = 'all', market: str = 'coins') -> dict:
        """
        Get the top word, emoji, or hashtag mentions from influential content.

        :param interval: The time interval to use. Options: '1d', '1w', '1m', '3m', '6m', '1y', '2y', 'all'.
        :param type: The type of mentions to show. Options: 'all', 'word', 'emoji', 'hashtag'.
        :param market: Choose an asset market. One of coins, nfts. Options: 'coins', 'nfts'.
        """
        return self._request('/top-mentions', interval=interval, type=type, market=market)
