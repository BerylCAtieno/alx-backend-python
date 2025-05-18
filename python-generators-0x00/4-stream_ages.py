import mysql.connector

def stream_user_ages():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',  # add your password if needed
        database='ALX_prodev'
    )
    cursor = connection.cursor()
    cursor.execute("SELECT age FROM user_data")

    for (age,) in cursor:
        yield age

    cursor.close()
    connection.close()

def calculate_average_age():
    total_age = 0
    count = 0
    for age in stream_user_ages():
        total_age += age
        count += 1

    average = total_age / count if count else 0
    print(f"Average age of users: {average}")

if __name__ == "__main__":
    calculate_average_age()
