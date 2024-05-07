from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from urllib.parse import urljoin
import csv
import time

# Login credentials
username = 'username'
password = 'password'

# JavaScript code to fill in username and password
js_script = f'''
let usernameField = document.getElementById('user_login');
let passwordField = document.getElementById('user_pass');
const submitButton = document.getElementById('wp-submit');
if (usernameField && passwordField) {{
    usernameField.value = '{username}';
    passwordField.value = '{password}';
    submitButton.click();
}} else {{
    console.error('Username field and Password field not found');
}}
'''

def check_acf_usage(urls_file):
  with open(urls_file, 'r') as f:
    reader = csv.reader(f)
    urls = [row[0] for row in reader]

  driver = webdriver.Chrome()

  results = []

  for url in urls:
    try:
      driver.get(url)
      time.sleep(1)
      # Perform login actions using Selenium
      driver.execute_script(js_script)
      # if after login gets redirected to confirm admin email, click confirm email
      try:
        admin_email_verification = driver.find_element(By.ID, "correct-admin-email")
        admin_email_verification.click()
      except NoSuchElementException:
        pass
      # Redirect to ACF page
      current_url = driver.current_url
      redirect_url = urljoin(current_url, '/wp-admin/edit.php?post_type=acf-field-group')
      driver.get(redirect_url)
      # Check if the wp-list-table element exists on ACF page
      has_acf_field_groups = 'No'
      try:
        field_groups_table = driver.find_element(By.CLASS_NAME, "wp-list-table")
        rows = field_groups_table.find_elements(By.TAG_NAME, "tr")
        if any("no-items" in row.get_attribute("class") for row in rows):
          has_acf_field_groups = 'No'
        else:
          has_acf_field_groups = 'Yes'
      except NoSuchElementException:
        if "404" in driver.title:
          has_acf_field_groups = 'Error: 404 Not Found'
        else:
          has_acf_field_groups = 'Error'

      # results.append([url, has_acf_field_groups])
      results.append([has_acf_field_groups])
      
    except Exception as e:
      print(f"Error accessing URL: {url}, Error: {e}")
      results.append([url, 'Error'])

  driver.quit()

  with open('csv/acf_usage_results.csv', 'w', newline='') as result_file:
    writer = csv.writer(result_file)
    writer.writerows(results)

urls_file = 'csv/wp-admin_urls.csv'
check_acf_usage(urls_file)

print("CSV file processed successfully. ACF usage results saved to", urls_file)

