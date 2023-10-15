# ScrapingAlert

ScrapingAlert is a Python script that monitors and scrapes data from various websites and sends notifications when changes are detected.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/ScrapingAlert.git
   cd ScrapingAlert

pip install -r requirements.txt


2. First Run 
   ```bash
   python main.py --new telegram-token

3. Telgram token

   Open the Telegram app and search for the "BotFather" (username: @BotFather).
   
   Start a chat with BotFather.
   
   Use the /newbot command to create a new bot. Follow the instructions provided by BotFather.
   
   Once your bot is created, BotFather will provide you with a unique API token. Save this token; you'll need it for your Python code.

4. Example:
   ```bah
   python main.py --all '''tag'''
   # use tag for all website

5. help
   ```bash
   python main.py --help
