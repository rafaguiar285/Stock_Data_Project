# 📈 Stock Data Analysis Project

This project retrieves, cleans, and visualizes stock price and revenue data for **Tesla (TSLA)** and **GameStop (GME)** using Python, Web Scraping, and the `yfinance` API. It demonstrates how to work with real financial time-series datasets and create meaningful visualizations.

---

## 🚀 Project Overview

The goal of this project is to:

- Extract historical **stock price data** using `yfinance`
- Scrape **quarterly revenue data** from HTML tables
- Clean and preprocess the datasets
- Generate clear, static visualizations with Matplotlib
- Practice modular programming by splitting code into multiple files
- Simulate real-world workflow using branches and pull requests

The final output includes time-series graphs showing the relationship between stock prices and company revenue.

---

## 📂 Project Structure

📁 Stock_Data_Project/
│
├── Webscraping_Extract_Revenue_Data.py # Scrapes revenue data for Tesla & GameStop
├── main.py # Downloads stock data and generates plots
├── exercise1.py #Practice script for working with stock data using yfinance.
├── exercise2.py #Practice script for working with stock data using yfinance.
├── amd.json #Practice script section for loading AMD stock metadata from a JSON file.
├── apple.json #Practice script section for loading APPLE stock metadata from a JSON file.
└──README.md # Project documentation


---

## 🧰 Technologies Used

- **Python**
- `yfinance` – stock market data
- `pandas` – data manipulation
- `requests` – fetch HTML content
- `BeautifulSoup` – web scraping
- `matplotlib` – static plots
- `warnings` – ignore non-critical warnings

---

## 🔍 Data Collected

### **Tesla (TSLA)**
- Daily stock price history  
- Quarterly revenue (scraped from HTML table)

### **GameStop (GME)**
- Daily stock price history  
- Quarterly revenue (scraped from HTML table)

Data cleaning steps include:

- Removing currency symbols and commas  
- Dropping missing values  
- Converting the Date column to `datetime` type  

---

## 📊 Visualizations

The project produces two figures:

1. **Tesla — Share Price vs. Revenue**
2. **GameStop — Share Price vs. Revenue**

Each figure has:

- A stock price chart  
- A quarterly revenue chart  

This makes it easy to analyze trends and compare company performance with market behavior.

---

## 🧪 How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/your-username/Stock_Data_Project.git
cd Stock_Data_Project

```
### 2. Install Dependences
```bash
pip install -r requirements.txt

```
### 3. Run the Script
```bash
First run the revenue scraper:

python Webscraping_Extract_Revenue_Data.py


Then run the main script:

python yfinance_Extract_Stock_Data.py
```

