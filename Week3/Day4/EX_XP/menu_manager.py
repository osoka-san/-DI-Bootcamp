import psycopg2

class MenuManager:
    @classmethod
    def get_by_name(cls, item_name):
        conn = psycopg2.connect(database="restaurant_menu", user="postgres", password="12")
        cur = conn.cursor()
        cur.execute("SELECT * FROM Menu_Items WHERE item_name = %s", (item_name,))
        item = cur.fetchone()
        cur.close()
        conn.close()
        if item:
            return item
        else:
            return None

    @classmethod
    def all_items(cls):
        conn = psycopg2.connect(database="restaurant_menu", user="postgres", password="12")
        cur = conn.cursor()
        cur.execute("SELECT * FROM Menu_Items")
        items = cur.fetchall()
        cur.close()
        conn.close()
        return items