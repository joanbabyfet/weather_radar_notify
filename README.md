## About
通过 telegram bot 发送雷达回波图，结合工作排程器或crontab功能可实现定时通知

## Feature

* 通过 telegram 机器人实现消息提醒
* 采集天气雷达回波图, 接口以 https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/O-A0058-003?Authorization=rdec-key-123-45678-011121314&format=JSON 为例
* 配置文件设置chat_id和token

## Requires
Python 3.11.0  
requests 2.28.1  
configparser 5.3.0  

## Usage
```
python main.py
```

## Change Log
v1.0.0

## Maintainers
Alan

## LICENSE
[MIT License](https://github.com/joanbabyfet/weather_radar_notify/blob/master/LICENSE)