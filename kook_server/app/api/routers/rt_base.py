# coding=utf8
import zlib

from fastapi import APIRouter

# 定义路由
base_rt = APIRouter(prefix='/base', tags=['base'])

# 验证webhook服务器
@base_rt.post('/challenge')

async def handleChallenge(form_data:dict):

    print(form_data)

    # decompress_data = zlib.decompress(form_data)
    # print(decompress_data)

    decompress_data = form_data

    try:
        challenge = decompress_data.get('d').get('challenge')
        return {'challenge': challenge}
    
    except:
        print('faile')
        return {'challenge':'aaa'}