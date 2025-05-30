# python-calender

## 概要
Python（tkinter）で作成したシンプルなカレンダーアプリケーションです。月ごとのカレンダー表示や前月・次月への移動が可能です。

## スクリーンショット / デモ
（ここにアプリのスクリーンショットやデモGIFを追加してください）

## 必要なライブラリ
- Python 3.8以上
- tkinter（標準ライブラリ）
- calendar（標準ライブラリ）
- datetime（標準ライブラリ）

## セットアップ方法
1. [uv](https://github.com/astral-sh/uv) をインストール（未導入の場合）:
   ```bash
   pip install uv
   ```
2. 依存パッケージのインストール:
   ```bash
   uv pip install -r requirements.txt
   ```
   ※ 本アプリは標準ライブラリのみで動作しますが、追加パッケージが必要な場合は `pyproject.toml` に記載してください。

## 実行方法
```bash
python calendar_app.py
```

## 既知の問題・今後の改善点
- 祝日表示や予定管理機能の追加
- スクリーンショットやデモGIFの追加
- デザインの改善

---
ご意見・ご要望は Issue でお知らせください。
