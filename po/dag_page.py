from selenium.webdriver.support.select import Select

from po.base import BasePage


class DagManagePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def create_dag(self):
        self.driver.find_element(*create_dag_button).click()

    def select_module(self):
        self.driver.find_element(*model_tab).click()

    def run_dag(self):
        self.driver.find_element(*dag_run_button).click()

    def select_dag(self, dag_name, index, value):
        selector = Select(self.driver.find_element(*select_dag_list))
        if dag_name is not None:
            return selector.select_by_visible_text(dag_name)
        elif index is not None:
            return selector.select_by_index(index)
        elif value is not None:
            return selector.select_by_value(value)


    # 恢复任务 - 重跑失败任务
    def recovery_task(self):
        pass

    # 查询任务
    def query_dag(self, dag_id):
        pass




class DagDetailPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)