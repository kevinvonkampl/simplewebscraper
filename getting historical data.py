import requests
from bs4 import BeautifulSoup

def get_historical_stock_prices(symbol, start_date, end_date):

  url = "https://finance.yahoo.com/quote/{}/history?period1={}&period2={}&interval=1d&includeAdjustedClose=true".format(symbol, start_date, end_date)
  response = requests.get(url)
  soup = BeautifulSoup(response.content, "html.parser")

  table = soup.find("table", class_="W(100%) Bdcl(c)")
  rows = table.find_all("tr")

  stock_prices = []
  for row in rows[1:]:
    columns = row.find_all("td")
    stock_price = {
      "Date": columns[0].text,
      "Open": columns[1].text,
      "High": columns[2].text,
      "Low": columns[3].text,
      "Close": columns[4].text,
      "Volume": columns[5].text,
    }
    stock_prices.append(stock_price)

  return stock_prices


def main():
  symbol = "AAPL"
  start_date = "2023-01-01"
  end_date = "2023-09-16"

  stock_prices = get_historical_stock_prices(symbol, start_date, end_date)
  if stock_prices is None:
    print("Error: Could not scrape historical stock prices.")
  for stock_price in stock_prices:
    print(stock_price)


if __name__ == "__main__":
  main()