import random, schedule, time

from twilio.rest import Client

QUOTES = [
    "I am love. I am purpose. I was made with divine intention",
    "I don’t sweat the small stuff",
    "I can. I will. End of story",
    "I feed my spirit. I train my body. I focus my mind. It’s my time",
    "I am in charge of how I feel and today I am choosing happiness"
]


def send_message(quotes_list=QUOTES):

    account = 'ACCOUNT'
    token = 'TOKEN'
    client = Client(account, token)
    quote = quotes_list[random.randint(0, len(quotes_list)-1)]

    client.messages.create(to='personal_phone',
                           from_='account_phone',
                           body=quote
                           )

# send a message every hour
schedule.every().hour.at(":00").do(send_message, QUOTES)

# testing
schedule.every().minute.at(":00").do(send_message, QUOTES)

while True:
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(2)
