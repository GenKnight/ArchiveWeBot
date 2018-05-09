#!/usr/bin/env python
# coding: utf-8
#

from wxbot import *
import archiveis

class MyWXBot(WXBot):
    def handle_msg_all(self, msg):
        if (msg['msg_type_id'] == 4) and msg['content']['type'] == 7:
            self.send_msg_by_uid(archiveis.capture(msg['content']['data']['url']), msg['user']['id'])
            self.send_msg_by_uid(u'请复制上述链接在墙外打开', msg['user']['id'])


def main():
    bot = MyWXBot()
    bot.DEBUG = True
    bot.conf['tty'] = 'png' # 非 Linux 服务器环境请将 tty 改为 qr
    bot.run()


if __name__ == '__main__':
    main()
