# Honeypot Visualization

This project visualizes cyber attack data collected from a honeypot, which was deployed on an **Azure VM** and intentionally exploited to attract attackers.

## Features

- **Real-time Attack Visualization**: Displays attack data on an interactive map.
- **Geo-location Mapping**: Visualizes attack locations based on IP addresses.
- **Frequency-based Size and Color**: Circles' sizes and colors change based on the attack frequency.

## Technologies Used

- **Azure VM**: The honeypot was hosted on an Azure Virtual Machine and purposely exposed to attract attackers.
- **Azure Sentinel**: Collects and analyzes attack data in real-time.
- **KQL (Kusto Query Language)**: Used for querying attack data from Azure Log Analytics.
- **Azure Log Analytics**: Collects and stores attack data from the honeypot.

## How It Works

1. **Honeypot Setup**: A honeypot was deployed on an **Azure VM** and intentionally exposed to attract malicious activity.
2. **Data Collection**: Attack data is gathered using **Azure Sentinel** and **Log Analytics**.
3. **Data Querying**: Queries are run using **KQL** to retrieve the attack data.
4. **Visualization**: The data is visualized on a map, showing the frequency and location of attacks.
5. The data collected from VM was from a 12-hour simulation.

## MAP

The visualization can be accessed here: [Honeypot Visualization Demo](https://kylew888.github.io/azurehoneypot/).

