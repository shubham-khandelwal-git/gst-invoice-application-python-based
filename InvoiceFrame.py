from tkinter import LabelFrame, StringVar, Frame, Label, Entry, Button, Tk


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


if __name__ == '__main__':
    root = Tk()
    InvoiceFrame(root)
    root.mainloop()
