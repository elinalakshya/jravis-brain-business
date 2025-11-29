# Stream run intervals in seconds
# 300 sec = 5 min

STREAM_INTERVALS = {
    1: 300,   # Printify POD
    2: 300,   # Meshy AI Store
    3: 360,   # Creative Market Templates
    4: 300,   # YouTube Scripts
    5: 420,   # Stock Images/Videos
    6: 600,   # KDP Books
    7: 420,   # Shopify Digital Products
    8: 360,   # Affiliate Blog
    9: 480,   # SaaS Micro Tools
    10: 720,  # Webflow Templates
    11: 900,  # Course Automation
    12: 360   # Micro-Niche Affiliate Sites
}

import os
BACKEND_URL = "https://jravis-backend.onrender.com"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MESHY_API_KEY = os.getenv("MESHY_API_KEY")
PRINTIFY_API_KEY = os.getenv("PRINTIFY_API_KEY")
GUMROAD_TOKEN = os.getenv("GUMROAD_ACCESS_TOKEN")
PAYHIP_API_KEY = os.getenv("PAYHIP_API_KEY")
