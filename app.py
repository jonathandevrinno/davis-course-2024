import streamlit as st
from bs4 import BeautifulSoup 
import cloudscraper 
import matplotlib.pyplot as plt

# Cryptocurrencies URL list
urls = [
    'https://www.investing.com/crypto/bitcoin',
    'https://www.investing.com/crypto/ethereum',
    'https://www.investing.com/crypto/tether',
    'https://www.investing.com/crypto/bnb',
    'https://www.investing.com/crypto/solana',
    'https://www.investing.com/crypto/xrp',
    'https://www.investing.com/crypto/dogecoin',
    'https://www.investing.com/crypto/shiba-inu',
    'https://www.investing.com/crypto/near-protocol',
    'https://www.investing.com/crypto/polygon',
    'https://www.investing.com/crypto/render',
    'https://www.investing.com/crypto/hedera',
    'https://www.investing.com/crypto/pepe',
    'https://www.investing.com/crypto/theta-network',
    'https://www.investing.com/crypto/floki-inu',
]

# Title and Description
st.title('💸Crypto 2024')
st.write(f'📊Crypto Currencies Data Visualization by using data from investing.com')

scraper = cloudscraper.create_scraper(delay=10, browser="chrome")
data = []

for url in urls:
    try:
        content = scraper.get(url).text
        soup = BeautifulSoup(content, 'html.parser')
        coin = soup.find('h1', {'class': 'mb-2.5 text-left text-xl font-bold leading-7 text-[#232526] md:mb-2 md:text-3xl md:leading-8 rtl:soft-ltr'}).text
        price = soup.find('div', {'class': 'text-5xl/9 font-bold text-[#232526] md:text-[42px] md:leading-[60px]'}).text
        
        links = soup.find_all('a', {'class':'hover:text-[#1256a0] hover:underline'})
        
        for link in links:
            try:
                href = link.get('href')
                if "company-profile" in href:
                    profile_url = "https://www.investing.com" + href
                    content1 = scraper.get(profile_url).text
                    soup1 = BeautifulSoup(content1, 'html.parser')
            except Exception as r:
                print(f"Failed to find content from {profile_url}: {str(r)}")
        data.append((company, price, deskripsi))
    except Exception as e:
        print(f"Failed to find content from {url}: {str(e)}")

coin, prices, descriptions = zip(*data)

prices = [float(price.strip('$')) for price in prices]

plt.figure(figsize=(10, 6))
plt.barh(coin, prices, color='#398bff')
plt.xlabel('Crypto Price ($)')
plt.ylabel('Coin')
plt.title('Coin Chart 2024')
plt.gca().invert_yaxis() 
st.pyplot(plt)

st.title('Coin profile')

selected_coin = st.selectbox('Choose Coin:', coin)

# Temukan indeks saham yang dipilih di daftar perusahaan
index = coin.index(selected_coin)

# Tampilkan detail perusahaan yang dipilih
st.write(f'Coin name: {coin[index]}')
st.write(f'Coin Price: ${prices[index]}')

st.write(f'Nama : Jonathan Devrinno')
st.write(f'NPM : 21082010204')
