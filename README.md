# Ratil

Ratil is a Streamlit web application that generates random verses from the Quran for contemplation and study.

## About

This application utilizes the Quran API to fetch verses in Arabic and English translations. Users can specify the number of verses they want to generate and view them instantly on the interface.

## Features

- **Random Verse Generation:** Generates verses randomly from the Quran.
- **Bilingual Display:** Shows verses in Arabic (Uthmani script) and English (Pickthall translation).
- **Interactive Interface:** Users can specify the number of verses to display with a simple slider.

## How to Use

1. Visit the [Ratil Web App](https://wa-ratili-alqoran-tartila.streamlit.app/).
2. Use the number input to select how many verses you want to generate.
3. Click on "Generate Random Verse" to see the verses displayed.

## Screenshots

![image](https://github.com/ErroujiOussama/Ratil/assets/107694414/78ffa631-3a98-4c26-917e-31e1d6199394)
![image](https://github.com/ErroujiOussama/Ratil/assets/107694414/7bef0aa7-c65e-454c-b395-895708223cd9)


## Requirements

- Python 3.x
- Streamlit
- Requests

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   streamlit run app.py
   ```

## Credits

- **Quran API:** Used for fetching Quranic verses.
- **Streamlit:** Framework used for building and deploying the web application.
