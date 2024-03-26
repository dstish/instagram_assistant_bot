# Instagram Assistant Bot 🤖

Welcome to Instagram Assistant Bot, your helpful companion for downloading Instagram posts effortlessly!

## Installation 🚀

1. **Clone the repository:**
   ```
   git clone https://github.com/dstish/instagram_assistant_bot.git
   cd instagram_assistant_bot
   ```

2. **Install the dependencies:**
   ```
   
   pip install -r requirements.txt
   
   ```

## Configuration ⚙️

Set up your Telegram Bot API token effortlessly using one of the following methods:

1. **PyCharm Configuration**:
   - Open the project in PyCharm.
   - Navigate to "Run" > "Edit Configurations".
   - Add a new Python configuration for `bot.py`.
   - In the "Environment variables" section, add a new environment variable with the name `BOT_TOKEN` and your Telegram Bot API token as the value.

2. **Using `.env` file**:
   - Create a file named `.env` in the root directory of the project.
   - Inside the `.env` file, add the following line:
     
     ```
     
     BOT_TOKEN=your_telegram_bot_api_token
     
     ```
   - Replace `your_telegram_bot_api_token` with your actual Telegram Bot API token.


## Usage 📝

1. **Run the bot:**
   ```
   
   python bot.py
   
   ```

2. **Start a chat with the bot in Telegram.**
   
3. **Send a link to an Instagram post you're interested in.**

4. **Sit back and relax! The bot will promptly reply with the post's description and media content (image or video).**

## Contributing 🙌

Contributions are welcome! If you have any suggestions, feature requests, or find any issues, please open an issue or a pull request.

## License 📄

This project is licensed under the [MIT License](LICENSE). Enjoy the freedom to explore and create!
