# Project 6: Favorite Movies List
# Topic: Lists in Python

movies = ["Inception", "Interstellar", "The Matrix"]

print("My movies:", movies)
print("First movie:", movies[0])
print("Last movie:", movies[-1])

# add new movie
movies.append("Tenet")
print("After adding:", movies)

# remove movie
movies.remove("The Matrix")
print("After removing:", movies)

# count movies
print("Total movies:", len(movies))
