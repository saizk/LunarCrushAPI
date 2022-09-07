# LunarCrushAPI
![PyPI version](https://img.shields.io/pypi/v/lunarcrush)

Unofficial LunarCrush API **v2** and **v3** Wrapper for Python. No API key needed for LCv2!

## 💽 Installation
LunarCrushAPI is supported on **Python 3.6+**. You can install this package via pip:
```
pip install lunarcrush
```
## 🔍 Quickstart for LunarCrush API v2
**1.** Create an instance of LunarCrush

```Python
from lunarcrush import LunarCrush

lc = LunarCrush()
```

**2.** Start requesting information!

```Python
eth_1_year_data = lc.get_assets(symbol=['ETH'],
                                data_points=365, interval='day')
```

## 🔍 Quickstart for LunarCrush API v3
**1.** Create an instance of LunarCrushV3

```Python
from lunarcrush import LunarCrushV3

lcv3 = LunarCrushV3('<YOUR API KEY>')
```

**2.** Start requesting information!

```Python
eth_insights = lcv3.get_coin_insights(coin='ETH', metrics='social_volume')
```

## 📜 API v2 Endpoints
Here is a short description for the LunarCrush API v2 Endpoints.

| Method                                                                | Description                                                                                                                             | Not authorized parameters |
|-----------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|---------------------------|
| ```get_assets(symbol, time_series_indicators, change, data_points)``` | Details, overall metrics, and time series metrics for one or multiple assets.                                                           | (*~~start~~*, *~~end~~*)  |
| ```get_market(limit, page, sort)```                                   | Summary information for all supported assets (Markets page) including 5 recent time series values for some metrics.                     |                           |
| ```get_market_pairs(symbol, limit, page)```                           | Provides the exchange information for assets, and the other assets they are being traded for.                                           |                           |
| ```get_global(interval, change, data_points)```                       | Overall aggregated metrics for all supported assets (top of Markets page).                                                              |                           |
| ```get_meta(type)```                                                  | Meta information for all supported assets                                                                                               |                           |
| ```get_exchange(exchange)```                                          | Meta information and market pairs for a single exchange that we track                                                                   |                           |
| ```get_exchanges(limit, order_by)```                                  | Meta information for all exchanges that we track                                                                                        |                           |
| ```get_coin_of_the_day()```                                           | The current coin of the day                                                                                                             |                           |
| ```get_coin_of_the_day_info()```                                      | Provides the history of the coin of the day on LunarCRUSH when it was last changed, and when each coin was last coin of the day         |                           |
| ```get_feeds(sources, page, type, limit)```                           | Social posts, news, and shared links for one or multiple coins.                                                                         | (*~~start~~*, *~~end~~*)  |
| ```get_influencer(id, screen_name, days, page)```                     | Individual influencer details including actual posts.                                                                                   | (*~~limit~~*)             |
| ```get_influencers(symbol, days, num_days, order_by)```               | List of social accounts that have the most influence on different assets based on number of followers, engagements and volume of posts. | (*~~limit~~*)             |

## ⚠️ Warning!
Some parameters might **NOT** work properly for LunarCrush API v2, making the server to response with a *5XX error*.


## 📰 API v3 Endpoints

| Method                                                 | Endpoint                  |
|--------------------------------------------------------|---------------------------|
| ```get_coin_of_the_day()```                            | /coinoftheday             |
| ```get_coin_of_the_day_info()```                       | /coinoftheday/info        |
| ```get_coins(sort, limit, desc)```                     | /coins                    |
| ```get_coin(coin)```                                   | /coins/{coin}             |
| ```get_coin_change(coin, interval)```                  | /coins/{coin}/change      |
| ```get_coin_historical(coin)```                        | /coins/{coin}/historical  |
| ```get_coin_influencers(coin, interval, order)```      | /coins/{coin}/influencers |
| ```get_coin_insights(coin, metrics, limit)```          | /coins/{coin}/insights    |
| ```get_coin_meta(coin)```                              | /coins/{coin}/meta        |
| ```get_coin_time_series(coin, interval, start)```      | /coins/{coin}/time-series |
| ```get_coins_global()```                               | /coins/global             |
| ```get_coins_global_change(interval)```                | /coins/global/change      |
| ```get_coins_global_historical()```                    | /coins/global/historical  |
| ```get_coins_global_insights(metrics, limit)```        | /coins/global/insights    |
| ```get_coins_global_time_series(interval, start)```    | /coins/global/time-series |
| ```get_coins_influencers(interval, order)```           | /coins/influencers        |
| ```get_coins_insights(metrics, limit)```               | /coins/insights           |
| ```get_coins_list()```                                 | /coins/list               |
| ```get_exchanges(order, limit)```                      | /exchanges                |
| ```get_exchange(exchange)```                           | /exchanges/{exchange}     |
| ```get_feeds(limit, since, hours, days, sources)```    | /feeds                    |
| ```get_feed(feed)```                                   | /feeds/{feed}             |
| ```get_influencer(influencer, fast, interval, sort)``` | /influencers/{influencer} |
| ```get_insight(insight, type)```                       | /insights/{insight}       |
| ```get_market_pairs(coin, limit, page, sort)```        | /market-pairs/{coin}      |
| ```get_nft_of_the_day()```                             | /nftoftheday              |
| ```get_nft_of_the_day_info()```                        | /nftoftheday/info         |
| ```get_nfts(sort, limit, desc)```                      | /nfts                     |
| ```get_nft(nft)```                                     | /nft/{nft}                |
| ```get_nft_change(nft, interval)```                    | /nfts/{nft}/change        |
| ```get_nft_historical(nft)```                          | /nfts/{nft}/historical    |
| ```get_nft_influencers(nft, interval, order)```        | /nfts/{nft}/influencers   |
| ```get_nft_insights(nft, metrics, limit)```            | /nfts/{nft}/insights      |
| ```get_nft_time_series(nft, interval, start)```        | /nfts/{nft}/time-series   |
| ```get_nft_tokens(nft, sort)```                        | /nfts/{nft}/tokens        |
| ```get_nfts_global()```                                | /nfts/global              |
| ```get_nfts_global_change(interval)```                 | /nfts/global/change       |
| ```get_nfts_global_historical()```                     | /nfts/global/historical   |
| ```get_nfts_global_insights(metrics, limit)```         | /nfts/global/insights     |
| ```get_nfts_global_time_series(interval, start)```     | /nfts/global/time-series  |
| ```get_nfts_influencers(interval, order)```            | /nfts/influencers         |
| ```get_nfts_insights(metrics, limit)```                | /nfts/insights            |
| ```get_nfts_list()```                                  | /nfts/list                |
| ```get_opinions(context, sort)```                      | /opinions                 |
| ```get_opinions_summary()```                           | /opinions/summary         |
| ```get_spark(spark_id)```                              | /sparks/{spark_id}        |
| ```get_stats_lunrfi()```                               | /stats/lunrfi             |
| ```get_top_mentions(interval, type, market)```         | /top-mentions             |

You can visit [LunarCrush API v3 documentation](https://lunarcrush.com/developers/api/endpoints) for a more detailed description of all the endpoints and parameters.

## 📈 Metrics description
| Metric           | Description                                                                                                                                                                                                                                                                                                                                         |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **GALAXY SCORE** | The Galaxy Score™ indicates how healthy a coin is by looking at combined performance indicators across markets and social engagement. Display the real-time Galaxy Score™ of any coin.                                                                                                                                                              |
| **ALT RANK**     | AltRank™ measures a coin's performance VS. all other coins that we actively support. In general, it is a unique measurement that combines ALT coin price performance relative to Bitcoin and other social activity indicators across the entire crypto market. A coin can have a high AltRank of 1 even in a bear market situation.                 |
| **INFLUENCERS**  | View Twitter influencer activity and their impact across all coins and tokens. All influencers are measured by the same metrics, which includes followers, replies, favorites, and retweets. Metrics are evaluated across all collected posts during the timeframe selected. Actual influence will vary over time and will depend on user activity. |
| **CANDLESTICK**  | The incredibly powerful Candlestick widget takes any data point and compares it to price over a specified timeframe.                                                                                                                                                                                                                                |
| **WORD CLOUD**   | Uncover keywords used throughout collected social content for any coin. The Word Cloud is generated from all recent and available social posts from Twitter and Reddit. It looks at frequency of mentions. All data is segmented by either all coins or specific, individual coins.                                                                 |
| **SOCIAL FEED**  | Display social feeds from multiple sources including Twitter, Reddit, news channels and more all at once. Gain unique insights into what's being talked about in real time. All social feeds have been cleaned with spam removed and can be organized by coin.                                                                                      |
