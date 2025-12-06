# BPL - Football Team Auction App

BPL is a Django-powered web application that allows users to create football teams, manage players, and conduct player auctions in real-time. It’s built to simulate an engaging team bidding system where teams can bid for players with virtual budgets—ideal for fantasy leagues, club simulations, and football management games.

## 🔧 Features

- Create and manage football teams
- Add and list players with attributes like position, base price, nationality, etc.
- Real-time player auctions with bid tracking
- Team budget and squad management
- Admin panel for player/team approvals and auction controls

## 🏗️ Tech Stack

- **Backend**: Django, Django Rest Framework
- **Frontend**: HTML, CSS, JavaScript (or integrate Vue.js for SPA capabilities)
- **Database**: PostgreSQL / SQLite (for development)
- **Real-Time Auction**: Channels (WebSockets) or polling-based implementation

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/jitheshjr/bpl.git
cd bpl
```
2. Install Dependencies
```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```
3. Setup Database
```bash
python manage.py migrate
python manage.py createsuperuser
```
4. Run the Server
```bash
python manage.py runserver
Visit http://127.0.0.1:8000 to access the app.
```
📁 Project Structure
bpl/
├── bpl/         
├── auction/     
├── static/      
├── media/       
└── manage.py
└── db.sqlite3
🧪 Sample Workflow
Admin creates available players.

Team managers register and build teams.

Auction begins: players are listed one at a time, bids are placed, highest bidder gets the player.

Budget check ensures fairness and balance.

Post-auction, teams can view full rosters and analytics.

✨ Future Enhancements
Player search/filter functionality

Auction countdown timer

Integration with payment gateways for fantasy league monetization

Role-based permissions for league owners
# kickoff
