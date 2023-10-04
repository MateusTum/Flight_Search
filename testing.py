# ARE FOR TESTING CODE

import pandas as pd

test_dic = {"city": {"IATA_Code": "AAA",
                     "Price": "111"},
            "new_city": {"IATA_Code": "BBB",
                         "Price": "222"}
            }

new_dic = {"city": ["city_a", "city_b", "city_c", "city_d"],
           "price": ["111", "222", "333", "444"]}
df = pd.DataFrame(new_dic)


new_price = 300  # Replace with the desired new price

df.loc[df['city'] == 'city_a', 'price'] = new_price


print(df)
