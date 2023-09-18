# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestBenepia2():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_benepia2(self):
    # login url 선언
    self.vars["loginUrl"] = self.driver.execute_script("return (\'https://hywelplus.skhynix.com/login\')")
    # 예약 url 선언
    self.vars["roomResvUrl"] = self.driver.execute_script("return (\'https://hywelplus.skhynix.com/condo/reservation/view\')")
    # 예약 url open
    self.driver.get("https://hywelplus.skhynix.com/condo/reservation/view")
    # 현재 url 가져오기
    self.vars["currentUrl"] = self.driver.execute_script("return (window.location.href)")
    # 현재 url 가져오기
    print("{}".format(self.vars["currentUrl"]))
    # 조건문(로그인url redirect)
    if self.driver.execute_script("return (arguments[0] == arguments[1])", self.vars["currentUrl"],self.vars["loginUrl"]):
      self.driver.find_element(By.ID, "userId").send_keys("2074661")
      self.driver.find_element(By.ID, "userPass").send_keys("bdpdnjs05*")
      self.driver.find_element(By.ID, "loginBtn").click()
      self.driver.get("https://hywelplus.skhynix.com/condo/reservation/viewself.vars["roomResvUrl"]")
    # 날짜선택가능 변수 선언
    self.vars["typeAttr"] = "false"
    # 반복문(날짜 선택 가능할때까지)
    while self.driver.execute_script("return (arguments[0] != \"button\")", self.vars["typeAttr"]):
      WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "//button[contains(.,\'충북\')]")))
      # Province click
      self.driver.find_element(By.XPATH, "//button[contains(.,\'충북\')]").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "//button[contains(.,\'제천시\')]")))
      # State click
      self.driver.find_element(By.XPATH, "//button[contains(.,\'제천시\')]").click()
      # Store Attribute of date
      attribute = self.driver.find_element(By.XPATH, "//button[contains(.,\'27\')]").get_attribute("type")
      self.vars["typeAttr"] = attribute
      # end
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "//button[contains(.,\'27\')]")))
    # Date click
    self.driver.find_element(By.XPATH, "//button[contains(.,\'27\')]").click()
    # roomAvaliableStatus
    self.vars["roomAvaliableStatus"] = self.driver.execute_script("return (document.querySelectorAll(\'#condoType-search-result > ul > li:nth-child(1) > button > span.resort-info > span.title\')[0].innerText)")
    # roomAvaliableStatus 확인
    print("{}".format(self.vars["roomAvaliableStatus"]))
    # room click
    self.driver.find_element(By.XPATH, "//div[@id=\'condoType-search-result\']/ul/li[2]/button/span/span").click()
    # 선택완료 click
    self.driver.find_element(By.ID, "reservationBtn").click()
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".checkbox")))
    # 약관 checkbox click
    self.driver.find_element(By.CSS_SELECTOR, ".checkbox").click()
    # 예약신청 click (최종)
    self.driver.find_element(By.ID, "reservationRequestBtn").click()
  
