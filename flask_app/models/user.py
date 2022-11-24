from flask_app.config.mysqlconnection import connectToMySQL

class User:
    db_name= 'users_cr'
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email= data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.db_name).query_db(query)
        # Create an empty list to append our instances of users
        users = []
        # Iterate over the db results and create instances of friends with cls.
        for user in results:
            users.append( user )
        return users
    
    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)
    @classmethod
    def get_user_byId(cls,data):
        query= "SELECT * FROM users WHERE id =  %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return results[0]
    @classmethod
    def deleteuser(cls, data):
        query = "DELETE FROM users WHERE id =  %(id)s"
        return connectToMySQL(cls.db_name).query_db(query, data)
    @classmethod
    def updateuser(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s,last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s; "
        return connectToMySQL(cls.db_name).query_db(query, data)

