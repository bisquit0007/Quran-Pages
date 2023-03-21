from pypdf import PdfMerger

pdfs = []

for i in range(604):
  string = 'page (' + str(i+1) + ')'
  pdfs += [string+'.pdf']
    
merger = PdfMerger()

for pdf in pdfs:
    print(pdf)
    merger.append(pdf)

merger.write("result.pdf")
merger.close()