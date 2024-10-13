# capestone-project-1
Redbus Data Scraping with Selenium and Dynamic Filtering using Streamlit

**Problem Statement:**
The "Redbus Data Scraping and Filtering with Streamlit Application" aims to revolutionize the transportation industry by providing a comprehensive solution for collecting, analyzing, and visualizing bus travel data. By utilizing Selenium for web scraping, this project automates the extraction of detailed information from Redbus, including bus routes, schedules, prices, and seat availability. By streamlining data collection and providing powerful tools for data-driven decision-making, this project can significantly improve operational efficiency and strategic planning in the transportation industry.

**Technologies used in this project :**
#Web Scraping using Selenium
#Python
#Streamlit 
#SQL

**Redbus project detailed explanations and its steps:** **
**Step 1:Data Scraping with Selenium:**(Web scraping)
      Using  Selenium  i have automated the extraction of Redbus data including routes, schedules, prices, and seat availability.
      1. Get all the libraries imported in the work enviroment(jupyter notebook).
      2.Store all the 10 state buses route link in a variable in a list format.
      
      3.Using selenium scraped all the routes under particular state  travels and its route links( **Route_Name & Route_Links**) and store it in a csv file.
      example(Kerela bus routes)

      ![Screenshot (17)](https://github.com/user-attachments/assets/dd961eac-7150-433f-8ab3-e5ce2553fadb)

      ![Screenshot (18)](https://github.com/user-attachments/assets/2bf63adc-9a10-49f6-9637-7c7cfee60c4e)

      4.Once the route links are scraped then move in to the particular route link and see all the available buses over there for that particular route.
      5.Now scrape all the bus detauls for that particular route (**Bus Name,Bus Type (Sleeper/Seater/AC/Non-AC),Departing Time,Duration,Reaching Time,Star 
        Rating,Price,Seat Availability)**
        
      ![Screenshot (19)](https://github.com/user-attachments/assets/83d2f248-a148-4c71-907d-c6f41f0ccf6e)
        
      6.Store all the scraped data in the csv file format for each routes under each state.
      7.This step follows data cleaning of the collected scraped data.
      8.Connecting the python and SQL.
      
**Step 2:Storing the scraped data in Database SQL**(SQL)
     1.Then the processed data is stored  in a database schema **(bus_routes)**
     
**Step 3: Streamlit Application:**
     1.Develped the streamlit application to display the scraped data .
     2.Implemented filters such as bustype, route, price range, star rating, availability.
     
**Step 4:Data Analysis/Filtering using Streamlit:**
     1.Used SQL queries to retrieve and filter data based on user inputs.
     2.Used Streamlit to allow users to interact with and filter the data through the application.
     
**Step 5:Interactive Application**
     1.Interactive applications is built so that the user can apply filters and get their bus details.
     ![image](https://github.com/user-attachments/assets/9cdf5c15-3073-4562-91ff-b42722887ffd)

     ![image](https://github.com/user-attachments/assets/f2a4876b-5afd-4aab-ab58-ed6b8b003253)
     
     ![image](https://github.com/user-attachments/assets/a3869636-52ef-4f8b-88c4-7a6a81edd721)



     
  
     
    

      










