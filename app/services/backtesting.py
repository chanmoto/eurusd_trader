from backtesting import Backtest, Strategy
from backtesting.lib import SignalStrategy, TrailingStrategy
import backtesting

import matplotlib.pyplot as plt
import pandas as pd

%matplotlib inline
from tqdm import tqdm

realdf = pd.read_csv(r'C://Users//User//Desktop//EURUSD.oj5k1.csv', sep=",",names=('date', 'time', 'Open', 'High', 'Low', 'Close', 'Volume'))
realdf.index = pd.to_datetime(realdf['date']+" "+realdf['time'])
realdf['signal']=-1


for item in img:
    v2,date = getprice(item,transform,0)   
    signal =GetSignal(v2)

    realdf.at[date, 'signal'] = signal
    

def SIGNAL():
    return realdf.signal

class pix2pix(Strategy):
    
    def init(self):
        self.signal1=self.I(SIGNAL)
        pass
    
    def next(self): #チャートデータの行ごとに呼び出される
        super().next()

        current_time = self.data.index[-1]
            
        if self.signal1>5 and self.signal1<100:
            #self.position.close()
            self.buy() # 買い
            
        elif self.signal1>0.001 and self.signal1<0.2:
            #self.position.close()
            self.sell()# 売り
    
        # Additionally, set aggressive stop-loss on trades that have been open 
        # for more than two days
        for trade in self.trades:
            if current_time - trade.entry_time > pd.Timedelta(5, "m"):
                self.position.close()
                    
                    
bt = Backtest(
    realdf, # チャートデータ
    pix2pix, # 売買戦略
    cash=100000, # 最初の所持金
    commission=0.000, # 取引手数料
    margin=0.5, # レバレッジ倍率の逆数（0.5で2倍レバレッジ）
    trade_on_close=True, # True：現在の終値で取引，False：次の時間の始値で取引
    exclusive_orders=True #自動でポジションをクローズ
)

output = bt.run() # バックテスト実行
print(output) # 実行結果(データ)
bt.plot() # 実行結果（グラフ）