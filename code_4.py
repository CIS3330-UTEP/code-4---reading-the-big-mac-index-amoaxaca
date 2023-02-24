#import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'
file = pd.read_csv(big_mac_file)

def get_big_mac_price_by_year(year,country_code):
    country = country_code
    country=country.upper()
    query= f"(iso_a3 == '{country}' and date >= '{year}-01-01'and date <= '{year}-12-31')"
    country_df = file.query(query)
    answer = round(country_df['dollar_price'].mean(),2)
    return answer


def get_big_mac_price_by_country(country_code):
    country=country_code
    country=country.upper()
    query= f"(iso_a3 == '{country}')"
    country_df=file.query(query)
    answer = round(country_df['dollar_price'].mean(),2)
    return answer

    

def get_the_cheapest_big_mac_price_by_year(year):
    query= f"(date >= '{year}-01-01'and date <= '{year}-12-31')"
    country_df=file.query(query)
    min_idx=country_df['dollar_price'].idxmin()
    price_min=file.loc[min_idx]
    answer=(f"{price_min['name']}({price_min['iso_a3']}): ${round(price_min['dollar_price'],2)}")
    return answer
    


def get_the_most_expensive_big_mac_price_by_year(year):
    query= f"(date >= '{year}-01-01'and date <= '{year}-12-31')"
    country_df=file.query(query)
    max_idx=country_df['dollar_price'].idxmax()
    price_max=file.loc[max_idx]
    answer=(f"{price_max['name']}({price_max['iso_a3']}): ${round(price_max['dollar_price'],2)}")
    return answer
if __name__ == "__main__":
    code_a=get_big_mac_price_by_year (2010,"arg")
    print(code_a)

    code_b=get_big_mac_price_by_country('mex')
    print(code_b)

    code_c=get_the_cheapest_big_mac_price_by_year('2008')
    print(code_c)

    code_d=get_the_most_expensive_big_mac_price_by_year('2014')
    print(code_d)