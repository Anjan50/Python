import re

def find_urls(input_string):
    # Define a regular expression pattern for matching URLs
    url_pattern = r'https?://\S+|www\.\S+'

    # Use re.findall to find all URLs in the input string
    urls = re.findall(url_pattern, input_string)

    return urls

# Example usage:
input_string = "This is a sample text with a URL: https://www.example.com and another URL: http://www.google.com"

urls_found = find_urls(input_string)

if urls_found:
    print("URLs found in the input string:")
    for url in urls_found:
        print(url)
else:
    print("No URLs found in the input string.")
