## ディレクトリ構成

```sh
/nitteigen
│
├── index.py              # メインのCLIツールスクリプト
├── constants.py          # 定数や設定を管理するファイル
├── requirements.txt      # 必要なパッケージを記載したファイル
├── README.md             # プロジェクトの説明や使い方を記載するファイル
└── .gitignore            # Gitで管理しないファイルを指定するファイル
```

## 使用方法

```sh
$ pip install -r requirements.txt
$ python index.py --help
Usage: index.py [OPTIONS]

  日程調整を行い、土日や祝日を除外して日程を出力します。

Options:
  --start TEXT       日程の開始日 (YYYY-MM-DD形式)
  --end TEXT         日程の終了日 (YYYY-MM-DD形式)
  --start-time TEXT  デフォルトの開始時間 (例: 9:00)
  --end-time TEXT    デフォルトの終了時間 (例: 19:00)
  --help             Show this message and exit.

$ python index.py
2024-08-28 (水) 9:00 ~ 19:00
2024-08-29 (木) 9:00 ~ 19:00
2024-08-30 (金) 9:00 ~ 19:00
2024-09-02 (月) 9:00 ~ 19:00
2024-09-03 (火) 9:00 ~ 19:00
2024-09-04 (水) 9:00 ~ 19:00

除外された日付:
https://www8.cao.go.jp/chosei/shukujitsu/gaiyou.html
2024-08-31 (土) は土日祝日のため除外されました。
2024-09-01 (日) は土日祝日のため除外されました。

結果をクリップボードにコピーしますか？ (y/n): 
```


## 使用ライブラリ

- jpholiday: 日本の祝日を取得するライブラリ
https://github.com/Lalcs/jpholiday

- pyperclip: クリップボードを操作するライブラリ
https://github.com/asweigart/pyperclip

## TODO

- [ ] シンボリックリンクの作成方法を追記
- [ ] CLIツール用の管理ディレクトリを用意
- [ ] Cloudfareにデプロイ
- [ ] localStorageで設定情報を保存（ex. 日付のフォーマットをYYYY/MM/DDからYYYY年MM月DD日を選択できるなど

```
chmod +x index.py

# シンボリックリンクを作成
ln -s ~/git/samples/cli-tools/nitteigen/index.py ~/bin/nitteigen

# シンボリックリンクを削除
rm ~/bin/nitteigen
```
