# def get_nutrients_name():
#
#     nutrients = ["Protein", "Total lipid (fat)", "Carbohydrate, by difference", "Energy", "Water", "Caffeine",
#                  "Sugars, total including NLEA", "Fiber, total dietary", "Calcium, Ca", "Iron, Fe", "Cholesterol",
#                  ]
#     return nutrients

class nutrients:
    @staticmethod
    def get_macronutrients():
        macros = ["Protein", "Carbohydrate, by difference", "Energy"]

        return macros

    @staticmethod
    def get_fats():
        fats = ["Total lipid (fat)", "Sugars, total including NLEA", "Cholesterol", "Fatty acids, total saturated"]

        return fats

    @staticmethod
    def get_minerals():
        minerals = ["Calcium, Ca", "Iron, Fe", "Magnesium, Mg", "Sodium, Na"]

        return minerals

    @staticmethod
    def get_vitamins():
        vitamins = ["Vitamin A, RAE", "Vitamin E (alpha-tocopherol)", "Vitamin D (D2 + D3)",
                    "Vitamin C, total ascorbic acid", "Vitamin B-12"]

        return vitamins
