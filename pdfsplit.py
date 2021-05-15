#!/usr/bin/env python
# pdfsplit

from PyPDF2 import PdfFileReader, PdfFileWriter
import sys

def pdfSplit(path, npages):
    pdfIn = PdfFileReader(path, strict=False)
    pdfOut = PdfFileWriter()

    for page in range(pdfIn.getNumPages()):
        pdfOut.addPage(pdfIn.getPage(page))

        if (page + 1) % npages == 0:
            outPath = path[2:path.index('.',1)] + '_pages-' + str(page) + '-' + str(page + npages -1) + path[path.index('.',1):]
            print('write ' + outPath)
            with open(outPath, 'wb') as out:
                pdfOut.write(out)

            pdfOut = PdfFileWriter()

if __name__ == '__main__':
    path = sys.argv[1]
    npages = sys.argv[2]
    print(path + '  ' + npages)
    pdfSplit(path, int(npages))
