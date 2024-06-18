import requests
from mutagen.mp3 import MP3
from app.services.AuthV3Util import addAuthParams


# 您的应用ID
APP_KEY = '6737e7d609d1eeb0'
# 您的应用密钥
APP_SECRET = 'zIjyyt1ByziKMQHIH8UW8qVEsSFkJiBs'


def createRequest(text, voice_name, audio_file):
    '''
    note: 将下列变量替换为需要请求的参数
    '''
    q = text
    voiceName = voice_name
    format = 'mp3'

    data = {'q': q, 'voiceName': voiceName, 'format': format}

    addAuthParams(APP_KEY, APP_SECRET, data)

    header = {'Content-Type': 'application/x-www-form-urlencoded'}
    res = doCall('https://openapi.youdao.com/ttsapi', header, data, 'post')
    saveFile(res, audio_file)
    duration = get_mp3_duration(audio_file)
    return duration


def doCall(url, header, params, method):
    if 'get' == method:
        return requests.get(url, params)
    elif 'post' == method:
        return requests.post(url, params, header)


def saveFile(res, PATH):
    contentType = res.headers['Content-Type']
    if 'audio' in contentType:
        fo = open(PATH, 'wb')
        fo.write(res.content)
        fo.close()
        print('save file path: ' + PATH)
    else:
        print(str(res.content, 'utf-8'))


def get_mp3_duration(file_path):
    audio = MP3(file_path)
    return audio.info.length


# # 网易有道智云语音合成服务api调用demo
# # api接口: https://openapi.youdao.com/ttsapi
# if __name__ == '__main__':
#     createRequest("生命的意义是什么", 'youkejiang', "./" )
