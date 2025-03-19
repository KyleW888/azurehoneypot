import pandas as pd
import requests
import time

# Load CSV file (update with your filename)
csv_filename = "azure_data.csv"  # Use your updated file name
df = pd.read_csv(csv_filename)

# Check if 'IpAddress' column exists
if "IpAddress" not in df.columns:
    raise ValueError("CSV file must have an 'IpAddress' column.")

attack_data = []

# Function to get geolocation from IP
def get_ip_location(ip):
    url = f"http://ip-api.com/json/{ip}?fields=lat,lon,country,status,message"
    try:
        response = requests.get(url)
        data = response.json()
        if data["status"] == "success":
            return data["lat"], data["lon"], data["country"]
        else:
            print(f"Failed to get location for {ip}: {data['message']}")
            return None, None, None
    except Exception as e:
        print(f"Error fetching data for {ip}: {e}")
        return None, None, None

# Process each IP
for ip in df["IpAddress"].unique():
    lat, lon, country = get_ip_location(ip)
    if lat and lon and country:
        attack_data.append({"lat": lat, "lng": lon, "info": f"Attack from {country}"})
    time.sleep(1)  # Prevents rate-limiting (can be adjusted or improved for large datasets)

# Save to attackData.js
js_filename = "attackData.js"
with open(js_filename, "w") as f:
    f.write("var attackData = " + str(attack_data).replace("'", '"') + ";")

print(f"Saved {len(attack_data)} attack records to {js_filename}")
