# 模拟淘宝登录，2022-4-20
import requests
import json
# 创建会话对象
session = requests.Session()

class LoginTaobao:
    def __init__(self, username, ua, password2):
        """
        使用用户名密码登录淘宝
        :param username: 用户名
        :param ua: ua参数
        :param password2: 加密后的密码
        """
        # 检查输入用户名后是否需要验证码的链接
        self.check_url = "https://login.taobao.com/newlogin/account/check.do?appName=taobao&fromSite=0&_bx-v=2.0.31"
        # 登录URL
        self.login_url = "https://login.taobao.com/newlogin/login.do?appName=taobao&fromSite=0&_bx-v=2.0.31"
        # 访问st码URL
        self.st_url = ""
        # 用户名
        self.username = username
        self.ua = ua
        self.password2 = password2

        def _check_user(self):
            data = {
                "username": self.username,
                "ua": self.ua
            }
            try:
                get_resp = session.post(url=self.check_url, data=data)
                get_resp.raise_for_status()
                # print()
            except Exception as error:
                print("请求失败，原因{}".format(error))
            result = get_resp.json()['needcode']
            print(result)
            return result


if __name__ == "__main__":
    username = "翱翔的鹰17"
    ua = "140#422DZKAFzzFzcQo2KiKswpSrciOmo1x6zwGO+iYGyEsCl1GhQR8IlaC5lxKDmkKWVx7gR+qlu/ewO/3bfZQJlp1zzqx0yE7shFzxy2Yd7tluzzrb22U3lp1xzB+TVOgBlQrzKID+V3hAGRfV2X83oQ1xz8rFIXVqlTux2PH+K6h/zQrFL283lSTdzWQiVdzHjd0I1wba7XETY02trcyy69MRH4Bd3vBrLUEsPmMcm1c9iQeudjBf58YuV28qPhr4P5yivdhfaZnNLLj+CSMTuu5R6IG2jXz06vghcHm4/hOrkPVc3SzawhZy6TahiCdjrVEL1gzgoApj4H6mziTfy6io0fxwBWIZ935qiO20fie9Z1qVYYgS+Fvrs7A25UcWwHagz+lpUCzZc/pZHcvV2Izh37mF1EjJQ+W5Ulw3Zeqxkh57STCOalcYvg27+5qKmzM6qiJrQ0jFFGpGNscf6YxIq9B4wlB61HYDyRqQV2Zwal4jiBx4yv04xU7NSJF+oYRZU0YzSkrTPK2cPuPEahUAvwAjpUva7sKQ4M6gBMM3qJRDbuLy4XcixnRgyfJqQRBEzhFyFnwCK66PsvN7XKIn0SSs4GPx4Sx97CgdYjrk3NiNEJpRSdf431MYtL8guJv4sm+jTtXral81BRdpLqWxciXqH5RJ1mDqSr7K42kJW6RdGga4shjWOl/GphRpwwkGy0+VA/7YPqIF9Ms3iGmRq9N9M/r9KL73ZwK7h6BTgKSZtuAhoqhDmp7vbVfch9oR5j1OhR0sanKtnSGDZHATXcryNyCTDsxF0mahnGf+FIZe2jyjiT6EBUXCR16phaRB5wv4bqtcXhEGTtI/yP2s92iJSd03diw7laYqjk1+TNf4yHLKvU9z/HueWg/s2K+aZ2hVLmAqFPpZPk27TmqVMcqTKxfZFL3IHWbIPOkForIWIhy3VzEvRtTd2s2V7Uu0roq66i9oXZNNkhOFqfav+f9WpgzsUEYcAX+YOD2Trsf2U3t3xnCnSwqG0Ea2saOyDoJ++9P1wUPSiLDGqKUgBDQkeXFQZBR2YcnleDcSu8BbLEcC6jEyOliEo+uLu5CVeU0hS8tGwgDobi2WboOvg+J6rajFf+DrTnEfmC+="
    login = LoginTaobao(username=username, ua=ua)



