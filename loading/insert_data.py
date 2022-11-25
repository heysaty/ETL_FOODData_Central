def insert_fooditem_query(fooditem, description, nutrients_id):
    query = f"""insert into fooditems(food_item,description,nutrients_id)
            values('{fooditem}','{description}','{nutrients_id}');"""
    return query


def insert_nutrients_query(nutrients_dict):
    query = f"""insert into nutrients(protein,
                              fiber, 
                              iron, 
                              cholesterol, 
                              lipid, 
                              carbohydrate,
                              energy, 
                              water, 
                              calcium, 
                              caffeine, 
                              sugar)
                values('{nutrients_dict['Protein']}',
                       '{nutrients_dict['Fiber, total dietary']}',
                       '{nutrients_dict['Iron, Fe']}',
                       '{nutrients_dict['Cholesterol']}',
                       '{nutrients_dict['Total lipid (fat)']}',
                       '{nutrients_dict['Carbohydrate, by difference']}',
                       '{nutrients_dict['Energy']}',
                       '{nutrients_dict['Water']}',
                       '{nutrients_dict['Calcium, Ca']}',
                       '{nutrients_dict['Caffeine']}',
                       '{nutrients_dict['Sugars, total including NLEA']}');"""
    # print(query)
    return query
