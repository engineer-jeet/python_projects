class movie:
    '''This class is developed by Jeet for demo'''

    def __init__(self, title, hero, heroine):
        self.title = title # instance variables 
        self.hero = hero
        self.heroine = heroine

    def info(self):
        print("Movie name: ", self.title)
        print("Hero name: ", self.hero)
        print("Heroin name: ", self.heroine)

    
list_of_movies = []
while True:
    title = input("enter movie name: ")
    hero = input("enter hero name: ")
    heroin = input("enter heroine name: ")

    obj = movie(title, hero, heroin)
    list_of_movies.append(obj)

    print("Movie added successfully!")
    option = input("Do you want to add more movies [yes/no]: ")
    if option.lower() == 'no':
        break
    

print("All Movies Information..... ")
print()
for movie in list_of_movies:
    movie.info()
    print()

# print(list_of_movies)





