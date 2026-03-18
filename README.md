# MN Crypto Portfolio Tracker

![CI](https://github.com/QubitPro/mn-crypto-tracker/actions/workflows/ci.yml/badge.svg)

Real-time cryptocurrency portfolio tracker with live prices, PnL analysis, and interactive dashboard.

## Features

- Live cryptocurrency prices via CoinGecko API
- Portfolio tracking with buy/sell transactions
- Real-time PnL (Profit & Loss) calculation
- WebSocket-powered live price updates
- Interactive charts and dashboard
- REST API with full CRUD operations

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | FastAPI (Python 3.11+) |
| Database | SQLAlchemy + SQLite |
| Real-time | WebSocket + aiohttp |
| Frontend | HTML/CSS/JS + Chart.js |
| Testing | pytest + httpx |
| CI/CD | GitHub Actions |

## Quick Start

\```bash
git clone https://github.com/QubitPro/mn-crypto-tracker.git
cd mn-crypto-tracker
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
python -m uvicorn backend.main:app --reload
\```

## API Docs

Visit `http://localhost:8000/docs` after starting the server.

## License

MIT