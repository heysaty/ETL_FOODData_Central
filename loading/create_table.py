def create_fooditems():
    query = """CREATE TABLE fooditems(
            id SERIAL PRIMARY KEY ,
            food_item VARCHAR(100),
            description VARCHAR(300),
            nutrients_id INT REFERENCES nutrients(id)
        );"""

    return query


def create_nutrients():
    query = """CREATE TABLE nutrients(
        id SERIAL PRIMARY KEY ,
        protein VARCHAR(50),
        fiber VARCHAR(50),
        iron VARCHAR(50),
        cholesterol VARCHAR(50),
        lipid VARCHAR(50),
        carbohydrate VARCHAR(50),
        energy VARCHAR(50),
        water VARCHAR(50),
        calcium VARCHAR(50),
        caffeine VARCHAR(50),
        sugar VARCHAR(50)
        
    );"""

    return query
