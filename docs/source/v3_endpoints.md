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
