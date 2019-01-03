import time
import requests
from selenium import webdriver
chromePath = r'C:\Users\hankai\Downloads\chromedriver_win32\chromedriver.exe' 
wd = webdriver.Chrome(executable_path= chromePath)
url = 'http://www.bjcancer.org/Account/LogOn'
wd.get(url)
time.sleep(10)
xhnkurl = 'http://www.bjcancer.org/Interactions/SchedulingAppointments/OPDoctorIndex?OPdepartmentId=18'
wd.get(xhnkurl)
table1=wd.find_element_by_class_name('table01')
print(table1)



