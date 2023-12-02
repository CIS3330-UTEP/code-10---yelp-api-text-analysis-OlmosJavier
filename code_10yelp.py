import yelpapi as yp
from yelpapi import YelpAPI
import pandas as pd

api_key = "TfB7QQwaJcpxaSf3C6Uhx4zAlPw-pKxN7bD0D_UAdbVPh56_7WsEkoGBXUVX3Cu_EjmCfBT7_0qWEmEOeu6q0ibXVlMK2Sg5GLP9hdBgQ99nv_y6GpzNkSLqTMBPZXYx"
yelp_api = YelpAPI(api_key)

# Flautas
search_term = "Flautas"
search_location = "El Paso, TX"
search_sort_by = "rating"
search_limit = 5

search_results = yelp_api.search_query(term=search_term, location=search_location,
sort_by=search_sort_by, limit=search_limit)

# DF
df = pd.DataFrame.from_dict(search_results['businesses'])
# Print the aliases
print(df['alias'])
# Random restaurant
id_rv = df.loc[0, 'alias']
# Retrieve rvs
rv_result = yelp_api.reviews_query(id=id_rv)
# Print rv
for reviews in rv_result['reviews']:
    print(reviews['text'])
# RV DF
rv_df = pd.DataFrame.from_dict(rv_result['reviews'])
# Results
print(df)
# CSV RESULT
df.to_csv(f"{search_term}_{search_location}_result.csv")
# CSV REVIEWS
rv_df.to_csv(f"{id_rv}_rv.csv")