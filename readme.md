# Python Automation for logging in to WP sites and checking if ACF is being used

Requirements:

-   Python 3 needs to be installed `brew install python` or go to their website and install https://www.python.org/downloads/
-   Install Selenium using `pip3 install selenium --break-system-packages`
-   Add list of sites to `input.csv`
-   Then run the scripts using `bash run_scripts.sh`

## The Problem this is solving:

Need an easy way to check all sites on WP multisite install to see if ACF is being used, with out manually having to login to each site and check. So I wrote a script that does this for me saving me time and stress. For example we have 470 sites and need to apply some escaping to some sites that are using ACF fields. This will quickly show me which sites i need to manually login and check without having to manually check 470 sites.

## Steps

1. In WP Network admin you can go to the sites listing and copy and paste the urls into a spreadsheet. Then copy the urls column into the input.csv file.
2. The urls column will most likely have the url and the other actions delete, archive, etc. and the link links to the network admin and not site url. So the first script `remove_words_trim.py` that will run will remove theses extra words and trim any extra spaces leaving just a list of the urls. May need to update the `words_to_remove` array in the file to fit needs. This will output the urls into a file `just_urls.csv`.
3. Since on multisite, the ACF plugin is network activated and so to make this easier I want to add to the urls `/wp-admin/edit.php?post_type=acf-field-group` so after login will be redirected to this page. So the `add_wp-admin_urls.py` will handle this and add the new urls into the file `wp-admin_urls.csv`.
4. Since it is multisite I have one login to access all sites. So will need to update the username and password variables in `automate_login.py` with correct credientials before trying to run.
5. Then the `automate_login.py` will loop through the urls in `wp-admin_urls.csv` and login to each site and check if ACF field groups are set up and output yes or no into a file `acf_useage_results.csv` next to the url. If it encounters an error it will output error into the file instead. For example the site has a custom login page set up.
6. I've tried to incorporate some edge cases for if when logging in and the site and the Confirm Admin Email page comes up it will select the confirm button.
7. Then just run the bash script `run_scripts.sh` and it will run all the scripts using the sites in the input.csv file. It will go through every site login, check if field groups are being used and out put results.
8. After finished open the `acf_usage_results.csv` file in spreadsheet and can easily see which sites are using ACF, and then review the sites that have errors.
