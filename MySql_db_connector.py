import mysql.connector
import pandas as pd

df = pd.read_excel('scraped_data.xlsx')

# Establish a database connection
conn = mysql.connector.connect(
    host='your_host',
    user='your_username',
    password='your_password',
    database='web_scraping'
)

cursor = conn.cursor()

# Insert data into the MySQL table
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO websites (url, meta_title, meta_description, social_media_links, tech_stack, payment_gateways, language)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (row['url'], row['meta_title'], row['meta_description'], row['social_media_links'], row['tech_stack'], row['payment_gateways'], row['language']))

conn.commit()
cursor.close()
conn.close()
