# import os
import pandas as pd
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest
from alpaca.trading.enums import AssetClass, AssetExchange

api_key = 'PK69JQXXJDRKR8QOSO35'
api_secret = 'nUWFkbNixWaKgz9UgYAuQuNiuTqvihbUaoEVa50o'

trading_client = TradingClient(api_key, api_secret, paper=True)

search_params = GetAssetsRequest(asset_class=AssetClass.US_EQUITY)
assets = trading_client.get_all_assets(search_params)

OTC = AssetExchange("OTC")
AMEX = AssetExchange("AMEX")
ARCA = AssetExchange("ARCA")
BATS = AssetExchange("BATS")
NYSE = AssetExchange("NYSE")
NASDAQ = AssetExchange("NASDAQ")
asset_list = [OTC, AMEX, ARCA, BATS, NYSE, NASDAQ]

assets_dict = [dict(item) for item in assets]
df = pd.DataFrame.from_records(assets_dict)
df.loc[df['exchange'].isin(asset_list)]
print(df.head(3))