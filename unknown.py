from datetime import datetime

from borb.pdf.canvas.color.color import HexColor
from borb.pdf.canvas.layout.image.image import Image
from borb.pdf.canvas.layout.layout_element import Alignment
from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from borb.pdf.canvas.layout.table.table import TableCell
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf.document import Document
from decimal import Decimal
from borb.pdf.canvas.layout.table.flexible_column_width_table import FlexibleColumnWidthTable as FlexibleTable
from borb.pdf.canvas.layout.table.fixed_column_width_table import FixedColumnWidthTable as Table
from borb.pdf.page.page import Page
from PIL import Image as Im

# Creating Document
from borb.pdf.pdf import PDF

from database_edited.NumberToWords import convert


class InvoiceToPdfGenerator:
    def __init__(self):

        self.company = company
        self.customer = customer
        self.bill_details = bill_details
        self.products = products
        self.amount_in_words = amount_in_words

        self.pdf = Document()

        # Adding Page
        page = Page(width=Decimal(700), height=Decimal(950))
        self.pdf.append_page(page)

        # PageLayout
        page_layout = SingleColumnLayout(page)

        # Adding the company header to page layout
        page_layout.add(self.build_invoice_company_header())
        # page_layout.add(Paragraph(" ", font_size=Decimal(1)))

        # Adding the customer header to page layout
        page_layout.add(self.build_invoice_customer_header())
        # page_layout.add(Paragraph(" ", font_size=Decimal(1)))

        # Adding the invoice details header
        page_layout.add(self.build_invoice_details_header())
        # page_layout.add(Paragraph(" ", font_size=Decimal(1)))

        # Adding the table
        page_layout.add(self.build_product_list_table())
        page_layout.add(self.build_product_list_table_totals())
        # page_layout.add(Paragraph(" ", font_size=Decimal(1)))

        # Adding the tncs
        page_layout.add(self.build_bill_tnc())
        # page_layout.add(Paragraph(" ", font_size=Decimal(1)))

        # Adding the signature
        # page_layout.add(self.build_bill_signature())
        # page_layout.add(Paragraph(" ", font_size=Decimal(1)))

        pass

    # building company header
    def build_invoice_company_header(self):
        table1 = Table(number_of_rows=3, number_of_columns=3, border_bottom=True, border_right=True, border_top=True,
                       border_left=True, margin_bottom=Decimal(4))

        table1.add(
            TableCell(Paragraph(self.company[0], text_alignment=Alignment.CENTERED, font_size=Decimal(24),
                                padding_bottom=Decimal(5)),
                      background_color=HexColor("48B0E5"), col_span=3,
                      border_bottom=True))
        table1.add(
            TableCell(Paragraph("GSTIN: " + self.company[1], font_size=Decimal(12), text_alignment=Alignment.CENTERED),
                      border_bottom=True))
        table1.add(
            TableCell(
                Paragraph("MAIL ID: " + self.company[2], font_size=Decimal(12), text_alignment=Alignment.CENTERED),
                border_bottom=True))
        table1.add(
            TableCell(Paragraph("MOB NO: " + self.company[3], font_size=Decimal(12), text_alignment=Alignment.CENTERED),
                      border_bottom=True))
        table1.add(
            TableCell(Paragraph(self.company[4], font_size=Decimal(12), text_alignment=Alignment.CENTERED), col_span=3,
                      border_bottom=True))

        table1.set_padding_on_all_cells(Decimal(2), Decimal(2), Decimal(2), Decimal(2))
        table1.no_borders()

        return table1
        pass

    # building customer header
    def build_invoice_customer_header(self):
        table1 = Table(number_of_rows=3, number_of_columns=2, border_bottom=True, border_right=True, border_top=True,
                       border_left=True, margin_top=Decimal(4), margin_bottom=Decimal(4))

        table1.add(TableCell(Paragraph("NAME: " + self.customer[0],
                                       padding_bottom=Decimal(2), padding_left=Decimal(2), font_size=Decimal(12)),
                             border_right=False))
        table1.add(TableCell(Paragraph("GSTIN: " + self.customer[1],
                                       padding_bottom=Decimal(2), padding_left=Decimal(2), font_size=Decimal(12)),
                             border_left=False))
        table1.add(TableCell(Paragraph("MAIL: " + self.customer[2],
                                       padding_bottom=Decimal(2), padding_left=Decimal(2), font_size=Decimal(12)),
                             border_right=False, ))
        table1.add(TableCell(Paragraph("MOBILE: " + self.customer[3],
                                       padding_bottom=Decimal(2), padding_left=Decimal(2), font_size=Decimal(12)),
                             border_left=False, ))
        table1.add(TableCell(Paragraph("ADDRESS: " + self.customer[4],
                                       padding_bottom=Decimal(2), padding_left=Decimal(2), font_size=Decimal(12)),
                             col_span=2))

        table1.set_padding_on_all_cells(Decimal(2), Decimal(2), Decimal(2), Decimal(2))
        table1.no_borders()

        return table1
        pass

    # building invoice details header
    def build_invoice_details_header(self):
        table1 = Table(number_of_rows=2, number_of_columns=4, border_bottom=True, border_right=True,
                       border_top=True, border_left=True, margin_top=Decimal(4), margin_bottom=Decimal(4))
        table1.add(TableCell(Paragraph("BILL NUMBER: " + self.bill_details[0], font_size=Decimal(10)),
                             padding_bottom=Decimal(2), padding_left=Decimal(2)))
        table1.add(TableCell(Paragraph("ORDER NUMBER: " + self.bill_details[2], font_size=Decimal(10)),
                             padding_bottom=Decimal(2), padding_left=Decimal(2)))
        table1.add(TableCell(Paragraph("VEHICLE NUMBER: " + self.bill_details[4], font_size=Decimal(10)),
                             padding_bottom=Decimal(2), padding_left=Decimal(2)))
        table1.add(TableCell(Paragraph("Eway Bill: 123456", font_size=Decimal(10)),
                             padding_bottom=Decimal(2), padding_left=Decimal(2)))
        table1.add(TableCell(Paragraph("BILL DATE: " + self.bill_details[1], font_size=Decimal(10)),
                             padding_bottom=Decimal(2), padding_left=Decimal(2)))
        table1.add(TableCell(Paragraph("ORDER DATE: " + self.bill_details[3], font_size=Decimal(10)),
                             padding_bottom=Decimal(2), padding_left=Decimal(2)))
        table1.add(TableCell(Paragraph("TRANSPORTATION: " + self.bill_details[5], font_size=Decimal(10)),
                             padding_bottom=Decimal(2), padding_left=Decimal(2)))
        table1.add(TableCell(Paragraph("STATE: MADHYA PRADESH", font_size=Decimal(10)),
                             padding_bottom=Decimal(2), padding_left=Decimal(2)))

        table1.set_padding_on_all_cells(Decimal(2), Decimal(2), Decimal(2), Decimal(2))
        table1.no_borders()

        return table1
        pass

    # building product list table
    def build_product_list_table(self):
        # 7 + no of items

        table1 = FlexibleTable(number_of_rows=11, number_of_columns=8, border_bottom=True, border_right=True,
                               border_top=True, border_left=True, margin_top=Decimal(4), margin_bottom=Decimal(4))

        heads = ["SNO", "ITEM NAME", "HSN CODE", "GST%", "QTY", "RATE", "DISC%", "AMOUNT"]

        table1.add(TableCell(Paragraph(heads[0], text_alignment=Alignment.CENTERED, font_size=Decimal(12))))
        table1.add(TableCell(Paragraph(heads[1], text_alignment=Alignment.CENTERED, font_size=Decimal(12))))
        table1.add(TableCell(Paragraph(heads[2], text_alignment=Alignment.CENTERED, font_size=Decimal(12))))
        table1.add(TableCell(Paragraph(heads[3], text_alignment=Alignment.CENTERED, font_size=Decimal(12))))
        table1.add(TableCell(Paragraph(heads[4], text_alignment=Alignment.CENTERED, font_size=Decimal(12))))
        table1.add(TableCell(Paragraph(heads[5], text_alignment=Alignment.CENTERED, font_size=Decimal(12))))
        table1.add(TableCell(Paragraph(heads[6], text_alignment=Alignment.CENTERED, font_size=Decimal(12))))
        table1.add(TableCell(Paragraph(heads[7], text_alignment=Alignment.CENTERED, font_size=Decimal(12))))

        odd_color = HexColor("BBBBBB")
        even_color = HexColor("FFFFFF")
        for row, item in enumerate(self.products):
            c = even_color if row % 2 == 0 else odd_color
            for col, data in enumerate(item):
                if len(data) > 50:
                    data = data[:50]
                # if col == 1:
                #     table1.add(TableCell(Paragraph(data, font_size=Decimal(12)), background_color=c))
                table1.add(TableCell(Paragraph(data, font_size=Decimal(12)),
                                     background_color=c))

        n = 10 - len(self.products)
        for row in range(n):
            if n % 2 == 0:
                c = even_color if row % 2 == 0 else odd_color
            else:
                c = odd_color if row % 2 == 0 else even_color

            for i in range(8):
                table1.add(TableCell(Paragraph(" ", font_size=Decimal(12)), background_color=c))

        # table1.no_borders()
        table1.set_padding_on_all_cells(Decimal(2), Decimal(2), Decimal(2), Decimal(2))

        return table1
        pass

    def build_product_list_table_totals(self):
        table2 = FlexibleTable(number_of_rows=6, number_of_columns=8)

        table2.add(TableCell(Paragraph("Amount in words: ", font_size=Decimal(12)), col_span=6,
                             background_color=HexColor('73D0FF')))

        table2.add(TableCell(Paragraph("TAXABLE AMT", font="Helvetica-Bold", font_size=Decimal(12),
                                       horizontal_alignment=Alignment.RIGHT),
                             background_color=HexColor('73D0FF')))

        table2.add(TableCell(
            Paragraph("111111111", font="Helvetica-Bold", font_size=Decimal(12), horizontal_alignment=Alignment.RIGHT),
            background_color=HexColor('73D0FF')))

        table2.add(TableCell(Paragraph(self.amount_in_words, font_size=Decimal(12)), col_span=6, row_span=2))

        table2.add(TableCell(
            Paragraph("DISCOUNT", font="Helvetica-Bold", font_size=Decimal(12), horizontal_alignment=Alignment.RIGHT)))
        table2.add(TableCell(
            Paragraph("111111111", font="Helvetica-Bold", font_size=Decimal(12), horizontal_alignment=Alignment.RIGHT)))

        table2.add(TableCell(
            Paragraph("IGST", font="Helvetica-Bold", font_size=Decimal(12), horizontal_alignment=Alignment.RIGHT)))
        table2.add(TableCell(
            Paragraph("111111111", font="Helvetica-Bold", font_size=Decimal(12), horizontal_alignment=Alignment.RIGHT)))

        table2.add(TableCell(Paragraph("BANK DETAILS", font_size=Decimal(12)), col_span=6,
                             background_color=HexColor('73D0FF')))

        table2.add(TableCell(
            Paragraph("CGST", font="Helvetica-Bold", font_size=Decimal(12), horizontal_alignment=Alignment.RIGHT)))
        table2.add(TableCell(
            Paragraph("111111111", font="Helvetica-Bold", font_size=Decimal(12), horizontal_alignment=Alignment.RIGHT)))

        table2.add(TableCell(Paragraph("BANK NAME: IDBI BANK, MAHARAJPURA, GWALIOR", font_size=Decimal(12)), col_span=6,
                             border_bottom=False))

        table2.add(TableCell(
            Paragraph("SGST", font="Helvetica-Bold", font_size=Decimal(12), horizontal_alignment=Alignment.RIGHT)))
        table2.add(TableCell(
            Paragraph("111111111", font="Helvetica-Bold", font_size=Decimal(12), horizontal_alignment=Alignment.RIGHT)))

        table2.add(TableCell(Paragraph("A/C NUMBER: 123456789010", font_size=Decimal(12)), col_span=3, border_top=False,
                             border_right=False))
        table2.add(TableCell(Paragraph("IFSC code: 0081ICIC0", font_size=Decimal(12)), col_span=3, border_top=False,
                             border_left=False))

        table2.add(TableCell(Paragraph("TOTAL AMOUNT", font_size=Decimal(12), font="Helvetica-Bold",
                                       horizontal_alignment=Alignment.RIGHT),
                             background_color=HexColor('73D0FF')))
        table2.add(TableCell(
            Paragraph("111111111", font="Helvetica-Bold", font_size=Decimal(12), horizontal_alignment=Alignment.RIGHT),
            background_color=HexColor('73D0FF')))

        # table2.no_borders()
        table2.set_padding_on_all_cells(Decimal(2), Decimal(2), Decimal(2), Decimal(2))
        return table2
        pass

    # building tncs
    # def build_bill_tnc(self):
    #
    #     table1 = Table(number_of_rows=6, number_of_columns=1, background_color=HexColor('73D0FF'),
    #                    margin_top=Decimal(2))
    #
    #     table1.add(TableCell(Paragraph("Conditions:", font_size=Decimal(12))))
    #
    #     table1.add(TableCell(Paragraph("Condition 1", font_size=Decimal(8))))
    #     table1.add(TableCell(Paragraph("Condition 2", font_size=Decimal(8))))
    #     table1.add(TableCell(Paragraph("Condition 3", font_size=Decimal(8))))
    #     table1.add(TableCell(Paragraph("Condition 4", font_size=Decimal(8))))
    #     table1.add(TableCell(Paragraph("Condition 5", font_size=Decimal(8))))
    #
    #     table1.no_borders()
    #     table1.set_padding_on_all_cells(Decimal(2), Decimal(2), Decimal(2), Decimal(2))
    #     return table1

    def build_bill_tnc(self):

        table1 = FlexibleTable(number_of_rows=3, number_of_columns=2, margin_top=Decimal(4), margin_bottom=Decimal(4))

        table1.add(TableCell(Paragraph("Conditions:", font_size=Decimal(10)), background_color=HexColor('73D0FF')))
        table1.add(TableCell(Image(Im.open(r"signature.jpeg"), width=Decimal(100), height=Decimal(50),
                                   horizontal_alignment=Alignment.RIGHT), row_span=2))

        table1.add(TableCell(Paragraph(
            "THIS IS TO JUSTIFY THAT WE DO NOT RETURN THE ITEMS AND THIS IS A FIXED RATE SHOP I WILL BE ADDING MORE DETAILS LATER THIS IS FOR THE GENERAL TEST",
            font_size=Decimal(6)), row_span=2, background_color=HexColor('73D0FF')))
        # table1.add(TableCell(Paragraph("Condition 2", font_size=Decimal(6))))
        # table1.add(TableCell(Paragraph("Condition 3", font_size=Decimal(6))))
        # table1.add(TableCell(Paragraph("Condition 4", font_size=Decimal(6))))
        # table1.add(TableCell(Paragraph("Condition 5", font_size=Decimal(6))))

        table1.add(TableCell(Paragraph("Signature", horizontal_alignment=Alignment.RIGHT, font_size=Decimal(8))))

        table1.no_borders()
        table1.set_padding_on_all_cells(Decimal(2), Decimal(2), Decimal(2), Decimal(2))
        return table1
        pass

    # building signature
    # def build_bill_signature(self):
    #     table1 = Table(number_of_rows=2, number_of_columns=1)
    #     table1.add(TableCell(Image(Im.open(r"signature.jpeg"), width=Decimal(100), height=Decimal(20),
    #                                horizontal_alignment=Alignment.RIGHT)))
    #     table1.add(TableCell(Paragraph("Signature", font_size=Decimal(8), horizontal_alignment=Alignment.RIGHT)))
    #     table1.no_borders()
    #     table1.set_padding_on_all_cells(Decimal(2), Decimal(2), Decimal(2), Decimal(2))
    #     return table1
    #     pass

    pass


if __name__ == "__main__":
    company = ["R.K. Sales", "23abdcd2019", "mailid@gmail.com", str(9977725299),
               "Address line-1,\nAddress Line-2,\nAddress Line3, City, State - Zipcode"]
    customer = ["Shubham Khandelwal", "23defghi2022", "shubhamespn@gmail.com", str(9977725299),
                "Address line-1,\nAddress Line-2,\nAddress Line3, City, State - Zipcode"]
    bill_details = [str(123), datetime.now().strftime("%x"), str(7008), datetime.now().strftime("%x"),
                    "MP07CH6859", "TRUCK"]
    amount_in_words = convert("999999999")
    # print(amount_in_words, type(amount_in_words))
    products = [
        ["1", "acer monitor 16\" screen", "hsn123", "18", "1", "12000", "0", "14000"],
        ["2", "logitech specialite rgb light keyboard and mouse", "hsn-876", "18", "1", "150000", "0", "180000"],
        ["1", "acer monitor 16\" screen", "hsn123", "18", "1", "12000", "0", "14000"]
    ]

    invoice = InvoiceToPdfGenerator()
    pdf = invoice.pdf
    with open("output.pdf", "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, pdf)
