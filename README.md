
## Overview

In this project, I attempt to create a Bing News Analytics Platform. Data is pulled from the Bing API, cleaned in Azure Databricks.Sentiment analysis is then performed using Azure ML. Tableau is then used to visualize the data.

### Data Visualization

<img src="https://github.com/user-attachments/assets/8f745159-7312-4d7c-9822-99913e48a201" alt="Data Visualization" width="500"/>


### Data Architecture
<img src="https://github.com/user-attachments/assets/2be99fec-9b62-4d4e-b087-e1f749ba5c45" alt="Data Architecture" width="500"/>


## Steps taken during the data transformation
1. Understand how to read a JSON file in Pyspark.
   ```
   df = spark.read.option('multiline','true').json("/mnt/sabingdataanalyticsyus/data/bing-latest-news.json")
```
2. Transform a JSON column to multiple rows using the explode library
```
from pyspark.sql.functions import explode
df_exploded = df.select(explode(df['value']).alias('json_object'))
```
Applied the explode function to the 'value' column of the DataFrame, transforming each element of the array into a separate row. The result is stored in a new DataFrame called df_exploded, with the column renamed to 'json_object'.

## Lessons Learned

1. I learned how to use the API service in Azure.
2. I learned how to use Pyspark to perform the data transformation
3. I also learned how to use AZURE ML and perform sentiment analysis.


## Contact

Please feel free to contact me if you have any questions at: LinkedIn, Twitter
