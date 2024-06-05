import unittest
from HTMLTestRunner import HTMLTestRunner


class TestHTMLTestRunnerPY3(unittest.TestCase):
    def test_py3_success(self):
        self.assertEqual(1 + 1, 2)

    def test_py3_fail(self):
        self.assertEqual(1 + 1, 2)


class TestHTML(unittest.TestCase):
    def test_html_success(self):
        self.assertEqual(1 + 2, 3)


class TestError(unittest.TestCase):
    def test_error(self):
        self.assertEqual(2 / 1, 2)


class report(unittest.TestCase):
    import os
    print("done")
    report = os.path.join(r'D:\PycharmProjects\软件测试脚本\2022-08-19 184846result.html')
    st = unittest.TestSuite()
    st.addTests([TestHTMLTestRunnerPY3('test_py3_success'), TestHTMLTestRunnerPY3('test_py3_fail'),
                 TestHTML('test_html_success'), TestError('test_error')])
    with open(r'C:\Users\10260\PycharmProjects\soft-test-main\软件测试脚本\运营平台自动化\pom\test_case_report\2022-08-19 184846result.html', 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='示例测试报告', description='执行人：灰蓝')
        runner.run(st)


if __name__ == '__main__':
    unittest.main()
