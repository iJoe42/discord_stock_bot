import requests
import json
import interactions
import datetime

def fetch_stock_info(url, number, mode):
    #get stocks information and put into a dictionary
    response = requests.get(url)

    data_dict = json.loads(response.text)
    if data_dict == []:
        print("Could not retrieve data")
        return interactions.Embed(title="Could not retrieve data")

    stock_info = data_dict["stocks"]

    #formatted time string
    time_now = datetime.datetime.now()
    time_string = time_now.strftime("%H:%M   %d/%m/%Y")

    #create an instance of embed object
    embed_return = interactions.Embed(title=f"Top {number} {mode}  @  {time_string}")

    col_symbol = []
    col_percentChange = []
    col_last = []    

    #insert value into lists
    #available keys: "symbol", "sign", "prior", "last", "change", "percentChange", "high", "low", "totalVolume", "totalValue", "aomVolume", "aomValue", "rankingValue"
    for rank in range(len(stock_info)):
        col_symbol.insert(rank, stock_info[rank]["symbol"])
        col_percentChange.insert(rank, round(stock_info[rank]["percentChange"], 2))
        col_last.insert(rank, stock_info[rank]["last"])        

    #convert elements in list to string
    col_symbol_str = list(map(str, col_symbol))
    col_percentChange_str = list(map(str, col_percentChange))
    col_last_str = list(map(str, col_last))    

    #concatenating values string
    str_symbol = ""
    str_percentChange = ""
    str_last = ""

    for i in range(len(stock_info)):
        str_symbol = str_symbol + col_symbol_str[i] + "\n"
        str_percentChange = str_percentChange + col_percentChange_str[i] + "\n"
        str_last = str_last + col_last_str[i] + "\n"

    embed_return.add_field(name="Symbol", value="**" + str_symbol + "**", inline=True)
    embed_return.add_field(name="Change(%)", value="**" + str_percentChange + "**", inline=True)
    embed_return.add_field(name="Last Price", value=str_last, inline=True)

    return embed_return

#--------------------------------------------------#

def fetch_top_gainer(number):
    top_gainer_url = f"https://www.settrade.com/api/set/ranking/topGainer/SET/S?count={number}"
    mode = "Gainer"
    embed_return = fetch_stock_info(top_gainer_url, number, mode)
    return embed_return

def fetch_top_loser(number):
    top_loser_url = f"https://www.settrade.com/api/set/ranking/topLoser/SET/S?count={number}"
    mode = "Loser"
    embed_return = fetch_stock_info(top_loser_url, number, mode)
    return embed_return