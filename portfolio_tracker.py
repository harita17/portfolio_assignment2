from yahoo_finance import Share
from sys import argv
import re

script, filename = argv 

def get_data_from_portfolio(filename):
    dict_data = {}
    filedata = open(filename)
    lines = filedata.readlines()
    lines = map(lambda s: s.strip(), lines)
    
    for i, line in enumerate(lines):
        dict_data[i] = eval(str(line))
        
    for key, portfolio_data in dict_data.items():
        dict_data[key] = [((symbol.replace(' ', '').upper()), abs(count))
        for symbol, count in portfolio_data if count != 0]
    return dict_data
    filedata.close()

def get_stock_price(symbol):  
    value= Share(symbol)
    stock_price = value.get_price()
    return stock_price
   
def get_full_portfolio_value(dict_d):
    for k in dict_d.keys():
        total = 0

        for symbol, count in dict_d[k]:
        
            total += float(get_stock_price(symbol))* float((count))

        dict_d[total] = dict_d[k]
        del dict_d[k]
    return dict_d

def sort_descending(portfolio_dict):

    for k in sorted(portfolio_dict, reverse=True):
        for x, y in portfolio_dict[k]:
            print (x.replace(' ', ''), y),
        print

if __name__ == '__main__':

       
    symbol_data = get_full_portfolio_value(get_data_from_portfolio(filename))
    sort_descending(symbol_data)

                

