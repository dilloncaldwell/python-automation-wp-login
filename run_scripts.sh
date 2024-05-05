#!/bin/bash

# to run script open terminal and type: bash run_scripts.sh or ./run_scripts.sh
# if needed change permissions to run script type: chmod +x run_scripts.sh

# Run Python Script 1: Modify URLs and Output to CSV
python3 remove_words_trim.py

# Run Python Script 2: Add wp-admin Path to URLs
python3 add_wp-admin_urls.py

# Run Python Script 3: Automation Script
python3 automate_login.py