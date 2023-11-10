# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class occupations:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.Last_name = data['Last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM occupations;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('new_schema12').query_db(query)
        # Create an empty list to append our instances of friends
        occupations = []
        # Iterate over the db results and create instances of friends with cls.
        for occupation in results:
            occupations.append(cls(occupation))
            # watch for s in these understand difference between dictonary and list
        return occupations
    # Retuen a list becuase we have ran a for loop to gather 
    # all the key value pairs in  the dictornary giving us all the values in this list 
            
