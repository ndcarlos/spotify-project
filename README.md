![Project Header](spotifyheader.jpg)

# Spotify Project

This repository contains various files, scripts, and applications I created using Spotify's Web API. The files serve different purposes: some are standalone applications, while others are reusable functions and scripts that may be used across multiple applications.

## Table of Contents

*   🙋 [What is covered in this README?](#what-is-covered-in-this-readme)
*   🌐 [Global Dependencies](#global-dependencies)
   *   🕸️ [Spotify Web API](#spotify-web-api)
   *   📚 [Libraries](#libraries)
*   ⏬ [Install](#install)
*   🗂️ [Contents](#contents)
   *   💻 [Projects](#projects)
   *   📝 [Scripts](#scripts)
*   🔮 [Future plans](#future-plans)
*   🤝 [Contribute](#contribute)
*   ©️ [License](#license)
*   🔌 [Sources](#sources)

## What is covered in this README
This README intends to provide a high-level overview of the files and folders of significance in this repository. 

## Global dependencies
_Note: local dependencies for folders within this repository will be detailed in their respective READMEs_
   * ### [Spotify Web API](https://developer.spotify.com/documentation/web-api)
      *  [Spotipy](https://spotipy.readthedocs.io/en/2.24.0/) is a lightweight Python library for the Spotify Web API. With Spotipy you get full access to all of the music data provided by the Spotify platform.  
   * ### Libraries
      * [dotenv](https://pypi.org/project/python-dotenv/) - Used to read key-value pairs from a `.env` file and can set them as environment variables. Specifically utilized in this repo to boost security by storing and loading sensitive API credentials.
      * [os](https://docs.python.org/3/library/os.html) - Python's built-in module for interacting with the operating system. This is used with `dotenv` to execute the retrieval of environmental variables.


## Install
Use git to clone this repository into your computer.

```
git clone https://github.com/ndcarlos/spotify-project
```

## Contents
Files denoted with 🏗️ are not yet complete.

   * ### Projects
     (each contained in their folder)
      * 🏗️ [`wander`](https://github.com/ndcarlos/spotify-project/blob/main/wander/README.md): New artist discovery tool.


   * ### Scripts 
      * [`get_token.py`](https://github.com/ndcarlos/spotify-project/blob/main/get_token.py): Retrieves authorization tokens from Spotify Web API and stores it as `access_token`

## Future Plans

## Contribute
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Sources

[react-markdown][react-markdown] - Project which served as an inspiration for this README

[Blog post templates][blog-post-templates] - Used to structure this template as an easy-to-read blog post

[About markdown][about-markdown] - Why should you use markdown?

[Markdown Cheat Sheet][markdown-cheatsheet] - Get a fast overview of the syntax

[//]: # "Source definitions"
[blog-post-templates]: https://backlinko.com/hub/content/blog-post-templates "Backlinko blog post templates"
[about-markdown]: https://www.markdownguide.org/getting-started/ "Introduction to markdown"
[markdown-cheatsheet]: https://www.markdownguide.org/cheat-sheet/ "Markdown Cheat Sheet"

>>>>>>> d46ed75aff37d176b88889cda74f9a5aaf22aab5
