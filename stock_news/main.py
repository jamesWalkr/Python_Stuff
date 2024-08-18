import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = ""
NEWS_API_KEY = ""

twilio_account_sid = ''
twilio_auth_token = ''

STOCK_PARAMS = {
    'function': "TIME_SERIES_DAILY",
    'symbol': STOCK_NAME,
    'apikey': STOCK_API_KEY
}

NEWS_PARAMS = {
    'q': "tesla",
    'from': "2024-04-16",
    'sortBy': "publishedAt",
    'apiKey': NEWS_API_KEY
}


def send_text(list_of_articles):
    for news_article in list_of_articles:
        client = Client(twilio_account_sid, twilio_auth_token)
        message = client.messages.create(
            from_='',
            body={news_article},
            to='+'
        )
        print(message.status)


# STEP 1: Use https://www.alphavantage.co/documentation/#daily


# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
response = requests.get('https://www.alphavantage.co/query', STOCK_PARAMS)
response.raise_for_status()
data = response.json()['Time Series (Daily)']
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_close_price = float(yesterday_data['4. close'])

# TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_close_price = float(day_before_yesterday_data['4. close'])

# TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
print(
    f"yesterday's closing price: {yesterday_close_price}, day before yesterday's closing price: {day_before_yesterday_close_price}")
diff = abs(yesterday_close_price - day_before_yesterday_close_price)

# TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
avg = (yesterday_close_price + day_before_yesterday_close_price) / 2
ratio = diff / avg
percent = ratio * 100
percent_diff = round(percent, 2)
print(f"percent difference: {percent_diff}")

# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if percent_diff > 1:
    print("sending News artilces...")

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

    # TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    news_response = requests.get('https://newsapi.org/v2/everything', NEWS_PARAMS)
    news_response.raise_for_status()
    news_data = news_response.json()['articles']
    # print(news_data)
    # TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    news_list = news_data[:3]
    # print(len(news_list))
    # print(news_list)

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    # to send a separate message with each article's title and description to your phone number.

    # TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    article_list = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in news_list]
    # print(article_list)

# TODO 9. - Send each article as a separate message via Twilio.
    send_text(article_list)
