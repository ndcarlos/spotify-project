## Getting started with wander
  
  1. Clone the repository
  * Use git to clone this project onto your machine:
  
  ```bash
  git clone https://github.com/ndcarlos/spotify-project/wander
  cd wander
  ```
  2. Create your ```.env``` file
  * Copy the ```example.env``` file and rename it to ```.env```:

  ``` bash
  cp example.env .env
  ```

  * Fill in the placeholders in the ```.env``` file with your Spotify API credentials. To obtain your API credentials: <br>
        1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com) <br>
        2. Create a new application <br>
        3. Copy the ```Client ID```, ```Client Secret```, and set your ```Redirect URI```<br>

  3. Install Dependencies
     To install all the dependencies listed in the file, use:

     ```bash
     pip install -r requirements.txt
     ```

  4. Run the Application
