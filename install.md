## pytho3、pip3のインストール及び更新

```bash
sudo apt update
sudo apt install -y python3-pip
python3 --version
pip3 --version
```

## 仮想環境のインストール
###  Python のバージョンが 3.12 でない場合は適宜バージョンを確認して変更してください

```bash
sudo apt install python3.12-venv
```

## 任意のディレクトリで仮想環境を作成
### ここでは「test」という名前で作成

```bash
python3 -m venv test
```

### 「test」仮想環境に入る

```bash
source test/bin/activate
```

### 仮想環境から抜ける

```bash
deactivate
```

## 仮想環境内で pytest をインストール


```bash
pip install pytest
```
