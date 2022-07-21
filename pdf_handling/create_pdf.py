from fpdf import FPDF

pdf = FPDF(orientation='P', unit='pt', format='A4')
pdf.add_page()

pdf.image('tiger.jpeg', w=80, h=50)

pdf.set_font(family='Times', style='B', size=20)
pdf.cell(w=0, h=50, txt="Malayan Tiger", align='C', ln=1)

pdf.set_font(family='Times', style='B', size=14)
pdf.cell(w=0, h=15, txt="Description", ln=1)

pdf.set_font(family='Times', size=12)
txt1 = """The Malayan tiger is a tiger from a specific population of the Panthera tigris tigris subspecies that is native 
to Peninsular Malaysia.This population inhabits the southern and central parts of the Malay Peninsula and has been classified as 
critically endangered on the IUCN Red List since 2015. 
"""
pdf.multi_cell(w=0, h=15, txt=txt1, align='L')


pdf.output('output.pdf')
