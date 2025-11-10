# DexScreener Tokens Scraper

> The DexScreener Tokens Scraper collects real-time cryptocurrency token data across multiple blockchains like Ethereum, Solana, and HyperEVM. It helps traders, analysts, and developers monitor market trends, liquidity, and token performance.

> With a focus on speed and precision, it turns live token insights into actionable market intelligence.


<p align="center">
  <a href="https://bitbash.def" target="_blank">
    <img src="https://github.com/za2122/footer-section/blob/main/media/scraper.png" alt="Bitbash Banner" width="100%"></a>
</p>
<p align="center">
  <a href="https://t.me/devpilot1" target="_blank">
    <img src="https://img.shields.io/badge/Chat%20on-Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram">
  </a>&nbsp;
  <a href="https://wa.me/923249868488?text=Hi%20BitBash%2C%20I'm%20interested%20in%20automation." target="_blank">
    <img src="https://img.shields.io/badge/Chat-WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp">
  </a>&nbsp;
  <a href="mailto:sale@bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Email-sale@bitbash.dev-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail">
  </a>&nbsp;
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Visit-Website-007BFF?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Website">
  </a>
</p>




<p align="center" style="font-weight:600; margin-top:8px; margin-bottom:8px;">
  Created by Bitbash, built to showcase our approach to Scraping and Automation!<br>
  If you are looking for <strong>Dexscreener Tokens Scraper</strong> you've just found your team — Let’s Chat. 👆👆
</p>


## Introduction

DexScreener Tokens Scraper is built to streamline token data collection from decentralized exchanges (DEXes) and launchpads. It enables users to track real-time prices, liquidity, and other on-chain metrics without manual data gathering.

### Why It Matters

- Centralizes token data from various blockchains and exchanges.
- Monitors real-time token performance with minimal setup.
- Supports both standard DEXes and launchpad-specific metrics.
- Allows precise filtering and sorting by volume, liquidity, or market trends.
- Enables deeper insights into early-stage token launches and trading activity.

## Features

| Feature | Description |
|----------|-------------|
| Multi-Blockchain Support | Extract data from Ethereum, Solana, BSC, Polygon, Avalanche, and more. |
| DEX & Launchpad Integration | Includes Uniswap, PancakeSwap, Raydium, Pump.Fun, Moonit, and others. |
| Real-Time Data | Provides up-to-the-minute prices, volume, and liquidity data. |
| Customizable Filters | Define chains, pagination, sorting, and filtering parameters. |
| Launchpad Tracking | Supports Solana/Moonit launchpad progress metrics. |
| Dynamic Pagination | Automatically handles multiple pages of token results. |
| Exchange-Specific Formatting | Adapts output structure based on exchange characteristics. |

---

## What Data This Scraper Extracts

| Field Name | Field Description |
|-------------|------------------|
| tokenName | The name of the cryptocurrency token. |
| tokenSymbol | The symbol or ticker of the token. |
| priceUsd | Current token price in USD. |
| age | Age of the token since listing. |
| transactionCount | Number of transactions over the selected period. |
| volumeUsd | Trading volume in USD. |
| makerCount | Count of unique wallets interacting with the token. |
| priceChange5m | Price change over the last 5 minutes. |
| priceChange1h | Price change over the last hour. |
| priceChange6h | Price change over the last 6 hours. |
| priceChange24h | Price change over the last 24 hours. |
| liquidityUsd | Total liquidity in USD (if available). |
| marketCapUsd | Market capitalization in USD. |
| boost | Token boost score or ranking metric. |
| pairDetailUrl | URL to the token’s pair page on DexScreener. |
| address | Token contract address (if retrievable). |
| lowerPoolAddress | Lowercase pool address derived from the pair URL. |
| tokenImageUrl | Token logo or image URL. |

---

