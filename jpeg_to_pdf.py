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
from shutil import rmtree
from PIL import Image
import PyPDF4


def image_merge(folder, result_folder, file='.jpeg'):
    """
    create one .jpeg file that incorporate face and back of the document splitted vertically

    Arguments:
        folder {[str]} -- [folder with face and back .jpeg files]
        result_folder {[str]} -- [result folder for output .jpeg file]

    Keyword Arguments:
        file {str} -- [description] (default: {'.jpeg'})
    """
    if os.path.exists(folder):
        end = ('_2.jpeg',)
        first_end = ('_1.jpeg',)
        for jpeg in sorted(
                filter(lambda file: str(file).endswith(end), os.listdir(folder))):
            print(f'{jpeg}')
            new = jpeg.split('_')
            first_file = ''.join([new[0], first_end[0]])

            img = Image.open(f'{folder}{jpeg}')
            img_face = Image.open(f'{folder}{first_file}')

            x_size, y_size = img.size
            center = int(x_size/2 - 50)

            box = (center, 0, y_size, y_size)
            # box_face = (0, 0, center, y_size)

            region_back = img.crop(box)
            # region_face = img_face.crop(box_face)

            img_face.paste(region_back, box)
            img_face.save(f'{result_folder}{new[0]+file}', 'jpeg')


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

    ext_list = ('.jpeg', '.jpg')
    # loop through the folder
    for file_ in sorted(
            filter(lambda x: str(x).endswith(ext_list), os.listdir(folder))
    ):
        print(file_)
        img = Image.open(f'{folder}{file_}')
        clean_name = os.path.splitext(file_)

        # convert to pdf
        img.save(f'{path}{clean_name[0]}.pdf', 'pdf')


def pdf_combiner(
        pdfs, folder='./temp/', out_folder='./result', out_filename='out.pdf'):
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
    merger.write(f'{out_folder}{out_filename}')
    print(f'\n{out_filename} is ready')


def pdf_merge(temp_folder, result_folder, out_file):
    """
    process folder with .pdf files and create single one that incorporates all
    files of the folder. Then delete temp folder with processed .pdf files

    Arguments:
        temp_folder {[str]} -- [temp folder]
        result_folder {[str]} -- [result folder]
        out_file {[str]} -- [name of the output .pdf file]
    """
    if not os.path.exists(result_folder):
        os.makedirs(result_folder)
    pdf_list = sorted(os.listdir(temp_folder))
    pdf_combiner(pdf_list, temp_folder, result_folder, out_file)
    rmtree(temp_folder)


if __name__ == "__main__":
    folder_name = './doc/'
    temp_folder = 'temp/'
    result_folder = 'result/'
    def_path = ''.join([folder_name, temp_folder])
    def_result = ''.join([folder_name, result_folder])
    out_file = 'out.pdf'
    image_merge_folder = './doc/doc/'

    if len(sys.argv) > 3:
        folder_name = sys.argv[1]
        result_folder = sys.argv[2]
        out_file = sys.argv[3]
        def_path = ''.join([folder_name, temp_folder])
        def_result = ''.join([folder_name, result_folder])
    else:
        print(f'Please input "source folder", "subfolder" and name of the output file!')
        if not input('Proceed with current folder? Y/N: ').lower() == 'y':
            sys.exit(os.EX_OK)

    if os.path.exists(folder_name):
        image_to_pdf()
        pdf_merge(def_path, def_result, out_file)
        image_merge(image_merge_folder, def_result)
