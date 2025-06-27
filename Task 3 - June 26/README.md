# News Headlines Web Scraper
A Python-based automation script that scrapes the latest headlines from the BBC News homepage and saves them to a local text file for offline reference or further processing.

## Features
- Live Scraping: Retrieves the most recent headlines from BBC News.
- File Output: Saves headlines in a readable format to a .txt file.
- Clean Output: Automatically strips unwanted HTML tags and whitespace.
- Simple CLI Execution: Just run the script and watch the headlines roll in.
- Throttled Writes: Introduces short delays while writing to avoid I/O spamming.

## Implementation Overview
- HTTP Request: Uses the requests library to fetch the BBC News homepage.
- HTML Parsing: Utilizes BeautifulSoup to parse and extract <h2> headline tags.
- Text Processing: Cleans headline content and prints to console while saving to file.
- File Handling: Writes headlines to a timestamped or manually named .txt file.
- Execution Block: Script follows modular structure with __main__ block for entry.

## Execution
![scrape_headlines py - Elevate Labs - Python Development - Visual Studio Code 26-06-2025 12_24_30 PM](https://github.com/user-attachments/assets/4ae4c859-18ed-4182-bd3c-b9a4468f35f5)

![scrape_headlines py - Elevate Labs - Python Development - Visual Studio Code 26-06-2025 12_22_47 PM](https://github.com/user-attachments/assets/24c911fe-b51a-4c1d-8e4b-d494c0d74fdb)


## Getting started
1. Clone this repository to your local machine.

   ```
   https://github.com/RohitBhavsar27/Elevate-Labs-Internship.git
   ```

   ```
   cd Task 3 - June 26
   ```


3. Make sure the required packages are installed.

   ```
   pip install requests beautifulsoup4
   ```


5. Run the todo list CLI.
   Make sure you have Python installed (version 3.6+ recommended).

   ```
   python scrape_headlines.py
   ```

## Acknowledgments
This project was built as part of an automation task to practice real-world web scraping using Python. Inspired by the need to keep up with the news without constantly checking websites manually.

## License
This project is released under the MIT License. Feel free to use and learn!
