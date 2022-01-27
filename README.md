# AI-Creativity

For the AI Art
```
upload the AI_Artist .ipynb file to Google Colab or kaggle to Run it
Make sure you have GPU enabled
```

For the Ascii Art
```
python -m venv venv #only run once
venv\Scripts\activate

pip install -r requirements.txt

cd '.\Ascii Art\'
python ascii.py

# Put the image to change in inputs
# You will see

Add Characters? (y/n): y   #Enter n if you want default string / skip next step
Enter characters to be added: SomethingWithoutSpaces
Add address: car.jpg
Done! Enjoy!

Outputs are in the output folder.
```

For running the API
```
python api.py

This api.py can be imported in other files as well by mentioning
from api import *
from api import search


search('token to be searched', max_results=10)
```