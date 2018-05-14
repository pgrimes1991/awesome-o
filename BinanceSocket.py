# Binance API most recent data

from binance.client import Client as binance_client
from binance.websockets import BinanceSocketManager


if __name__ == '__main__':
    client = binance_client(keys)
    bm = BinanceSocketManager(client)

