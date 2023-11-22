var = "What is the Airspeed Velocity of an Unladen Swallow?"

l_of_words = var.split()

dict_for_words = {word: len(word) for word in l_of_words}

print(dict_for_words)
