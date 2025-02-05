__ORIGINAL MEMBERS & GITHUB:__
Louis G. Binwag III - louis-uwie 
Jean Maximus C. Cacacho - jeanmaxcacacho 
Paco Antonio V. Zabala - Pacozabala
Ysaac Rainier Mesa - Ysaac12

__AS OF FEB 2, 2025__ - @louis-uwie is repurposing this
repository for ISCS 30.23 Containerizing Applications.

__Project Set Up__
Clone the repository into your designated directory.
Inside this directory:
'''git clone <url>'''

Get into this repository folder.
'''cd /repository'''

Create and activate python virtual environment
'''python -m venv myenv
venv\Scripts\activate #Windows
source venv/bin/activate #Mac/Linux
'''

Once activated, install dependencies
'''pip install --upgrade pip
pip install -r requirements.txt
'''

Applying django migrations and running development server.
''' python manage.py migrade #migrating necessary files / data
python manage.py runserver'''

For more information: https://docs.djangoproject.com/en/5.1/


