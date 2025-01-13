import requests
import pandas as pd

url = "http://localhost/Web%20Service/export.php"

response = requests.get(url)

if response.status_code == 200:
    data = response.json() 
    
    df = pd.DataFrame(data)
    
    excel_file = "database_export.xlsx"
    df.to_excel(excel_file, index=False, engine='openpyxl')
    print(f"Data successfully saved to {excel_file}")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
