from abc import ABC , abstractmethod
#ABC class and abstract method are imported to create abstract methods 
import database
# DataBase is imported to maintain connection between Service layer and Database layer

# Parent class : Vehicle
class Vehicle(ABC):
    # Vehicle class inherits ABC because , to implement abstract methods

    #occupation is a constant dictionary where we can get the occupation details of the car owner
    occupation = {"businessman" : "BUSINESS MAN",
                  "medical assistant" : "MEDICAL ASSISTANT",
                  "retail sales associate" : "RETAIL SALES ASSOCIATE",
                  "sales representative" : "SALES REPRESENTATIVE",
                  "social media specialist" : "SOCIAL MEDIA SPECIALIST",
                  "teacher" : "TEACHER",
                  "Nurse" : "NURSE",
                  "software engineer" : "SOFTWARE ENGINEER",
                  "cable tv operation" : "CABLE TV OPERATION",
                  "software developer" : "SOFTWARE DEVELOPER"
                  }
    
    def __init__(self, owner, vehicle_name, vehicle_make, age, kilometers_driven, first_hand, second_hand, registration_number, owner_occupation ):
        self.owner = owner                          # owner variable refers to car owner name
        self.vehicle_name = vehicle_name            # vehicle_name  variable refers to vehicle name
        self.vehicle_make = vehicle_make            # vehicle_make variable refers to vehicle make
        self.age = age                              # age variable refers to number of months did the owner used the used the vehicle
        self.kilometers_driven = kilometers_driven  # kilometers_driven variable refers to how many kilometers the vehicle is driven
        self.first_hand = first_hand                # first_hand variable refers to know weather the vehicle is new or not there will be only yes or no values for this variable
        self.second_hand = second_hand              # second_hand variable is same as first_hand variable but in the reverse way
        self.registration_number = registration_number  #registration_number variable is used to note the registration number  
        self.owner_occupation = Vehicle.occupation.get(owner_occupation)    # owner_occupation variable collects the occupation of owner of   
        
        # A car must be First hand or Second hand, but not both at a time. So, here we checking that situation and raising exception if it occurs
        if ((first_hand == "Yes" or first_hand =="yes") and (second_hand == "Yes" or second_hand =="yes")) or ((first_hand == "No" or first_hand ==  "no") and (second_hand == "No" or second_hand == "no")) :
            raise Exception("the value of first hand and second hand cannot be same at a time")

    @abstractmethod
    def get_vehicle_name(self):
        # it is a abstract method it will be implemented in the respective child classes
        # prints vehicle name
        pass
    
    @abstractmethod
    def get_vehicle_type(self):
        # it is a abstract method it will be implemented in the respective child classes
        # prints vehicle type
        pass

# child class : Hatchback 
class Hatchback(Vehicle):
    #   inherits Vehicle class
    def __init__(self, owner, vehicle_name, vehicle_make, age, kilometers_driven, first_hand, second_hand, registration_number, owner_occupation):
        self.vehicle_type = "Hatchback"         #vehicle_type refers to the type of vehicle 
        super().__init__(owner, vehicle_name, vehicle_make, age, kilometers_driven, first_hand, second_hand, registration_number, owner_occupation)     
        user_details(owner, vehicle_name,self.vehicle_type, vehicle_make, age, kilometers_driven, first_hand, second_hand, registration_number, self.owner_occupation)
        
    def get_vehicle_name(self):
        print(self.vehicle_name)
    
    def get_vehicle_type(self):
        print(self.vehicle_type)
        
# child class : sedan
class Sedan(Vehicle):
    #   inherits Vehicle class

    def __init__(self, owner, vehicle_name, vehicle_make, age, kilometers_driven, first_hand, second_hand, registration_number, owner_occupation):
        self.vehicle_type = "Sedan"
        super().__init__(owner, vehicle_name, vehicle_make, age, kilometers_driven, first_hand, second_hand, registration_number, owner_occupation)
        user_details(owner, vehicle_name,self.vehicle_type, vehicle_make, age, kilometers_driven, first_hand, second_hand, registration_number, self.owner_occupation)
        
    def get_vehicle_name(self):
        print(self.vehicle_name)
    
    def get_vehicle_type(self):
        print(self.vehicle_type)
    
