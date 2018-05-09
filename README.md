## ArchiveWeBot

便捷的微信公众号文章备份工具，会将所有微信联系人（含自己）发送的分享类文章，自动备份到 <https://archive.is/>，并返回备份后的网址。

**注意**：该备份后的网址请用代理打开。

### 环境与依赖

**ArchiveWeBot** 使用了 [wxBot](https://github.com/liuwons/wxBot) 和 [archiveis](https://github.com/pastpages/archiveis)，只能运行于 Python2 环境。

需要安装依赖：

```bash
pip install requests
pip install pyqrcode
pip install pypng
pip install Pillow
pip install archiveis
```

### 运行

``` python
python ArchiveWeBot.py
```
如果想保持后台持续运行

```bash
nohup python ArchiveWeBot.py
```

程序运行之后，用微信扫描此二维码并按操作指示确认登录网页微信。
