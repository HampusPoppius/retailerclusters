import pandas as pd
import numpy as np
from sklearn.decomposition import LatentDirichletAllocation
import sqlite3


conn = sqlite3.connect('C:\~\database.db')
c = conn.cursor()
data = pd.DataFrame(c.execute("SELECT product_id, product_name, shop_name, shop_id\
                               FROM MAIN\ 
                               WHERE batch = '01-02-20'"))
c.close()
conn.close()

data.columns = ['product_id','product_name','shop_name','shop_id']

# Create list of retailers that offer at least 50 products
counts = data.groupby('shop_id').size().reset_index(name='n_products')
shops = counts.loc[counts['n_products'] >= 50,'shop_id']
shop_names = data.loc[data['shop_id'].isin(shops),['shop_id','shop_name']].groupby('shop_id').first()

# Create list of all products that are offered by any of these retailers
# but only products that are sold by at least 5 retailers
product_counts = data.groupby('product_id').size().reset_index(name='n_shops')
products = product_counts.loc[product_counts['n_shops'] >= 8,'product_id']
products = data.loc[data['shop_id'].isin(shops) & data['product_id'].isin(products),'product_id'].unique()
product_names = data.loc[data['product_id'].isin(products),['product_id','product_name']].groupby('product_id').first().reset_index()

# Empty data frame to fill with ones and zeros (OneHotEncoder raises MemoryError)
input_dummies = pd.DataFrame(0, index=shops,\
                             columns=products,dtype=bool) 


# impute ones in the columns for which product the retailer offers
for shop in shops:

    product_ids = data.loc[data['shop_id'] == shop,'product_id'].unique()
    values = np.array(list(map(lambda x: x in product_ids,input_dummies.columns)))
    input_dummies.loc[shop] = values


# Fit the LDA
n_clusters = 100 # 100 seems good
lda_model = LatentDirichletAllocation(n_components=n_clusters, 
                                      learning_method = 'online',
                                      max_iter=25)

lda_model.fit(input_dummies)

# Estimate cluster belonging
df_shop_probabilities = pd.DataFrame(lda_model.transform(input_dummies)).set_index(shop_names.index)
df_shop_probabilities = shop_names.join(df_shop_probabilities)

# Get lists of most common products per cluster
tm_df = pd.DataFrame(lda_model.components_).T
tm_df['product_id'] = input_dummies.columns
tm_df = tm_df.merge(product_names,on='product_id')

for n, k in enumerate(range(0,n_clusters,1)):
    
    print('Topic nr: '+str(n))
    print(', '.join(tm_df.sort_values(by=k, ascending=False)['product_name'].tolist()[0:5]))
    print(' ')
    print(', '.join(df_shop_probabilities.sort_values(by=k, ascending=False)['shop_name'].tolist()[0:5]))
    print(' ')

