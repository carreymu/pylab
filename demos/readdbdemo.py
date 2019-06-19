import sqlite3


if __name__=="__main__":

    print("============create table============")
    db = sqlite3.connect('database.db')
    c = db.cursor()
    c.execute('create table protfolio(symbol text,share integer,price real)')
    db.commit()

    print("============insert records============")
    stocks = [
        ('GOOG', 100, 490.1),
        ('AAPL', 50, 545.75),
        ('FB', 150, 7.45),
        ('HPQ', 75, 33.2),
    ]
    c.executemany('insert into portfolio values (?,?,?)', stocks)

    print("============select============")
    for row in db.execute('select * from portfolio'):
        print(row)


    for row in db.execute('select * from portfolio where price >=?',100):
        print(row)



