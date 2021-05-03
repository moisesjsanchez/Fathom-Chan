
# Fathom Chan

This is a discord bot which fetches current Fathom sponsored movie events. Currently the bot used a automated google sheet to update and display current anime movies sponsored by Fathom. Down below is information about the bot and how to set up your own version of the bot for your own needs!

## How Set Up

### Downloading Project

First clone this repository to your local machine. To do this under the repository name, click **clone or download**.

### Setting Up Google Sheets Scrapper

1. Now to set up your own google sheets web scrapper. Go to Google Console Developer dashboard.
2. From dashboard click the top left area with the drop down and then select New Project.
3. Name your project anything
4. Go to APIs & Services, then search for Google Drive and enable it
5. Now on the top right click create credentials. Your credential should be downloaded on your machine.
6. Select Google Drive API, web server, and application data.
7. Set up your ownership.  Inputting here, but be sure to have the key type to be JSON.
8. Now go back to APIs & Services and enable Google Sheets API.

### Implementing Web Scrapping to Google Sheet

1. First create your google sheet
2. To implement web scrapping we will use IMPORTXLM function built into google sheets. Set a column with IMPORTXLM
3. Next we use XPath to choose which part of the webpage we want to scrapper to update and collect from. In this case we want to movies time and dates. To choose these easily we right click, inspect, then click the tag needed and copy as XPath
4. Finally we set IMPORTXLM parameters with the copied XPath.
Example:  `=IMPORTXML("https://www.fathomevents.com/categories/anime","//p[@class ='date card__date']")`
5. Now in our project. Cd into fetch.py and to use our google sheet we change our sheet variable from Anime Movies Showing to the name of our google sheet.

### Setting Up Discord Bot Configurations

1. Go to Discord Developer portal and create new application
2. Now in settings under username click to see Token. Save this token and place it in your .env file in your Fathom project
3. After setting up your google sheets you can now allow your bot on your server by going to the OAuth2 tab and checking the bot checkbox
4. Next give your bot permissions. Fathom just needs to send messages at the moment.
5. Finally copy and paste link given under scope to choose your channel you want Fathom to be on!
6. Finally add Fathom, and now the your bot is in your server!


### Run On Local Machine

1. Open your command line and cd into Fathom-Chan
2. Create your virtual environment by running
` pipenv shell ` then `pipenv install` to get all dependencies running.
3. Start up the bot by running bot.py in your command line.


## Built With

* [Python 3.7.4](https://www.python.org/downloads/) - Current supported language
* [Google Sheets API](https://developers.google.com/sheets/api/quickstart/python) - For hosting Fathom movie information
* [discord.py](https://github.com/moisesjsanchez/Guitarist-Toolbox) - API wrapper for discord

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/moisesjsanchez/prog-generator/blob/master/LICENSE) file for details
