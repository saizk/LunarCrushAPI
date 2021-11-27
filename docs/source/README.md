# LunarCrush-API
LunarCrush API v2 Wrapper for Python. 

## Installation
LunarCrush-API is supported on Python 3.6+. You can install this package via pip:
```
pip install lunarcrush
```
# Quickstart
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