# child class : SUV 
class SUV(Vehicle):
    #   inherits Vehicle class
    
    def __init__(self, owner, vehicle_name, vehicle_make, age, kilometers_driven, first_hand, second_hand, registration_number, owner_occupation):
        self.vehicle_type = "SUV"
        super().__init__(owner, vehicle_name, vehicle_make, age, kilometers_driven, first_hand, second_hand, registration_number, owner_occupation)
        user_details(owner, vehicle_name,self.vehicle_type, vehicle_make, age, kilometers_driven, first_hand, second_hand, registration_number, self.owner_occupation)
        
    def get_vehicle_name(self):
        print(self.vehicle_name)
    
    def get_vehicle_type(self):
        print(self.vehicle_type)
    
# child class : Premium SUV 
class PremiumSUV(Vehicle):
    #   inherits Vehicle class
    
    def __init__(self, owner, vehicle_name, vehicle_make, age, kilometers_driven, first_hand, second_hand, registration_number, owner_occupation):
        self.vehicle_type = "Premium SUV"
        super().__init__(owner, vehicle_name, vehicle_make, age, kilometers_driven, first_hand, second_hand, registration_number, owner_occupation)
        user_details(owner, vehicle_name,self.vehicle_type, vehicle_make, age, kilometers_driven, first_hand, second_hand, registration_number, self.owner_occupation)        

    def get_vehicle_name(self):
        print(self.vehicle_name)
    
    def get_vehicle_type(self):
        print(self.vehicle_type)
    
# child class : Limousine  
class Limousine(Vehicle):
    #   inherits Vehicle class
    
    def __init__(self, owner, vehicle_name, vehicle_make, age, kilometers_driven, first_hand, second_hand, registration_number, owner_occupation):
        self.vehicle_type = "Limousine"
        super().__init__(owner, vehicle_name, vehicle_make, age, kilometers_driven, first_hand, second_hand, registration_number, owner_occupation)
        user_details(owner, vehicle_name,self.vehicle_type, vehicle_make, age, kilometers_driven, first_hand, second_hand, registration_number, self.owner_occupation)
        
    def get_vehicle_name(self):
        print(self.vehicle_name)
    
    def get_vehicle_type(self):
        print(self.vehicle_type)
    
# child class : Crossovers 
class Crossovers(Vehicle):
    #   inherits Vehicle class
    
    def __init__(self, owner, vehicle_name, vehicle_make, age, kilometers_driven, first_hand, second_hand, registration_number, owner_occupation):
        self.vehicle_type = "Crossover"
        super().__init__(owner, vehicle_name, vehicle_make, age, kilometers_driven, first_hand, second_hand, registration_number, owner_occupation)
        user_details(owner, vehicle_name,self.vehicle_type, vehicle_make, age, kilometers_driven, first_hand, second_hand, registration_number, self.owner_occupation)
        
    def get_vehicle_name(self):
        print(self.vehicle_name)
    
    def get_vehicle_type(self):
        print(self.vehicle_type)

#   dic is dictionary that is used to store the details of every user
dic = {"Owner_name" : [], "Vehicle_Name" : [], "Vehicle_Type" : [], "Vehicle_Make" : [], "Owner_Age" : [], "Kilometers_Driven" : [],
            "First_Hand" : [], "Second_Hand" : [], "Registraion_Number" : [], "Owner_Occupation" : []}

# user_details function is used to store each and every detail of the different users into a dictionary dic 
def user_details(owner, vehicle_name,vehicle_type, vehicle_make, age, kilometers_driven, first_hand, second_hand, registration_number, owner_occupation):
    
    dic["Owner_name"].append(owner)
    dic["Vehicle_Name"].append(vehicle_name)
    dic["Vehicle_Type"].append(vehicle_type)
    dic["Vehicle_Make"].append(vehicle_make)
    dic["Owner_Age"].append(age)
    dic["Kilometers_Driven"].append(kilometers_driven)
    dic["First_Hand"].append(first_hand)
    dic["Second_Hand"].append(second_hand)
    dic["Registraion_Number"].append(registration_number)
    dic["Owner_Occupation"].append(owner_occupation)
    
# upload data function call the update_file function in database file which loads all user data into a csv file using dataframes concept through pandas module
def upload_data():
    database.update_file(dic)

# show details function call the get_data function in database file and get the data of required vehicle type 
def show_details(v_type):
    filter_data = database.get_data(v_type)
    return filter_data
