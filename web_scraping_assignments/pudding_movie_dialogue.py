# Import necessary libraries
from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

# Load the cleaned CSV file into a pandas DataFrame
df = pd.read_csv('cleaned_pudding_data.csv')

# Extract the 'link' column from the DataFrame
links = df['link']

# Open a new CSV file in write mode with utf-8 encoding
with open('pudding_movie_dialogue.csv', 'w', encoding='utf-8') as file:
    # Create a CSV writer object
    writer = csv.writer(file)
    
    # Write the header row to the CSV file
    writer.writerow(['Link', 'Dialogue Text'])
    
    # Loop through each URL in the 'link' column
    for link in links:
        # Send a GET request to the URL
        response = requests.get(link)
        
        # If the GET request is not successful, skip this URL
        if response.status_code != 200:
            continue
        
        # Parse the HTML content of the page with BeautifulSoup
        dialogue_soup = BeautifulSoup(response.text, "html.parser")
        
        # Prettify the BeautifulSoup object
        dialogue_soup.prettify()
        
        # Extract the first 1000 characters of the text content
        script = dialogue_soup.get_text()[:1000]
        
        # Write the URL and the extracted text to the CSV file
        writer.writerow([link, script])