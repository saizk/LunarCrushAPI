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