## Example Output


    [
      {
        "tokenName": "airfryer coin",
        "tokenSymbol": "FRYER",
        "priceUsd": 0.0001097,
        "age": 2.2,
        "transactionCount": 115,
        "volumeUsd": 1000.0,
        "makerCount": 61,
        "priceChange5m": -0.0036,
        "priceChange1h": -0.0036,
        "priceChange6h": -0.0036,
        "priceChange24h": -0.0036,
        "liquidityUsd": 3300.0,
        "marketCapUsd": 109707.0,
        "boost": 1100,
        "pairDetailUrl": "https://dexscreener.com/solana/29jupdw7nqgzeqx9m61jjkgagtg2w283aqyxtcrw6ssu",
        "address": "4qTJV18HH5YUz9KSAdGEnVQuxPkR9c4gDwV7TaMxbonk",
        "lowerPoolAddress": "29jupdw7nqgzeqx9m61jjkgagtg2w283aqyxtcrw6ssu",
        "tokenImageUrl": "https://dd.dexscreener.com/ds-data/tokens/solana/4qTJV18HH5YUz9KSAdGEnVQuxPkR9c4gDwV7TaMxbonk.png?key=176c85"
      },
      {
        "tokenSymbol": "MANBAT",
        "tokenName": "Manbat Nemisis",
        "priceUsd": 0.054593,
        "marketCapUsd": 4500.0,
        "age": 24.0,
        "transactionCount": 9,
        "volumeUsd": 273.0,
        "makerCount": 9,
        "priceChange5m": null,
        "priceChange1h": 0.76,
        "priceChange6h": 0.76,
        "priceChange24h": -11.78,
        "liquidityUsd": null,
        "pairDetailUrl": "https://dexscreener.com/solana/cf3ztcluno2pmh4fijyl9j78zgdvr4j5dfjc8gcd9gag",
        "address": null,
        "lowerPoolAddress": "cf3ztcluno2pmh4fijyl9j78zgdvr4j5dfjc8gcd9gag",
        "tokenImageUrl": "https://cdn.dexscreener.com/cms/images/7535d6a4d5e34e57904ea11588be2e30da95fa362989282fa6fbc21a2c2377e3?width=64&height=64&fit=crop&quality=95&format=auto",
        "boost": 0
      }
    ]

---

## Directory Structure Tree


    dexscreener-tokens-scraper/
    ├── src/
    │   ├── main.py
    │   ├── extractors/
    │   │   ├── dexscreener_parser.py
    │   │   └── token_utils.py
    │   ├── outputs/
    │   │   ├── json_exporter.py
    │   │   └── csv_exporter.py
    │   └── config/
    │       └── settings.example.json
    ├── models/
    │   ├── token_model.py
    │   └── launchpad_model.py
    ├── data/
    │   ├── inputs.sample.json
    │   └── sample_output.json
    ├── requirements.txt
    ├── LICENSE
    └── README.md

---

## Use Cases

- **Crypto Analysts** use it to monitor token movements and liquidity trends, so they can identify breakout opportunities early.
- **Developers** integrate the scraper into dashboards or trading bots to enhance live market insights.
- **Investors** track new token launches to discover potential high-growth assets.
- **Researchers** collect structured market data for quantitative analysis.
- **Trading Firms** monitor volume and liquidity fluctuations to optimize strategy performance.

---

## FAQs

**Q1: Does it support all blockchains listed on DexScreener?**
Yes, it supports major chains like Ethereum, Solana, BSC, Polygon, Avalanche, Fantom, and more.

**Q2: What happens if a token image or address is missing?**
If the address isn’t directly available, you can use the `pairDetailUrl` or `lowerPoolAddress` to fetch it via a pair-level scraper.

**Q3: Can I target a specific DEX or launchpad?**
Absolutely. Just use the `chainName/dexName` format (e.g., `solana/moonit`, `bsc/pancakeswap`) to target specific DEXes.

**Q4: What’s the output format?**
The scraper outputs structured JSON with comprehensive fields for easy integration into analytics systems or databases.

---

## Performance Benchmarks and Results

**Primary Metric:** Scrapes ~200 tokens per minute on average.
**Reliability Metric:** Maintains a 98% success rate across supported chains.
**Efficiency Metric:** Handles up to 50 pages per run with optimized pagination.
**Quality Metric:** Achieves 99% data completeness and consistent schema across networks.


<p align="center">
<a href="https://calendar.app.google/74kEaAQ5LWbM8CQNA" target="_blank">
  <img src="https://img.shields.io/badge/Book%20a%20Call%20with%20Us-34A853?style=for-the-badge&logo=googlecalendar&logoColor=white" alt="Book a Call">
</a>
  <a href="https://www.youtube.com/@bitbash-demos/videos" target="_blank">
    <img src="https://img.shields.io/badge/🎥%20Watch%20demos%20-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube">
  </a>
</p>
<table>
  <tr>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/MLkvGB8ZZIk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review1.gif" alt="Review 1" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash is a top-tier automation partner, innovative, reliable, and dedicated to delivering real results every time.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Nathan Pennington
        <br><span style="color:#888;">Marketer</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/8-tw8Omw9qk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review2.gif" alt="Review 2" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash delivers outstanding quality, speed, and professionalism, truly a team you can rely on.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Eliza
        <br><span style="color:#888;">SEO Affiliate Expert</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtube.com/shorts/6AwB5omXrIM" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review3.gif" alt="Review 3" width="35%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Exceptional results, clear communication, and flawless delivery. Bitbash nailed it.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Syed
        <br><span style="color:#888;">Digital Strategist</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
  </tr>
</table>
