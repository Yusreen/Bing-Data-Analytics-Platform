#!/usr/bin/env python
# coding: utf-8

# In[28]:


import pandas as pd
from azureml.fsspec import AzureMachineLearningFileSystem

# define the URI - update <> placeholders
uri = 'azureml://<>"


# create the filesystem
fs = AzureMachineLearningFileSystem(uri)

# append parquet files in folder to a list
dflist = []
for path in fs.glob('transform_data/*.parquet'):
    with fs.open(path) as f:
        dflist.append(pd.read_parquet(f))

# concatenate data frames
df = pd.concat(dflist,ignore_index=True)
display(df)


# In[31]:


import pandas as pd
from textblob import TextBlob


# Function to classify sentiment
def classify_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.2:
        return "neutral"
    elif polarity < -0.2:
        return "angry"
    else:
        return "sad"

# Apply sentiment classification
df['sentiment'] = df['description'].apply(classify_sentiment)

display(df)



# In[38]:


#df.to_csv("Users/yusreen.DataEngineer/news-sentiment-analysis-final.csv")


# In[37]:


from azure.storage.filedatalake import DataLakeServiceClient

# Azure ADLS Gen2 configuration
account_name = ""
account_key = ""
file_system_name = ""
folder_name = ""
file_name = ""

# Initialize the DataLakeServiceClient
service_client = DataLakeServiceClient(account_url=f"https://{account_name}.dfs.core.windows.net", credential=account_key)

# Create a file system client
file_system_client = service_client.get_file_system_client(file_system_name)

# Create a directory client for the folder
directory_client = file_system_client.get_directory_client(folder_name)

# Create the folder if it doesn't exist
directory_client.create_directory()

# Save the DataFrame to a CSV file in memory
csv_data = df.to_csv(index=False)

# Create a file client and upload the CSV
file_client = directory_client.get_file_client(file_name)
file_client.upload_data(csv_data, overwrite=True)

print(f"DataFrame saved to ADLS Gen2 under folder '{folder_name}' as '{file_name}'.")

