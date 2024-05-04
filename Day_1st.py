import pandas as pd
weather_data={
    'day':["1/1/24","1/2/24","1/3/24","1/4/24","1/5/24","1/6/24"],
    'Temperature':[32,35,28,24,32,31],
    'windspeed':[6,7,2,7,4,2],
    'event':["Rain","Sunny","Snow","Rain","Sunny","Rain"]
}
df=pd.DataFrame(weather_data)
print(df)
#print(df.shape)
rows,columns=df.shape
print("The NO of rows in a data frame is",rows)
print("the nos of cloumns in a data frame as ",columns)
print(df.head)#some time we have a large data set to print the head we used that 
print(df.head(2))#it will print the first 2 rows in a data set
print(df.tail)#it will print the last data in a data set
print(df.tail(1))#whenever we pass the the parameter it will print some specific values i.e it print the last row in a data frame
# let suppose i want to print from row 2 to 4 we used indexing and slicing
print(df[2:5])#it include 2 and 5 is not included in it
#to print all and everything we use
print(df[:])#oR print(df)
print(df.columns)#print the columns Name
#to print the contents of the columns we used
print(df.day)# simalarly we used  df.event to print the event columnsa and soo on

#some operation on the above data
print(df.Temperature.max())#the maximum values in temperature columns will print
# min(), mean(),std(),
print(df.describe())




