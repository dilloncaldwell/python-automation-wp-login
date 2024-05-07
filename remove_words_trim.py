import csv

def modify_urls(input_file, output_file, words_to_remove):
  with open(input_file, 'r') as f:
    reader = csv.reader(f)
    urls = [row[0] for row in reader]

  modified_urls = []
  error_urls = []
  for url in urls:
    try:
      for word in words_to_remove:
        url = url.replace(word, '')
      modified_urls.append(url.strip())
    except Exception as e:
      print(f"Error processing URL: {url}, Error: {e}")
      error_urls.append(url)

  with open(output_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows([[url] for url in modified_urls])

  if error_urls:
    with open('errors.csv', 'w', newline='') as err_file:
      writer = csv.writer(err_file)
      writer.writerows([[url] for url in error_urls])

# Example usage:
input_file = 'csv/input.csv'
output_file = 'csv/just_urls.csv'
words_to_remove = ['Delete', 'Archive', 'Select', 'Deactivate', 'Dashboard', 'Spam', '|', 'Visit', 'Copy', 'Edit']
modify_urls(input_file, output_file, words_to_remove)

print("CSV file processed successfully. Removed words from urls and saved to", output_file)