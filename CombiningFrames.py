from tkinter import LabelFrame, Frame, Label, StringVar, Button, Toplevel, Entry, messagebox, Scrollbar, Tk
from tkinter.ttk import Combobox, Treeview

from database_edited.DetailsTable import DetailsTable


from unknown import InvoiceToPdfGenerator

class KeepingData:
    def __init__(self):
        self._company_gst: str
        self._customer_gst: str
        self._bill_number: int
        pass


class CompanyFrame:
    def __init__(self, parent):
        self.parent = parent
        details = DetailsTable()
        self.company_details = details.get_company_details()
        if self.company_details is None:
            self.company_details = [""] * 12
        self.company = LabelFrame(self.parent, text="Company Details")
        self.company.pack(padx=5, pady=5)

        self.company_frame()
        pass

    def company_frame(self):
        frame1 = Frame(self.company)
        frame1.pack(side="left")

        frame2 = Frame(self.company)
        frame2.pack(side="right")

        Label(frame1, text=self.company_details[1]).grid(row=1, padx=40, pady=5, ipadx=10)  # company name
        Label(frame1, text=self.company_details[0]).grid(row=2, padx=50, pady=5, ipadx=10)  # company gst
        Label(frame1,
              text=self.company_details[2] + "\n" + self.company_details[3] + "\n" + self.company_details[4] + " " +
                   self.company_details[5] + " " + self.company_details[6] + " - " + str(self.company_details[8])).grid(
            row=3, padx=40, pady=5, ipadx=10)  # address

        Label(frame2, text=self.company_details[0]).grid(row=3, padx=40, pady=5, ipadx=10)  # mobile
        Label(frame2, text=self.company_details[0]).grid(row=4, padx=40, pady=5, ipadx=10)  # mail id

        pass

    def get_company_gst(self):
        return self.company_details[0]
        pass

    pass


class CustomerFrame:
    def __init__(self, parent):
        self.parent = parent
        self.details = DetailsTable()

        # self.customer = ["customer1 - gstin1 - mobile number", "customer2 - gst2", "customer2 - gst3", "shubham - 123"]

        self.customer = self.get_arranged_customers()

        self.parent_frame = LabelFrame(self.parent)
        self.parent_frame.pack(padx=5, pady=5)

        self.customer_name = StringVar()

        Label(self.parent_frame, text="Customer Name:").pack(side="left")

        self.customer_combobox = Combobox(self.parent_frame, textvariable=self.customer_name)
        self.customer_combobox['values'] = self.customer
        self.customer_combobox.pack(side="left")
        self.customer_combobox.bind("<KeyRelease>", self.update_combobox_values)

        self.proceed_btn = Button(self.parent_frame, text="Proceed", command=self.proceed)
        self.add_new_customer = Button(self.parent_frame, text="Add New", command=self.adding_new_customer)
        self.update_old_customer = Button(self.parent_frame, text="Update")
        self.update_old_customer.pack(side="right")
        self.add_new_customer.pack(side="right")
        self.proceed_btn.pack(side="right")
        pass

    def proceed(self):

        pass

    def adding_new_customer(self):
        top = Toplevel()
        Label(top, text="NAME").grid(row=1, column=1, padx=2, pady=2)
        name = Entry(top)
        name.focus()
        name.grid(row=1, column=2, padx=2, pady=2)

        Label(top, text="GST").grid(row=2, column=1, padx=2, pady=2)
        gst = Entry(top)
        gst.grid(row=2, column=2, padx=2, pady=2)

        Label(top, text="MOBILE NUMBER").grid(row=3, column=1, padx=2, pady=2)
        mobile = Entry(top)
        mobile.grid(row=3, column=2, padx=2, pady=2)

        Label(top, text="MAIL ID").grid(row=4, column=1, padx=2, pady=2)
        mail = Entry(top)
        mail.grid(row=4, column=2, padx=2, pady=2)

        Label(top, text="ADDRESS LINE1").grid(row=5, column=1, padx=2, pady=2)
        add1 = Entry(top)
        add1.grid(row=5, column=2, padx=2, pady=2)

        Label(top, text="ADDRESS LINE2").grid(row=6, column=1, padx=2, pady=2)
        add2 = Entry(top)
        add2.grid(row=6, column=2, padx=2, pady=2)

        Label(top, text="ADDRESS LINE3").grid(row=7, column=1, padx=2, pady=2)
        add3 = Entry(top)
        add3.grid(row=7, column=2, padx=2, pady=2)

        Label(top, text="CITY").grid(row=8, column=1, padx=2, pady=2)
        city = Entry(top)
        city.grid(row=8, column=2, padx=2, pady=2)

        Label(top, text="STATE").grid(row=9, column=1, padx=2, pady=2)
        state = Entry(top)
        state.grid(row=9, column=2, padx=2, pady=2)

        Label(top, text="ZIPCODE").grid(row=10, column=1, padx=2, pady=2)
        zipcode = Entry(top)
        zipcode.grid(row=10, column=2, padx=2, pady=2)

        func1 = lambda: self.add_customer([gst.get(), name.get(), add1.get(), add2.get(), add3.get(), city.get(),
                                           state.get(), gst.get()[:2], zipcode.get(), mobile.get(),
                                           mail.get()])
        Button(top, command=func1, text="Proceed").grid(row=11, column=2)
        pass

    def add_customer(self, customer):
        print(customer)
        try:
            customer[7] = int(customer[7])
            customer[8] = int(customer[8])
            customer[9] = int(customer[9])

            self.details.insert_customer_in_customers(customer)
            self.customer = self.get_arranged_customers()
        except ValueError as e:
            print("Value Error - " + str(e))
            if not messagebox.showerror("Error", "Integer Number expected instead of - " + str(e).split(": ")[1]):
                self.adding_new_customer()
        pass

    def update_customer(self):
        pass

    def get_arranged_customers(self):
        customer_list = []

        for data in self.details.get_customer_details_name_gst_mobile():
            customer_list.append(data[0] + " - " + data[1] + " - " + str(data[2]))

        return customer_list
        pass

    # def fill_combobox_entry(self, event):
    #     self.customer_combobox.delete(0, 'end')
    #     self.customer_combobox.insert(0, self.customer_combobox.selection_get())
    #     pass

    def update_combobox_values(self, event):
        name = self.customer_name.get()

        if name == "":
            data = self.customer
        else:
            data = []
            for item in self.customer:
                if name.lower() in item.lower():
                    data.append(item)
        self.customer_combobox['values'] = data
        pass

    pass


