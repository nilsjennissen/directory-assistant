import datetime


def timer():
    now = datetime.datetime.now()
    return now.strftime(f"<----- NEW RUN ----->: %Y-%m-%d %H:%M:%S\n")


print(timer())
