# -*- coding: utf8 -*-
import requests
import re
import json
import time
import random
import urllib.parse
import warnings
warnings.filterwarnings("ignore")


def main_handler(event, context):
    return main()


def main():
    qiandao('renke2118', "密码, "寝室号")


if __name__ == '__main__':
    main()


def qiandao(username, password, qinshi):
    # 获取session
    sess = requests.session()
    sess.verify = False


    # 获取wengine_vpn_ticket
    url1_headers = {
        'Host': 'vpns.jlu.edu.cn',
        'Cache-Control': 'max-age=0',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36',
    }
    sess.post('https://vpns.jlu.edu.cn/', headers=url1_headers)
    cookie1 = ''
    for x in sess.cookies:
        cookie1 += x.name + '=' + x.value + ';'
    cookie1 = cookie1[:-1]


    # 登陆vpns.jlu.edu.cn
    url_2 = 'https://vpns.jlu.edu.cn/do-login?local_login=true'    
    url2_headers = {
        'Host': 'vpns.jlu.edu.cn',
        'Cache-Control': 'max-age=0',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36',
        'cookie': cookie1,
    }
    url2_data = 'auth_type=local&username='+username+'&sms_code=&password='+password
    sess.post(url_2, headers=url2_headers, data=url2_data)
    cookie2 = ''
    for x in sess.cookies:
        cookie2 += x.name + '=' + x.value + ';'
    cookie2 = cookie2[:-1]


    # 登陆打卡页面
    cookie_url = 'https://vpns.jlu.edu.cn/https/77726476706e69737468656265737421f5ff40902b7e625c6b468ca88d1b203b/sso/login'
    cookie_headers = {
        'Host': 'vpns.jlu.edu.cn',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36',
        'Cookie': cookie2,
    }
    cookie_data = 'username='+username+'&password='+password
    sess.post(cookie_url, headers=cookie_headers, data=cookie_data, verify=False)
    cookie = ''
    for x in sess.cookies:
        cookie += x.name + '=' + x.value + ';'
    cookie = cookie[:-1]



    # 获取元信息
    start_url = 'https://vpns.jlu.edu.cn/https/77726476706e69737468656265737421f5ff40902b7e625c6b468ca88d1b203b/infoplus/form/BKSMRDK/start'
    start_headers = {
        'Host': 'vpns.jlu.edu.cn',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36',
        'Cookie': cookie,
        'Referer': 'https://vpns.jlu.edu.cn/https/77726476706e69737468656265737421f5ff40902b7e625c6b468ca88d1b203b/infoplus/form/BKSMRDK/start'
    }
    start_res = sess.get(start_url, headers=start_headers, verify=False).text
    csrfToken = re.findall(re.compile(r'<meta itemscope="csrfToken" content="(\w*)'), start_res)[0]
    idc = re.findall(re.compile(r'id="idc" value="(\w*)'), start_res)[0] 
    release = re.findall(re.compile(r'id="release" value="(\w*)'), start_res)[0]



    # 获取当前表单的step_id
    get_url = 'https://vpns.jlu.edu.cn/https/77726476706e69737468656265737421f5ff40902b7e625c6b468ca88d1b203b/infoplus/interface/start?vpn-12-o2-ehall.jlu.edu.cn'
    get_headers = {   
        'X-Requested-With': 'XMLHttpR equest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie':  cookie,
    }
    get_data = 'idc='+idc+'&release='+release+'&csrfToken='+csrfToken
    resss = sess.post(get_url, headers = get_headers, data=get_data).text
    pp = json.loads(resss)['entities'][0]
    plus_url = re.findall(re.compile('(/infoplus.*)'), pp)[0]    # 用于获取个人信息
    step_id = re.findall(re.compile('/form/(\d*)'), pp)[0]    # step_id



    # 获取个人信息
    data_headers = {
        'X-Requested-With': 'XMLHttpRequest',
        'Host': 'vpns.jlu.edu.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36',
        'Referer': 'https://vpns.jlu.edu.cn/https/77726476706e69737468656265737421f5ff40902b7e625c6b468ca88d1b203b'+plus_url,
        'Cookie': cookie,
    }
    post_url = 'https://vpns.jlu.edu.cn/https/77726476706e69737468656265737421f5ff40902b7e625c6b468ca88d1b203b/infoplus/interface/render?vpn-12-o2-ehall.jlu.edu.cn'
    postPayload = {'stepId': step_id, 'csrfToken': csrfToken}
    r = sess.post(post_url, headers= data_headers, data=postPayload)
    data = json.loads(r.content)['entities'][0]


    # 6:00 -12:00
    data['data']["fieldSQxq"] = "1"
    data['data']["fieldSQgyl"] = "1"
    data['data']["fieldSQgyl"] = qinshi
    data['data']["fieldZtw"] = "1"    # 早、中签到

    #提交
    post_data = {
        'actionId': 1,
        'formData': json.dumps(data['data']),
        'nextUsers': '{}',
        'stepId': step_id,
        'timestamp': int(time.time()),
        'boundFields': ','.join(data['fields'].keys()),
        'csrfToken': csrfToken
    }

    # 开始签到
    post_headers = {
        'Host': 'vpns.jlu.edu.cn',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36',
        'Cookie': cookie,
    }
    post_url = 'https://vpns.jlu.edu.cn/https/77726476706e69737468656265737421f5ff40902b7e625c6b468ca88d1b203b/infoplus/interface/doAction?vpn-12-o2-ehall.jlu.edu.cn'


    r = sess.post(post_url, headers=post_headers, data=post_data)
    print(username+'签到信息：')
    print(r.content)
