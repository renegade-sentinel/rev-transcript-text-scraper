# Rev.io Transcript Text Scraper
This is a Python script for scraping transcript text from Rev.com using Selenium WebDriver. It automates the process of visiting multiple transcript links and extracting the text content from each transcript.

## Prerequisites
* Python 3.x
* Selenium WebDriver
* ChromeDriver
## Usage
* Install the required dependencies mentioned in the prerequisites.
* Download and configure ChromeDriver.
* Replace the transcript_links list in the code with the URLs of the transcripts you want to scrape.
* Run the script using the Python interpreter.

The script opens each transcript link in a headless Chrome browser, waits for the page to load, and extracts the text content from the element with the ID "editor". The extracted transcript text is then saved to a CSV file named "example.csv".

Please note that this script uses ChromeDriver, so make sure you have the compatible version of ChromeDriver installed on your system.

Feel free to modify the script according to your specific requirements.
