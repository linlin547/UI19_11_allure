import allure, time
from selenium import webdriver


class Test002:

    def setup(self):
        # 声明driver
        self.driver = webdriver.Chrome()
        # 访问百度
        self.driver.get("http://www.baidu.com")
        # 等待
        time.sleep(2)

    @allure.step("输入用户名")
    def input_name(self, name):
        pass

    @allure.step("输入密码")
    def input_password(self, pwd):
        pass

    @allure.step("登录步骤")
    def test_login(self):
        # 输入用户名
        self.input_name("lili")
        # 输入密码
        self.input_password("123456")
        # 添加文本附件到报告
        allure.attach("这是登录方法", "标题", allure.attachment_type.TEXT)

        # 添加PNg格式图片附件到报告
        allure.attach(self.driver.get_screenshot_as_png(), "图片名字", allure.attachment_type.PNG)

        self.driver.quit()
