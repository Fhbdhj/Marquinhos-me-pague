import sqlite3

conn = sqlite3.connect('crop_guide.sqlite')

cur = conn.cursor()

# try:
#     cur.execute('CREATE TABLE crop (season VARCHAR, North_High VARCHAR, North_Low VARCHAR, South_High VARCHAR, South_Low VARCHAR, northern VARCHAR,southern VARCHAR)')
# except:
#     print("Databse Connection Error")

# cur.execute('INSERT INTO crop (season, North_High, North_Low, South_High, South_Low) values ("Kharif","Sugarcane","Rice","Cotton","Maize")')
# cur.execute('INSERT INTO crop (season, North_High, North_Low, South_High, South_Low) values ("Rabi","Wheat","Mustard","Banana","Mango")')
# cur.execute('INSERT INTO crop (season, North_High, North_Low, South_High, South_Low) values ("Zaid","Cucumber","Jute","Pumpkin","Tomato")')
# cur.execute('INSERT INTO crop (northern) values ("Chandigarh  Delhi  Haryana  Himachal Pradesh  Jammu  Kashmir  Ladakh  Punjab  Rajasthan  Uttarakhand  Uttar Pradesh  Madhya Pradesh  West Bengal  Bihar  Gujarat  ")')
# cur.execute('INSERT INTO crop (southern) values ("Andhra Pradesh  Karnataka  Kerala  Lakshadweep  Puducherry  Tamil Nadu  Telangana  Chennai  Bengaluru  Hyderabad  Kochi  Warangal  Thiruvananthapuram  Coimbatore  Visakhapatanam  Mysuru  Madurai  Vijayawada Kozhikode")')

# cur.execute("DELETE FROM crop")

conn.commit()