from operations import Hatchback , Sedan , PremiumSUV , SUV , Limousine , Crossovers 
import operations
#operations is imported to maintain connection between interface layer and service layer

# function for creating database records
def create_database_records():
    
    #h1,h2,h3,h4,h5,sed1,sed2,sed3,sed4,sed5,suv1,suv2,suv3,suv4,suv5,psuv1,psuv2,psuv3,psuv4,psuv5,l1,l2,l3,l4,l5,c1,c2,c3,c4,c5 are the objectives of respectve classes Hatchback , Sedan , SUV , PremiumSUV , Limousine , Crossovers 
    
    h1 = Hatchback("varshith","I20","Hyundai",6,1000,"Yes","No","TS-01-EL-3888","businessman")
    h2 = Hatchback("Prasanth","Baleno","Maruthi Suzuki",8,2000,"No","Yes","KA-03-HA-1985","medical assistant")
    h3 = Hatchback("Saketh","Swift","Maruthi Suzuki",3,26000,"Yes","No","MH-19-AG-5465","retail sales associate")
    h4 = Hatchback("Sai Kiran","Altroz","Tata",1,700,"No","yes","TN-75-AA-7106","sales representative")
    h5 = Hatchback("Divesh","Jazz","Honda",8,2000,"No","Yes","AP 21 BP 7331","social media specialist")
    
    sed1 = Sedan("Balaji","Verna","Hyundai",33,12345,"Yes","No","UP 19 D 0343","teacher")
    sed2 = Sedan("Abhilash","Virtus","Volks Wagen",46,23200,"Yes","No","KA 08 J 9192","Nurse")
    sed3 = Sedan("Venu","A4","Audi",57,16000,"Yes","No","MH 12 RN 1289","software engineer")
    sed4 = Sedan("Abhinav","Octavia","Skoda",27,92000,"No","Yes","TS 07 D TR 2020","cable tv operation")
    sed5 = Sedan("Sampath","Phantom VIII","Rolls Royce",51,89000,"Yes","No","TS-01-EL-3888","social media specialist")
    
    suv1 = SUV("Revanth","Scorpio","Mahindra",5,42010,"Yes","No","TS 28 A 2345","businessman")
    suv2 = SUV("Gurudatta","Thar","Mahindra",15,20020,"Yes","No","TS 9 AB 1200","software engineer")
    suv3 = SUV("Aravind","XUV","Mahindra",66,20200,"Yes","No","TS 13 T5 4656","medical assistant")
    suv4 = SUV("Vamshi Krishna","Creta","Hyundai",17,11100,"Yes","No","TS-01-EL-3888","software engineer")
    suv5 = SUV("Mastaan","Harrier","Tata",38,43000,"Yes","No","AP 21 BP 7331","medical assistant")
    
    psuv1 = PremiumSUV("Kumar","Expendition","Ford",81,2000,"No","Yes","TS 9 AB 1200","software engineer")
    psuv2 = PremiumSUV("Sravan","Land rover","Range Rover",58,2000,"Yes","No","AP 21 BP 7331","social media specialist")
    psuv3 = PremiumSUV("Hari Krishna","Mercedes","Benz",18,2000,"No","Yes","MH-19-AG-5465","cable tv operation")
    psuv4 = PremiumSUV("Mahesh","X7","BMW",34,2000,"Yes","No","MH 12 RN 1289","Nurse")
    psuv5 = PremiumSUV("Venu madhav","Urus","Lamborgini",23,2000,"No","Yes","TS 06 SA 1234","software developer")
    
    l1 = Limousine("Prabhas","A6","Audi",72,24000,"Yes","No","TN-75-AA-7106","businessman")
    l2 = Limousine("Varun","5 series","BMW",37,27330,"No","Yes","UP 19 D 0343","Nurse")
    l3 = Limousine("Jayanth","Mercedes E-Class","Benz",9,200,"No","Yes","MH-19-AG-5465","medical assistant") 
    l4 = Limousine("Eshwar","Mercedes S-Class","Benz",47,40600,"No","Yes","TS-01-EL-3888","cable tv operation")
    l5 = Limousine("Ruthvik","A8 L","Audi",43,47620,"No","Yes","TS 9 AB 1200","businessman")
    
    c1 = Crossovers("Rohith","Kwid","Renault",25,78645,"No","Yes","UP 19 D 0343","teacher")
    c2 = Crossovers("Yashwanth","S-Presso","Maruthi Suzuki",35,96458,"Yes","No","AP 21 BP 7331","social media specialist")
    c3 = Crossovers("Raj Kamal","Ignis","Maruthi Suzuki",28,98762,"Yes","No","MH 12 RN 1289","software engineer")
    c4 = Crossovers("Naveen","freestyle","Ford",33,13242,"Yes","No","MH-19-AG-5465","teacher")
    c5 = Crossovers("Abhishek","S-Cross","Maruthi Suzuki",11,22000,"No","Yes","TN-75-AA-7106","businessman")

# function for loading database 
def load_database():
    operations.upload_data()
   
# function for display records for particular vehicle type
def display_records_for_particular_vehicle_type():
    v_type = "Limousine"      # v_type can be the filter that helps to get the particular vehicle type data 
    
    #printing the data according to requirement
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
    print(operations.show_details(v_type))
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
    
#calling the (API's) functions respectively

create_database_records() 

load_database()

display_records_for_particular_vehicle_type()