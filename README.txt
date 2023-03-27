Project Name
    Mapbox API Project

Project Description
    A project that consumes the Mapbox API to look at the geography of the earth and to place markers on locations provided by the user.

How to run the project
    1. Download the project
    2. Open the command prompt or terminal on the base folder of the project
    3. Install Django and the virtual environment (if not done so already)
        - pip install django
        - pip install virtualenvwrapper-win
    4. Create a new virtual environment and download Django inside it
        - mkvirtualenv (name_of_environment)
        - pip install django
    5. Use the virtual environment
        5.1 type:  workon (name_of_environment)
        5.2 Input your Token (Refer to How to use the project)
    6. Run the server
        - python manage.py runserver

How to use the project
    Go to the Mapbox website and create an account at https://account.mapbox.com/
    When logged in got to Tokens tab on the top and look for "Default public token"
    Copy this value and go to the views.py file in the following directory
        - .../mapbox/addresses/views.py
        - Within this file go to line 12 and look for the following
            - 'access_key': '...'
                - Replace ... with your Default public token
    We also need to change this in the models.py file. The directory is
        - .../mapbox/addresses/models.py
        - On line 7 after 'access_token =' is where you will put the access_key
    Now it is good to go.
    When running the application you can input an address into the input box and upon submission will add a marker onto the map with the address.
    Look around the map, zoom in and out to find it.
