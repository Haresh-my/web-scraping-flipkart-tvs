def flipkart():
     # brand = input(str("Enter the brand name : "))
     url = "https://www.flipkart.com/search?q=new+launch+tv&sid=ckf%2Cczl&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_12_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_12_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=new+launch+tv%7CTelevisions&requestId=33ae24d5-65fa-4e7d-ae1b-36f74371f62d&as-backfill=on&otracker=nmenu_sub_TVs%20%26%20Appliances_0_New%20Launches"

     import pandas as pd
     pd.set_option("display.max_colwidth", None)
     from bs4 import BeautifulSoup
     import requests as r

     try:
         # Send HTTP request
         response = r.get(url)
         response.raise_for_status()  # Raise an error for bad responses
         soup = BeautifulSoup(response.content, 'html.parser')

         # Initialize lists for storing data
         NAME = []
         PRICE = []
         RATING = []

         # Data extraction
         for item in soup.find_all("div", class_="KzD1HZ"):
             name = item.find("div", class_="Otbq5D").text.split("-")[0] if item.find("div",
                                                                                      class_="Otbq5D") else "No Name"
             price = item.find("div", class_="CN1yYO").text if item.find("div", class_="CN1yYO") else "No Price"
             rating = item.find("div", class_="_5OesEi").text if item.find("div", class_="_5OesEi") else "No Rating"

             NAME.append(name)
             PRICE.append(price)
             RATING.append(rating)

         # Create DataFrame

         Df = pd.DataFrame({
             "Television": NAME,
             "PRICE": PRICE,
             "RATING": RATING
         })

         print(Df)
         return Df
         # Display the DataFrame

     except Exception as e:
         print(f"An error occurred: {e}")

 # Call the function to execute
Df = flipkart()

import matplotlib.pyplot as plt

if not Df.empty:
    Df["PRICE"] = Df["PRICE"].str.replace("₹", "").str.replace(",", "").astype(int)
    top5 = Df.head(5)

    plt.barh(top5["Television"], top5["PRICE"], color="skyblue")
    plt.xlabel("Price (INR)")
    plt.title("Top 5 New Launch TVs")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()
else:
    print("No data to plot.")