class InvoiceFrame:
    def __init__(self, parent):
        super().__init__()

        self.parent = parent

        self.bill = LabelFrame(self.parent)
        self.bill.pack(padx=5, pady=5)

        self.invoice_details()

        pass

    # Framing invoice details
    def invoice_details(self):
        bill_no = StringVar()
        date = StringVar()

        frame1 = Frame(self.bill)
        frame1.pack(side="left", padx=30)
        Label(frame1, text="Invoice Number: ").grid(row=1, column=1, sticky="w")
        my_entry_invoice = Entry(frame1, textvariable=bill_no)
        my_entry_invoice.grid(row=1, column=2)

        # my_entry_invoice.bind("<KeyRelease>", lambda x: self.print_it(bill_no.get()))
        # Label(frame1, text=bill_no).grid(row=1, column=4, sticky="e")

        frame2 = Frame(self.bill)
        frame2.pack(side="left", padx=50)
        Label(frame2, text="Date: ").grid(row=1, column=7, sticky="w")
        my_entry_date = Entry(frame2, textvariable=date)
        my_entry_date.grid(row=1, column=10, sticky="e")

        frame3 = Frame(self.bill)
        frame3.pack(side="right", padx=40)

        Button(frame3, text="OK").pack()

        pass

    pass


class ProductListFrame:
    def __init__(self, parent):
        self.parent = parent
        self.details = DetailsTable()
        # self.invoice_generator = InvoiceToPdfGenerator()

        # self.products = ["apple", "banana", "mango", "guava", "mongo", "dhaka", "brinjal"]
        self.products = self.get_products_names()
        self.rates = ["0", "5", "10", "12", "18", "28"]
        self.type = "local"

        self.parent_frame = LabelFrame(self.parent)
        self.parent_frame.pack(padx=5, pady=5)

        self.product_entry_frame = Frame(self.parent_frame)
        self.product_entry_frame.pack(padx=2, pady=2, side="top")
        self.product_list_frame = Frame(self.parent_frame)
        self.product_list_frame.pack(padx=2, pady=2, side="top")
        self.values_calculated_frame = Frame(self.parent_frame)
        self.values_calculated_frame.pack(padx=2, pady=2, side="right")

        """
            product list frame have three parts

            part1: basic user given details :- product name, hsn(automatic and disabled), quantity(default 1), 
                            rate(automatic), price(automatic), discount(default 0), amount(disabled, calculated)

            part2: treeview:- details are then added to the treeview

            part3: discount: input
                    automatic calculated values:- total, igst, cgst, sgst, total amount
        """

        self.product_name_label = Label(self.product_entry_frame, text="Product Name", width=20)
        self.product_name_label.grid(row=1, column=1, padx=2, pady=2)

        self.product_name_entry = Combobox(self.product_entry_frame, width=20)
        self.product_name_entry['values'] = self.products
        self.product_name_entry.bind("<KeyRelease>", self.update_combobox_values)
        self.product_name_entry.grid(row=2, column=1, padx=2, pady=2)

        self.product_name_entry.bind("<Tab>", self.fill_in_hsn)
        self.product_name_entry.bind("<Return>", self.fill_in_hsn)

        self.product_hsn_label = Label(self.product_entry_frame, text="HSN Code", width=20)
        self.product_hsn_label.grid(row=1, column=2, padx=2, pady=2)

        self.product_hsn_entry = Entry(self.product_entry_frame, width=20, state="disabled")
        self.product_hsn_entry.grid(row=2, column=2, padx=2, pady=2)

        self.product_qty_label = Label(self.product_entry_frame, text="Quantity", width=20)
        self.product_qty_label.grid(row=1, column=3, padx=2, pady=2)

        self.product_qty_entry = Entry(self.product_entry_frame, width=20)
        self.product_qty_entry.insert("end", "1")
        self.product_qty_entry.bind("<Tab>", self.fill_in_hsn)
        self.product_qty_entry.bind("<Return>", self.fill_in_hsn)
        self.product_qty_entry.grid(row=2, column=3, padx=2, pady=2)

        self.product_rate_label = Label(self.product_entry_frame, text="Rate", width=20)
        self.product_rate_label.grid(row=1, column=4, padx=2, pady=2)

        self.product_rate_entry = Combobox(self.product_entry_frame, width=20)
        self.product_rate_entry['values'] = self.rates
        self.product_rate_entry.grid(row=2, column=4, padx=2, pady=2)

        self.product_rate_entry.bind("<Tab>", self.fill_in_hsn)
        self.product_rate_entry.bind("<Return>", self.fill_in_hsn)

        self.product_price_label = Label(self.product_entry_frame, text="Price", width=20)
        self.product_price_label.grid(row=1, column=5, padx=2, pady=2)

        self.product_price_entry = Entry(self.product_entry_frame, width=20)
        self.product_price_entry.bind("<Return>", self.fill_amount)
        self.product_price_entry.bind("<Tab>", self.fill_amount)
        self.product_price_entry.grid(row=2, column=5, padx=2, pady=2)

        self.product_discount_label = Label(self.product_entry_frame, text="Discount", width=20)
        self.product_discount_label.grid(row=1, column=6, padx=2, pady=2)

        self.product_discount_entry = Entry(self.product_entry_frame, width=20)
        self.product_discount_entry.insert('end', "0")
        self.product_discount_entry.grid(row=2, column=6, padx=2, pady=2)

        self.product_discount_entry.bind("<Tab>", self.fill_amount, add=True)
        self.product_discount_entry.bind("<Return>", self.fill_amount)
        # self.product_discount_entry.bind("<Tab>", self.is_overall_discount_active, add=True)
        # self.product_discount_entry.bind("<Return>", self.is_overall_discount_active, add=True)
        # self.product_discount_entry.bind("<KeyRelease>", self.is_overall_discount_active, add=True)

        self.product_amount_label = Label(self.product_entry_frame, text="Amount", width=20)
        self.product_amount_label.grid(row=1, column=7, padx=2, pady=2)

        self.product_amount_entry = Entry(self.product_entry_frame, width=20, state="disabled")
        self.product_amount_entry.grid(row=2, column=7, padx=2, pady=2)

        self.add_product_btn = Button(self.product_entry_frame, text="Add", width=10, command=self.insert_into_treeview)
        self.add_product_btn.grid(row=2, column=8, padx=2, pady=2)

        self.new_item = Button(self.product_entry_frame, text="New Product", width=15, command=self.add_new_product)
        self.new_item.grid(row=2, column=9, padx=2, pady=2)

        self.treeview = Treeview(self.product_list_frame, show="headings")

        scroll = Scrollbar(self.product_list_frame, orient="vertical", command=self.treeview.yview)
        self.treeview.config(yscrollcommand=scroll.set)

        scroll.pack(side="right", fill='y')

        self.treeview["columns"] = ["SNO", "Product Name", "HSN Code", "Quantity", "Rate", "Price", "Discount",
                                    "Amount"]

        for heading in self.treeview["columns"]:
            self.treeview.column(heading, width=160, anchor="c")
            self.treeview.heading(heading, text=heading)

        self.treeview.pack(side="left", padx=2, pady=2)

        self.taxable_label = Label(self.values_calculated_frame, text="Taxable Amount")
        self.taxable_label.grid(row=1, column=1)

        self.taxable_entry = Entry(self.values_calculated_frame)
        self.taxable_entry.insert('end', "0")
        self.taxable_entry.config(state="disabled")
        self.taxable_entry.grid(row=1, column=2)

        self.overall_discount_label = Label(self.values_calculated_frame, text="Discount")
        self.overall_discount_label.grid(row=2, column=1)

        self.overall_discount_entry = Entry(self.values_calculated_frame)
        self.overall_discount_entry.insert("end", "0")
        self.overall_discount_entry.grid(row=2, column=2)

        self.igst_label = Label(self.values_calculated_frame, text="IGST")
        self.igst_label.grid(row=3, column=1)

        self.igst_entry = Entry(self.values_calculated_frame)
        self.igst_entry.insert('end', "0")
        self.igst_entry.config(state="disabled")
        self.igst_entry.grid(row=3, column=2)

        self.cgst_label = Label(self.values_calculated_frame, text="CGST")
        self.cgst_label.grid(row=4, column=1)

        self.cgst_entry = Entry(self.values_calculated_frame)
        self.cgst_entry.insert('end', "0")
        self.cgst_entry.config(state="disabled")
        self.cgst_entry.grid(row=4, column=2)

        self.sgst_label = Label(self.values_calculated_frame, text="SGST")
        self.sgst_label.grid(row=5, column=1)

        self.sgst_entry = Entry(self.values_calculated_frame)
        self.sgst_entry.insert('end', "0")
        self.sgst_entry.config(state="disabled")
        self.sgst_entry.grid(row=5, column=2)

        self.total_amount_label = Label(self.values_calculated_frame, text="Total Amount")
        self.total_amount_label.grid(row=6, column=1)

        self.total_amount_entry = Entry(self.values_calculated_frame)
        self.total_amount_entry.insert('end', "0")
        self.total_amount_entry.config(state="disabled")
        self.total_amount_entry.grid(row=6, column=2)

        self.generate_bill_btn = Button(self.values_calculated_frame, text="Generate Invoice",
                                        command=self.generate_bill)
        self.generate_bill_btn.bind("<Return>", self.generate_bill)
        self.generate_bill_btn.grid(row=7, column=2)
        pass

    def is_overall_discount_active(self, event):
        print(self.product_discount_entry.get(), type(self.product_discount_entry.get()))
        if self.product_discount_entry.get() != "0":
            self.overall_discount_entry.config(state="disabled")
        pass

    def add_new_product(self):
        top = Toplevel()
        top.bind("<Escape>", lambda x: top.destroy())
        top.resizable(False, False)

        Label(top, text="NAME").grid(row=1, column=1, padx=2, pady=2)
        name = Entry(top)
        name.focus()
        name.grid(row=1, column=2, padx=2, pady=2)

        Label(top, text="HSN").grid(row=2, column=1, padx=2, pady=2)
        hsn = Entry(top)
        hsn.grid(row=2, column=2, padx=2, pady=2)

        Label(top, text="GST RATE").grid(row=3, column=1, padx=2, pady=2)
        rate = Entry(top)
        rate.grid(row=3, column=2, padx=2, pady=2)

        Label(top, text="PRICE").grid(row=4, column=1, padx=2, pady=2)
        price = Entry(top)
        price.grid(row=4, column=2, padx=2, pady=2)

        func1 = lambda: self.add_product_in_db([hsn.get(), name.get(), rate.get(), price.get()])

        Button(top, text="Add", command=func1).grid(row=5, column=2, padx=2, pady=2)
        pass

    def add_product_in_db(self, product):
        try:
            product[2] = int(product[2])
            product[3] = float(product[3])

            self.details.insert_product_in_hsn_code(product)

            self.products = self.get_products_names()
        except ValueError as e:
            print("Value error - " + str(e))
            messagebox.showerror("Error", "Type Integer expected : " + str(e).split(": ")[1])
        pass

    def fill_in_hsn(self, event):

        self.fill_in_rate_and_price()

        self.product_hsn_entry.config(state="normal")
        self.product_hsn_entry.delete("0", "end")
        self.product_hsn_entry.insert('end', self.details.get_product_hsn_from_name(self.product_name_entry.get()))
        self.product_hsn_entry.config(state="disabled")

        self.fill_amount("")
        pass

    def fill_in_rate_and_price(self):
        self.product_rate_entry.delete("0", "end")
        self.product_price_entry.delete("0", "end")

        self.product_rate_entry.insert("end", self.details.get_product_rate_from_name(self.product_name_entry.get()))
        self.product_price_entry.insert("end", self.details.get_product_price_from_name(self.product_name_entry.get()))
        pass

    def fill_amount(self, event):
        self.product_amount_entry.config(state="normal")
        self.product_amount_entry.delete("0", "end")
        self.product_amount_entry.insert('end', str(round(eval(
            self.product_qty_entry.get() + "*" + self.product_price_entry.get() + "*" + "(1+" +
            self.product_rate_entry.get() + "/100)*" + "(1-" + self.product_discount_entry.get() + "/100)"), 2)))
        self.product_amount_entry.config(state="disabled")
        pass

    def insert_into_treeview(self):
        self.fill_in_hsn("")
        self.is_overall_discount_active("")
        count = len(self.treeview.get_children())
        self.treeview.insert("", 'end',
                             values=(count + 1, self.product_name_entry.get(), self.product_hsn_entry.get(),
                                     self.product_qty_entry.get(), self.product_rate_entry.get(),
                                     self.product_price_entry.get(), self.product_discount_entry.get(),
                                     self.product_amount_entry.get()))

        self.fill_in_taxable_amount()
        if self.type == "state":
            self.fill_in_igst()
        elif self.type == "local":
            self.fill_in_lgst()
        else:
            print("Error")
        self.fill_in_total_amount()
        pass

    def fill_in_taxable_amount(self):
        _children = self.treeview.get_children()
        taxable_amount = "0"
        for _child in _children:
            taxable_amount = str(eval(taxable_amount + "+" + str(self.treeview.item(_child)['values'][5])))
        self.taxable_entry.config(state="normal")
        self.taxable_entry.delete("0", 'end')
        self.taxable_entry.insert('end', taxable_amount)
        self.taxable_entry.config(state="disabled")
        pass

    def fill_in_igst(self):
        _children = self.treeview.get_children()
        igst = "0"
        for _child in _children:
            igst = str(eval(igst + "+" + str(self.treeview.item(_child)['values'][5]) + "*" +
                            str(self.treeview.item(_child)['values'][4]) + "/100"))

        self.igst_entry.config(state="normal")
        self.igst_entry.delete("0", 'end')
        self.igst_entry.insert('end', igst)
        self.igst_entry.config(state="disabled")
        pass

    def fill_in_lgst(self):
        _children = self.treeview.get_children()
        lgst = "0"
        for _child in _children:
            lgst = str(eval(lgst + "+" + str(self.treeview.item(_child)['values'][5]) + "*" +
                            str(self.treeview.item(_child)['values'][4]) + "/100"))

        self.sgst_entry.config(state="normal")
        self.sgst_entry.delete("0", 'end')
        self.sgst_entry.insert('end', eval(lgst + "/2"))
        self.sgst_entry.config(state="disabled")

        self.cgst_entry.config(state="normal")
        self.cgst_entry.delete("0", 'end')
        self.cgst_entry.insert('end', eval(lgst + "/2"))
        self.cgst_entry.config(state="disabled")
        pass

    def fill_in_total_amount(self):
        _children = self.treeview.get_children()
        total_amount = "0"
        for _child in _children:
            total_amount = str(eval(total_amount + "+" + str(self.treeview.item(_child)['values'][7])))
        self.total_amount_entry.config(state="normal")
        self.total_amount_entry.delete("0", 'end')
        self.total_amount_entry.insert('end', total_amount)
        self.total_amount_entry.config(state="disabled")
        pass

    def update_combobox_values(self, event):
        name = self.product_name_entry.get()

        if name == "":
            data = self.products
        else:
            data = []
            for item in self.products:
                if name.lower() in item.lower():
                    data.append(item)
        self.product_name_entry['values'] = data
        pass

    def get_products_names(self):
        products = []
        for data in self.details.get_product_names():
            products.append(data[0])

        return products
        pass

    def add_product_list(self):
        for data in self.treeview.get_children():
            self.details.insert_product_in_product_list(data[1:])
        pass

    def generate_bill(self):

        self.add_product_list()

        # pdf = self.invoice_generator.pdf
        # with open("output.pdf", "wb") as pdf_file_handle:
        #     PDF.dumps(pdf_file_handle, pdf)
        pass

    pass


def main(parent):
    global company_gst_here
    global customer_gst_here
    global bil_number_here

    company = CompanyFrame(parent)
    customer = CustomerFrame(parent)
    invoice = InvoiceFrame(parent)
    products = ProductListFrame(parent)
    pass


if __name__ == "__main__":
    root = Tk()
    main(root)
    root.mainloop()
    pass
