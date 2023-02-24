import pandas
#pandas is imported to create , modify , access CSV(Data) file of User data

#   creating csv file function is used to create a csv file if it doesn't exists
def creating_csv_file():
    file = open("data.csv","w")
    file.close()
#calling above function because if the csv file in the required directory is not created  the above code will create it automatically 
creating_csv_file()


#update file function  creates data frame and update the data in csv file
def update_file(dic):
    data_frame = pandas.DataFrame(dic)
    data_frame.to_csv("data.csv",index=False)

    
#   get data function is used to retrive data from CSV file and filter the data according to requirement
def get_data(v_type):
    data = pandas.read_csv("data.csv")
    user_data1 = data[data["Vehicle_Type"]==v_type] #filtering data
    user_data2 = user_data1.to_string(index=False)  #converting dataframe into string
    return user_data2