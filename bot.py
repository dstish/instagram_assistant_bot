from os import getenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import telebot

bot_token = getenv("BOT_TOKEN")
bot = telebot.TeleBot(bot_token)


# Function to get the description of the page and the video link
def get_page_info(url):
    # Setting up headless mode
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")  # Disable GPU to avoid errors

    # Initializing WebDriver (e.g., Chrome)
    driver = webdriver.Chrome(options=options)

    try:
        # Opening the page
        driver.get(url)

        # Wait until element by CSS selector becomes available
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div._a9zs"))
        )

        # Get text from the element
        description = element.text

        # Try to find an image in div._aagv
        try:
            element_media = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "img.x5yr21d.xu96u03.x10l6tqk.x13vifvy.x87ps6o.xh8yej3"))
            )
            media_url = element_media.get_attribute("src")
        except:
            # If the image is not found, try to find a video
            try:
                element_video = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "video.x1lliihq.x5yr21d.xh8yej3"))
                )
                media_url = element_video.get_attribute("src")
            except:
                # If no video is found either, assign None
                media_url = "Sorry, I couldn't find"

    finally:
        # In any case, close the browser after completion
        driver.quit()

    return description, media_url


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Hi! Send a link to an Instagram post you're interested in")


# Message handler for URLs
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        # Get the message text
        url = message.text

        # Get the description of the page and the media link
        description, media_url = get_page_info(url)

        # Send the description and media to the user
        if media_url and "mp4" in media_url:
            if len(description) <= 1024:
                # If the link leads to a video, send the video
                bot.send_video(message.chat.id, media_url, caption=description)
            else:
                bot.send_video(message.chat.id, media_url, caption=description[:1024])
                bot.send_message(message.chat.id, description[1024:])
        else:
            # Otherwise, send the image
            if len(description) <= 1024:
                bot.send_photo(message.chat.id, media_url, caption=description)
            else:
                bot.send_photo(message.chat.id, media_url, caption=description[:1024])
                bot.send_message(message.chat.id, description[1024:])

    except Exception as e:
        # If an error occurs, inform the user
        bot.reply_to(message, f"An error occurred, please send a link to your Instagram post.")


# Start the bot
bot.infinity_polling()
