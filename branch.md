## Git のローカルブランチを、GitHub に別の名前で push したい場合

### ✅ コマンド構文

```bash
git push origin ローカルブランチ名:リモートブランチ名
```

### ✅ 例：p1 というローカルブランチを、t25001 という名前で GitHub に push したい場合

```bash
git push origin p1:t25001
```

### 🔁 追跡ブランチとして設定したい場合（以後、pull/push が楽になる）

```bash
git push -u origin p1:t25001
```

## リモートブランチを削除するコマンド

### ✅ コマンド構文

```bash
git push origin --delete ブランチ名

```

### ✅ 例：t25001 ブランチを GitHub から削除したい場合

```bash
git push origin --delete t25001

```
