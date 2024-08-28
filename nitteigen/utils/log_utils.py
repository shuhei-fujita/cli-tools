def format_valid_date(date, weekday_jp, start_time, end_time):
    return f"{date} ({weekday_jp}) {start_time} ~ {end_time}"

def format_excluded_date(date, weekday_jp, reason):
    return f"{date} ({weekday_jp}) は {reason} のため除外されました。"
