import dash
from dash import dcc, html, Input, Output
import yfinance as yf
import plotly.graph_objs as go
from datetime import datetime, timedelta
import pandas as pd

# Define the list of stock tickers
#sp500_tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "FB"]
sp500_tickers = [
    "AAPL", "MSFT", "GOOGL", "AMZN", "META", "TSLA", "BRK.B", "NVDA", "JPM", "JNJ",
    "V", "PG", "UNH", "HD", "DIS", "PYPL", "MA", "NFLX", "VZ", "ADBE",
    "PFE", "KO", "MRK", "PEP", "T", "INTC", "CSCO", "ABT", "NKE", "CMCSA",
    "WMT", "XOM", "CRM", "LLY", "COST", "CVX", "MCD", "DHR", "MDT", "NEE",
    "TXN", "AVGO", "WFC", "LIN", "BMY", "HON", "ACN", "AMGN", "QCOM", "ORCL",
    "PM", "UNP", "IBM", "TMO", "MMM", "INTU", "AMAT", "GE", "UPS", "LOW",
    "CAT", "GS", "LMT", "AXP", "USB", "MS", "AMD", "ISRG", "SCHW", "BA",
    "SPGI", "NOW", "BLK", "BKNG", "SYK", "CI", "DE", "MDLZ", "CB", "MO",
    "CCI", "PLD", "DUK", "MMC", "CME", "ADI", "TGT", "APD", "ANTM", "ZTS",
    "TFC", "CSX", "COP", "EL", "SHW", "NSC", "ICE", "BIIB", "SO", "EQIX",
    "HUM", "GM", "ETN", "CL", "ITW", "ADI", "FDX", "ROP", "KMB", "CHTR",
    "MET", "AON", "DG", "ADSK", "BSX", "PGR", "FISV", "EW", "CNC", "TRV",
    "EXC", "PSA", "ADP", "APTV", "AZO", "KHC", "GILD", "HCA", "AIG", "MAR",
    "KMI", "MPC", "ILMN", "EA", "F", "PRU", "WMB", "PH", "ATVI", "AFL",
    "MNST", "HES", "FTV", "BAX", "CTSH", "TEL", "NOC", "JCI", "D", "ORLY",
    "LRCX", "GIS", "BLL", "CMG", "DTE", "HPQ", "MTB", "LHX", "PEG", "PPG",
    "PAYX", "STZ", "AEE", "DOV", "SRE", "FRC", "CERN", "WELL", "VTR", "ECL",
    "AWK", "GPN", "XEL", "IDXX", "LYB", "ROK", "HIG", "KEYS", "KR", "AES",
    "DLR", "WDC", "ED", "FTNT", "HOLX", "A", "K", "RE", "PCAR", "RF",
    "EFX", "HPE", "VLO", "CTVA", "CINF", "CLX", "CARR", "IP", "MLM", "NTRS",
    "CMS", "SYY", "GL", "MTD", "EQR", "VRSN", "TSCO", "OKE", "MAA", "NUE",
    "CFG", "HSY", "REGN", "SWK", "BBY", "CTAS", "LKQ", "EXR", "CAG", "NTAP",
    "ALB", "VMC", "AVB", "DRI", "ROST", "AMP", "QRVO", "IPG", "MRO", "MHK",
    "FITB", "AME", "BF.B", "PKI", "GRMN", "SIVB", "MOS", "SNA", "ETSY", "RHI",
    "DGX", "O", "FE", "CHD", "LEN", "MKTX", "SNPS", "AVY", "BRO", "L",
    "CNP", "ZBRA", "ES", "UDR", "FRT", "RMD", "MTN", "CMS", "ROL", "NDAQ",
    "BIO", "CAH", "EPAM", "SPG", "KMX", "EMN", "PKG", "TROW", "NVR", "LNT",
    "PFG", "IRM", "LDOS", "MGM", "WRB", "UHS", "LNC", "VTRS", "NWL", "TXT",
    "FLS", "J", "AOS", "STE", "TAP", "AKAM", "SEE", "MCK", "HAS", "HRB",
    "LEG", "BXP", "J", "FFIV", "NRG", "NDSN", "WHR", "DRH", "WY", "HST",
    "NLSN", "AIZ", "BKR", "XYL", "DXC", "KIM", "ROL", "JKHY", "WU", "FIS",
    "RJF", "WRK", "FMC", "MPWR", "CDNS", "NI", "MOS", "ALK", "NCLH", "DISH",
    "FRC", "WBA", "PBCT", "DVA", "NLOK", "NWL", "AAL", "NRG", "SLB", "CBRE"
]

