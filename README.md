# auto_health_sign

**吉林大学每日自动健康打卡，配合腾讯云函数**

**每天四个时间段的自动打卡，四个时间段打卡提交的表单如下，具体参数值自行修改：**


    # 7:00 - 8:00
    form_Data = {
        "fieldXY2":"",
        "fieldWY":"1",
        "fieldXY1":"",
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
        "fieldZtw":"1",    # 早
        "fieldZtwyc":"",
        "fieldZhongtw":"",
        "fieldZhongtwyc":"",
        "fieldWantw":"",
        "fieldWantwyc":"",
        "fieldHide":"",
        "fieldXY3":""
    }


    # 11:00 - 12:00
    formData = {
        "fieldXY2":"",    # fieldXY 是否显示隐藏表项
        "fieldWY":"zhong",
        "fieldXY1":"1",
        "fieldSQrq":timestamp,    # 时间戳
        "fieldSQxm":xuehao,    # 姓名
        "fieldXH":xuehao,    # 学号
        "fieldSQxy":"bks_100",    # 学院  计算机科学与技术
        "fieldSQnj":"2118",    # 年级  2018级
        "fieldSQbj":"1203",    # 班级  211816
        "fieldSQxq":"1",    # 校区  中心校区
        "fieldSQgyl":"1",    # 公寓楼  北苑1公寓
        "fieldSQqsh":qinshi,    # 寝室号
        "fieldHidden":"",
        "fieldSheng":"",
        "fieldShi":"",
        "fieldQu":"",
        "fieldQums":"",
        "fieldZtw":"1",    # 早签到
        "fieldZtwyc":"",
        "fieldZhongtw":"1",    # 午签到
        "fieldZhongtwyc":"",
        "fieldWantw":"",    # 下午签到
        "fieldWantwyc":"",
        "fieldHide":"",
        "fieldXY3":""    # 晚签到
    }

    # 17:00 - 18:00
    formData = {"fieldXY2":"1",
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
                "fieldZtw":"1",
                "fieldZtwyc":"",
                "fieldZhongtw":"1",    # 中
                "fieldZhongtwyc":"",
                "fieldWantw":"1",    # 下午
                "fieldWantwyc":"",
                "fieldHide":"",
                "fieldXY3":""}

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
