
def create_fooditems():
    query = """CREATE TABLE fooditems(
            id SERIAL PRIMARY KEY ,
            food_item VARCHAR(100),
            description VARCHAR(300),
            nutrients_log_id INT REFERENCES nutrients_log(id)
        );"""

    return query


def create_nutrientslog():
    query = """CREATE TABLE nutrients_log(
               id SERIAL PRIMARY KEY ,
               macro_nutrients_id INT REFERENCES macro_nutrients(id),
               micro_nutrients_id INT REFERENCES micro_nutrients(id)
          
               
           );"""
    return query

def create_macronutrients():
    query = """CREATE TABLE macro_nutrients(
               id SERIAL PRIMARY KEY ,
               Protein VARCHAR(100),
               Carbohydrate VARCHAR(100),
               Energy VARCHAR(100),
               fats_id INT REFERENCES fats(id)
           );"""
    return query


def create_micronutrients():
    query = """CREATE TABLE micro_nutrients(
               id SERIAL PRIMARY KEY ,
               minerals_id INT REFERENCES minerals(id),
               vitamins_id INT REFERENCES vitamins(id)
           );"""
    return query


def create_fats():
    query = """CREATE TABLE fats(
               id SERIAL PRIMARY KEY ,
               lipid VARCHAR(100),
               Sugars VARCHAR(100),
               Cholesterol VARCHAR(100),
               Fatty_acids VARCHAR(100)
           );"""
    return query


def create_minerals():
    query = """CREATE TABLE minerals(
               id SERIAL PRIMARY KEY ,
               Calcium VARCHAR(100),
               Iron VARCHAR(100),
               Magnesium VARCHAR(100),
               Sodium VARCHAR(100)
                              
            
           );"""
    return query


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


# def create_nutrients():
#     query = """CREATE TABLE nutrients(
#         id SERIAL PRIMARY KEY ,
#         protein VARCHAR(50),
#         fiber VARCHAR(50),
#         iron VARCHAR(50),
#         cholesterol VARCHAR(50),
#         lipid VARCHAR(50),
#         carbohydrate VARCHAR(50),
#         energy VARCHAR(50),
#         water VARCHAR(50),
#         calcium VARCHAR(50),
#         caffeine VARCHAR(50),
#         sugar VARCHAR(50)
#
#     );"""
#
#     return query
