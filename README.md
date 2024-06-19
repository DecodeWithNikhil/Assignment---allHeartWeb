
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)


# Hi, I'm Nikhil 👋

## 🚀 About Me
Data Science enthusiast with a solid foundation in Data Science, SQL, Python, Data Visualization, and much more. I am passionate about leveraging data to drive insights and innovation, and I am eager to embark on a journey of continuous learning and growth in the field of data analytics.

#### Key Technical Skills:
- **Data Analysis:** Exploratory Data Analysis (EDA), Statistical Analysis
- **Programming:** Python (Pandas, NumPy, Matplotlib, Seaborn), SQL
- **Data Visualization:** PowerBI, Tableau, Excel
- **Web Development:** HTML, CSS, JavaScript
- **Tools:** Jupyter Notebook, VS Code, Git, MySQL 

My educational background and Experience at Internship has provided me with a robust theoretical understanding and practical knowledge of various analytical tools and methodologies.


## Web Scraping Solution for Extracting Website Information

#### Description
This project provides a web scraping solution to extract specific information from a list of websites. The extracted information includes:

- Meta Title 
- Meta Description 
- Social Media Links
- Tech Stack (e.g., MVC, CMS, JS type)
- Payment Gateways (e.g., PayPal, Stripe, Razorpay)
- Website Language
The scraped data is stored in an Excel file named scraped_data.xlsx


## Prerequisites
Python 3.x, 
Necessary Python packages:
requests, 
beautifulsoup4, 
pandas, 
openpyxl

A list of URLs stored in an Excel file named excel_data.xlsx with a column named url (or URL).
## Installation

#### Clone the repository:

```shell
git clone <repository_url>
cd <repository_directory>
```
#### Install the required packages:
```command-line
pip install requests beautifulsoup4 pandas openpyxl
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |


## Usage
Ensure your excel_data.xlsx file is in the same directory as the script.

- Run the script
- After the script runs, the output will be saved in scraped_data.xlsx.
## Configuration
If you want to use a proxy, replace the placeholder proxy addresses in the script with your actual proxy addresses.
```http
pip install free-proxy
```
Note: 
- The script includes error handling to skip websites that fail to scrape.
- A random sleep interval is included between requests to reduce the likelihood of being blocked.
## Approach
#### Identify Information Requirements:

We determined the key information to extract from each website, including meta titles, descriptions, social media links, tech stack, payment gateways, and website language.

#### Setup Environment:

We used Python with requests for making `HTTP` requests and `BeautifulSoup` for parsing HTML.
The list of URLs was stored in an Excel file, which was read using pandas.
Web Scraping Implementation:

Random User-Agent headers were used to mimic browser requests and avoid blocking.

Error handling was incorporated to skip websites that could not be scraped and continue with the rest.

Data was extracted using BeautifulSoup by searching for specific HTML tags and attributes.

Scraped data was stored in a list and then converted to a DataFrame for easy export to Excel.
#### Proxy Configuration (Optional):

Proxy usage was integrated but not mandatory. This can be enabled by replacing placeholders with actual proxy addresses.
Saving Results:

The final scraped data was saved to an Excel file named `scraped_data.xlsx.`
## Challenges
#### Website Blocking:

Some websites block requests from non-browser clients. This was mitigated by using random User-Agent headers.
HTML Structure Variations:

Different websites have varying HTML structures, making it challenging to create a one-size-fits-all solution for scraping. We handled this by using conditional checks for each element.
Proxy Issues:

Finding reliable free proxies can be difficult. The solution includes a placeholder for proxies, but it may require using paid services for better reliability.
Error Handling:

Implementing robust error handling was crucial to ensure the script continues running even if some websites fail to be scraped.
#### Conclusion
The project successfully extracts the required information from a list of websites, skipping those that fail to be scraped and storing the results in an Excel file. 

The solution is configurable and includes error handling and proxy support. Further improvements could include more sophisticated HTML parsing and handling dynamic content with tools like `Selenium`.
## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://decodeWithnikihl.github.io/portfolio) 
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mittalnikhil809/)



## Feedback

If you have any feedback, please reach out to us at mittalnikhil809@gmail.com

