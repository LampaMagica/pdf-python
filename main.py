from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font(family='helvetica',style="B",size=16)
pdf.cell(w=40,h=10,text="Hello World")

pdf.output("testing.pdf")