from fpdf import FPDF
pdf = FPDF()
imagelist = "dp.jpeg"

#first add blank page
pdf.add_page()

#give the img path
pdf.image("D:\python mini projects\imge to pdf converter\dp.jpeg",60,120,w=120)

#print the output
pdf.output("dp.pdf","f") 

