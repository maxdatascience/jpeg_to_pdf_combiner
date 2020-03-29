"""
[Convert .jpeg files from the folder to a single .pdf file]
"""
#*****************************************************************************#
# MIT License                                                                 #
#                                                                             #
# Copyright(c)[2020][Max Luckystar]                                           #
# max.datascience@gmail.com         www.linkedin.com/in/maxdatascience        #
#                                                                             #
# Permission is hereby granted, free of charge, to any person obtaining a     #
# copy of this software and associated documentation files(the "Software"),   #
# to deal in the Software without restriction, including without limitation   #
# the rights to use, copy, modify, merge, publish, distribute, sublicense,    #
# and/or sell copies of the Software, and to permit persons to whom the       #
# Software is furnished to do so, subject to the following conditions:        #
#                                                                             #
# The above copyright notice and this permission notice shall be included in  #
# all copies or substantial portions of the Software.                         #
#                                                                             #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  #
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,    #
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE #
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER      #
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING     #
# FROM OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS #
# IN THE  SOFTWARE.                                                           #
#                                                                             #
#*****************************************************************************#

import os
import sys
from PIL import Image
import PyPDF4


def image_to_pdf(folder='./doc/', subfolder='temp/'):
    """
    convert .jpeg images to .pdf files for each image separate .pdf file

    Keyword Arguments:
        folder {str} -- [folder with .jpeg files] (default: {'./doc/'})
        subfolder {str} -- [subfolder to put .pdf files] (default: {'temp/'})
    """
    # check if output folder exist
    path = ''.join([folder, subfolder])
    if not os.path.exists(path):
        os.makedirs(path)

    # loop through the folder
    for file_ in sorted(
            filter(lambda x: str(x).endswith('.jpeg'), os.listdir(folder))
    ):
        print(file_)
        img = Image.open(f'{folder}{file_}')
        clean_name = os.path.splitext(file_)

        # convert to pdf
        img.save(f'{path}{clean_name[0]}.pdf', 'pdf')


def pdf_combiner(pdfs, folder='./temp/', out_filename='out.pdf'):
    """
    merge all .pdf files from folder to a single .pdf file

    Arguments:
        pdf_list {[list]} -- [sorted list of .pdf files in the folder]

    Keyword Arguments:
        folder {str} -- [folder with .pdf files to process] (default: {'./temp/'})
        out_filename {str} -- [name of output combined .pdf] (default: {'out.pdf'})
    """
    # merge all pdf to out_file
    merger = PyPDF4.PdfFileMerger()
    for pdf in pdfs:
        merger.append(f'{folder}{pdf}')
        print(f'{pdf} processed')
    merger.write(f'{folder}{out_filename}')
    print(f'\n{out_filename} is ready')


if __name__ == "__main__":
    folder_name = './doc/'
    result_folder = 'temp/'
    def_path = ''.join([folder_name, result_folder])
    out_file = 'out.pdf'

    if len(sys.argv) > 3:
        folder_name = sys.argv[1]
        result_folder = sys.argv[2]
        out_file = sys.argv[3]
        def_path = folder_name + result_folder
    else:
        print(f'Please input "source folder", "subfolder" and name of the output file!')
        if not input('Proceed with current folder? Y/N: ').lower() == 'y':
            sys.exit(os.EX_OK)

    if os.path.exists(folder_name):
        image_to_pdf()
        pdf_list = sorted(os.listdir(def_path))
        pdf_combiner(pdf_list, def_path)
