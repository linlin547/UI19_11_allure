import allure


class Test003:

    @allure.severity(allure.severity_level.BLOCKER)  # 最严重的
    def test_0031(self):
        assert True

    @allure.severity(allure.severity_level.CRITICAL)  # 严重的
    def test_0032(self):
        assert False

    @allure.severity(allure.severity_level.NORMAL)  # 一般的
    def test_0033(self):
        assert True

    @allure.severity(allure.severity_level.MINOR)  # 轻微的
    def test_0034(self):
        assert True

    @allure.severity(allure.severity_level.TRIVIAL)  # 忽略的
    def test_0035(self):
        assert True
