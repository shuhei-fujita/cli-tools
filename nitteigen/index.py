#!/usr/bin/env python3

import click
import datetime
import jpholiday
import pyperclip
from constants import DEFAULT_START_TIME, DEFAULT_END_TIME, WEEKDAY_JP, HOLIDAY_URL
from utils.date_utils import parse_date, get_date_range
from utils.log_utils import format_valid_date, format_excluded_date

@click.command()
@click.option('--start', default=None, help='日程の開始日 (YYYY-MM-DD形式)')
@click.option('--end', default=None, help='日程の終了日 (YYYY-MM-DD形式)')
@click.option('--start-time', default=DEFAULT_START_TIME, help='デフォルトの開始時間 (例: 9:00)')
@click.option('--end-time', default=DEFAULT_END_TIME, help='デフォルトの終了時間 (例: 19:00)')
def generate_schedule(start, end, start_time, end_time):
    """日程調整を行い、土日や祝日を除外して日程を出力します。"""

    start_date = parse_date(start) if start else datetime.date.today()
    end_date = parse_date(end) if end else start_date + datetime.timedelta(days=7)

    valid_dates = []
    excluded_dates = []

    for current_date in get_date_range(start_date, end_date):
        weekday = current_date.strftime('%A')
        weekday_jp = WEEKDAY_JP.get(weekday, weekday)

        if current_date.weekday() >= 5:  # 土日
            excluded_dates.append(format_excluded_date(current_date, weekday_jp, "週末"))
        elif jpholiday.is_holiday(current_date):  # 祝日
            holiday_name = jpholiday.is_holiday_name(current_date)
            excluded_dates.append(format_excluded_date(current_date, weekday_jp, holiday_name))
        else:
            valid_dates.append(format_valid_date(current_date, weekday_jp, start_time, end_time))

    for valid_date in valid_dates:
        print(valid_date)

    if excluded_dates:
        print("\n除外された日付:\n" + HOLIDAY_URL)
        for excluded_date in excluded_dates:
            print(excluded_date)

    copy_to_clipboard = input("\n結果をクリップボードにコピーしますか？ (y/n): ").lower()
    if copy_to_clipboard == 'y':
        result_text = '\n'.join(valid_dates)
        pyperclip.copy(result_text)
        print("結果がクリップボードにコピーされました！")

if __name__ == '__main__':
    generate_schedule()
