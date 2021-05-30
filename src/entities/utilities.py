from datetime import datetime


def format_timestamp(timestamp):
    dt_obj = datetime.fromisoformat(timestamp)
    human_time = dt_obj.strftime('%a, %d %b %Y %l:%M %p %Z')
    return human_time

