#import neccesary packages
import fitz  

doc = "OBINNA.pdf" # path to pdf file
doc = fitz.open(doc)
pno = doc.loadPage(6)
text = pno.getText('dict')# dict format of the file
blocks = text["blocks"]
imgblocks = [b for b in blocks if b["type"] == 1]
textblocks = [t for t in blocks if t["type"] == 0]

if imgblocks:
   for index, img in enumerate(imgblocks):
       img_name = "obinna_img/%s-%s.%s" % (doc, index, img['ext'])
       with open(img_name, 'wb') as f:
            f.write(img['image'])