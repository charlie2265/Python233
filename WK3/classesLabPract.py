# Calorie counter with class

class Food_Item:
    def __init__(self, name, carbs, fats, proteins):
        self.name = name
        self.carbs = carbs
        self.fats = fats
        self.proteins = proteins

    # def det_cals(self):
    #     cals = self.carbs * 4 + self.fats * 9 + self.proteins * 4
    #     return(cals)
    def lambda_cals(self):
        l_cals = lambda x,y: x * y
        carbs = l_cals(self.carbs, 4)
        fats = l_cals(self.fats, 9)
        proteins = l_cals(self.proteins, 4)
        return carbs+fats+proteins
    
    def disp_cals(self):
        print(f"Calories for {self.name} are {self.lambda_cals()}")


myFood = Food_Item("banana", 4, 5, 3)

# print(f"Calories for {myFood.name} is {myFood.det_cals()}")

# myFood.disp_cals()

# print(f"Calories for {myFood.name} is {myFood.lambda_cals()}")

# myFood.lambda_cals()
myFood.disp_cals()
