
## Overview

In this project, I attempt to create a Bing News Analytics Platform. Data is pulled from the Bing API, cleaned in Azure Databricks.Sentiment analysis is then performed using Azure ML. Tableau is then used to visualize the data.






### Data Visualization

<img src="https://github.com/user-attachments/assets/8f745159-7312-4d7c-9822-99913e48a201" alt="Data Visualization" width="500"/>


### Data Architecture
<img src="https://github.com/user-attachments/assets/2be99fec-9b62-4d4e-b087-e1f749ba5c45" alt="Data Architecture" width="500"/>


### Steps taken during the data transformation
1. Understand how to read a JSON file in Pyspark
```bash
   df = spark.read.option('multiline','true').json("/mnt/sabingdataanalyticsyus/data/bing-latest-news.json")
```
2. Transform a JSON column to multiple rows using the explode library. Applied the explode function to the 'value' column of the DataFrame, transforming each element of the array into a separate row. The result is stored in a new DataFrame called df_exploded, with the column renamed to 'json_object'.
```bash
from pyspark.sql.functions import explode
df_exploded = df.select(explode(df['value']).alias('json_object'))
```


3.  Converts each row in df_exploded to a JSON string and collects all of them into a list called json_list.
```bash
json_list = df_exploded.toJSON().collect()
```
4. Initializes empty lists to store the respective fields for all the JSON objects.
```bash
   description=[]
title=[]
category=[]
image=[]
url=[]
provider=[]
datePublished=[]
```
5. Iterates over each JSON string in json_list, parses it into a dictionary (article), and attempts to extract the specified fields. If the 'category' and 'contentUrl' fields are present, it appends the values to the respective lists. Errors in parsing are caught and printed.
```bash
   for json_str in json_list:
    try:
        article = json.loads(json_str)
        
        if article['json_object'].get('category') and article['json_object']['provider'][0].get('image', {}).get('thumbnail', {}).get('contentUrl'):

         title.append(article['json_object']['name'])
         description.append(article['json_object']['description'])
         category.append(article['json_object']['category'])
         image.append(article['json_object']['provider'][0]['image']['thumbnail']['contentUrl'])
         url.append(article['json_object']['url'])
         provider.append(article['json_object']['provider'][0]['name'])
         datePublished.append(article['json_object']['datePublished'])

    except Exception as e:
        print(f"Error parsing {json_str}: {e}")
```
6. Imports StructField, StructType, and StringType from PySpark SQL types module. These are used to define the schema for a DataFrame.
  ```bash
  from pyspark.sql.types import StructField, StructType, StringType
  ```
7. Combines the lists into a list of tuples, where each tuple represents a row of data.
```bash
data = list(zip(title, description, category, image, url, provider, datePublished))
```
8.  Defines a schema for the new DataFrame, specifying the column names and their data types.
   ```bash

  schema = StructType(
    [
        StructField("title", StringType(), True),
        StructField("description", StringType(), True),
        StructField("category", StringType(), True),
        StructField("image", StringType(), True),
        StructField("url", StringType(), True),
        StructField("provider", StringType(), True),
        StructField("datePublished", StringType(), True)
    ]
 )
```
9. Creates a new DataFrame df_cleaned using the combined data and the defined schema.
```bash
df_cleaned = spark.createDataFrame(data, schema)
```
10. Imports the to_date and date_format functions from PySpark SQL functions.
```bash
    df_cleaned_final = df_cleaned.withColumn("datePublished", date_format(to_date("datePublished"), "dd-MM-yyyy"))

```
11. Writes the df_cleaned_final DataFrame to a Delta table at the specified path, overwriting any existing data.
```bash
df_cleaned_final.write.format("delta").mode("overwrite").save("/mnt/<path>")

```
### Pseudocode

Certainly! Here's a pseudocode version of the provided code:

1. Import necessary libraries:
Import all functions from PySpark SQL.
Import the json module for handling JSON data.
2. Read JSON file into a DataFrame:
Set multiline option to true and read the JSON file from the specified path into a DataFrame (df).
3. Display the DataFrame:
Display the contents of the DataFrame.
4. Select specific column:
Select the 'value' column from the DataFrame and create a new DataFrame (df).
5. Display the updated DataFrame:
Display the contents of the updated DataFrame.
6. Explode the DataFrame:
Import the explode function.
Apply explode to the 'value' column to create multiple rows from the array and rename the resulting column to 'json_object'.
Store the exploded data in a new DataFrame (df_exploded).
7. Display the exploded DataFrame:
Display the contents of the exploded DataFrame.
8. Convert DataFrame to JSON strings:
Convert each row in the exploded DataFrame to a JSON string and collect them into a list (json_list).
9. Print the JSON list:
Print the entire list of JSON strings.
10. Parse the last JSON string:
Parse the last JSON string in the list into a Python dictionary (news_json).
11. Print specific fields from the dictionary:
Print various fields (description, name, category, url, contentUrl, provider, datePublished) from the dictionary.
12. Initialize lists to store fields:
Create empty lists to store the title, description, category, image, url, provider, and datePublished fields.
13. Iterate over the JSON list:
For each JSON string in the list:
 Parse the string into a dictionary (article).
 Check if 'category' and 'contentUrl' exist.
 If they exist, append the respective values to the corresponding lists.
 Handle any parsing errors.
14. Define schema for new DataFrame:
Define the schema with title, description, category, image, url, provider, and datePublished as columns, all of type String.
15. Create new DataFrame:
Combine the lists into a list of tuples (data).
Create a new DataFrame (df_cleaned) using the combined data and defined schema.
Display the cleaned DataFrame:
Display the contents of the cleaned DataFrame.
16. Format the date column:
Convert the 'datePublished' column to the dd-MM-yyyy format and update the DataFrame (df_cleaned_final).
17. Display the final cleaned DataFrame:
Display the contents of the final cleaned DataFrame.
Write the final cleaned DataFrame to a Delta table at the specified path, overwriting any existing data.


## Lessons Learned

1. I learned how to use the API service in Azure.
2. I learned how to use Pyspark to perform the data transformation
3. I also learned how to use AZURE ML and perform sentiment analysis.


## Contact

Please feel free to contact me if you have any questions at: LinkedIn, Twitter
