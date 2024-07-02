from flask import Flask, render_template, request

# Flaskアプリケーションを作成
app = Flask(__name__)

# カウンターの設定用クラス
class Counts:
    # クラス変数としてカウントを保持
    counts = {2: 0, 3: 0}

    # カウントをインクリメントするメソッド
    @classmethod
    def increment(cls, id):
        if id in cls.counts:
            cls.counts[id] += 1
        else:
            cls.counts[id] = 1

# カラーのマッピング（数値から色名への変換）
color_mapping = {
    1: "透明",
    2: "赤/ピンク",
    3: "オレンジ",
    4: "黄色/金色",
    5: "緑",
    6: "青",
    7: "紺",
    8: "紫",
    9: "光"
}

# 年の計算を行う関数
def seireki(year):
    # 年の数字をカラーにマッピング
    seireki_color = {
        1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9
    }
    # 年の各桁をリストに変換
    year_digits = [int(digit) for digit in str(year)]
    # 先頭2桁を合計
    front = sum(year_digits[:2])
    # 合計が10以上の場合は再度合計
    if front >= 10:
        front = sum(int(digit) for digit in str(front))

    # 後半2桁を合計
    end = sum(year_digits[2:])
    if end >= 10:
        end = sum(int(digit) for digit in str(end))

    # フロントとエンドの合計
    total = front + end
    if total >= 10:
        total = sum(int(digit) for digit in str(total))

    # 結果をカラーに変換して返す
    return seireki_color[total]

# 月日から計算を行う関数
def color(month, day):
    # 月と日の合計
    total = month + day
    if total >= 10:
        total = sum(int(digit) for digit in str(total))
        if total >= 10:
            total = sum(int(digit) for digit in str(total))

    # 数字をカラーにマッピング
    month_days_color = {
        1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9
    }
    return month_days_color[total]

# 合計計算を行う関数
def total(seireki, birthday):
    # 年と月日の合計
    total = seireki + birthday
    if total >= 10:
        total = sum(int(digit) for digit in str(total))

    # 数字をカラーにマッピング
    total_color = {
        1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9
    }
    return total_color[total]

# ルートパスでフォームを表示する
@app.route('/')
def index():
    return render_template('index.html')

# 結果を表示するパス
@app.route('/result', methods=['POST'])
def result():
    # フォームから送信されたデータを取得
    year = int(request.form['year'])
    month = int(request.form['month'])
    day = int(request.form['day'])

    # 西暦の計算結果
    seireki_result = seireki(year)
    # 生年月日の計算結果
    birthday_result = color(month, day)
    # 総合結果の計算
    total_result = total(seireki_result, birthday_result)

    # 数字をカラー名に変換
    seireki_color_name = color_mapping[seireki_result]
    birthday_color_name = color_mapping[birthday_result]
    total_color_name = color_mapping[total_result]

    # カウンターのインクリメント
    Counts.increment(2)
    Counts.increment(3)

    # 結果をテンプレートに渡して表示
    return render_template('result.html', seireki=seireki_color_name, birthday=birthday_color_name, total=total_color_name)

if __name__ == '__main__':
    app.run(debug=True)
