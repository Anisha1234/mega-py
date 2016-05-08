import fpdf
from fpdf import FPDF
pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial','I',24)
pdf.cell(50,50,'this is demo')
pdf.output('fpdf.pdf','F')