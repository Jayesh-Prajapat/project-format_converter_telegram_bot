from conversion_pdf import pdf_jpg
from pdf2image import convert_from_path

import os

def docx_jpg_convert(a):
    
    images=convert_from_path(a)
    
    b = os.path.splitext(a)
    for i in range(len(images)):

        images[i].save(b[0]+ str(i) +'.jpg', 'JPEG')
        
    
    