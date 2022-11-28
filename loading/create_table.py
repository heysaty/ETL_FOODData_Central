class tables:
    @staticmethod
    def create_fooditems():
        query = """CREATE TABLE fooditems(
                id SERIAL PRIMARY KEY ,
                food_item VARCHAR(100),
                description VARCHAR(300),
                nutrients_log_id INT REFERENCES nutrients_log(id)
            );"""

        return query

    @staticmethod
    def create_nutrientslog():
        query = """CREATE TABLE nutrients_log(
                   id SERIAL PRIMARY KEY ,
                   macro_nutrients_id INT REFERENCES macro_nutrients(id),
                   micro_nutrients_id INT REFERENCES micro_nutrients(id)
              
                   
               );"""
        return query

    @staticmethod
    def create_macronutrients():
        query = """CREATE TABLE macro_nutrients(
                   id SERIAL PRIMARY KEY ,
                   Protein VARCHAR(100),
                   Carbohydrate VARCHAR(100),
                   Energy VARCHAR(100),
                   fats_id INT REFERENCES fats(id)
               );"""
        return query

    @staticmethod
    def create_micronutrients():
        query = """CREATE TABLE micro_nutrients(
                   id SERIAL PRIMARY KEY ,
                   minerals_id INT REFERENCES minerals(id),
                   vitamins_id INT REFERENCES vitamins(id)
               );"""
        return query

    @staticmethod
    def create_fats():
        query = """CREATE TABLE fats(
                   id SERIAL PRIMARY KEY ,
                   lipid VARCHAR(100),
                   Sugars VARCHAR(100),
                   Cholesterol VARCHAR(100),
                   Fatty_acids VARCHAR(100)
               );"""
        return query

    @staticmethod
    def create_minerals():
        query = """CREATE TABLE minerals(
                   id SERIAL PRIMARY KEY ,
                   Calcium VARCHAR(100),
                   Iron VARCHAR(100),
                   Magnesium VARCHAR(100),
                   Sodium VARCHAR(100)
                   
               );"""
        return query

    @staticmethod
    def create_vitamins():
        query = """CREATE TABLE vitamins(
                   id SERIAL PRIMARY KEY ,
                   Vitamin_A VARCHAR(100),
                   Vitamin_E VARCHAR(100),
                   Vitamin_D VARCHAR(100),
                   Vitamin_C VARCHAR(100),
                   Vitamin_B12 VARCHAR(100)
                   
               );"""
        return query

    @staticmethod
    def recipes():
        query = """CREATE TABLE recipes(
                           id SERIAL PRIMARY KEY ,
                           recipe TEXT,
                           food_id INT REFERENCES fooditems(id)

                       );"""
        return query

    @staticmethod
    def food_recipes():
        query = """CREATE TABLE food_recipes(
                           id SERIAL PRIMARY KEY ,
                           food VARCHAR(100),
                           recipe TEXT
                        
                       );"""
        return query


