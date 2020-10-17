# -*- coding: utf8 -*-
import requests
import re
import json
import time
import random
import urllib.parse


def main_handler(event, context):
    return main()


def main():
    qiandao('renke2118', "*******", "********", "*********")


if __name__ == '__main__':
    main()
  

def qiandao(username, password, xuehao, qinshi):
    
    # 获取session
    sess = requests.session()


    # 获取wengine_vpn_ticket
    url1 = 'https://vpns.jlu.edu.cn/'    
    url1_headers = {
        'Host': 'vpns.jlu.edu.cn',
        'Cache-Control': 'max-age=0',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36',
    }
    sess.post(url1, headers=url1_headers, verify=False)
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
    sess.post(url_2, headers=url2_headers, data=url2_data, verify=False)
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
    }
    start_res = sess.get(start_url, headers=start_headers, verify=False).text
    csrfToken = re.findall(re.compile(r'<meta itemscope="csrfToken" content="(\w*)'), start_res)[0]
    idc = re.findall(re.compile(r'id="idc" value="(\w*)'), start_res)[0] 
    release = re.findall(re.compile(r'id="release" value="(\w*)'), start_res)[0]
    # print(idc, release, csrfToken)


    # 获取当前表单的step_id
    get_url = 'https://vpns.jlu.edu.cn/https/77726476706e69737468656265737421f5ff40902b7e625c6b468ca88d1b203b/infoplus/interface/start?vpn-12-o2-ehall.jlu.edu.cn'
    get_headers = {   
        'X-Requested-With': 'XMLHttpR equest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie':  cookie,
    }
    get_data = 'idc='+idc+'&release='+release+'&csrfToken='+csrfToken
    resss = sess.post(get_url, headers = get_headers, data=get_data, verify=False).text
    # print(resss)
    pp = json.loads(resss)['entities'][0]
    pattern = re.compile('(/infoplus.*)')
    plus_url = re.findall(pattern, pp)[0]
    step_pattern = re.compile('/form/(\d*)')
    step_id = re.findall(step_pattern, pp)[0]
    # print(plus_url, step_id)
    
    # 21:00 - 22:00
    formData = {
        "fieldXY2":"1",
        "fieldWY":"wan",
        "fieldXY1":"1",
        "fieldSQrq":timestamp,
        "fieldSQxm":xuehao,
        "fieldXH":xuehao,
        "fieldSQxy":"bks_100",  
        "fieldSQnj":"2118",
        "fieldSQbj":"1203",
        "fieldSQxq":"1",
        "fieldSQgyl":"1",
        "fieldSQqsh":qinshi,
        "fieldHidden":"",
        "fieldSheng":"",
        "fieldSheng_Name":"",
        "fieldShi":"",
        "fieldQu":"",
        "fieldQums":"",
        "fieldZtw":"1",    # 早晨
        "fieldZtwyc":"",
        "fieldZhongtw":"1",    # 中午
        "fieldZhongtwyc":"",
        "fieldWantw":"1",    # 下午
        "fieldWantwyc":"",
        "fieldHide":"",
        "fieldXY3":"晚点名"    # 晚
    }
    
    boundFields = "fieldXH,fieldZtw,fieldHidden,fieldSQqsh,fieldSQbj,fieldSQgyl,fieldQums,fieldQu,fieldSQxm,fieldWantw,fieldSQxy,fieldWY,fieldXY1,fieldZtwyc,fieldXY2,fieldXY3,fieldZhongtw,fieldSQxq,fieldShi,fieldWantwyc,fieldSQnj,fieldSheng,fieldZhongtwyc,fieldHide,fieldSQrq"
    
    # 开始签到
    post_headers = {
        'Host': 'vpns.jlu.edu.cn',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36',
        'Cookie': cookie,
    }
    post_url = 'https://vpns.jlu.edu.cn/https/77726476706e69737468656265737421f5ff40902b7e625c6b468ca88d1b203b/infoplus/interface/doAction?vpn-12-o2-ehall.jlu.edu.cn'
    post_data = {
        'actionId': 1,
        'formData': formData,
        'remark': '',
        'rand': rand,
        'nextUsers': "{}",
        'stepId': step_id,
        'timestamp': timestamp,
        'boundFields': boundFields,
        'csrfToken': csrfToken,
        'lang': 'zh',
    }
    post_data = urllib.parse.urlencode(post_data)
    post_res = sess.post(post_url, headers=post_headers, data=post_data, verify=False).text
    print(post_res)

    # server酱推送
    textPush = username + '签到信息'
    despPush = post_res
    urlPush = 'https://sc.ftqq.com/SCU107843T2f8731d8dcbb7b6fdae07ccb585b9c705f23e6e52ede8.send'    # 填写自己的推送地址，http://sc.ftqq.com/?c=wechat&a=bind
    dataPush = {'text':textPush, 'desp':despPush}
    requests.post(urlPush, data=dataPush, verify=False)
