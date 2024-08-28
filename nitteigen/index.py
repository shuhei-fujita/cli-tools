#!/usr/bin/env python

import click
import datetime
import jpholiday
import pyperclip
from constants import DEFAULT_START_TIME, DEFAULT_END_TIME, WEEKDAY_JP, LOGS

@click.command()
@click.option('--start', default=None, help='日程の開始日 (YYYY-MM-DD形式)')
@click.option('--end', default=None, help='日程の終了日 (YYYY-MM-DD形式)')
@click.option('--start-time', default=DEFAULT_START_TIME, help='デフォルトの開始時間 (例: 9:00)')
@click.option('--end-time', default=DEFAULT_END_TIME, help='デフォルトの終了時間 (例: 19:00)')
def generate_schedule(start, end, start_time, end_time):
    """日程調整を行い、土日や祝日を除外して日程を出力します。"""

    # 開始日と終了日をパース
    if start:
        start_date = datetime.datetime.strptime(start, '%Y-%m-%d').date()
    else:
        start_date = datetime.date.today()

    if end:
        end_date = datetime.datetime.strptime(end, '%Y-%m-%d').date()
    else:
        end_date = start_date + datetime.timedelta(days=7)  # デフォルトで1週間後

    # 日程を生成
    current_date = start_date
    valid_dates = []  # 有効な日付を保存するリスト
    excluded_dates = []  # 除外された日付を保存するリスト

    while current_date <= end_date:
        weekday = current_date.strftime('%A')
        weekday_jp = WEEKDAY_JP.get(weekday, weekday)

        # 土日または祝日を除外
        if current_date.weekday() >= 5:  # 土曜日 (5) または 日曜日 (6)
            excluded_dates.append(LOGS["excluded_weekend"].format(date=current_date, weekday_jp=weekday_jp))
        elif jpholiday.is_holiday(current_date):  # 祝日判定
            holiday_name = jpholiday.is_holiday_name(current_date)
            excluded_dates.append(LOGS["excluded_holiday"].format(date=current_date, weekday_jp=weekday_jp, holiday_name=holiday_name))
        else:
            valid_dates.append(f"{current_date} ({weekday_jp}) {start_time} ~ {end_time}")

        # 次の日に進む
        current_date += datetime.timedelta(days=1)

    # 結果を表示
    for valid_date in valid_dates:
        print(valid_date)

    if excluded_dates:
        print("\n" + LOGS["excluded_summary"])
        for excluded_date in excluded_dates:
            print(excluded_date)

    # 結果をクリップボードにコピーするか確認
    copy_to_clipboard = input(LOGS["copy_to_clipboard_prompt"]).lower()
    if copy_to_clipboard == 'y':
        result_text = '\n'.join(valid_dates)
        pyperclip.copy(result_text)
        print(LOGS["copy_success"])

if __name__ == '__main__':
    generate_schedule()
