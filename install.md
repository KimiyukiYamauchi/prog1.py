```bash
sudo apt update
sudo apt install -y python3-pip
python3 --version
pip3 --version

#  Python のバージョンが 3.12 でない場合は適宜バージョンを確認して変更してください
sudo apt install python3.12-venv

# 任意のディレクトリで仮想環境を作成(ここでは「test」)
python3 -m venv test

# 仮想環境に入る
source test/bin/activate

# 仮想環境から抜ける
deactivate

# 仮想環境内で pytest をインストール
pip install pytest
```
