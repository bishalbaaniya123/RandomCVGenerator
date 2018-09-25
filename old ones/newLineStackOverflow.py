from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm

my_text = "Hello\nThis is a multiline text\nHere we do not have to handle the positioning of each line manually"

doc = SimpleDocTemplate("example_flowable.pdf", pagesize=A4,
                        rightMargin=2 * cm, leftMargin=2 * cm,
                        topMargin=2 * cm, bottomMargin=2 * cm)

doc.build([Paragraph(my_text.replace("\n", "<br />"), getSampleStyleSheet()['Normal']), ])
