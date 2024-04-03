#print("Hello Dear")
#fruits = ["apple", "pear", "orange"]

#for fruit in fruits:
#    print(fruit)


#Nesting a List in a  dictioary
Capitals={
    "France" : "Paris" ,
    "Germany" : "Berlin" ,
    "Hungary" : "Budapest" ,

}

travel_log= {
    "France":  ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Munchen", "Hamburg"],
    }
#Nesting dictionary in a dictionary

travel_log={
    "france":{"cities_visited" :["Paris", "Lille", "Dijon"]}, 
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Köln"], "total_visits": 12 }         
}

#Nesting Dictionary ina a List

travel_log =[
    {
     "Country": "France",
     "cities_visited" :["Paris", "Lille", "Dijon"],
     "total_visits": 12 ,

    },
    {
     "Country": "Germany",
     "cities_visited": ["Berlin", "Hamburg", "Köln"], 
     "total_visits": 5 , 


    },
]

