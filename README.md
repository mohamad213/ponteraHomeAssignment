# ponteraHomeAssignment

Instructions for Users
To ensure the necessary browsers are installed after setting up the Python environment, users should run the post_install.py script after installing the requirements. Here's how:
1. Create a Virtual Environment

    `python -m venv myVenv`


2. Activate the Virtual Environment

    `myVenv\Scripts\activate`


3. Install requirements, using one of the following commands: 
   *  `pip install -r requirements.txt`

    or
   *  `pip install playwright pytest requests`


4. Install Browsers for Playwright, using one of the following commands: 

   * `python post_install.py`

    or 

   * `playwright install`


5. To run the tests run the following command:
   
   `pytest -v -m "apiTests or uiTests" `
   
   note: Question1 and Question2 tests marked as "apiTests", Question3-bonus test marked as "uiTests"