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
from PIL import Image
from urllib.parse import urljoin
import time
import logging
import shutil


logging.basicConfig(level=logging.INFO) 
current_file_path = os.path.abspath(__file__)
parent_directory = os.path.dirname(current_file_path)


def write_logging(log):
    logging.info(log)


def option_chrome():
    options = Options()
    prefs = {
        "download.default_directory": parent_directory, 
        "download.prompt_for_download": False, 
        "download.directory_upgrade": True, 
        "safebrowsing.enabled": True
    }
    options.add_experimental_option("prefs",  prefs)
    return options


class ElementWaiter:
    def __init__(self,  browser):
        self.browser = browser

    def wait_for_element_by_class(self,  class_name,  timeout=3):
        return WebDriverWait(self.browser,  timeout).until(
            EC.presence_of_element_located((By.CLASS_NAME,  class_name))
        )

    def wait_for_element_by_id(self,  element_id,  timeout=3):
        return WebDriverWait(self.browser,  timeout).until(
            EC.presence_of_element_located((By.ID,  element_id))
        )

    def wait_element_by_click_by_class(self,  class_name,  timeout=3):
        return WebDriverWait(self.browser,  timeout).until(
            EC.element_to_be_clickable((By.CLASS_NAME,  class_name))
        )

    @staticmethod
    def wait_by_user_count(count = 2):
        time.sleep(count)


class FileManager:
    @staticmethod
    def remove_file(url):
        file_name = url.split("/")[-1]
        os.remove(os.path.join(parent_directory,  file_name))
        return True

    @staticmethod
    def take_file_data(url):
        csv_file_path = os.path.join(parent_directory,  url.split("/")[-1])
        with open(csv_file_path,  "r") as csvfile:
            csv_reader = csv.reader(csvfile)
            rows_from_second = islice(csv_reader,  1,  None)
            return list(rows_from_second)
        

class ImageProcessor:
    @staticmethod
    def combine_images(name):
        image1 = Image.open("image0.png")
        image2 = Image.open("image1.png")
        image3 = Image.open("image2.png")

        width1,  height1 = image1.size
        width2,  height2 = image2.size
        width3,  height3 = image3.size

        new_width = max(width1,  width2,  width3)
        new_height = height1 + height2 + height3
        result_image = Image.new("RGB",  (new_width,  new_height))

        result_image.paste(image1,  (0,  0))
        result_image.paste(image2,  (0,  height1))
        result_image.paste(image3,  (0,  height1 + height2))

        result_image.save(f"{parent_directory}\\output\\{name}.png")

    @staticmethod
    def delete_images():
        os.remove("image0.png")
        os.remove("image1.png")
        os.remove("image2.png")

    @staticmethod
    def save_images(imgs):
        for img in range(len(imgs)):
            with open(f"image{img}.png",  "wb") as file:
                file.write(imgs[img])


class ElementChecker:
    @staticmethod
    def check_by_id_element(element,  element_id):
        try:
            element.find_element(By.ID,  element_id)
            return True
        except Exception as e:
            write_logging(e)
            return False

    @staticmethod
    def check_by_class_element(element,  class_name):
        try:
            element.find_element(By.CLASS_NAME,  class_name)
            return True
        except Exception as e:
            write_logging(e)
            return False


