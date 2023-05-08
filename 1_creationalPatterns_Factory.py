'''

    Design Pattern 1: Creational Pattern - Factory.

'''

class Burger:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def print(self):
        print(self.ingredients)

class BurgerFactory:
    
    def createCheeseBurger(self):
        ingredients = ['bun', 'cheese', 'beef-patty']
        return Burger(ingredients)
    
    def createDeluxeCheeseBurger(self):
        ingredients = ['bun', 'tomato', 'lettuce','cheese', 'beef-patty']
        return Burger(ingredients)
    
    def createVegenBurger(self):
        ingredients = ['bun', 'special-sauce', 'veggie-patty']
        return Burger(ingredients)

if __name__ == '__main__':
    burgerFactory = BurgerFactory()
    burgerFactory.createCheeseBurger().print()
    burgerFactory.createDeluxeCheeseBurger().print()
    burgerFactory.createVegenBurger().print()