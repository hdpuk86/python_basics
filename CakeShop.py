class CakeShop:
    def __init__(self, name, cakes):
        self.name = name
        self.cakes = cakes

    def average_rating(self):
        ratings = []
        for cake in self.cakes:
            ratings.append(cake.rating)
        total = sum(ratings)
        length = float(len(ratings))
        return total/length
