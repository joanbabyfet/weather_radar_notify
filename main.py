import requests
import configparser

# 配置文件
config_file = 'config.ini'

# 发送文字信息
def send_message(text):
    conf = configparser.ConfigParser()
    conf.read(config_file, encoding='utf-8') # 这里要加utf-8, 否则会报错, 默认gbk
    config_section  = 'telegram_config'
    token   = conf.get(config_section, 'token') # 存取令牌
    chat_id = conf.get(config_section, 'chat_id') # 用户或群组id

    data = {
        'chat_id': chat_id,
        'text': text,
        'parse_mode': 'HTML',
        'disable_web_page_preview': True
    }
    resp = requests.post(f'https://api.telegram.org/bot{token}/sendMessage', json = data)
    return resp.json()

def send_photo(img_url):
    conf = configparser.ConfigParser()
    conf.read(config_file, encoding='utf-8') # 这里要加utf-8, 否则会报错, 默认gbk
    config_section  = 'telegram_config'
    token   = conf.get(config_section, 'token') # 存取令牌
    chat_id = conf.get(config_section, 'chat_id') # 用户或群组id

    data = {
        'chat_id': chat_id,
        'photo': img_url,
    }
    resp = requests.post(f'https://api.telegram.org/bot{token}/sendPhoto', json = data)
    return resp.json()

# 获取天气雷达回波图
def get_weather_radar():
    radar_img = ''
    radar_time = ''

    url = 'https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/O-A0058-003?Authorization=rdec-key-123-45678-011121314&format=JSON'
    resp = requests.get(url)
    resp.encoding = 'utf-8' # 使用与网页相对应的编码格式, 避免乱码
    data = resp.json()

    if data:
        radar_img = data['cwbopendata']['dataset']['resource']['uri'] # 字段大小写要区分, 否则获取到数据
        radar_time = data['cwbopendata']['dataset']['time']['obsTime'] # 获取图片更新时间
    return [radar_img, radar_time]

def main():
    try:
        info = get_weather_radar() # 获取图片
        ret1 = send_message('從雷達回波看看會不會下雨～') # 先送文字信息再送图片
        ret2 = send_photo(info[0])

        print(f'雷达回波 {info[1]} 通知成功')
    except Exception as e:
        print(f'雷达回波 {e} 通知失败')

if __name__ == '__main__': # 主入口
    main()