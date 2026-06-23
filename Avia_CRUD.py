from db import get_connection


def parvoz_qoshish(flight_number, departure_airport_id, arrival_airport_id, departure_time, price, seats_available):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO flights (flight_number, departure_airport_id, arrival_airport_id, departure_time, price, seats_available)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (flight_number, departure_airport_id, arrival_airport_id, departure_time, price, seats_available))

    conn.commit()
    print("Parvoz qo'shildi!")

    cur.close()
    conn.close()



def barcha_parvozlar():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT f.flight_number,
               a1.name, a1.city,
               a2.name, a2.city,
               f.departure_time, f.price, f.status
        FROM flights f
        INNER JOIN airports a1 ON f.departure_airport_id = a1.id
        INNER JOIN airports a2 ON f.arrival_airport_id = a2.id
    """)

    parvozlar = cur.fetchall()
    for p in parvozlar:
        print(p)

    cur.close()
    conn.close()


def parvoz_yangilash(flight_id, yangi_narx):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        UPDATE flights SET price = %s WHERE id = %s
    """, (yangi_narx, flight_id))

    conn.commit()
    print("Narx yangilandi!")

    cur.close()
    conn.close()


def parvoz_ochirish(flight_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM flights WHERE id = %s", (flight_id,))

    conn.commit()
    print("Parvoz o'chirildi!")
    cur.close()
    conn.close()


def shahar_boyicha_qidirish(shahar):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT f.flight_number,
               a1.name, a1.city,
               a2.name, a2.city,
               f.departure_time, f.price
        FROM flights f
        INNER JOIN airports a1 ON f.departure_airport_id = a1.id
        INNER JOIN airports a2 ON f.arrival_airport_id = a2.id
        WHERE a1.city ILIKE %s OR a2.city ILIKE %s
    """, (f'%{shahar}%', f'%{shahar}%'))

    natija = cur.fetchall()
    for n in natija:
        print(n)

    cur.close()
    conn.close()


def chipta_band_qilish(flight_id, passenger_id, seats_booked):
    
    conn = get_connection()
    cur = conn.cursor()

    try:

        cur.execute("SELECT seats_available FROM flights WHERE id = %s", (flight_id,))
        row = cur.fetchone()

        if row[0] < seats_booked:
            print("Joy yetarli emas!")
            conn.rollback()
            return

        
        cur.execute("""
            UPDATE flights SET seats_available = seats_available - %s WHERE id = %s
        """, (seats_booked, flight_id))

      
        cur.execute("""
            INSERT INTO bookings (flight_id, passenger_id, seats_booked)
            VALUES (%s, %s, %s)
        """, (flight_id, passenger_id, seats_booked))

        conn.commit()
        print("Chipta band qilindi!")

    except Exception as e:
        conn.rollback()
        print("Xatolik:", e)

    finally:
        cur.close()
        conn.close()
