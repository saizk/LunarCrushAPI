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
