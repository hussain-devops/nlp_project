from fpdf import FPDF
 
s="log2(N) is about the expected number of probes in an average successful search, and the worst case is log2(N), just one more probe. If the list is empty, no probes at all are made. Thus binary search is a logarithmic algorithm and executes in O(logN) time. In most cases it is considerably faster than a linear search. It can be implemented using iteration, or recursion. In some languages it"



pdf = FPDF()
pdf.add_page()
# pdf.open()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Welcome to Python!", ln=1, align="C")
# pdf.cell(10,10,txt=s)
pdf.write(10,s)
pdf.output("simple_demo.pdf")