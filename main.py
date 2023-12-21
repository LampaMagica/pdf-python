from fpdf import FPDF

pdf = FPDF()

number = 30
x = 1

while x <= 30:
    print(x,"tada")

    #Add a page
    pdf.add_page()

    #Add text first ligne
    pdf.set_font(family="Times", style="B", size=12)
    pdf.cell(w=0, h=12,text="Hello world!", border=1, new_x="LEFT", new_y="NEXT", align="L" )

    #Add text Secnd ligne
    pdf.set_font(family="helvetica", size=10)
    pdf.cell(w=0, h=10,text="Not Form This !", border=0, new_x="LEFT", new_y="NEXT" )


    x+=1

# for x in number:
#     #Add a page
#     pdf.add_page()
#
#     #Add text first ligne
#     pdf.set_font(family="Times", style="B", size=12)
#     pdf.cell(w=0, h=12,text="Hello world!", border=1, new_x="LEFT", new_y="NEXT", align="L" )
#
#     #Add text Secnd ligne
#     pdf.set_font(family="helvetica", size=10)
#     pdf.cell(w=0, h=10,text="Not Form This !", border=0, new_x="LEFT", new_y="NEXT" )

pdf.output("hello01010.pdf")