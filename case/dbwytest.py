# coding=utf-8

import time

import logging

from utils.mytestcase import mytestcase
from utils.logincookie import dengLuPage
from utils.screenshort import get_screenshort


class dbwytest(mytestcase):
    """担保无忧测试集"""

    def test_dbwy(self):
        """担保无忧测试"""

        # logging.basicConfig(filename='../LOG/' + __name__ + '.log',
        #                     format='[%(asctime)s-%(filename)s-%(levelname)s: %(message)s]', level=logging.DEBUG,
        #                     filemode='a', datefmt='%Y-%m-%d%I:%M:%S %p')
        dl = dengLuPage(self.driver)
        # 官方推荐有find_element(By.*(""))代替find_element_by_*("")
        # self.driver.find_element_by_id()
        # self.driver.find_element()
        dl.dengLu()
        time.sleep(2)
        self.driver.find_element_by_css_selector("#com-navbar > div > ul > li:nth-child(1) > a").click()
        time.sleep(1)
        self.assertIn("商标注册-权大师", self.driver.title)
        print(self.driver.title)
        # abwy注册
        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-serviceItems > table > tbody > tr > td.td-cont > ul > li:nth-child(2)").click()

        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:"+a.text)
            aa=a.text

        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
        self.driver.find_element_by_name("ownerContactPerson").send_keys("全大师")
        self.driver.find_element_by_css_selector(
            "body > div.myOrder-wrap > div.section-myorder.width1200 > div > table:nth-child(2) > tbody > tr:nth-child(2) > td.td-2 > input").send_keys(
            "15624992498")
        self.driver.find_element_by_css_selector(
            "body > div.myOrder-wrap > div.section-myorder.width1200 > div > table:nth-child(2) > tbody > tr:nth-child(3) > td.td-2 > input").clear()
        self.driver.find_element_by_css_selector(
            "body > div.myOrder-wrap > div.section-myorder.width1200 > div > table:nth-child(2) > tbody > tr:nth-child(3) > td.td-2 > input").send_keys(
            "4564564@qq.com")
        self.driver.find_element_by_css_selector("#remark").send_keys("test")

        get_screenshort(self.driver, "test_dbwy.png")

        for i in self.driver.find_elements_by_css_selector("body > div.myOrder-wrap > div.section-myorder.width1200 > div > div > ul > li.row-sense > em > i"):
            print("总价:"+i.text)
            ii=i.text

        self.assertIn(aa,ii)
        print("价格一致")


        self.driver.find_element_by_css_selector(
            "body > div.myOrder-wrap > div.section-myorder.width1200 > div > div > ul > li.row-step > a.btn-next.submitOrder").click()
        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:"+o.text)
            oo=o.text

        self.assertIn(oo,ii)

        print("测试通过")

        self.driver.find_element_by_css_selector("#alisubmit").click()