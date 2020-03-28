import os
import sys
from PIL import Image
import PyPDF4


def image_to_pdf(folder='./doc/', subfolder='temp/'):
    # check if output folder exist
    path = ''.join([folder, subfolder])
    if not os.path.exists(path):
        os.makedirs(path)

    # loop through the folder
    for file_ in sorted(filter(is_file, os.listdir(folder))):
        print(file_)
        img = Image.open(f'{folder}{file_}')
        clean_name = os.path.splitext(file_)

        # convert to pdf
        img.save(f'{path}{clean_name[0]}.pdf', 'pdf')


def is_file(list_folder):
    return str(list_folder).endswith('.jpeg')


def pdf_combiner(pdf_list, folder='./temp/', out_filename='out.pdf'):
    # merge all pdf to out_file
    merger = PyPDF4.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(f'{folder}{pdf}')
        print(f'{pdf} processed')
    merger.write(f'{folder}{out_filename}')
    print(f'\n{out_filename} is ready')


if __name__ == "__main__":
    # folder with jpeg files '/folder/doc/'
    path = './doc/temp/'
    if len(sys.argv) > 2:
        if not len(sys.argv[1]):
            folder_name = sys.argv[1]

        # subfolder for output files result
        if not len(sys.argv[2]):
            result_folder = sys.argv[2]

        # output filename output.pdf
        if not len(sys.argv[3]):
            out_file = sys.argv[3]
        if folder_name and result_folder:
            path = folder_name+result_folder

    image_to_pdf()
    pdf_list = sorted(os.listdir(path))
    pdf_combiner(pdf_list, path)
