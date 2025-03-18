import pandas as pd
import requests
import time

# Load CSV file (update with your filename)
csv_filename = "query_data (1).csv"
df = pd.read_csv(csv_filename)

# Check if 'SourceIP' column exists
if "SourceIP" not in df.columns:
    raise ValueError("CSV file must have a 'SourceIP' column.")

attack_data = []

# Function to get geolocation from IP
def get_ip_location(ip):
    url = f"http://ip-api.com/json/{ip}?fields=lat,lon,status,message"
    try:
        response = requests.get(url)
        data = response.json()
        if data["status"] == "success":
            return data["lat"], data["lon"]
        else:
            print(f"Failed to get location for {ip}: {data['message']}")
            return None, None
    except Exception as e:
        print(f"Error fetching data for {ip}: {e}")
        return None, None

# Process each IP
for ip in df["SourceIP"].unique():
    lat, lon = get_ip_location(ip)
    if lat and lon:
        attack_data.append({"lat": lat, "lng": lon, "info": f"Attack from {ip}"})
    time.sleep(1)  # Prevents rate-limiting

# Save to attackData.js
js_filename = "attackData.js"
with open(js_filename, "w") as f:
    f.write("var attackData = " + str(attack_data).replace("'", '"') + ";")

print(f"Saved {len(attack_data)} attack records to {js_filename}")
