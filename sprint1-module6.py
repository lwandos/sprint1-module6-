import pandas as pd 

# creating the dictionary
data_dict = {'packages': ['chips', 'cooldrinks' ,'Chocolates','pies', 'Fruit', 'Cupcakes', 'Veggies'], 'Product 1': ['simba','coke','cadbury','pepper steak', 'pear', 'vanilla','spinach'], 'product2':['lays','Fanta','Tex','Chicken','Apple','Chocolate','cabbage'], 'product3':['Doritos','Sprite','Lunchbar','steak and kidney','orange','Carrots']}
#creating a pandas dataframe from a dictionar
dframe = pd.DataFrame(data_dict)
