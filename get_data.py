from urllib.request import urlopen
import json
import pandas as pd

# Example of how to get data from the API
response = urlopen('https://api.openf1.org/v1/car_data?driver_number=55&session_key=9159&speed>=315')
data = json.loads(response.read().decode('utf-8'))

# Convert the data to a pandas DataFrame
df = pd.DataFrame(data)

# Print the DataFrame
print(df)
