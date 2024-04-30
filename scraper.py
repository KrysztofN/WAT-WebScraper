from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def login_to_website(username, password):
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://s1.wcy.wat.edu.pl/ed1/")

    username_element = driver.find_element(By.NAME, "userid")
    username_element.send_keys(username)

    password_element = driver.find_element(By.NAME, "password")
    password_element.send_keys(password)

    login_element = driver.find_element(By.XPATH, "//input[@type='submit']")
    login_element.click()

    return driver

def extract_date(driver):
    date_element = driver.find_element(By.XPATH, '//td[contains(text(), "Plan zajęć")]/b')
    date = date_element.text
    return date

def extract_schedule(driver):
    first_block_td = driver.find_element(By.XPATH, '//td[contains(text(), "08:00-09:35")]')
    first_block_td_class = first_block_td.find_element(By.XPATH, './following-sibling::td[1]').text

    second_block_td = driver.find_element(By.XPATH, '//td[contains(text(), "9:50-11:25")]')
    second_block_td_class = second_block_td.find_element(By.XPATH, './following-sibling::td[1]').text

    third_block_td = driver.find_element(By.XPATH, '//td[contains(text(), "11:40-13:15")]')
    third_block_td_class = third_block_td.find_element(By.XPATH, './following-sibling::td[1]').text

    fourth_block_td = driver.find_element(By.XPATH, '//td[contains(text(), "13:30-15:05")]')
    fourth_block_td_class = fourth_block_td.find_element(By.XPATH, './following-sibling::td[1]').text

    fifth_block_td = driver.find_element(By.XPATH, '//td[contains(text(), "15:45-17:20")]')
    fifth_block_td_class = fifth_block_td.find_element(By.XPATH, './following-sibling::td[1]').text

    sixth_block_td = driver.find_element(By.XPATH, '//td[contains(text(), "17:35-19:10")]')
    sixth_block_td_class = sixth_block_td.find_element(By.XPATH, './following-sibling::td[1]').text

    seventh_block_td = driver.find_element(By.XPATH, '//td[contains(text(), "19:25-21:00")]')
    seventh_block_td_class = seventh_block_td.find_element(By.XPATH, './following-sibling::td[1]').text

    lectures = [first_block_td_class,second_block_td_class,third_block_td_class,fourth_block_td_class
    ,fifth_block_td_class,sixth_block_td_class,seventh_block_td_class]

    return lectures


def print_schedule(result, date):
    from tabulate import tabulate
    time_blocks = [
        "8:00-9:35",
        "9:50-11:25",
        "11:40-13:15",
        "13:30-15:05",
        "15:45-17:20",
        "17:35-19:10",
        "19:25-21:00"
    ]
    result = ["Brak" if res == " " else res for res in result]

    table_data = []
    for i in range(len(time_blocks)):
        table_data.append([date if i == 0 else "", time_blocks[i], result[i]])
    print(tabulate(table_data, headers=["Date", "Time", "Class"]))



if __name__ == "__main__":
    # Call the function with the desired username and password
    username = "username"
    password = "password"

    driver = login_to_website(username, password)
    date = extract_date(driver)
    result = extract_schedule(driver)
    print_schedule(result, date)

    driver.quit()
