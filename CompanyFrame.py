from tkinter import Frame, Label, LabelFrame, Tk
from database_edited.DetailsTable import DetailsTable


class CompanyFrame:
    def __init__(self, parent):
        self.parent = parent
        details = DetailsTable()
        self.company_details = details.get_company_details()
        if self.company_details is None:
            self.company_details = [""]*12
        self.company = LabelFrame(self.parent, text="Company Details")
        self.company.pack(padx=5, pady=5)

        self.company_frame()
        pass

    def company_frame(self):
        frame1 = Frame(self.company)
        frame1.pack(side="left")

        frame2 = Frame(self.company)
        frame2.pack(side="right")

        Label(frame1, text=self.company_details[0]).grid(row=1, padx=40, pady=5, ipadx=10)  # company name
        Label(frame1, text=self.company_details[1]).grid(row=2, padx=50, pady=5, ipadx=10)  # compnay gst
        Label(frame1,
              text=self.company_details[2] + "\n" + self.company_details[3] + "\n" + self.company_details[4] + " " +
                   self.company_details[5] + " " + self.company_details[6] + " - " + str(self.company_details[8])).grid(
            row=3, padx=40, pady=5, ipadx=10)  # address

        Label(frame2, text=self.company_details[0]).grid(row=3, padx=40, pady=5, ipadx=10)  # mobile
        Label(frame2, text=self.company_details[0]).grid(row=4, padx=40, pady=5, ipadx=10)  # mail id

        pass

    pass


if __name__ == "__main__":
    root = Tk()
    CompanyFrame(root)
    root.mainloop()
    pass
