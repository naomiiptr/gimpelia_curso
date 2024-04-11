from pymongo import MongoClient
from dateutil import parser
from pandas import DataFrame

def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = "mongodb+srv://nap_mongotest:v1AMmQkBgxmvJsGE@clusternap.o18ahls.mongodb.net/?retryWrites=true&w=majority&appName=ClusterNAP"
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return client['user_shopping_list']
 
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":  
 
   # Get the database
   dbname = get_database()
   collection_name = dbname["user_1_items_naomi"]
   
   item_1 = {
    "_id" : "U1IT00001",
    "item_name" : "Blender",
    "max_discount" : "10%",
    "batch_number" : "RR450020FRG",
    "price" : 340,
    "category" : "kitchen appliance"
   }
   
   item_2 = {
        "_id" : "U1IT00002",
        "item_name" : "Egg",
        "category" : "food",
        "quantity" : 12,
        "price" : 36,
        "item_description" : "brown country eggs"
   }
   
#collection_name.insert_many([item_1,item_2])
   


expiry_date = '2021-07-13T00:00:00.000Z'

expiry = parser.parse(expiry_date)
item_3 = {
  "item_name" : "Bread",
  "quantity" : 2,
  "ingredients" : "all-purpose flour",
  "expiry_date" : expiry
}
#collection_name.insert_one(item_3)


expiry_date = '2021-07-13T00:00:00.000Z'
expiry = parser.parse(expiry_date)
orderdate = '2021-06-23T00:00:00.000Z'
order_date = parser.parse(orderdate)

item_4 = {"item_name" : "butter",
"category" : "food",
"batch_number" : "BU5E0020FK",
"price" : 20
}

item_5 = {"item_name" : "face cream",
"category" : "beauty",
"expiry_date" : expiry,
"max_discount" : "4%",
"ingredients" : "Hyaluronic acid, Ceramides, vitamins A,C,E, fruit acids"
}

item_6 = {"item_name" : "fishing plier",
"category" : "sports",
"item_description" : "comes with tungsten carbide cutters to easily cut fishing lines and hooks"
}

item_7 = {"item_name" : "pizza sauce",
"category" : "food",
"quantity" : 5,
"expiry_date" : expiry
}

item_8 = {"item_name" : "fitness band",
"price" : 300,
"max_discount" : "12%",
"order_date" : order_date
}

item_9 = {"item_name" : "cinnamon",
"category" : "food",
"warning" : "strong smell, not to be consumed directly",
"order_date" : order_date,
"price" : 2
}

item_10 = {"item_name" : "lego building set",
"category" : "toys",
"warning" : "very small parts, not suitable for children below 3 years",
"parts_included" : "colored interlocking plastic bricks, gears, minifigures, plates, cones, round bricks"
}

item_11 = {"item_name" : "dishwasher",
"category" : "kitchen appliance",
"order_date" : order_date,
"warranty" : "2 years"
}

item_12 = {"item_name" : "running shoes",
"brand" : "Nike",
"category" : "sports",
"price" : 145,
"max_discount" : "5%"
}

item_13 = {"item_name" : "leather bookmark",
"category" : "books",
"design" : "colored alphabets",
"item_description" : "hand-made, natural colors used"
}

item_14 = {"item_name" : "maple syrup",
"category" : "food",
"item_description" : "A-grade, dark, organic, keep in refrigerator after opening",
"price" : 25,
"order_date" : order_date
}


collection_name.insert_many([item_4,item_5,item_6,item_7,item_8,item_9,item_10,item_11,item_12, item_13, item_14])

 
item_details = collection_name.find()
for item in item_details:
   # This does not give a very readable output
   print(item)

#Convertimos a df a ver que tal
# convert the dictionary objects to dataframe
items_df = DataFrame(item_details)

# see the magic
print(items_df)