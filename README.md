# LunarCrush-API
LunarCrush API v2 Wrapper for Python. 

## Installation
LunarCrush-API is supported on Python 3.6+. You can install this package via pip:
```
pip install lunarcrush
```
## Quickstart
**1.** Sign up in <https://legacy.lunarcrush.com> and go to *Settings* & *API* to get the **API key**.

**2.** Create an instance of LunarCrush

```Python
from lunarcrush import LunarCrush

lc = LunarCrush('<YOUR API KEY>')
```

**3.** Start requesting information!

```Python
eth_1_year_data = lc.get_assets(symbol=['ETH'],
                                data_points=365, interval='day')
```


### API Endpoints
Here is a short description for the LunarCrush API v2 Endpoints.
You can find more details about the request parameters in <https://legacy.lunarcrush.com/developers/docs> 

* **get_assets():** Details, overall metrics, and time series metrics for one or multiple assets.
* **get_market_pairs()**	Provides the exchange information for assets, and the other assets they are being traded for.
* **get_market():**	Summary information for all supported assets (Markets page) including 5 recent time series values for some metrics.
* **get_global():**	Overall aggregated metrics for all supported assets (top of Markets page).
* **get_meta():**	Meta information for all supported assets
* **get_exchanges():**	Meta information for all exchanges that we track
* **get_exchange():**	Meta information and market pairs for a single exchange that we track
* **get_coin_of_the_day():**	The current coin of the day
* **get_coin_of_the_day_info():**	Provides the history of the coin of the day on LunarCRUSH when it was last changed, and when each coin was last coin of the day
* **get_feeds():**	Social posts, news, and shared links for one or multiple coins.
* **get_influencers():**	List of social accounts that have the most influence on different assets based on number of followers, engagements and volume of posts.
* **get_influencer():**	Individual influencer details including actual posts.
