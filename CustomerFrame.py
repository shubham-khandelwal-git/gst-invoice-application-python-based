from tkinter import Tk, StringVar, LabelFrame, Label, Button, Toplevel, Entry, messagebox
from tkinter.ttk import Combobox

from database_edited.DetailsTable import DetailsTable


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
        customer_gst = self.customer_name.get().split(' - ')[1]
        print(customer_gst)
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


if __name__ == '__main__':
    # customer = ["customer1 - gstin1", "customer2 - gst2", "customer2 - gst3", "shubham - 123"]
    root = Tk()
    CustomerFrame(root)
    root.mainloop()
    pass
