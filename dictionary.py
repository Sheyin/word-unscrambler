import mysql.connector
import secret

# Note to self: This will no longer work locally because of this file.


def lookup(words):
    mydb = mysql.connector.connect(
        host=secret.host,
        user=secret.user,
        password=secret.password,
        database=secret.db
    )

    found_words = []

    for search_word in words:
        query = "SELECT word FROM words WHERE word='" + search_word + "'"
        cursor = mydb.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        if result:
            # Results are in tuple form, doing this to clean formatting
            for x in result:
                (_,) = x
                found_words.append(_)

    found_words.sort()
    return found_words


# Test code
if __name__ == "__main__":
    search_words = ["bird", "apple", "potato", "sdfsdf", "aaahld", "123"]
    results = lookup(search_words)
    results.sort()
    print("Found words: ")
    for x in results:
        print(x)
