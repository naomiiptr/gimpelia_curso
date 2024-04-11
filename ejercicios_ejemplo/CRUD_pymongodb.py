import pymongo
import sys

uri = "mongodb+srv://nap_mongotest:v1AMmQkBgxmvJsGE@clusternap.o18ahls.mongodb.net/?retryWrites=true&w=majority&appName=ClusterNAP"

try: 
    client = pymongo.MongoClient(uri)
except pymongo.errors.ConfigurationError:
    print("An invalid URI host was provided")
    sys.exit(1)

db = client.sample_mflix

#filtro = {}
#print(db.movies.count_documents(filtro))

#for name in db.list_collection_names():
 #   print(name)


#movie = db.movies.find_one(filtro)
#theater = db.theaters.find_one(filtro)

#movies_keys = list(movie.keys())
#theater_keys = list(theater.keys())

#print(movies_keys)
#print(theater_keys)


#####
#filtro2 = {'rated':'TV-G', 'year':1903}
#print(db.movies.count_documents(filtro2))
#print(db.movies.find(filtro2))


#####
#filtro3 = {'num_mflix_comments':{'$gt':15}}
#db.movies.count_documents(filtro3)


#####
#filtro4 = {'num_mflix_comments':{'$gt':15}, 'year':{'$gte':2000}}
#db.movies.count_documents(filtro4) 


#####
#filtro5 = {'num_mflix_comments':{'$gt':1}, 
 #          'year':{'$gte':2000},
  #         'type':{'$ne':'movie'}}
#db.movies.count_documents(filtro5) 

#####
#filtro6 = {'genres':'Western', 
      #     'year':{'$gte':2000},
       #    'tomatoes.viewer.rating':{'$gt':4}}
#db.movies.count_documents(filtro6)

#####
#filtro7 = {'genres':'Fantasy', 
       #    'year':1990}
#for movie in db.movies.find(filtro7).limit(3):
 #   print(movie["title"])

#print(db.movies.count_documents(filtro7))


#####
# 1= ASC, -1= DESC
filtro8 = {'genres':{'$in':['Action', 'Thriller']},
           'year':{'$lt':2000},
           'tomatoes.viewer.rating':{'$gt':4},
           'num_mflix_comments':{'$gt':1}}

#print(db.movies.count_documents(filtro8))

#for movie in db.movies.find(filtro8).sort("tomatoes.viewer.rating",-1):
  #  print(movie["title"])

best_ratted_movie = db.movies.find(filtro8).sort("tomatoes.viewer.rating",-1)

for movie_ratted in best_ratted_movie:
    print(movie_ratted["title"])

