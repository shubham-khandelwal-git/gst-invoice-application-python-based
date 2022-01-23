from tkinter import Tk

from database_edited.CompanyFrame import CompanyFrame
from database_edited.CustomerFrame import CustomerFrame
from database_edited.InvoiceFrame import InvoiceFrame
from database_edited.ProductListFrame import ProductListFrame


class IndexPage:
    def __init__(self, parent):
        self.parent = parent
        CompanyFrame(self.parent)
        CustomerFrame(self.parent)
        InvoiceFrame(self.parent)
        ProductListFrame(self.parent)
        pass

    pass


if __name__ == '__main__':
    global company_gst_here
    global customer_gst_here
    global bill_number_here
    root = Tk()
    IndexPage(root)
    root.mainloop()
