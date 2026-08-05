import requests
import smtplib

NEWS_API_KEY = "YOUR_NEWS_API_KEY"

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = "YOUR_STOCK_API_KEY"

MY_EMAIL = "YOUR_EMAIL"
MY_PASSWORD = "YOUR_PASS"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    
params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": API_KEY,
}

def get_news():
    news_params = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    return articles[:3]  # Get the first 3 articles



response = requests.get(STOCK_ENDPOINT, params=params)
data = response.json()
time_series = data["Time Series (Daily)"]
days = list(time_series.keys())
yesterday_closing = float(time_series[days[0]]["4. close"])

day_before_yesterday_closing = float(time_series[days[1]]["4. close"])

difference = abs(yesterday_closing - day_before_yesterday_closing)
percentage_difference = (difference / day_before_yesterday_closing) * 100

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    
    if percentage_difference > 5:
        news = get_news()

        for article in news:
            message = f"Subject:Stock Alert!\n\n{STOCK_NAME}: {percentage_difference:.2f}%\nHeadline: {article['title']}\nBrief: {article['description']}"
            connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=MY_EMAIL,
                    msg=message.encode('utf-8')
                )
    else:
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Stock Alert!\n\nNo significant change in stock price."
        )



