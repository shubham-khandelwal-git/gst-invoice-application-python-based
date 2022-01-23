from sqlite3 import connect, OperationalError, IntegrityError

"""
    Details table will be listed here

    Company table (gst, name, address_line1, address_line2, address_line3, city, state, code, zipcode)

    Customer table(gst, name, address_line1, address_line2, address_line3, city, state, code, zipcode)

    HSN code table(hsn code, product name, rate, price)
 """

""" 
    Bill Details:
    company_gst, customer_gst, bill_number, bill_date, 
    products(hsn, product name, rate, price), 
    total_igst, total_cgst, total_sgst, total_price, total amount, 
    type
"""


class DetailsTable:
    def __init__(self):
        self.conn = connect("prefilled_bill_details.db")
        pass

    def create_company(self):
        c = self.conn.cursor()

        try:
            c.execute(""" CREATE TABLE COMPANIES(
                    GST TEXT PRIMARY KEY,
                    NAME TEXT,
                    ADDRESSLINE1 TEXT,
                    ADDRESSLINE2 TEXT,
                    ADDRESSLINE3 TEXT,
                    CITY TEXT, 
                    STATE TEXT, 
                    CODE INTEGER,
                    ZIPCODE NUMBER,
                    'MOBILE NUMBER' INTEGER,
                    'MAIL ID' TEXT
                    ); """)
            self.conn.commit()
        except OperationalError as e:
            print("Operational Error: " + str(e))
        except IntegrityError as e:
            print("Integrity Error: " + str(e))
        finally:
            c.close()
        pass

    def create_customers(self):
        c = self.conn.cursor()

        try:
            c.execute(""" CREATE TABLE CUSTOMERS(
                    GST TEXT PRIMARY KEY,
                    NAME TEXT,
                    ADDRESSLINE1 TEXT,
                    ADDRESSLINE2 TEXT,
                    ADDRESSLINE3 TEXT,
                    CITY TEXT, 
                    STATE TEXT, 
                    CODE INTEGER,
                    ZIPCODE NUMBER,
                    'MOBILE NUMBER' INTEGER,
                    'MAIL ID' TEXT
                    ); """)
            self.conn.commit()
        except OperationalError as e:
            print("Operational Error: " + str(e))
        except IntegrityError as e:
            print("Integrity Error: " + str(e))
        finally:
            c.close()
        pass

    def create_hsn(self):
        c = self.conn.cursor()

        try:
            c.execute(""" CREATE TABLE HSN_CODE(
                    HSN_CODE TEXT PRIMARY KEY,
                    PRODUCT_NAME TEXT,
                    RATE INTEGER,
                    PRICE NUMBER
                    ); """)
            self.conn.commit()
        except OperationalError as e:
            print("Operational Error: " + str(e))
        except IntegrityError as e:
            print("Integrity Error: " + str(e))
        finally:
            c.close()
        pass

    def create_products_billed_table(self):
        c = self.conn.cursor()

        try:
            c.execute(""" CREATE TABLE PRODUCTS_LIST(
                    HSN TEXT,
                    NAME TEXT, 
                    QUANTITY INTEGER,
                    RATE INTEGER,
                    PRICE NUMBER,
                    DISCOUNT NUMBER,
                    AMOUNT NUMBER,
                    BILL_NUMBER INTEGER,
                    FOREIGN KEY (BILL_NUMBER) REFERENCES BILL_DETAILS(BILL_NUMBER)
                    ON UPDATE CASCADE
                    ON DELETE SET NULL
                    ); """)
            self.conn.commit()
        except OperationalError as e:
            print("Operational Error: " + str(e))
        except IntegrityError as e:
            print("Integrity Error: " + str(e))
        finally:
            c.close()
        pass

    def create_bill_details(self):
        c = self.conn.cursor()

        try:
            c.execute(""" CREATE TABLE BILL_DETAILS(
                            BILL_NUMBER INTEGER PRIMARY KEY,
                            BILL_DATE DATE,
                            COMPANY_GST TEXT,
                            CUSTOMER_GST TEXT, 
                            TOTAL_IGST NUMBER,
                            TOTAL_CGST NUMBER,
                            TOTAL_SGST NUMBER, 
                            TOTAL_PRICE NUMBER,
                            TOTAL_AMOUNT NUMBER, 
                            FOREIGN KEY(COMPANY_GST) REFERENCES COMPANIES(GST)
                            ON UPDATE CASCADE
                            ON DELETE SET NULL,
                            FOREIGN KEY(CUSTOMER_GST) REFERENCES CUSTOMERS(GST)
                            ON UPDATE CASCADE
                            ON DELETE SET NULL
                            ); """)
            self.conn.commit()
        except OperationalError as e:
            print("Operational Error: " + str(e))
        except IntegrityError as e:
            print("Integrity Error: " + str(e))
        finally:
            c.close()
        pass

    def insert_customer_in_customers(self, new_customer):
        c = self.conn.cursor()
        customer = None

        try:
            customer = c.execute(""" INSERT INTO CUSTOMERS VALUES(?,?,?,?,?,?,?,?,?,?,?) """, new_customer).fetchall()
            self.conn.commit()
        except OperationalError as e:
            print("Operational Error: " + str(e))
        except IntegrityError as e:
            print("Integrity Error: " + str(e))
        finally:
            c.close()
            return customer
        pass

    def insert_product_in_hsn_code(self, products):
        c = self.conn.cursor()

        try:
            c.execute(""" INSERT INTO HSN_CODE VALUES (?,?,?,?) """, products)
        except OperationalError as e:
            print("Operational Error: " + str(e))
        except IntegrityError as e:
            print("IntegrityError: " + str(e))
        finally:
            c.close()
        pass

    def insert_product_in_product_list(self, product):
        c = self.conn.cursor()

        try:
            c.execute("""INSERT INTO PRODUCTS_LIST(NAME, HSN, QUANTITY, RATE, PRICE, DISCOUNT, AMOUNT, BILL_NUMBER) 
            VALUES(?,?,?,?,?,?,?) """, product)
        except OperationalError as e:
            print("Operational Error: " + str(e))
        except IntegrityError as e:
            print("Integrity Error: " + str(e))
        finally:
            c.close()
        pass

    def get_company_details(self):
        c = self.conn.cursor()
        company = None

        try:
            company = c.execute(""" SELECT * FROM COMPANIES """).fetchone()
            self.conn.commit()
        except OperationalError as e:
            print("Operational Error: " + str(e))
        except IntegrityError as e:
            print("Integrity Error: " + str(e))
        finally:
            c.close()
            return company
        pass

    def get_customer_details_via_gst(self, gstin):
        c = self.conn.cursor()
        customer = None

        try:
            customer = c.execute(""" SELECT * FROM CUSTOMERS WHERE GST=? """.format(gstin)).fetchone()
            self.conn.commit()
        except OperationalError as e:
            print("Operational Error: " + str(e))
        except IntegrityError as e:
            print("Integrity Error: " + str(e))
        finally:
            c.close()
            return customer
        pass

    def get_customer_details_name_gst_mobile(self):
        c = self.conn.cursor()
        customer = None

        try:
            customer = c.execute(""" SELECT NAME, GST, "MOBILE NUMBER" FROM CUSTOMERS """).fetchall()
            self.conn.commit()
        except OperationalError as e:
            print("Operational Error: " + str(e))
        except IntegrityError as e:
            print("Integrity Error: " + str(e))
        finally:
            c.close()
            return customer
        pass

    def get_product_names(self):
        c = self.conn.cursor()
        product = None

        try:
            product = c.execute(""" SELECT PRODUCT_NAME FROM HSN_CODE """).fetchall()
            self.conn.commit()
        except OperationalError as e:
            print("Operational Error: " + str(e))
        except IntegrityError as e:
            print("Integrity Error: " + str(e))
        finally:
            c.close()
            return product
        pass

    def get_product_hsn_from_name(self, name):
        c = self.conn.cursor()
        product = None

        try:
            product = c.execute(""" SELECT HSN_CODE FROM HSN_CODE WHERE PRODUCT_NAME='{}' """.format(name)).fetchone()[
                0]
            self.conn.commit()
        except OperationalError as e:
            print("Operational Error: " + str(e))
        except IntegrityError as e:
            print("Integrity Error: " + str(e))
        finally:
            c.close()
            return product
        pass

    def get_product_rate_from_name(self, name):
        c = self.conn.cursor()
        product = None

        try:
            product = c.execute(""" SELECT RATE FROM HSN_CODE WHERE PRODUCT_NAME='{}' """.format(name)).fetchone()[0]
            self.conn.commit()
        except OperationalError as e:
            print("Operational Error: " + str(e))
        except IntegrityError as e:
            print("Integrity Error: " + str(e))
        finally:
            c.close()
            return product
        pass

    def get_product_price_from_name(self, name):
        c = self.conn.cursor()
        product = None

        try:
            product = c.execute(""" SELECT PRICE FROM HSN_CODE WHERE PRODUCT_NAME='{}' """.format(name)).fetchone()[0]
            self.conn.commit()
        except OperationalError as e:
            print("Operational Error: " + str(e))
        except IntegrityError as e:
            print("Integrity Error: " + str(e))
        finally:
            c.close()
            return product
        pass

    pass


if __name__ == '__main__':
    details = DetailsTable()
    details.create_company()
    details.create_customers()
    details.create_hsn()
    details.create_products_billed_table()
    details.create_bill_details()

    print(details.get_product_hsn_from_name('apple'))
