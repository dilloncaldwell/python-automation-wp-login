import subprocess

subprocess.run("python3 remove_words_trim.py", shell=True)
subprocess.run("python3 add_wp-admin_urls.py", shell=True)
subprocess.run("python3 automate_login.py", shell=True)