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

## ⚠️ Warning!
Some parameters might **NOT** work properly for LunarCrush API v2, making the server to response with a *5XX error*.


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

## 📰 API v3 Endpoints
You can find a detailed description of all the endpoints and parameters for LunarCrush API v3 in <https://lunarcrush.com/developers/api/endpoints>.

## 📋 Response fields
A short description of the response fields can be found in the [example](examples/doge.jsmin) response.


## 📈 Metrics description
| Metric           | Description                                                                                                                                                                                                                                                                                                                                         |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **GALAXY SCORE** | The Galaxy Score™ indicates how healthy a coin is by looking at combined performance indicators across markets and social engagement. Display the real-time Galaxy Score™ of any coin.                                                                                                                                                              |
| **ALT RANK**     | AltRank™ measures a coin's performance VS. all other coins that we actively support. In general, it is a unique measurement that combines ALT coin price performance relative to Bitcoin and other social activity indicators across the entire crypto market. A coin can have a high AltRank of 1 even in a bear market situation.                 |
| **INFLUENCERS**  | View Twitter influencer activity and their impact across all coins and tokens. All influencers are measured by the same metrics, which includes followers, replies, favorites, and retweets. Metrics are evaluated across all collected posts during the timeframe selected. Actual influence will vary over time and will depend on user activity. |
| **CANDLESTICK**  | The incredibly powerful Candlestick widget takes any data point and compares it to price over a specified timeframe.                                                                                                                                                                                                                                |
| **WORD CLOUD**   | Uncover keywords used throughout collected social content for any coin. The Word Cloud is generated from all recent and available social posts from Twitter and Reddit. It looks at frequency of mentions. All data is segmented by either all coins or specific, individual coins.                                                                 |
| **SOCIAL FEED**  | Display social feeds from multiple sources including Twitter, Reddit, news channels and more all at once. Gain unique insights into what's being talked about in real time. All social feeds have been cleaned with spam removed and can be organized by coin.                                                                                      |