# Initialize the Dash app
app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("S&P 500 Insights: Market Trends & Stock Analysis", style={'text-align': 'center', 'color': '#ADD8E6', 'padding': '20px', 'font-size': '32px', 'font-weight': 'bold'}),

    # Stock Selection, Interval, and Date Range Picker in one line
    html.Div([
        html.Div([
            html.Label("Select Stock:", style={'font-weight': 'bold', 'color': '#FF5722'}),
            dcc.Dropdown(
                id='stock-dropdown',
                options=[{'label': ticker, 'value': ticker} for ticker in sp500_tickers],
                value='AAPL',
                style={'width': '100%', 'backgroundColor': '#FFFFFF', 'border-radius': '5px', 'color': '#333333'}
            ),
        ], style={'width': '30%', 'display': 'inline-block'}),

        html.Div([
            html.Label("Select Interval:", style={'font-weight': 'bold', 'color': '#FF5722'}),
            dcc.Dropdown(
                id='interval-dropdown',
                options=[
                    {'label': 'Daily', 'value': '1d'},
                    {'label': 'Weekly', 'value': '1wk'},
                    {'label': 'Monthly', 'value': '1mo'}
                ],
                value='1d',
                style={'width': '100%', 'backgroundColor': '#FFFFFF', 'border-radius': '5px', 'color': '#333333'}
            ),
        ], style={'width': '20%', 'display': 'inline-block', 'margin-left': '2%'}),

        html.Div([
            html.Label("Select Date Range:", style={'font-weight': 'bold', 'color': '#FF5722'}),
            dcc.DatePickerRange(
                id='date-picker-range',
                start_date=(datetime.now() - timedelta(days=365)).date(),
                end_date=datetime.now().date(),
                display_format='YYYY-MM-DD',
                calendar_orientation='vertical'  # Display calendar vertically
            ),
        ], style={'width': '45%', 'display': 'inline-block', 'margin-left': '2%'}),
    ], style={'display': 'flex', 'justify-content': 'center', 'margin-bottom': '20px'}),

    # KPI Section with colorful cards
    html.Div(id='kpi-cards', style={
        'display': 'flex', 
        'justify-content': 'space-around', 
        'padding': '10px',
        'backgroundColor': '#00000',  # Soft, light background for KPI section
        'border-radius': '10px',
        'box-shadow': '0px 4px 8px rgba(0, 0, 0, 0.1)'
    }),

    # 2x2 Grid for First Four Plots with rounded corners and shadow
    html.Div([
        html.Div([
            dcc.Graph(id='price-chart', style={'width': '100%', 'margin-bottom': '20px', 'border-radius': '15px', 'box-shadow': '0px 4px 8px rgba(0, 0, 0, 0.2)'}),
            dcc.Graph(id='volume-chart', style={'width': '100%', 'margin-bottom': '20px', 'border-radius': '15px', 'box-shadow': '0px 4px 8px rgba(0, 0, 0, 0.2)'}),
        ], style={'width': '48%', 'display': 'inline-block', 'vertical-align': 'top'}),

        html.Div([
            dcc.Graph(id='moving-average-chart', style={'width': '100%', 'margin-bottom': '20px', 'border-radius': '15px', 'box-shadow': '0px 4px 8px rgba(0, 0, 0, 0.2)'}),
            dcc.Graph(id='rsi-chart', style={'width': '100%', 'margin-bottom': '20px', 'border-radius': '15px', 'box-shadow': '0px 4px 8px rgba(0, 0, 0, 0.2)'}),
        ], style={'width': '48%', 'display': 'inline-block', 'vertical-align': 'top'}),
    ], style={'display': 'flex', 'justify-content': 'space-between'}),

    # MACD Plot Below the 2x2 Grid with rounded corners and shadow
    html.Div([
        dcc.Graph(id='macd-chart', style={'width': '100%', 'margin-top': '20px', 'border-radius': '15px', 'box-shadow': '0px 4px 8px rgba(0, 0, 0, 0.2)'}),
    ], style={'width': '100%', 'display': 'block'}),
], style={
    'backgroundColor': '#000000',  # Set dashboard background color to black
    'color': '#333333',
    'font-family': 'Arial, sans-serif',
    'box-shadow': '0px 8px 16px rgba(0, 0, 0, 0.3)',  # Shadow effect for the dashboard
    'padding': '20px',
    'border-radius': '15px'  # Rounded corners for the entire dashboard
})

