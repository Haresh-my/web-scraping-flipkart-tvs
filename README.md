# web-scraping-flipkart-tvs
This Python project scrapes data from Flipkart to gather details about newly launched televisions, including their name, price, and rating. It then visualizes the top 5 listings using a horizontal bar chart.

🔍 Features
Scrapes:

Product names

Prices (₹)

Ratings (if available)

Uses BeautifulSoup and requests for scraping

Cleans and organizes data into a Pandas DataFrame

Visualizes the top 5 TVs by price using matplotlib

🧰 Technologies Used
Python 3

BeautifulSoup

Requests

Pandas

Matplotlib

🚀 How to Run
Clone the repository or download the script.

Install the required libraries (if not already installed):

bash
Copy
Edit
pip install requests beautifulsoup4 pandas matplotlib
Run the script:

bash
Copy
Edit
python Flipkart_webscrap.py
Output: You'll see a DataFrame printed in the console and a bar chart showing the top 5 TVs by price.

📊 Sample Output
python-repl
Copy
Edit
Television              PRICE    RATING
Samsung 55 inch ...     ₹55,999    4.3★
...
(plus bar chart visualization)

⚠️ Disclaimer
This project is for educational purposes only.

Flipkart's website structure may change, breaking the scraper.

Avoid running it too frequently to respect the site's terms of service.
