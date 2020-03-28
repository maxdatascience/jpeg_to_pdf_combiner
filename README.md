# jpeg_to_pdf_combiner
Process folder with `.jpeg` files and convert them into single `.pdf` file


Title: `.jpeg` to `.pdf` combiner

**Combine .jpg files in the target folder to single .pdf file**

**Input:** folder with .jpeg files subfolder output filename
 ex. python jpegToPdf.py /myfolder/ subfolder/ result.pdf

**Output:** `result.pdf` that incorporate all `.jpeg` files from the sourse
folder

Table of content
================

-   Description
    -   Problem
    -   Goal
    -   Solution
-   Getting Started
-   Prerequisites
-   Installing
    -   Install and Run GitHub
    -   Install Python 3
    -   Install package manager `pip`
    -   Set up virtual environment
        -   Create virtual environment for project
    -   Clone repository from GitHub to environment
    -   Install necessary packages

Credits

Description
-----------

### <span class="title-ref">Problem</span>

Documents have been scanned and stored into the folder.
One `.pdf` file should be build incorporating all the scanned `.jpeg` files

### <span class="title-ref">Goal</span>

Create single `.pdf` file incorporating all the scanned images from the
source folder.

### <span class="title-ref">Solution</span>

Design jpegToPdf.py software product for converting `.jpeg` files into single `.pdf` file.

example of execution:
   python jpegToPdf.py /myfolder/ result/ output.pdf

The execution of this command creates subfolder `result` in the `myfolder`. Process all `.jpeg` files in the `myfolder` and put converted `.pdf` files into `result`
subfolder. Then all  `.pdf` files incorporated into single `output.pdf` file.

Getting Started
---------------

These instructions will get you a copy of the project up and running on
your local machine for testing purpose. See deployment part for notes on
how to deploy the project on a live system.

Prerequisites
-------------

-   Linux - Ubuntu
-   GitHub
-   Python v 3.x
-   pip (package manager)
-   Virtual environment package 'venv' to distinguish the project from
    other ones
-   Pillow library from pypi.org
-   PyPDF4 library from pypi.org
-   Terminal

Installing
----------

Feel free to skip the step if you already have the tool installed

### Install and Run GitHub

> `` ` sudo apt-get update sudo apt-get install git ``<span
> class="title-ref"> verify the installation was successful by typing
> \`github --version</span>
>
> ![image](./docs/pic/git_install.png)

### Install Python 3

> Python 3 is installed in Linux. verify the installation by typing
> <span class="title-ref">python3 --version</span>
>
> ![image](./docs/pic/python3.png)

### Install package manager `pip`

> `` ` sudo apt-get update sudo apt-get install python3-pip ``<span
> class="title-ref"> verify the installation was successful by typing
> \`pip --version</span>
> ![image](./docs/pic/pip.png)

### Set up virtual environment

> `` ` sudo apt-get install python3-venv ``\`

#### Create virtual environment for project

Create and activate virtual environment

:   `` ` python -m venv ./venv/project-folder source bin/activate ``<span
    class="title-ref"> as the virtual environment is activated you'll
    see the name of your environment first in the command prompt like
    where \`jpeg_to_pdf_combiner`</span> is the name of the virtual environment

    ![image](./docs/pic/venv.png)

### Clone repository from GitHub to environment

> `` ` git clone link-to-repository ``\` verify that you have the project in your folder
>

### Install necessary packages

> `` ` pip install -r jpeg_to_pdf_combiner/requirements.txt ``\`

**Congratulations, your environment is ready to test!!!**

Credits
-------

Thanks to <span class="title-ref">Alex Clark and Team</span> for the <span
class="title-ref">Pillow library</span> https://pypi.org/project/Pillow/ ,
<span class="title-ref"> Phaseit, Inc.</span> for the <span
class="title-ref">PyPDF4 library</span> https://pypi.org/project/PyPDF4/