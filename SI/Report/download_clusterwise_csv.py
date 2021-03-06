import os
import time

from selenium.webdriver.support.select import Select

from Data.parameters import Data
from get_dir import pwd
from reuse_func import GetData


class donwload_clusterwise_csv():
    def __init__(self,driver):
        self.driver = driver

    def test_clusterwise(self):
        self.p = GetData()
        self.driver.find_element_by_xpath(Data.hyper).click()
        self.p.page_loading(self.driver)
        p =pwd()
        District_wise=Select(self.driver.find_element_by_name("downloadType"))
        District_wise.select_by_index(3)
        time.sleep(3)
        self.driver.find_element_by_id(Data.Download_scator).click()
        time.sleep(10)
        self.filename = p.get_download_dir() + "/Cluster_level_Infra_Report.csv"
        self.p.page_loading(self.driver)
        return os.path.isfile(self.filename)

    def remove_csv(self):
        os.remove(self.filename)


