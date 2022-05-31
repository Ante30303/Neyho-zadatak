import time
import logging
import json

import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains



logging.basicConfig(level=logging.DEBUG,
format='%(asctime)s %(levelname)s %(message)s',
      filename='application.log',
      filemode='w')

chromedriver_autoinstaller.install()

options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)
driver.get("https://www.linkedin.com/")
email = "testacc12801@gmail.com"
password = "testACC12345[]"

# User Log-in
driver.maximize_window()
driver.find_element(By.ID, "session_key").send_keys(email)
driver.find_element(By.ID, "session_password").send_keys(password)
driver.find_element(By.CLASS_NAME, "sign-in-form__submit-button").click()

# Goes to the profile
driver.find_element(By.XPATH, "/html/body/div[7]/header/div/nav/ul/li[6]/div/button").click()
profile_view = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/header/div/nav/ul/li[6]/div/div/div/header/a[2]")))
profile_view.click()
logging.debug(profile_view)

# Add Experience
add_exp = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[aria-label='Add new experience']")))
add_exp.click()
logging.debug(add_exp)

add_position = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-field='experience_add_position']")))
add_position.click()
logging.debug(add_position)

input_title = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "single-typeahead-entity-form-component-profileEditFormElement-POSITION-profilePosition-ACoAADvS14kBeFTr6PUf-2-D66GpXKzgEwyEKI-1-title")))
input_title.send_keys("Junior software engineer")
logging.debug(input_title)

input_company_name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "single-typeahead-entity-form-component-profileEditFormElement-POSITION-profilePosition-ACoAADvS14kBeFTr6PUf-2-D66GpXKzgEwyEKI-1-requiredCompany")))
input_company_name.send_keys("Neyho Informatika d.o.o.")
logging.debug(input_company_name)

select_date_day = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "date-range-form-component-profileEditFormElement-POSITION-profilePosition-ACoAADvS14kBeFTr6PUf-2-D66GpXKzgEwyEKI-1-dateRange-start-date")))
select_date_day_ins = Select(select_date_day)
select_date_day_ins.select_by_visible_text("May")
logging.debug(select_date_day_ins)

select_date_year = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "date-range-form-component-profileEditFormElement-POSITION-profilePosition-ACoAADvS14kBeFTr6PUf-2-D66GpXKzgEwyEKI-1-dateRange-start-date-year-select")))
select_date_year_ins = Select(select_date_year)
select_date_year_ins.select_by_visible_text("2022")
logging.debug(select_date_year_ins)

input_industry = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "single-typeahead-entity-form-component-profileEditFormElement-POSITION-profilePosition-ACoAADvS14kBeFTr6PUf-2-D66GpXKzgEwyEKI-1-industryId")))
input_industry.clear()
input_industry.send_keys("Software Development")
logging.debug(input_industry)

select_from_industry = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[2]/div[1]/div[8]/div/div/div/div/div[2]/div/div[1]/div/span/span")))
select_from_industry.click()
logging.debug(select_from_industry)

save_exp = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div[3]/button")))
save_exp.click()
logging.debug(save_exp)

close_alert = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div[3]/div/button")))
close_alert.click()
logging.debug(close_alert)


# Searching for the jobs, setting alerts on and saving search results in JSON file
go_to_jobs = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/header/div/nav/ul/li[3]/a/div/div")))
go_to_jobs.click()
logging.debug(go_to_jobs)
search_job = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/header/div/div/div/div[2]/div[2]/div/div/input[1]")))
search_job.click()
search_job.send_keys("Software developer intern")
logging.debug(search_job)
time.sleep(1)
webdriver.ActionChains(driver).send_keys(Keys.TAB).perform()
enter_location = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/header/div/div/div/div[2]/div[3]/div/div[2]/input[1]")))
enter_location.click()
enter_location.send_keys("Croatia")
logging.debug(enter_location)
search_job_loc = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/header/div/div/div/div[2]/div[3]/div/div[3]/div/ul/li[1]/button")))
search_job_loc.click()
logging.debug(search_job_loc)
alerts_on = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/div[3]/div[3]/div[2]/div/section[1]/div/header/div[2]/div/div")))
if alerts_on.text[:9] == "Set alert":
    alerts_on.click()
logging.debug(alerts_on)
time.sleep(2)
job_titles = driver.find_elements(By.CSS_SELECTOR, "[class^='jobs-search-results__list-item occludable-update']")
logging.debug(job_titles)


def writeToJSON(path, filename, data):
    filePathName = './' + path + '/' + filename + '.json'
    with open(filePathName, 'w') as fpn:
        json.dump(data, fpn)

path = './'
file_name = "job listings linkedIn"
json_data = {}
l = []

for job in job_titles:
    """Iterate over the list of jobs and saves title, company_name, location in JSON file"""
    title = job.find_element(By.CSS_SELECTOR, "[class='full-width artdeco-entity-lockup__title ember-view']").text
    company_name = job.find_element(By.CSS_SELECTOR, "[data-control-name='job_card_company_link']").text
    location = job.find_element(By.CSS_SELECTOR, "[class='job-card-container__metadata-item']").text
    core_dict = {
        'title': title,
        'company_name': company_name,
        'location': location,
    }
    l.append(core_dict)

    # Loggers
    logging.debug(title)
    logging.debug(company_name)
    logging.debug(location)
    logging.debug(core_dict)

json_data['jobs'] = l

writeToJSON(path, file_name, json_data)



# Sends pre defined messages
go_to_messages = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/header/div/nav/ul/li[4]/a/div")))
go_to_messages.click()
logging.debug(go_to_messages)

compose_message = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/div[3]/div[2]/div/div/main/div/section[1]/div[1]/div[1]/a")))
compose_message.click()
logging.debug(compose_message)


recipient = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/div[3]/div[2]/div/div/main/div/section[2]/div[2]/div[2]/div/div/section/div/input")))
recipient.send_keys("Antonio Dučkić")
logging.debug(compose_message)

compose_msg = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/div[3]/div[2]/div/div/main/div/section[2]/div[2]/form/div[3]/div/div[1]/div[1]/p")))
compose_msg.send_keys("Hi,\n\nMy name is Robert Robotić and this is test message.")
logging.debug(compose_message)


time.sleep(100)
