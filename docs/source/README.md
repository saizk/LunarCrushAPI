# LunarCrush-API
Unofficial LunarCrush API v2 Wrapper for Python. No API key needed!

## Installation
LunarCrush-API is supported on **Python 3.6+**. You can install this package via pip:
```
pip install lunarcrush
```
## Quickstart
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

## Warning!
Due to the constant changes in LunarCrush internal API, some parameters might **NOT** work properly, making the server to response with a *5XX error*.
