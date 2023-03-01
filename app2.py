import pandas as pd

# below method subtracts two numbers and returns their output
def substract(a, b):
    return a - b

print(substract(10, 5))


# create a pandas dataframe with columns as account_id and deal_id
df = pd.DataFrame({'account_id': [1, 2, 3, 4, 5], 'deal_id': [1, 2, 3, 4, 5]})

# create a empty pandas dataframe with columns as account_id and deal_id
df1 = pd.DataFrame(columns=['account_id', 'deal_id'])

# insert dummy data in df1 dataframe
df1 = df1.append({'account_id': 1, 'deal_id': 1}, ignore_index=True)
df1 = df1.append({'account_id': 2, 'deal_id': 2}, ignore_index=True)
df1 = df1.append({'account_id': 3, 'deal_id': 3}, ignore_index=True)
df1 = df1.append({'account_id': 4, 'deal_id': 4}, ignore_index=True)
df1 = df1.append({'account_id': 5, 'deal_id': 5}, ignore_index=True)


# delete rows from df1 where deal ids are even
df1 = df1.drop(df1[df1['deal_id'] % 2 == 0].index)

# print df1
print(df1)

