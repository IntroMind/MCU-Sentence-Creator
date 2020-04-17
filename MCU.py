import random

movies = ['Iron Man', 'The Incredible Hulk', 'Iron Man 2', 'Thor', 'Captain America: The First Avenger',
          'The Avengers', 'Iron Man 3', 'Thor: The Dark World', 'Captain America: The Winter Soldier',
           'Guardians of the Galaxy', 'Avengers: Age of Ultrom', 'Ant-Man', 'Captain America: Civil War',
          'Doctor Strange', 'Guardains of the Galaxy Vol. 2', 'Spider-Man: Homecoming', 'Thor: Ragnarok',
          'Black Panther', 'Avengers: Infinity War', 'Ant-Man and the Wasp', 'Captain Marvel', 'Averngers: Endgame',
          'Spider-Man: Far From Home']

adjectives = ['most underrated', 'best', 'worst', 'most overrated', 'most confusing', 'most uplifting', 'darkest',
              'most light-hearted']

movie = random.choice(movies)

adjective = random.choice(adjectives)

phrase = movie + ' is the ' + adjective + ' film of the Marvel Cinematic Universe.'

print(phrase)



