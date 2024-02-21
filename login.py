def autentikasi(db):
    cursor = db.cursor()
    uname = input ("Input username: ")
    pwd = input("Input password: ")
    sql = "SELECT . FROM users WHERE username = %s AND password = %s"
    val = (uname, pwd)
    cursor. execute(sql, val)
    cursor.fetchall()

    if cursor. rowcount == 0:
        return False
    else:
        return True