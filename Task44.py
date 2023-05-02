#Задание 44
#
#В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

import pandas
import random

def get_one_hot(data: list):
    unique_vals = data['whoAmI'].unique()
    val_to_idx = {val: i for i, val in enumerate(unique_vals)}
    for val in unique_vals:
        col_name = f"{val}_one_hot"
        data[col_name] = (data['whoAmI'] == val).astype(int)
    return data

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pandas.DataFrame({'whoAmI':lst})
data = get_one_hot(data)
data.head()

print(data)


