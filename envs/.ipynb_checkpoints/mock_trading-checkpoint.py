import pandas as pd

class TradingSystem():
    def __init__(self, df, holdings, trade_step, cash, tc=0.002):
        self.cash = cash
        self.df = df # columns: time, close0, itvl, datetime, close1, spread, zscore
        self.tc = tc # transaction cost
        self.holdings = holdings #[400, -300] That means we have 400 unit of leg0 and -300 unit of leg1
        self.trade_step = trade_step

    def close_position(self):
        self.cash += (self.holdings[0]*self.df.iloc[self.trade_step]['close0'] + self.holdings[1]*self.df.iloc[self.trade_step]['close1']) * (1-self.tc)
        self.holdings = [0, 0]

        return self.cash, self.holdings

    def open_position(self, action):
        self.close_position()

        max_units_leg0 = self.cash/self.df.iloc[self.trade_step]['close0']
        max_units_leg1 = self.cash/self.df.iloc[self.trade_step]['close1']

        if action == 0:
            self.holdings = [-max_units_leg0*(1-self.tc), max_units_leg1*(1-self.tc)]
        elif action == 2:
            self.holdings = [max_units_leg0*(1-self.tc), -max_units_leg1*(1-self.tc)]

        return self.cash, self.holdings

    def get_holdings(self):
        return self.holdings

    def get_networth(self):
        return self.cash + self.holdings[0]*self.df.iloc[self.trade_step]['close0'] + self.holdings[1]*self.df.iloc[self.trade_step]['close1']
