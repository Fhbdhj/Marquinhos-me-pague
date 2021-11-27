import sqlite3

conn = sqlite3.connect('cropDB.sqlite')

cur = conn.cursor()

# try:
    # cur.execute('CREATE TABLE crop (season VARCHAR, North_High VARCHAR, North_Low VARCHAR, South_High VARCHAR, South_Low VARCHAR)')
# , northern VARCHAR,southern VARCHAR
# except:
    # print("Databse Connection Error")

# cur.execute('INSERT INTO crop (season, North_High, North_Low, South_High, South_Low) values ("Kharif","Sugarcane","Rice","Cotton","Maize")')
# cur.execute('INSERT INTO crop (season, North_High, North_Low, South_High, South_Low) values ("Rabi","Wheat","Mustard","Banana","Mango")')
# cur.execute('INSERT INTO crop (season, North_High, North_Low, South_High, South_Low) values ("Zaid","Cucumber","Jute","Pumpkin","Tomato")')

# cur.execute("DELETE FROM crop")

# TEST QUERY
# season = "Kharif"
# cur.execute("SELECT North_High FROM crop WHERE season=?", [season])
# dd = cur.fetchall()
# dd = str(dd[0])[2:-3]
# print(dd)

conn.commit()