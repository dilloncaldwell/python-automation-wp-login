import csv

# Input and output files
input_file = 'csv/just_urls.csv'
output_file = 'csv/wp-admin_urls.csv'

# Function to trim spaces from URL
def trim_spaces(url):
  return url.strip()

# Function to add /wp-admin to URL
def add_wp_admin(url):
  if url.endswith('/'):
    return url + 'wp-admin/edit.php?post_type=acf-field-group'
  else:
    return url + '/wp-admin/edit.php?post_type=acf-field-group'

# Read input CSV file, trim spaces, add /wp-admin to URLs, and write to output CSV file
with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
  reader = csv.reader(infile)
  writer = csv.writer(outfile)

  for row in reader:
    trimmed_row = [trim_spaces(url) for url in row]
    modified_row = [add_wp_admin(url) for url in trimmed_row]
    writer.writerow(modified_row)

print("CSV file processed successfully. Added wp-admin/edit.php?post_type=acf-field-group to urls and saved to", output_file)
