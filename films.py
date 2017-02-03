def get_films_starting_with(char):
    films = [
        "The Shawshank Redemption",
        "The Godfather",
        "The Godfather: Part II",
        "Il buono, il brutto, il cattivo.",
        "Pulp Fiction",
        "Inception",
        "Schindler's List",
        "12 Angry Men",
        "One Flew Over the Cuckoo's Nest",
        "The Dark Knight",
        "Star Wars: Episode V - The Empire Strikes Back",
        "The Lord of the Rings: The Return of the King",
        "Shichinin no samurai",
        "Star Wars",
        "Goodfellas"
    ]

    results = []

    for f in films:
        if f.lower().startswith(char.lower()):
            results.append(f)

    return results
