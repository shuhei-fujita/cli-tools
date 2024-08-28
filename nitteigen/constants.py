## 定数を管理するためのファイルです

# デフォルトの時間帯設定
DEFAULT_START_TIME = "11:00"
DEFAULT_END_TIME = "13:00"

# 曜日を日本語に変換する辞書
WEEKDAY_JP = {
    "Monday": "月",
    "Tuesday": "火",
    "Wednesday": "水",
    "Thursday": "木",
    "Friday": "金",
    "Saturday": "土",
    "Sunday": "日"
}

# ログメッセージ
LOGS = {
    "excluded_weekend": "{date} ({weekday_jp}) は土日祝日のため除外されました。",
    "excluded_holiday": "{date} ({weekday_jp}) は {holiday_name} のため除外されました。",
    "excluded_summary": "除外された日付:\n" + "https://www8.cao.go.jp/chosei/shukujitsu/gaiyou.html",
    "copy_to_clipboard_prompt": "\n結果をクリップボードにコピーしますか？ (y/n): ",
    "copy_success": "結果がクリップボードにコピーされました！"
}

# 祝日のURL
HOLIDAY_URL = "https://www8.cao.go.jp/chosei/shukujitsu/gaiyou.html"
