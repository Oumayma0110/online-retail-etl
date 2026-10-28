import pandas as pd


print("Reading raw data...")
df_raw = pd.read_csv("OnlineRetail.csv", encoding="ISO-8859-1")
#the encoding is for the special international characters so python doesnt crash 

print(f"Total raw rows loaded: {len(df_raw)}")#counting the rows 
print("\nFirst 5 rows of raw data:")
#el n traj3ek lel star w taatik visiual space followed by clear label '3onwen"
print(df_raw.head())       
#tawa bch nadhfou data (removing missing customer IDs and negative/cancelled orders).
#transorm tw


#tawa el T:transorfm
print("\nCleaning data...")#c'est just un message 

df_clean = df_raw.dropna(subset=['CustomerID']).copy()
#lcopy hedhi 3ibara bebe touled w 9asina el umbilical cord walla 3abd wahdou blech omou , 
# so we can modify how we want
#subset hne tkoul lel pandas bch yoghzr ken lel column mtaa customeID
#w ken fama row blech customer id yetnaha completely 
df_clean = df_clean[(df_clean['Quantity'] > 0) & (df_clean['UnitPrice'] > 0)]
#hedhi filtrage , m tkhali ken rows eli fihom quant w unitprice strict pos

print(f"Rows before cleaning: {len(df_raw):,}")
print(f"Rows after cleaning: {len(df_clean):,}")
#zouz ostra bch ncomlpari dataset size before and after cleaning 

#now el L : Load

print("\nPreparing final columns...")#juste un message 
df_clean['TotalPrice'] = df_clean['Quantity'] * df_clean['UnitPrice']
#hedha li fou9i row jdida esmha totalprice bch nadhrbou lquant fl unitprice 
df_clean['CustomerID'] = df_clean['CustomerID'].astype(int)
#behi hedhi fazet el int khatr bekri kent 3ana raw data which means fama customerid 
# kenou farghin , w ki yabdew farghin el panda yrodhom automatically a float w hata 
# ki faraghna bekri 3chirna pandas m resetech lel int out of safety ig


print(f"Ready to load {len(df_clean):,} rows into Oracle database.")#hedha msg tektab f lekhr yaatik 
#9adech men row bch nhotou fl oracle
from sqlalchemy import create_engine #hedhi library kima pandas
print("\nConnecting to SQLite database...")#juste message bch naaref rana nconnectiw rn
db_connection_str = 'sqlite:///retail_database.db'
#db=database

try:
    engine = create_engine(db_connection_str)
    #try hedhi kes7a 9alek incase tfaili lconnection python yetsaamel li bch nektbou tw
    
    print("Loading clean data into SQLite table 'fact_sales'")
    #hedhi lel user msg
    df_clean.to_sql(name='fact_sales', con=engine, if_exists='replace', index=False)
    #pandas andou built in method tarjem dataframe lel sql li heya .to_sql 
    #if exists yaani ken fama tableau deja esmou akeka badlou w hot mte3i hedha w najm 
    # netsaamel append zeda mch ken replace
    #index = false yaani m t7otlich index column feha 1 2 3 al lisar khalini raydha
    
    print("SUCCESS: Data successfully loaded into SQLite table 'fact_sales'!")
    
except Exception as e:
    #hedhi ken el try failet zeda m youhelch lpc w yjini this msg
    print(f"Database connection error: {e}")
