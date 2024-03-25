# group-3-proj-3

### Project Overview and Purpose
This project streamlines the analysis of restaurants information by establishing a data pipeline from the Yelp API. Through an ETL process, we extract Yelp data, refine it, and populate a relational database, setting the stage for advanced restaurants analytics.

### How to Use
FLASK RELATED

### Ethical Considerations
- **Adherence to Data Usage Terms:**
  - Comply with Yelp's API terms of service.
  - Respect restrictions on use, sharing, and monetization of Yelp data.

- **Transparency of Methodology:**
  - Clearly describe data collection and analysis methods in the project.
  - Document data sources and analytical processes for shared results.

### Data Sources

Yelp Fusion API

### Process

Our first step in setting up the project is to import the necessary Python libraries, which include requests for API interactions, pandas for data handling, matplotlib and seaborn for visualization, and the api_key from a configuration file for secure authentication with the Yelp API.

![importing libraries](https://github.com/emely-zelaya/PICTURES_GROUP3_PROJECT3/blob/main/Project%203%20Fotos/requests%20libraries.png?raw=true)


The given code sends a GET call to the search endpoint of the Yelp API to get information about restaurants in Nashville. We set up the required parameters and authorization headers, wait for a successful answer, and then read the JSON to get information like the name of the restaurant, its rating, its prices, and the number of reviews. After that, these data are added to lists, which are then used to make a pandas DataFrame. Finally, we save this DataFrame as a CSV file so that we can look at it again later.

![Nashville Data ](https://github.com/emely-zelaya/PICTURES_GROUP3_PROJECT3/blob/main/Project%203%20Fotos/Nashville%20Restaurants%20Data.png?raw=true)

From this code we obtained the following dataframe:

![nashville info dataframe1](https://github.com/emely-zelaya/PICTURES_GROUP3_PROJECT3/blob/main/Project%203%20Fotos/nashville%20info%20dataframe1.png?raw=true)

In this part of the code, we are creating a DataFrame to organize the category information of restaurants from Nashville obtained via the Yelp API. After ensuring a successful API response, we loop through the data, appending the restaurant name, category, and pricing information to their respective lists. If pricing information isn't available, we append 'N/A'. Then, we convert this structured data into a pandas DataFrame and save it to a CSV file, allowing us to easily access or share this categorized information later.

![df restaurants category ](https://github.com/emely-zelaya/PICTURES_GROUP3_PROJECT3/blob/main/Project%203%20Fotos/Creating%20df%20of%20Nashville%20restaurant%20categories.png?raw=true)

In the code for Franklin restaurants, we follow a similar process to Nashville. We begin by defining the parameters specific to Franklin's geographic location to query the Yelp API. Once we've made the request and confirmed a successful response, we parse the JSON data, looping through each entry to extract information like the restaurant's name, rating, pricing, and number of reviews. We handle the potential absence of pricing information by appending 'N/A' if needed. This extracted data is then used to create another DataFrame, which is saved as a CSV file for Franklin restaurant information.

![Franklin Data ](https://github.com/emely-zelaya/PICTURES_GROUP3_PROJECT3/blob/main/Project%203%20Fotos/Franklin%20Restaurants%20Data.png?raw=true)

From this code we obtained the following dataframe:

![franklin info df](https://github.com/emely-zelaya/PICTURES_GROUP3_PROJECT3/blob/main/Project%203%20Fotos/franklin%20info%20df.png?raw=true)

In this snippet of our code, we’re focusing on the ‘Restaurant Categories’ for Franklin. We make a GET request to the Yelp API, and if it’s successful, we loop through the data, appending the name, category, and pricing details for each restaurant to our lists. We handle any missing pricing information by appending 'N/A'. These lists are then used to create the ‘Restaurant Categories’ DataFrame, which is subsequently saved to a CSV file for further use.

![creating df of franklin restaurant categories](https://github.com/emely-zelaya/PICTURES_GROUP3_PROJECT3/blob/main/Project%203%20Fotos/creating%20df%20of%20franklin%20restaurant%20categories.png?raw=true)

In this code segment for Portland, we are conducting the same structured process as we did for Nashville and Franklin. We start by setting the API request parameters specific to Portland. Once we have made the API call and verified a successful response, we loop through each piece of data, extracting the restaurant’s name, rating, pricing, and number of reviews. If pricing data is not available, we note it as 'N/A'. This information is compiled into a DataFrame, which is then saved as a CSV file for subsequent analysis of Portland restaurant information.

![Portland data](https://github.com/emely-zelaya/PICTURES_GROUP3_PROJECT3/blob/main/Project%203%20Fotos/Portland%20data.png?raw=true)

For Portland, we follow the established process: we query the Yelp API, verify the response, and extract restaurant names, categories, and pricing into a DataFrame, which we then save as a CSV file.

![creating df for portland restaurant categories](https://github.com/emely-zelaya/PICTURES_GROUP3_PROJECT3/blob/main/Project%203%20Fotos/creating%20df%20for%20portland%20restaurant%20categories.png?raw=true)

In this step of the code, we are loading the recently created CSV files for restaurant categories from each city — Nashville, Portland, and Franklin — into separate pandas DataFrames for the data cleaning and analysis phase of our project.

![reading categories files](https://github.com/emely-zelaya/PICTURES_GROUP3_PROJECT3/blob/main/Project%203%20Fotos/reading%20categories%20files.png?raw=true)

In this part of the process, we added a 'Location' column to each DataFrame to clearly mark whether the data came from Nashville or Portland. Then, we combined these two DataFrames into one, using an outer merge to ensure all data is included, even if there are mismatches between the two cities' datasets.

![first merged category csv](https://github.com/emely-zelaya/PICTURES_GROUP3_PROJECT3/blob/main/Project%203%20Fotos/first%20merged%20category%20csv.png?raw=true)

In this step, we incorporated the Franklin data by adding it to our combined dataset and marking each entry with a 'Location' column set to "Franklin". We then merged the Franklin dataset with our previously combined Nashville and Portland data, using an outer merge to capture all entries. Following that, we cleaned up the data by dropping duplicate entries based on restaurant names and removing any entries without pricing information, streamlining our dataset for analysis.

![second merged category csv](https://github.com/emely-zelaya/PICTURES_GROUP3_PROJECT3/blob/main/Project%203%20Fotos/second%20merged%20category%20csv.png?raw=true)

Here, we removed the 'Pricing' column from our restaurant_Category DataFrame. This could be for various reasons, such as the pricing data not being relevant to our analysis or the column containing too many missing values. After dropping the column, we're left with a dataset that's more focused on the remaining attributes.

![dropping pricing in category csv](https://github.com/emely-zelaya/PICTURES_GROUP3_PROJECT3/blob/main/Project%203%20Fotos/dropping%20pricing%20in%20category%20csv.png?raw=true)

And now, after dropping the 'Pricing' column, we have our final restaurant_Category DataFrame, refined and ready for the next stages of our data analysis.

![cleaned category df](https://github.com/emely-zelaya/PICTURES_GROUP3_PROJECT3/blob/main/CLEANED.png?raw=true)

Now we’re repeating our data preparation process for the ‘info’ CSV files. We’re loading the restaurant information from Nashville, Portland, and Franklin into separate DataFrames for further cleaning and analysis. This ensures that all the detailed data we've gathered about restaurants, such as ratings and review counts, is ready to be integrated into our workflow.

![reading info files](https://github.com/emely-zelaya/PICTURES_GROUP3_PROJECT3/blob/main/Project%203%20Fotos/reading%20info%20files.png?raw=true)

In these steps, we're mirroring our earlier data preparation methods for the restaurant information DataFrames. We add a 'Location' column to distinguish between the data from Nashville, Portland, and Franklin. Next, we combine these DataFrames, ensuring that the information from all three cities is represented in one consolidated DataFrame. As before, we remove duplicate entries and any rows that are missing crucial data to maintain the integrity and usability of our dataset.

![first merged info csv](https://github.com/emely-zelaya/PICTURES_GROUP3_PROJECT3/blob/main/Project%203%20Fotos/first%20merged%20info%20csv.png?raw=true)

![second merged info csv](https://github.com/emely-zelaya/PICTURES_GROUP3_PROJECT3/blob/main/Project%203%20Fotos/second%20merged%20info%20csv.png?raw=true)

So, after repeating these data cleaning steps for each city's restaurant info, we now have a cleaned and consolidated DataFrame ready for further analysis or integration into our data pipeline and our new info data frame is below.

![cleaned info df](https://github.com/emely-zelaya/PICTURES_GROUP3_PROJECT3/blob/main/Project%203%20Fotos/cleaned%20info%20df.png?raw=true)

Now in the following code we're combining the restaurant information and the restaurant categories into a single DataFrame, giving us a comprehensive dataset that includes both sets of details for each establishment. This merged DataFrame is then saved to a CSV file, ensuring we have a clean, combined dataset ready for any further steps in our project.

![merged both dataframes](https://github.com/emely-zelaya/PICTURES_GROUP3_PROJECT3/blob/main/Project%203%20Fotos/merged%20both%20dataframes.png?raw=true)

At this point , we are exporting our cleaned data: both the restaurant_Category and restaurant_info DataFrames are being saved as separate CSV files. This allows us to maintain organized records of our data, which can be easily accessed for future analysis or reporting.

![export df](https://github.com/emely-zelaya/PICTURES_GROUP3_PROJECT3/blob/main/Project%203%20Fotos/export%20df.png?raw=true)

Now in this part of the code we are starting with the visualizations.

In here we're creating a bar graph to show how many restaurants fall into each category, making it big and easy to read, coloring the bars sky blue, and labeling everything clearly before showing it on screen.

![bar graph Ser](https://github.com/emely-zelaya/PICTURES_GROUP3_PROJECT3/blob/main/Project%203%20Fotos/bar%20graph%20Ser.png?raw=true)

and this is the first result:

![first visualization](https://github.com/emely-zelaya/PICTURES_GROUP3_PROJECT3/blob/main/Project%203%20Fotos/first%20visualization.png?raw=true)

We're making a heat map to show the count of restaurants across various locations and categories. It's set to be large and clear, with location on the y-axis, category on the x-axis, and the numbers in the cells to show counts. The colors range from light to dark blue to represent different counts, and we're ensuring all labels fit well on the page before presenting the heat map.

![heat map Ser](https://github.com/emely-zelaya/PICTURES_GROUP3_PROJECT3/blob/main/Project%203%20Fotos/heat%20map%20Ser.png?raw=true)

and this is the result for this heat map:

![heatmap visualization](https://github.com/emely-zelaya/PICTURES_GROUP3_PROJECT3/blob/main/Project%203%20Fotos/heatmap%20visualization.png?raw=true)

In this next code we're putting together a bar plot to compare the popularity of restaurant locations based on the number of reviews. With this, we can quickly see which locations are most talked about. We'll label the axes to make it clear what we're measuring and then display the plot.

![bar plot code](https://github.com/emely-zelaya/PICTURES_GROUP3_PROJECT3/blob/main/Project%203%20Fotos/bar%20plot%20code.png?raw=true)

and this is the result for this bar plot code:

![location-based popularity graph](https://github.com/emely-zelaya/PICTURES_GROUP3_PROJECT3/blob/main/Project%203%20Fotos/location-based%20popularity%20graph.png?raw=true)

In this code, we are plotting a count plot to display the number of restaurants by rating, which we've rounded to the nearest half-point for more straightforward visualization. We've set the figure size, labeled the axes, rotated the x-axis labels for better visibility, added a legend to differentiate locations, and then displayed the plot to see the results.

![count of restaurants by rating code](https://github.com/emely-zelaya/PICTURES_GROUP3_PROJECT3/blob/main/Project%203%20Fotos/count%20of%20restaurants%20by%20rating%20code.png?raw=true)

and this is the result for this code:

![count of restaurants visualiation](https://github.com/emely-zelaya/PICTURES_GROUP3_PROJECT3/blob/main/Project%203%20Fotos/count%20of%20restaurants%20visualiation.png?raw=true)

We are creating a scatter plot to explore the potential correlation between the ratings of restaurants and the number of reviews they get, using color coding to distinguish between different locations. We label the plot and the axes, and then we display it to see if higher ratings tend to get more reviews.

![scatter plot code](https://github.com/emely-zelaya/PICTURES_GROUP3_PROJECT3/blob/main/Project%203%20Fotos/scatter%20plot%20code.png?raw=true)

and this is the result for this code:

![last plot](https://github.com/emely-zelaya/PICTURES_GROUP3_PROJECT3/blob/main/Project%203%20Fotos/last%20plot.png?raw=true)


After all of this work, we're now using PostgreSQL for our database creation. We start by ensuring that any previous database with the same name is dropped to avoid conflicts. Then, we create a new database with UTF-8 encoding and set the owner to 'postgres'. We also define the collation and ctype to 'C' for consistent sorting behavior regardless of the operating system's locale settings.

Following that, we establish the table schema by dropping any existing tables to ensure a clean setup. We create two new tables: 'restaurant_info' and 'restaurant_categories'. The 'restaurant_info' table has fields for the name, rating, pricing, number of reviews, and location, with appropriate data types and constraints to ensure that no null values are entered. The name field is also set as the primary key to uniquely identify each entry. Similarly, the 'restaurant_categories' table is structured to include the name, category, and location, ensuring data integrity with NOT NULL constraints.

Finally, we test our setup by selecting all entries from both tables to ensure that they have been created successfully and are ready for data insertion and further manipulation.

![SQL](https://github.com/emely-zelaya/PICTURES_GROUP3_PROJECT3/blob/main/Project%203%20Fotos/SQL.png?raw=true)

and lastly we created our ERD wich is the following:

![ERD](https://github.com/emely-zelaya/PICTURES_GROUP3_PROJECT3/blob/main/Project%203%20Fotos/ERD.png?raw=true)

Our powerpoint is the following. [Our Presentation](https://docs.google.com/presentation/d/1pXs8cVcfpdoFK2RFgf6HB-vpvv2FKx86kcPODn9mKQc/edit#slide=id.p1)
