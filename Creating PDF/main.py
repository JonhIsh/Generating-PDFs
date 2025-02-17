from fpdf import FPDF

pdf = FPDF(orientation='P', unit='pt', format='A4')
pdf.add_page()

pdf.image('tiger.jpeg', w=80, h=50)

pdf.set_font(family='Times', style='B', size=24)
pdf.cell(w=0, h=50, txt="Malayan Tiger", align="C", ln=True)

pdf.set_font(family='Times', style='B', size=14)
pdf.cell(w=0, h=15, txt="Description", ln=True)

pdf.set_font(family='Times', size=12)
txt1 = """
The Malayan Tiger is one of the smallest tiger species found throughout the southern and central parts of the Malay Peninsula and southern parts of Thailand. It is the national symbol of Malaysia. In fact, it was only recognised as a tiger subspecies in 2004. In the past, the Malayan tiger and Indochinese tiger were thought to be the same. The body of this species is orange-coloured with thin black stripes that perfectly conceals its motive in the background when stalking prey or retreating into seclusion and safety.
"""
pdf.multi_cell(w=0, h=15, txt=txt1)

pdf.output('result.pdf')