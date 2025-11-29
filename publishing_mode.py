# JRAVIS-BRAIN — Publishing Mode Controller
import time
import requests
import random
from config import BACKEND_URL

STREAMS = [
    ("printify_pod", "daily_pod_designs"),
    ("meshy_assets", "3d_asset"),
    ("gumroad_upload", "digital_product"),
    ("payhip_upload", "digital_pack"),
    ("creative_market", "template_bundle"),
    ("youtube_automation", "video_script"),
    ("stock_media", "stock_prompts"),
    ("kdp_books", "book_outline"),
    ("shopify_digital_products", "digital_items"),
    ("affiliate_blog", "seo_articles"),
    ("course_automation", "course"),
    ("micro_niche_sites", "affiliate_page")
]


def send_task(stream_type, content):
    task = {
        "type": stream_type,
        "action": "publish",     # IMPORTANT
        "mode": "production",
        "content": content
    }
    try:
        r = requests.post(f"{BACKEND_URL}/task/new", json=task)
        print("➡️ Sent publish task:", task)
        print("⬅️ Backend Response:", r.text)
    except Exception as e:
        print("❌ Failed sending task:", e)


def run_publishing_loop():
    print("🔥 JRAVIS BRAIN — PUBLISH MODE ACTIVATED")
    print("🤖 All publishing tasks will now run 24/7")

    while True:
        stream = random.choice(STREAMS)
        send_task(stream[0], stream[1])

        wait = random.uniform(5, 12)
        print(f"⏳ Waiting {wait:.2f}s before next publish…\n")
        time.sleep(wait)


if __name__ == "__main__":
    run_publishing_loop()
