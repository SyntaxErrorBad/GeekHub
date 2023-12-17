import os
import csv
from itertools import islice
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from PIL import Image
import time




current_file_path = os.path.abspath(__file__)
parent_directory = os.path.dirname(current_file_path)

class ElseObjects:
    def option_chrome(self):
        options = Options()
        prefs = {
            "download.default_directory": parent_directory,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        }
        options.add_experimental_option("prefs", prefs)
        return options

    def pil_combine_img(self,name):
        image1 = Image.open("image0.png")
        image2 = Image.open("image1.png")
        image3 = Image.open("image2.png")

        width1, height1 = image1.size
        width2, height2 = image2.size
        width3, height3 = image3.size

        new_width = max(width1, width2, width3)
        new_height = height1 + height2 + height3
        result_image = Image.new("RGB", (new_width, new_height))

        result_image.paste(image1, (0, 0))
        result_image.paste(image2, (0, height1))
        result_image.paste(image3, (0, height1 + height2))

        result_image.save(f"{parent_directory}\\output\\{name}.png")
        self.delete_img()


    def delete_img(self):
        os.remove("image0.png")
        os.remove("image1.png")
        os.remove("image2.png")

    def save_imgs(self,imgs):
        for img in range(len(imgs)):
            with open(f"image{img}.png","wb") as file:
                file.write(imgs[img])


class OrdersRobots:
    def remove_file(self,url):
        file_name = url.split("/")[-1]
        os.remove(parent_directory+"\\"+file_name)
        return True

    def take_file_data(self,url):
        csv_file_path= parent_directory + "\\" + url.split("/")[-1]
        with open(csv_file_path,"r") as csvfile:
            csv_reader = csv.reader(csvfile)
            rows_from_second = islice(csv_reader, 1, None)
            return list(rows_from_second)

    def wait_download_csvfile(self,url):
        browser = self.browser
        file = url.split("/")[-1]
        WebDriverWait(browser, 2).until(
            lambda browser: file in os.listdir(parent_directory))

    def open_and_parse_csv_file_from_url(self):
        browser = self.browser
        url = "https://robotsparebinindustries.com/orders.csv"
        
        browser.get(url)

        self.wait_download_csvfile(url)
        data_list = self.take_file_data(url)

        self.remove_file(url)
        return data_list


class CheckElements:
    def check_element_by_id_element(self,element,id):
        try:
            element.find_element(By.ID,id)
            return True
        except:
            return False    
        
    def check_element_by_class_element(self,element,class_):
        try:
            element.find_element(By.CLASS_NAME,class_)
            return True
        except:
            return False 
    
    def wait_element_class(self,class_):
        element = WebDriverWait(self.browser, 3).until(
            EC.presence_of_element_located((By.CLASS_NAME, class_))
        )
        return element
    
    def wait_element_id(self,id):
        element = WebDriverWait(self.browser, 3).until(
            EC.presence_of_element_located((By.ID, id))
        )
        return element

class SeleniumBot(OrdersRobots,CheckElements):
    def __init__(self) -> None:
        self.obj = ElseObjects()
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=self.obj.option_chrome())

    def close_browser(self):

        self.browser.close()
        self.browser.quit()

    def check(self):
        print(self.open_and_parse_csv_file_from_url())

    def from_list_to_form_data(self):
        data = self.open_and_parse_csv_file_from_url()
        self.open_and_wait_orders_link()

        for dt in data:
            self.work_with_form(int(dt[1]),dt[2],dt[3],dt[4])
            time.sleep(3)
            if self.check_element_by_class_element(self.browser,"alert-buttons"):
                print(f"Parsing this data{dt}")
            self.close_pop_up_window()

    def open_and_wait_orders_link(self):
        url = "https://robotsparebinindustries.com/"
        self.browser.get(url)
        self.wait_and_switch_window()
        self.close_pop_up_window()

    def close_pop_up_window(self):
        element = self.wait_element_class("alert-buttons")
        element.find_element(By.CLASS_NAME,"btn.btn-dark").click()
            
    def wait_and_switch_window(self):
        self.wait_element_class("nav-link")
        lis = self.browser.find_elements(By.CLASS_NAME,"nav-link")
        for li in lis:
            if li.text == "Order your robot!":
                li.click()

    def work_with_form(self,head,body,legs,address):

        form = self.browser.find_element(By.CSS_SELECTOR,"form")
        div_blocks_mb_3 = form.find_elements(By.CLASS_NAME,"mb-3")
        for div_block in div_blocks_mb_3:
            if self.check_element_by_id_element(div_block,"head"):
                select = Select(div_block.find_element(By.CLASS_NAME,"custom-select"))
                select.select_by_index(head)
                time.sleep(1)

            elif self.check_element_by_class_element(div_block,"stacked"):
                inputs = div_block.find_elements(By.CLASS_NAME,"form-check-input")
                for in_put in inputs:
                    if in_put.get_attribute("value") == body:
                        in_put.click()
                        time.sleep(1)

            elif self.check_element_by_class_element(div_block,"form-control"):
                if self.check_element_by_id_element(div_block,"address"):
                    div_block.find_element(By.ID,"address").send_keys(address)
                    time.sleep(1)
                else:
                    div_block.find_element(By.CLASS_NAME,"form-control").send_keys(legs)
                    time.sleep(1)

        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        self.press_order(form)

    def press_order(self,form):
        for button in form.find_elements(By.CSS_SELECTOR,"button"):
            if button.text == "ORDER":
                self.browser.execute_script("arguments[0].click();", button)
        
        if self.check_element_by_class_element(self.browser,"alert.alert-danger"):
            time.sleep(2)
            self.press_order(form)


        self.save_img()

        new_order_button = self.browser.find_element(By.ID,"order-another")
        self.browser.execute_script("arguments[0].click();", new_order_button)
        
    def save_img(self):
        time.sleep(3)
        element = self.browser.find_element(By.ID,"robot-preview-image") 
        img_name = self.browser.find_element(By.CLASS_NAME,"badge.badge-success").text
        imgs = element.find_elements(By.CSS_SELECTOR,"img")
        m_list = []
        for img in imgs:
            m_list.append(img.screenshot_as_png)
        self.obj.save_imgs(m_list)
        self.obj.pil_combine_img(img_name)
        time.sleep(1)


def work_with_folder():
    folder_path = os.path.join(parent_directory,"output")
    if os.path.exists(folder_path):
        os.rmdir(folder_path)
        os.makedirs(folder_path)
    else:
        os.makedirs(folder_path)



def main():
    test = SeleniumBot()

    try:
        work_with_folder()
        test.from_list_to_form_data()
        test.close_browser()
    except Exception as e:
        print(e)
        test.close_browser()

if __name__ == "__main__":
    main()