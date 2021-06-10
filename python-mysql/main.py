from getpass import getpass 
from mysql.connector import connect, Error

try:
    with connect(
        host = "localhost",
        # user = input("Enter username: "),
        user = "root",
        password = getpass('Enter password: '),
        database = "war_movies"
    ) as connection:
        create_db_query = 'CREATE DATABASE IF NOT EXISTS war_movies'
        with connection.cursor() as cursor:
            cursor.execute(create_db_query)
            connection.commit()

        create_movies_table = """
        CREATE TABLE IF NOT EXISTS movies(
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(100),
            release_year YEAR(4),
            genre VARCHAR(100)
        )
        """
        with connection.cursor() as cursor:
            cursor.execute(create_movies_table)
            connection.commit()

        create_ratings_table = """
        CREATE TABLE IF NOT EXISTS ratings (
            movie_id INT,
            reviewer_id INT,
            rating DECIMAL(2, 1),
            # FOREIGN KEY(movie_id) REFERENCES movies(id),
            # FOREIGN KEY(reviewer_id) REFERENCES reviewers(id),
            PRIMARY KEY(movie_id, reviewer_id)
        )
        """
        with connection.cursor() as cursor:
            cursor.execute(create_ratings_table)
            connection.commit()
except Error as e:
    print(e)






