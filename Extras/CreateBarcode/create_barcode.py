import barcode
from barcode.writer import ImageWriter
from IPython.display import Image, display

def create_barcode(data):
    code_class = barcode.get_barcode_class('code128')
    code = code_class(data, writer=ImageWriter())
    barcode_file = code.save("./CreateBarcode/Barcode")
    display(Image(barcode_file))

create_barcode('5901-2341-3457')