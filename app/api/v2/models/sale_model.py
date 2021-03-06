from manage import init_db


class Sale:
    def __init__(self):
        self.db = init_db()

    def create_sale(self, user_id, product_id, quantity, unit_price):
        payload = {
            "user_id": user_id,
            "product_id": product_id,
            "quantity": quantity,
            "unit_price": unit_price

        }
        query = """INSERT INTO sales(user_id, product_id, quantity, unit_price)
                    VALUES(%(user_id)s, %(product_id)s, %(quantity)s, %(unit_price)s) """
        cursor = self.db.cursor()
        cursor.execute(query, payload)
        self.db.commit()
        return payload

    def get_all_sales(self):
        cursor = self.db.cursor()
        cursor.execute("""select users.first_name, products.product_name, sales.quantity, products.unit_price, 
        sales.quantity*products.unit_price AS cost from sales inner join products
         on sales.product_id=products.product_id inner join users on sales.user_id=users.user_id""")
        data = cursor.fetchall()
        rows = []
        for i, items in enumerate(data):
            first_name, product_name, quantity, unit_price, cost, = items
            datum = dict(
                first_name=first_name,
                product_name=product_name,
                quantity=int(quantity),
                unit_price=unit_price,
                cost=cost
            )
            rows.append(datum)
        return rows

    def filter_sales_records_by_attendant(self, user_id):
        cursor = self.db.cursor()
        cursor.execute("""select users.first_name, products.product_name, sales.quantity, products.unit_price, 
        sales.quantity*products.unit_price AS cost from sales inner join products
         on sales.product_id=products.product_id inner join users on sales.user_id=users.user_id
         WHERE users.user_id={} """.format(user_id))
        data = cursor.fetchall()
        rows = []
        for i, items in enumerate(data):
            first_name, product_name, quantity, unit_price, cost, = items
            datum = dict(
                first_name=first_name,
                product_name=product_name,
                quantity=int(quantity),
                unit_price=unit_price,
                cost=cost
            )
            rows.append(datum)
        return rows
