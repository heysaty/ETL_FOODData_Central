class insert_query:
    @staticmethod
    def insert_fooditem_query(fooditem, description, nutrientslog_id):
        description = description.replace("'", "")

        query = f"""insert into fooditems(food_item,description,nutrients_log_id)
                        values('{fooditem}',
                               '{description}',
                               '{nutrientslog_id}');"""

        return query

    @staticmethod
    def insert_nutrientslog(macros_id, micros_id):
        query = f"""insert into nutrients_log(macro_nutrients_id ,micro_nutrients_id)
                       values('{macros_id}',
                              '{micros_id}');"""

        return query

    @staticmethod
    def insert_macronutrients(macronutrients, fats_id):
        query = f"""insert into macro_nutrients(Protein ,Carbohydrate,Energy,  fats_id)
                       values('{macronutrients['Protein']}',
                              '{macronutrients['Carbohydrate, by difference']}',
                              '{macronutrients['Energy']}',
                              '{fats_id}');"""

        return query

    @staticmethod
    def insert_micronutrients(minerals_id, vitamins_id):
        query = f"""insert into micro_nutrients(minerals_id, vitamins_id)
                         values('{minerals_id}',
                                '{vitamins_id}');"""

        return query

    @staticmethod
    def insert_fats(fats):
        query = f"""insert into fats(lipid, Sugars, Cholesterol, Fatty_acids  )
                            values('{fats["Total lipid (fat)"]}',
                                   '{fats["Sugars, total including NLEA"]}',
                                   '{fats["Cholesterol"]}', 
                                   '{fats["Fatty acids, total saturated"]}');"""

        return query

    @staticmethod
    def insert_minerals(minerals):
        query = f"""insert into minerals(Calcium, Iron, Magnesium, Sodium  )
                               values('{minerals["Calcium, Ca"]}',
                                      '{minerals["Iron, Fe"]}',
                                      '{minerals["Magnesium, Mg"]}',
                                      '{minerals["Sodium, Na"]}');"""

        return query

    @staticmethod
    def insert_vitamins(vitamins):
        query = f"""insert into vitamins(Vitamin_A, Vitamin_E, Vitamin_D, Vitamin_C, Vitamin_B12 )
                                   values('{vitamins["Vitamin A, RAE"]}',
                                          '{vitamins["Vitamin E (alpha-tocopherol)"]}',
                                          '{vitamins["Vitamin D (D2 + D3)"]}',
                                          '{vitamins["Vitamin C, total ascorbic acid"]}',
                                          '{vitamins["Vitamin B-12"]}');"""

        return query

    @staticmethod
    def insert_recipes(recipes, food_id):
        query = f"""insert into recipes(recipe, food_id)
                      values('{recipes}',
                             '{food_id}');"""

        return query

    @staticmethod
    def insert_food_recipes(food, recipe):
        query = f"""insert into food_recipes(food,recipe)
                          values('{food}',
                                 '{recipe}');"""

        return query


