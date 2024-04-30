import sqlite3

# Vulnerable function that constructs SQL query using string concatenation
def search_users_vulnerable(name):
    db = sqlite3.connect('users.db')
    cursor = db.cursor()
    query = "SELECT * FROM users WHERE name = '" + name + "';"  # Vulnerable line
    cursor.execute(query)
    results = cursor.fetchall()
    db.close()
    return results

# Example usage
search_users_vulnerable("Alice' OR '1'='1")
