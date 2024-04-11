import pymongo
import sys

uri = "mongodb+srv://nap_mongotest:v1AMmQkBgxmvJsGE@clusternap.o18ahls.mongodb.net/?retryWrites=true&w=majority&appName=ClusterNAP"

try: 
    client = pymongo.MongoClient(uri)
except pymongo.errors.ConfigurationError:
    print("An invalid URI host was provided")
    sys.exit(1)

