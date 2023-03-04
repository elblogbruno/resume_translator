# Resume Translator
This Python software allows you to translate CVs downloaded from the website RX Resume into the language of your choice using Google Translate. The software utilizes the Google Cloud Translation API, so you'll need to set up an API key before you can use it. 

https://rxresu.me/

## Installation
To install the software, follow these steps:

- Clone this repository to your local machine.
- Optional:
    - Create a virtual environment for the project using a tool like virtualenv.
    - Activate the virtual environment.
- Install the required Python packages using the command pip install -r requirements.txt.
- Download the json file of your CV from RX Resume.

To use the software, run the resume_translator.py script. Here's all the available commands:



Replace <input> with the path to the CV file you want to translate, and <target> with the language code of the language you want to translate the CV into (e.g., es for Spanish, fr for French, etc.).

If output name is not established, the translated CV will be saved as a new file in the same directory as the original CV, with the language code appended to the original filename.

## Support
If you encounter any issues or have any questions, please create a GitHub issue in this repository.

## License
This software is released under the MIT License. See the LICENSE file for more information.