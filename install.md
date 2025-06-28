```bash
sudo apt update
sudo apt install -y python3-pip
python3 --version
pip3 --version

sudo apt install python3.12-venv

# 任意のディレクトリで仮想環境を作成
python3 -m venv codingbat

# 仮想環境を有効化（Linux/macOS）
source codingbat/bin/activate

# 仮想環境内で pytest をインストール
pip install pytest
```