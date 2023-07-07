import pandas as pd
original = pd.read_csv(r"C:\Users\Eyepatch\Documents\Uber data analysis\uber_data.csv")
df = original


# Vendor details (Dimension)
vendors_dict = {1:'Creative Mobile Technologies,LLC',
           2:'Verifone Inc'}
vendors = pd.DataFrame()
vendors['Vendor_id'] = df['VendorID'].drop_duplicates().reset_index(drop=True)
vendors['Vendor_name'] = vendors['Vendor_id'].map(vendors_dict)
vendors['Vendor_id']
df['tpep_pickup_datetime']=pd.to_datetime(df['tpep_pickup_datetime'])
df['tpep_dropoff_datetime']=pd.to_datetime(df['tpep_dropoff_datetime'])


# all we are doing here is 1. creating categories so that each value can have a unique id(its code or cat code) 
# so that even if we have duplicate values new value will not get assigned to
# each category with same value will have same code
# then we're using cat.codes(codes assigned to the category) to exchange values with the codes (as ids) in main data frame.
# datetime_df = pd.DataFrame()
# datetime_df['datetime'] = (df['tpep_pickup_datetime'].astype('str')+df['tpep_dropoff_datetime'].astype('str'))
# datetime_df['datetime'] = datetime_df['datetime'].astype('category')
# datetime_df['datetime_id'] = datetime_df['datetime'].cat.codes
# df.insert(loc=1,column='datetime_id',value=datetime_df['datetime_id'])
'''
this code can be used to check that the datetime_id we inserted in the main dataframe 
and the value inide the datetime_df dataframe are same and just to check that we can apply
this technique on further dataframes.
print(df.loc[df['datetime_id'].isin([99800])][['tpep_pickup_datetime','tpep_dropoff_datetime']])
print(new_col.loc[df['datetime_id'].isin([99800])])'''


# Pickup datetime (Dimension)
datetime_details = pd.DataFrame()
datetime_details['datetime_id'] =(df['tpep_pickup_datetime'].astype('str')+df['tpep_dropoff_datetime'].astype('str')).astype('category').cat.codes
datetime_details['pickup_date'] =df['tpep_pickup_datetime'].dt.date
datetime_details['pickup_time'] = df['tpep_pickup_datetime'].dt.time
datetime_details['pickup_day_number'] = df['tpep_pickup_datetime'].dt.day 
datetime_details['pickup_weekday'] = df['tpep_pickup_datetime'].dt.day_name() 
datetime_details['pickup_month'] = df['tpep_pickup_datetime'].dt.month
datetime_details['pickup_year'] = df['tpep_pickup_datetime'].dt.year


# Propoff datetime (Dimension)
datetime_details['dropoff_date'] = df['tpep_dropoff_datetime'].dt.date 
datetime_details['dropoff_time'] = df['tpep_dropoff_datetime'].dt.time 
datetime_details['dropoff_day_number'] = df['tpep_dropoff_datetime'].dt.day 
datetime_details['dropoff_weekday'] = df['tpep_dropoff_datetime'].dt.day_name() 
datetime_details['dropoff_month'] = df['tpep_dropoff_datetime'].dt.month
datetime_details['dropoff_year'] = df['tpep_dropoff_datetime'].dt.year
df = df.drop(columns=['tpep_pickup_datetime','tpep_dropoff_datetime'])


# Pickup details (Dimension)
pickup_details = pd.DataFrame()
myframe = pd.DataFrame()
myframe['catagories'] = ((df['pickup_longitude'].astype('str')+"           "+df['pickup_latitude'].astype('str'))).astype('category')
print(myframe['catagories'].cat.codes)
print("}-----------------------------")
pickup_details['pickup_id'] = (df['pickup_longitude'].astype('str')+df['pickup_latitude'].astype('str')).astype('category').cat.codes
pickup_details['pickup_latitude'] = df['pickup_latitude']
pickup_details['pickup_longitude'] = df['pickup_longitude']
df.insert(loc=4,column='pickup_id',value=pickup_details['pickup_id'])
pickup_details['pickup_location_id'],pickup_details['pickup_longitude'],pickup_details['pickup_latitude'] = pickup_details['pickup_id'],df[['pickup_longitude']],df['pickup_latitude']
df = df.drop(columns=['pickup_longitude','pickup_latitude'])


# Dropoff details
dropoff_details = pd.DataFrame()
dropoff_id = (df['dropoff_longitude'].astype('str')+df['dropoff_latitude'].astype('str')).astype('category').cat.codes
df.insert(loc=7,column='dropoff_id',value=dropoff_id)
dropoff_details['dropoff_location_id'],dropoff_details['dropoff_longitude'],dropoff_details['dropoff_latitude'] = dropoff_id,df[['dropoff_longitude']],df['dropoff_latitude']
df = df.drop(columns=['dropoff_longitude','dropoff_latitude'])


# Payment methods/types (Dimension)
payment_types_names = {
    1:"Credit card",
    2:"Cash",
    3:"No charge",
    4:"Dispute",
    5:"Unknown",
    6:"Voided trip"
}
payment_types = pd.DataFrame()
payment_types['payment_type_id'] = list(payment_types_names.keys())
payment_types['payment_type_name'] = payment_types['payment_type_id'].map(payment_types_names)


# Rate types (Dimension)
rate_code_type = {
    1:"Standard rate",
    2:"JFK",
    3:"Newark",
    4:"Nassau or Westchester",
    5:"Negotiated fare",
    6:"Group ride"
}
ratecodes = pd.DataFrame()
ratecodes['rate_code_id'] = list(rate_code_type.keys())
ratecodes['rate_code_name'] = ratecodes['rate_code_id'].map(rate_code_type)

# Fact table 
fact_table =df

