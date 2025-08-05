もちろん、tkinter で「**定期的にDBから情報を取得し、ラベル内容を更新する」」アプリのシンプルな例を紹介します。
前のラベルが残る問題は、「新しい値でラベルのテキストを書き換える」ことで解決します。
また、定期実行は after() を使ってイベントループを邪魔しない形で行うのがベストプラクティスです。

ここではDBアクセス部分は「ダミー関数」で示しています。実際にはDBアクセス部分を好きなコードに置き換えてください。

⸻

サンプルコード

import tkinter as tk
import sqlite3  # サンプル用。実際のDBに合わせて修正
import threading

# ダミー: データベースから値を取得する関数
def fetch_from_db():
    # 実際のDBアクセスをここに書く
    # 例: SQLiteで 'SELECT value FROM my_table LIMIT 1'
    # ここではダミーで時刻を返す
    import datetime
    return f"現在時刻: {datetime.datetime.now().strftime('%H:%M:%S')}"

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("定期DBアクセスサンプル")
        self.geometry("300x100")
        
        self.label = tk.Label(self, text="初期値", font=("Meiryo", 16))
        self.label.pack(pady=20)
        
        self.update_label()

    def update_label(self):
        # DBから値を取得
        new_text = fetch_from_db()
        # ラベルの内容を更新（前の内容は消える）
        self.label.config(text=new_text)
        # 1000ミリ秒後（1秒後）に再度この関数を呼び出す
        self.after(1000, self.update_label)

if __name__ == "__main__":
    app = App()
    app.mainloop()


⸻

ポイント
	•	ラベル内容の更新は self.label.config(text=新しい値) でOK。古い内容は残らず、都度書き換わります。
	•	定期的な実行は after(ミリ秒, 関数) を使うことでUIの応答性を落とさずに処理できます。
	•	DBアクセスが重い場合は threading を使いバックグラウンドでDB取得→afterでラベル更新、という設計も検討しましょう。

⸻

もし実際にDBアクセスを「バックグラウンドスレッドで実行」したい場合のサンプルも必要なら、そのパターンも追加で書きます。

（「本番ではDB接続が重い」ケースも多いので、その場合はスレッドで処理＆メインスレッドでラベルだけ更新するのが推奨です）

ご要望あれば追加でどうぞ！