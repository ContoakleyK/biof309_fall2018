
# coding: utf-8

# In[1]:


### Import packages to pull csv file from repo for analysis
import requests
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
from urllib.request import urlretrieve


# In[4]:


### Assign URL to variable: url
url = 'https://raw.githubusercontent.com/BIOF309/group-project-rmndr/master/Family_PACT_Providers_File.csv'


# In[5]:


### Apply pandas package to read the .csv file: url
df = pd.read_csv(url)


# In[6]:


### Display the dataframe in Notebook
df


# In[27]:


print(np.shape(df))


# In[28]:


type(df)


# In[49]:


### Get information on DataFrame
df.info()


# In[51]:


### Display the last 6 columns of the DataFrame
df.iloc[:,-6:]


# In[39]:


### Index list by zipcodes: zclist  NOTE: Doing this removed the column 'Provider_Address_Zip', not what you intended
zclist = df.set_index(['Provider_Address_Zip'])


# In[40]:


zclist


# In[43]:


zclist.columns


# In[42]:


zclist.shape


# In[48]:


zclist.info()


# In[44]:


type(zclist.columns)


# In[45]:


zclist.index


# In[46]:


zclist.head(5)


# In[47]:


zclist.iloc[:,:]


# In[52]:


### Make a numpy series for the zipcode column data
zipcode_arr = df['Provider_Address_Zip'].values


# In[53]:


### Confirm array type
type(zipcode_arr)


# In[54]:


### Use pyplot to display the zipcode array
plt.plot(zipcode_arr)


# In[68]:


### plot a histogram using the zipcode array series with 58 bins (the number of counties in CA)
plt.hist((zipcode_arr), bins=58)


# In[69]:


###  Trying another way
zipcode_series = df['Provider_Address_Zip']


# In[70]:


type(zipcode_series)


# In[71]:


plt.plot(zipcode_series)


# In[75]:


df.plot()
plt.yscale('log')


# In[76]:


### Plot all columns as subplots
df.plot(subplots=True)
plt.show()


# In[78]:


### Plot only the Provider_Type_Code and City data
z_list =['Provider_Type_Code','Provider_Address_City']
df[z_list].plot()
plt.show()


# In[83]:


### Run a Cumulative distribution on the Provider_Type_Code as a histogram
df.plot(y='Provider_Type_code', kind='box', bins=60, range=(0,60), cumulative=True, normed=True)
plt.xlabel('Provider_Type_Code_Desc')
plt.show()


# In[86]:


### Return the number of entries of zipcodes in the series (column)
df['Provider_Address_Zip'].describe()


# In[88]:


###  Finally find all of the unique zipcodes from the DataFrame; assign to zc_array
zc_array = df['Provider_Address_Zip'].unique()


# In[91]:


zc_array.shape


# In[108]:


### Select rows and columns for zipcode
only_zip = df.loc[:,'Provider_Address_Zip']
print(only_zip)


# In[109]:


### Sort the df by zipcode
df.sort_values(by='Provider_Address_Zip')


# In[247]:


### Parse the data against Provider_Type_Code and Provider_Address_Zip
parsed = pd.read_csv(url, index_col=['Provider_Type_Code', 'Provider_Type_Code_Desc','Provider_Address_Zip'])
parsed


# In[248]:


### sort the parsed data
ans = parsed.sort_values(by='Provider_Address_Zip')
ans


# In[287]:


### Ask user their zipcode
CAzip = int(input('What is your zipcode?: '))
type(CAzip)


# In[288]:


### Find all rows that contain input CAzip
xs = pd.IndexSlice
row = ans.loc[xs[:,:,CAzip],:]
row


# In[289]:


### Sort resulting dataframe by Provider_Type_Code
row.sort_values(by='Provider_Type_Code')


# In[118]:


### Find the number of unique zipcodes
uzips = only_zip.unique()
uzips


# In[124]:


### count unique values in Series only_zip 
pd.value_counts(only_zip, sort=False)


# In[135]:


### Sort the Series of Provider_Address_Zip; assign to soz
soz = only_zip.sort_values()
soz


# In[137]:


type(soz)


# In[139]:


### Sort the zipcodes with the most Providers to least
pd.value_counts(soz)


# In[145]:


### Make a histogram of soz
soz.hist()


# In[144]:


plt.figure(figsize=(10,10)) # note: figure size argument must come before the figure is generated
df['Provider_Address_Zip'].hist(bins=704)
plt.title('Volume of Providers by Zipcode')


# In[55]:


import seaborn as sns


# In[58]:


sns.__version__


# In[140]:


# making a line graph with Seaborn
sns.lineplot(x='Provider_Address_Zip', y='Provider_Address_city', hue='country',data=soz)


# In[56]:


###  Use seaborn to better visualize the data
plt.style.use('seaborn-dark')
zipcode_arr.hist(bins=20)


# In[ ]:


# solution
plt.figure(figsize=(5,5)) # note: figure size argument must come before the figure is generated
df['gdp per cap'].hist(bins=50)
plt.title('what a gorgeous plot title!')
plt.savefig('my_hist.pdf')

