import random, schedule, time

from twilio.rest import Client

QUOTES = [
    "You are a king",
    "My imagination is vivid and powerful",
    "Seeing and understanding the big picture comes naturally to me",
    "I am connected to the wisdom of the Universe",
    "I am able to see and act in alignment with my divine purpose"
]


def send_message(quotes_list=QUOTES):

    account = 'AC6f2e1e50d879fdf510e86edcc16c9f3c'
    token = 'f5f0629ea6c74c891652a072e5d79f83'
    client = Client(account, token)
    quote = quotes_list[random.randint(0, len(quotes_list)-1)]

    client.messages.create(to='+14235809433',
                           from_='+16087955604',
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