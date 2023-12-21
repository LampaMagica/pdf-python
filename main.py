from fpdf import FPDF
import pandas as pd

# Charger les données depuis le fichier CSV
with open('topics.csv', 'r') as csv_file:
    data = pd.read_csv(csv_file)

# Créer une instance de la classe FPDF
pdf = FPDF()
pdf.set_auto_page_break(auto=False)

# Itérer sur les lignes du DataFrame
for _,row in data.iterrows():


    #print(f"Order : {row['Order']} Topic : {row['Topic']} Pages : {row['Pages']}")
    pdf.add_page()
    pdf.set_font('Times','B', 24)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=12,text=row['Topic'])
    pdf.set_line_width(0.25)
    pdf.set_draw_color(r=100, g=100, b=100)
    pdf.line(x1=10, y1=21, x2=200, y2=21)
    # Bottom integration main page
    pdf.set_font(family='helvetica', style='I', size=10)
    pdf.set_xy(15, 278)
    pdf.cell(w=0, h=10, text=row['Topic'], border=0, align="R")


#First logic about adding lines notebook
    #Adding Notebook Line
    for i in range(32, 280, 10):
        pdf.set_draw_color(153,153,255)
        pdf.set_line_width(0.15)
        pdf.line(x1 = 10, y1=i, x2=200,y2=i)


    for i in range(int(row['Pages']-1)):
        #Bottom integration
        pdf.add_page()
        pdf.set_font(family='helvetica',style='I',size=10)
        pdf.set_xy(15,278)
        pdf.cell(w=0,h=10,text=row['Topic'],border=0, align="R")

#Second Logic about adding line notebook
        # Adding Notebook Line
        for i in range(25):
            line_height = 32
            pdf.set_draw_color(153, 153, 255)
            pdf.set_line_width(0.15)
            pdf.line(x1=10, y1=line_height + (i * 10), x2=200, y2=line_height + (i * 10))

pdf.output("output.pdf")




