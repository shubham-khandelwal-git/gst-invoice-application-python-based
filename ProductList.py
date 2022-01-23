from sqlite3 import connect


class ProductListFrame:
    def __init__(self):
        self.conn = connect('bill.db')
        pass

    pass


if __name__ == "__main__":
    product_list = ProductListFrame()
