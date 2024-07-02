import sys
import logging

# プロジェクトのパスを指定する
sys.path.insert(0, '/path/to/your/project')

# Flaskアプリケーションをインポートする
from app import app as application

# ログを設定する
logging.basicConfig(stream=sys.stderr)
