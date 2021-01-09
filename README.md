# auto_health_sign

**吉林大学每日自动健康打卡，配合腾讯云函数**

**现只需在两个时段打卡，之前四个时间段打卡提交的form_Data信息各参数解释如下（两个时段的参数含义类似）**

**此次更新后无需手动填写formData，通过https://vpns.jlu.edu.cn/https/77726476706e69737468656265737421f5ff40902b7e625c6b468ca88d1b203b/infoplus/interface/render?vpn-12-o2-ehall.jlu.edu.cn 自动获取个人所有信息。**

**如果学校更改了打卡需要填的表项，那么只需要手动打一次，以后都可以自动打上了**

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
