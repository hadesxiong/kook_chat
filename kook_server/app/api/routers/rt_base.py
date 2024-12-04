# coding=utf8
import zlib,json

from fastapi import APIRouter

from app.utils.decrypt import CookEncrypt
from app.core.config import settings

# 定义路由
base_rt = APIRouter(prefix='/base', tags=['base'])

# 验证webhook服务器
@base_rt.post('/challenge')

async def handleChallenge(form_data:dict):

    print(form_data)

    # decompress_data = zlib.decompress(form_data)
    # print(decompress_data)

    decompress_data = form_data

    kook_encryptor = CookEncrypt(settings.KOOK_KEY)
    
    decrypt_str = kook_encryptor.aes_decrypt(form_data.get('encrypt'))
    decrypt_data = json.loads(decrypt_data)
    print(decrypt_data)

    print(type(decrypt_data))
    print(decrypt_data.get('d'))

    try:
        challenge = decrypt_data.get('d').get('challenge')
        return {'challenge': challenge}
    
    except:
        print('fail')
        return {'challenge':'aaa'}