# Stock-Analysis
S&amp;P 500 Insights: Market Trends &amp; Stock Analysis
# S&P 500 Insights: Market Trends & Stock Analysis Dashboard

## Overview

The **S&P 500 Insights: Market Trends & Stock Analysis Dashboard** is designed to analyze and track the trends of S&P 500 stocks. This dashboard provides essential stock insights, technical indicators, and performance metrics, making it a valuable for investors, and aspiring analysts. The dashboard is built using Python, Dash, and Plotly, and pulls real-time data from Yahoo Finance.

## Features

- **Stock Selection**: Choose from a wide array of S&P 500 stocks to analyze.
- **Customizable Time Intervals**: Set the data interval to daily, weekly, or monthly based on your analysis needs.
- **Date Range Picker**: Select a custom date range to focus on specific time periods.
- **Key Performance Indicators (KPIs)**: Track metrics like current price, previous close, percentage change, 20-day volume moving average, and more.
- **Technical Analysis**:
  - **Price Trend with Moving Averages**: Visualize the stock's price with 20, 50, 100, and 200-day moving averages.
  - **Volume Analysis**: Review the daily trading volume and its moving average to understand buying/selling pressure.
  - **Relative Strength Index (RSI)**: Identify overbought or oversold conditions in the market.
  - **MACD and Signal Line**: Examine potential buy/sell signals using the MACD and signal line with divergence indications.

## Project Structure

- `app.py`: Main application file containing the Dash app layout and callback functions to update data based on user input.
- `requirements.txt`: Lists the necessary Python libraries to install for running the app.
- `Procfile` (optional): Specifies the start command for deployment on platforms like Heroku.

## Installation

To run this project locally, follow the instructions below:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/NirmalShiroya/Stock-Analysis.git
   cd Stock-Analysis
   ```

2. **Create a Virtual Environment** (Recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate   # On Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   python app.py
   ```

5. **Open the Dashboard**:
   - Once running, open a web browser and go to `http://127.0.0.1:8050` to view the dashboard.

## Usage

- **Stock Selection**: Choose any stock from the S&P 500 list using the dropdown menu.
- **Select Interval**: Set the interval to daily, weekly, or monthly.
- **Date Range**: Use the date picker to focus on a specific date range.
- **Analyze KPIs and Technical Indicators**:
  - **KPIs**: Track current price, previous close, volume moving average, market cap, and buy/sell recommendations.
  - **Price Trend**: Observe stock trends with moving averages for various timeframes.
  - **Volume Analysis**: Compare daily and average volume for insights on market momentum.
  - **RSI and MACD**: Identify potential buy/sell opportunities with these technical indicators.

### Render Deployment

To deploy on Render:

1. **Sign Up** at [Render](https://render.com/) and link your GitHub repository.
2. **Create a New Web Service** from the Render dashboard.
3. **Select your repository**, choose the branch, and set the start command as `python app.py`.
4. **Deploy** and get the URL to access the app.

## Example Screenshots

![Python_Dashboard_Web](https://github.com/user-attachments/assets/0ea54fce-ed37-4b48-8bf3-77c06f03db35)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Data sourced from Yahoo Finance via `yfinance` library.
- Built using Dash, Plotly, and Python.
- Special thanks to the open-source community for the tools and libraries used.

---

Developed by **Nirmalkumar Shiroya** - [Portfolio Project](https://stock-analysis-p72s.onrender.com/)