class SeleniumBot(FileManager,  ImageProcessor,  ElementChecker):
    url_csv = "https://robotsparebinindustries.com/orders.csv"
    start_url = "https://robotsparebinindustries.com/"

    def __init__(self):
        self.browser = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()), 
            options=option_chrome(), 
        )
        self.element_waiter = ElementWaiter(self.browser)

    def close_browser(self):
        self.browser.close()
        self.browser.quit()

    def take_csv_file_from_website(self):
        self.browser.get(self.url_csv)
        self.element_waiter.wait_by_user_count(3)

        data_csv = self.take_file_data(self.url_csv)
        self.remove_file(self.url_csv)

        return data_csv
    
    def switch_window(self):
        nav_links = self.browser.find_elements(By.CLASS_NAME, "nav-link")
        order_robost_link = nav_links[-1].get_attribute("href")
        self.browser.get(urljoin(self.start_url, order_robost_link))

    def close_pop_up_window(self):
        modal_popup_window = self.element_waiter.wait_element_by_click_by_class("modal-content")
        modal_popup_window.find_element(By.CLASS_NAME, "btn.btn-dark").click()

    def fill_out_form(self, head, body, legs, address):

        form = self.browser.find_element(By.CSS_SELECTOR, "form")
        div_blocks_mb_3 = form.find_elements(By.CLASS_NAME, "mb-3")
        for div_block in div_blocks_mb_3:
            if self.check_by_id_element(div_block, "head"):
                select = Select(div_block.find_element(By.CLASS_NAME, "custom-select"))
                select.select_by_index(head)
                self.element_waiter.wait_by_user_count(1)

            elif self.check_by_class_element(div_block, "stacked"):
                inputs = div_block.find_elements(By.CLASS_NAME, "form-check-input")
                for in_put in inputs:
                    if in_put.get_attribute("value") == body:
                        in_put.click()
                        self.element_waiter.wait_by_user_count(1)

            elif self.check_by_class_element(div_block, "form-control"):
                if self.check_by_id_element(div_block, "address"):
                    div_block.find_element(By.ID, "address").send_keys(address)
                    self.element_waiter.wait_by_user_count(1)
                else:
                    div_block.find_element(By.CLASS_NAME, "form-control").send_keys(legs)
                    self.element_waiter.wait_by_user_count(1)
    
    def open_start_url(self):
        self.browser.get(self.start_url)
        self.element_waiter.wait_by_user_count(3)
        self.switch_window()

    def press_order_button(self):
        self.element_waiter.wait_by_user_count(2)

        button = self.browser.find_element(By.ID, "order")
        self.browser.execute_script("arguments[0].click();",  button)

        if self.check_by_class_element(self.browser, "alert.alert-danger"):
            self.press_order_button()

    def take_name_and_work_with_imgs(self):
        self.combine_images(
             name = self.browser.find_element(By.CLASS_NAME, "badge.badge-success").text
        )
        self.delete_images()

    def save_with_imgs_by_website(self):
        element = self.element_waiter.wait_for_element_by_id("robot-preview-image")
        imgs = element.find_elements(By.CSS_SELECTOR, "img")

        self.save_images([img.screenshot_as_png for img in imgs])

    def press_another_order(self):
        button = self.browser.find_element(By.ID, "order-another")
        self.browser.execute_script("arguments[0].click();",  button)

    def press_preview_button(self):
        button = self.browser.find_element(By.ID, "preview")
        self.browser.execute_script("arguments[0].click();",  button)
        self.element_waiter.wait_by_user_count(3)

    def for_csv_file_in_form_on_website(self):
        data_csv = self.take_csv_file_from_website()
        self.open_start_url()
        for csv_data_for_form in data_csv:

            self.close_pop_up_window()

            self.fill_out_form(
                head=int(csv_data_for_form[1]), 
                body=csv_data_for_form[2], 
                legs=csv_data_for_form[3], 
                address=csv_data_for_form[4]
            )
            
            self.press_preview_button()

            self.save_with_imgs_by_website()

            self.press_order_button()
            
            self.take_name_and_work_with_imgs()

            self.press_another_order()

            self.element_waiter.wait_by_user_count(2)
            

def create_output_folder():
    folder_path = os.path.join(parent_directory, "output")
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        shutil.rmtree(folder_path)
        os.makedirs(folder_path)
    else:
        os.makedirs(folder_path)


def main():
    order_bot = SeleniumBot()

    try:
        create_output_folder()
        order_bot.for_csv_file_in_form_on_website()
        order_bot.close_browser()
    except Exception as e:
        print(f"Error : {e}")
        order_bot.close_browser()


if __name__ == "__main__":
    main()
