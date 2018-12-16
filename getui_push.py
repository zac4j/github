# get_info_list -> push it

import requests

import sys

sys.path.append('/Users/zac/PycharmProjects/github/lib/getui')
from lib.getui import RequestException
from lib.getui.igetui.igt_target import Target
from lib.getui.igetui.template.igt_link_template import LinkTemplate
from lib.getui.igt_push import IGeTui
from lib.getui.igetui.igt_message import IGtSingleMessage

app_id = 'Epo2omNkQb7DuIsFKALHU3'
app_key = 'DxthNnRdwH9Tj0aNnAvnj8'
master_sec = 'JIbUKV6FYiAg6OebEsXqr3'
client_id = 'a481f21dbba2db69976c0b867353a81b'
api_url = 'http://sdk.open.api.igexin.com/apiex.htm'


def get_info_list():
    api = 'https://api.github.com/search/repositories?q='
    query = 'topic:crawler+language:python+'
    full_url = api + query
    print(full_url)
    r = requests.get(full_url)
    return r.json()['items']


def make_message(repo_info):
    title = repo_info['name']
    url = repo_info['html_url']
    text = repo_info['description']
    return {'title': title, 'text': text, 'url': url}


def push_message(msg_info):
    push = IGeTui(api_url, app_key, master_sec)

    # 新建一个推送模版, 以链接模板为例子，就是说在通知栏显示一条含图标、标题等的通知，用户点击可打开您指定的网页
    template = LinkTemplate()
    template.appId = app_id
    template.appKey = app_key
    print(msg_info)
    template.title = msg_info['title']
    template.text = msg_info['text']
    template.url = msg_info['url']
    template.logo = ""
    template.transmissionType = 1
    template.transmissionContent = ''
    template.isRing = True
    template.isVibrate = True
    template.isClearable = True

    # 定义"AppMessage"类型消息对象，设置消息内容模板、发送的目标App列表、是否支持离线发送、以及离线消息有效期(单位毫秒)
    message = IGtSingleMessage()
    # 是否离线推送
    message.isOffline = True
    # 离线有效时间
    message.offlineExpireTime = 1000 * 3600 * 12
    message.data = template
    # 推送的网络类型：(0:不限;1:wifi;2:4G/3G/2G)
    # message.pushNetWorkType = 2

    target = Target()
    target.appId = app_id
    target.clientId = client_id

    try:
        ret = push.pushMessageToSingle(message, target)
        print(ret)
    except RequestException as e:
        requstId = e.getRequestId()
        ret = push.pushMessageToSingle(message, target, requstId)
        print(ret)


info = get_info_list()[0]
msg = make_message(info)
push_message(msg)