# Callback to update charts and KPIs based on inputs, including date picker and interval selector
@app.callback(
    [Output('kpi-cards', 'children'),
     Output('price-chart', 'figure'),
     Output('volume-chart', 'figure'),
     Output('moving-average-chart', 'figure'),
     Output('rsi-chart', 'figure'),
     Output('macd-chart', 'figure')],
    [Input('stock-dropdown', 'value'),
     Input('interval-dropdown', 'value'),
     Input('date-picker-range', 'start_date'),
     Input('date-picker-range', 'end_date')]
)
def update_dashboard(stock, interval, start_date, end_date):
    # Calculate start and end dates based on the date picker
    start_date = pd.to_datetime(start_date).date() if start_date else (datetime.now() - timedelta(days=365)).date()
    end_date = pd.to_datetime(end_date).date() if end_date else datetime.now().date()

    # Fetch data with the selected interval
    try:
        data = yf.download(stock, start=start_date, end=end_date, interval=interval, progress=False)
        data = data[['Open', 'High', 'Low', 'Close', 'Volume']].dropna()
        data.columns = data.columns.get_level_values(0)  # Flatten multi-level columns
    except Exception as e:
        print(f"Error fetching data: {e}")
        return [html.Div("Error fetching data")], go.Figure(), go.Figure(), go.Figure(), go.Figure(), go.Figure()

    # Define plot styles and colors for vibrant theme
    layout_settings = {
        'plot_bgcolor': '#FFFFFF',  # Light background for plots
        'paper_bgcolor': '#FFFFFF',  # White background for plot papers
        'font': {'color': '#333333'},  # Dark text for readability
    }

    # Check if data is empty
    if data.empty:
        print("No data fetched for the specified date range.")
        return [html.Div("No data available")], go.Figure(), go.Figure(), go.Figure(), go.Figure(), go.Figure()

    # Fetch market cap
    try:
        ticker = yf.Ticker(stock)
        market_cap = ticker.info.get("marketCap", None)
        
        # Format Market Cap
        if market_cap:
            if market_cap >= 1e9:
                market_cap_str = f"${market_cap / 1e9:.2f}B"
            elif market_cap >= 1e6:
                market_cap_str = f"${market_cap / 1e6:.2f}M"
            else:
                market_cap_str = f"${market_cap:.2f}"
        else:
            market_cap_str = "N/A"
    except Exception as e:
        print(f"Error fetching market cap: {e}")
        market_cap_str = "N/A"

    # Calculate additional KPIs
    current_price = data['Close'].iloc[-1]
    previous_close = data['Close'].iloc[-2]
    percentage_change = ((current_price - previous_close) / previous_close) * 100
    high_low_spread = data['High'].iloc[-1] - data['Low'].iloc[-1]
    
    # Moving Averages
    data['20-day MA'] = data['Close'].rolling(window=20).mean()
    data['50-day MA'] = data['Close'].rolling(window=50).mean()
    data['100-day MA'] = data['Close'].rolling(window=100).mean()
    data['200-day MA'] = data['Close'].rolling(window=200).mean()

    # Daily Buy/Sell Recommendation
    recommendation = "HOLD"
    if data['20-day MA'].iloc[-1] > data['50-day MA'].iloc[-1]:
        recommendation = "BUY"
    elif data['20-day MA'].iloc[-1] < data['50-day MA'].iloc[-1]:
        recommendation = "SELL"

    # RSI Calculation
    delta = data['Close'].diff(1)
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()
    rs = avg_gain / avg_loss
    data['RSI'] = 100 - (100 / (1 + rs))

    # Volume Moving Average
    data['10-day Volume MA'] = data['Volume'].rolling(window=10).mean()

    # MACD Calculation
    data['12-day EMA'] = data['Close'].ewm(span=12, adjust=False).mean()
    data['26-day EMA'] = data['Close'].ewm(span=26, adjust=False).mean()
    data['MACD'] = data['12-day EMA'] - data['26-day EMA']
    data['Signal Line'] = data['MACD'].ewm(span=9, adjust=False).mean()

    # MACD Divergence
    macd_divergence = "Positive" if data['MACD'].iloc[-1] > data['Signal Line'].iloc[-1] else "Negative"

    # KPI Cards with distinct colors
    kpi_colors = ['#4CAF50', '#2196F3', '#FFC107', '#FF5722', '#9C27B0', '#03A9F4', '#8BC34A', '#FF9800']
    kpis = [
        html.Div([html.H3("Current Price"), html.P(f"${current_price:.2f}")], style={'backgroundColor': kpi_colors[0], 'color': '#FFFFFF', 'padding': '15px', 'border-radius': '8px', 'text-align': 'center'}),
        html.Div([html.H3("Previous Close"), html.P(f"${previous_close:.2f}")], style={'backgroundColor': kpi_colors[1], 'color': '#FFFFFF', 'padding': '15px', 'border-radius': '8px', 'text-align': 'center'}),
        html.Div([html.H3("Percentage Change"), html.P(f"{percentage_change:.2f}%")], style={'backgroundColor': kpi_colors[2], 'color': '#FFFFFF', 'padding': '15px', 'border-radius': '8px', 'text-align': 'center'}),
        html.Div([html.H3("High-Low Spread"), html.P(f"${high_low_spread:.2f}")], style={'backgroundColor': kpi_colors[3], 'color': '#FFFFFF', 'padding': '15px', 'border-radius': '8px', 'text-align': 'center'}),
        html.Div([html.H3("20-Day Volume MA"), html.P(f"{data['10-day Volume MA'].iloc[-1]:,.0f}")], style={'backgroundColor': kpi_colors[4], 'color': '#FFFFFF', 'padding': '15px', 'border-radius': '8px', 'text-align': 'center'}),
        html.Div([html.H3("Market Cap"), html.P(market_cap_str)], style={'backgroundColor': kpi_colors[5], 'color': '#FFFFFF', 'padding': '15px', 'border-radius': '8px', 'text-align': 'center'}),
        html.Div([html.H3("BUY/SELL"), html.P(recommendation)], style={'backgroundColor': kpi_colors[6], 'color': '#FFFFFF', 'padding': '15px', 'border-radius': '8px', 'text-align': 'center'}),
        html.Div([html.H3("MACD Divergence"), html.P(macd_divergence)], style={'backgroundColor': kpi_colors[7], 'color': '#FFFFFF', 'padding': '15px', 'border-radius': '8px', 'text-align': 'center'}),
    ]

        # Define plot styles and colors for vibrant theme
    layout_settings = {
        'plot_bgcolor': '#FFFFFF',  # Light background for plots
        'paper_bgcolor': '#FFFFFF',  # White background for plot papers
        'font': {'color': '#333333'},  # Dark text for readability
        'title': {'font': {'size': 20, 'color': '#1A5276'}, 'x': 0.5}  # Centered title
    }
   # Price Trend Plot with Moving Averages
    price_fig = go.Figure()
    price_fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name="Close Price"))
    price_fig.add_trace(go.Scatter(x=data.index, y=data['20-day MA'], mode='lines', name="20-day MA"))
    price_fig.add_trace(go.Scatter(x=data.index, y=data['50-day MA'], mode='lines', name="50-day MA"))
    price_fig.add_trace(go.Scatter(x=data.index, y=data['100-day MA'], mode='lines', name="100-day MA"))
    price_fig.add_trace(go.Scatter(x=data.index, y=data['200-day MA'], mode='lines', name="200-day MA"))
    price_fig.update_layout(
        title="Price Trend with Moving Averages", 
        xaxis_title="Date", 
        yaxis_title="Price", 
        legend=dict(x=0.01, y=0.99),
        title_x=0.5,
        title_font=dict(size=20, color='#1F77B4')  # Vibrant color for title
    )

    # Volume Plot with darker bars
    volume_fig = go.Figure()
    volume_fig.add_trace(go.Bar(x=data.index, y=data['Volume'], name="Volume", marker_color='#FF4500'))
    volume_fig.update_layout(
        title="Daily Trading Volume", 
        xaxis_title="Date", 
        yaxis_title="Volume",
        title_x=0.5,
        title_font=dict(size=20, color='#E74C3C')  # Vibrant color for title
    )

    # Moving Average Volume Plot
    moving_avg_fig = go.Figure()
    moving_avg_fig.add_trace(go.Scatter(x=data.index, y=data['Volume'], mode='lines', name="Daily Volume"))
    moving_avg_fig.add_trace(go.Scatter(x=data.index, y=data['10-day Volume MA'], mode='lines', name="10-day Volume MA"))
    moving_avg_fig.update_layout(
        title="Trading Volume with 10-Day MA", 
        xaxis_title="Date", 
        yaxis_title="Volume", 
        legend=dict(x=0.01, y=0.99),
        title_x=0.5,
        title_font=dict(size=20, color='#2ECC71')  # Vibrant color for title
    )

    # RSI Plot
    rsi_fig = go.Figure(data=[go.Scatter(x=data.index, y=data['RSI'], mode='lines', name="RSI", line=dict(color='#DA70D6'))])
    rsi_fig.add_hline(y=70, line_dash="dash", line_color="red", annotation_text="Overbought")
    rsi_fig.add_hline(y=30, line_dash="dash", line_color="green", annotation_text="Oversold")
    rsi_fig.update_layout(
        title="Relative Strength Index (RSI)", 
        xaxis_title="Date", 
        yaxis_title="RSI", 
        legend=dict(x=0.01, y=0.99),
        title_x=0.5,
        title_font=dict(size=20, color='#9B59B6')  # Vibrant color for title
    )

    # MACD Plot with Divergence
    macd_fig = go.Figure()
    macd_fig.add_trace(go.Scatter(x=data.index, y=data['MACD'], mode='lines', name="MACD"))
    macd_fig.add_trace(go.Scatter(x=data.index, y=data['Signal Line'], mode='lines', name="Signal Line"))
    macd_fig.add_trace(go.Scatter(x=data.index, y=data['MACD'] - data['Signal Line'],
                              fill='tozeroy', mode='none', name="Divergence",
                              fillcolor='rgba(255,0,0,0.3)' if macd_divergence == "Negative" else 'rgba(0,255,0,0.3)'))
    macd_fig.update_layout(
        title="MACD and Signal Line with Divergence", 
        xaxis_title="Date", 
        yaxis_title="MACD", 
        legend=dict(x=0.01, y=0.99),
        title_x=0.5,
        title_font=dict(size=20, color='#F39C12')  # Vibrant color for title
    )

    return kpis, price_fig, volume_fig, moving_avg_fig, rsi_fig, macd_fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
