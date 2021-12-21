import mysql.connector

db = mysql.connector.connect(
host="miranda.mysql.pythonanywhere-services.com",
user="miranda",
passwd="molinase",
database= "miranda$default")
cur= db.cursor()
cur.execute("SELECT * FROM molini limit 10000 offset 10")
data = cur.fetchall()
query='british'
cur.close()
print('-----------------------ppppppppppppppppppppppppppppppppppppppppppppppppppp----------------------------')
a= [] #if query.lower() in x]
for square in data:
    for round in square:
        if query.lower() in round.lower():
            a.append(round)
print(a)