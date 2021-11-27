import sqlite3

conn = sqlite3.connect('stateDB.sqlite')

cur = conn.cursor()

# try:
#     cur.execute('CREATE TABLE state (northern VARCHAR,southern VARCHAR)')
# except:
#     print("Databse Connection Error")

# cur.execute('INSERT INTO state (northern) values ("Chandigarh  Delhi  Haryana  Himachal Pradesh  Jammu & Kashmir  Ladakh  Punjab  Rajasthan  Uttarakhand  Uttar Pradesh  Madhya Pradesh  West Bengal  Bihar  Gujarat")')
# cur.execute('INSERT INTO state (southern) values ("Andhra Pradesh  Karnataka  Kerala  Lakshadweep  Puducherry  Tamil Nadu  Telangana  Chennai  Bengaluru  Hyderabad  Kochi  Warangal  Thiruvananthapuram  Coimbatore  Visakhapatanam  Mysuru  Madurai  Vijayawada Kozhikode")')

# cur.execute("DELETE FROM state")

# TEST QUERY
# cur.execute("SELECT * FROM state WHERE northern IS NOT NULL")
# ans = cur.fetchall()
# ans = list(ans[0][:-1])
# print(ans[0])

conn.commit()