# Entries

**Version:** 0.0.1

Entries is an open-source, entry-topic based content sharing platform built with Flask.

## Setup

```bash
git clone "https://github.com/scandnk52/entries.git"
cd "entries"
```

### Create virtual environment
```bash
python -m venv venv
```

### Enter the virtual environment
```bash
source venv/bin/activate  # macOS/Linux
```
```bash
venv\Scripts\activate     # Windows
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Copy environment variables
```bash
cp .env.example .env
```

### Run database migrations
```bash
flask db upgrade
```

### Run the application
```bash
python run.py
```

## Additional Notes

These features have not been added.

- Moderation
- Rich text editor
- Saved posts
- Tags
- Likes / Upvote & Downvote
- Ranking algorithm
- Advanced search
- Detailed pagination
- Direct messaging
- Notifications
- Follow system
- Rate limiting & security
- Admin panel
- Meta tags
- RSS & Robots.txt
- Multi-language support
- Tests
- Logging
- Dark / Light mode
