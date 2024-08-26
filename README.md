
## Overview

In this project, I attempt to create a Bing News Analytics Platform. Data is pulled from the Bing API, cleaned in Azure Databricks.Sentiment analysis is then performed using Azure ML. Tableau is then used to visualize the data.

### Data Visualization

![image](https://github.com/user-attachments/assets/8f745159-7312-4d7c-9822-99913e48a201)


### Data Architecture


If you decide to include this, you should also talk a bit about why you chose the architecture and tools you did for this project.



## Lessons Learned

1. I learned how to use the API service in Azure.
2. I learned how to use Pyspark to perform the data transformation
   ```
   df = spark.read.option('multiline','true').json("/mnt/sabingdataanalyticsyus/data/bing-latest-news.json")
   ```


## Contact

Please feel free to contact me if you have any questions at: LinkedIn, Twitter
