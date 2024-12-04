# coding=utf8

import base64

from Crypto.Cipher import AES

class CookEncrypt:

    def __init__(self,key,bs=32):

        pad = lambda x: x+(bs-len(x))*"\0"
        key = pad(key)
        self.key = key.encode('utf-8')

    def aes_decrypt(self,content):

        str = base64.b64decode(content)
        iv = str [0:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return cipher.decrypt(base64.b64decode(str[16:])).decode('utf-8')