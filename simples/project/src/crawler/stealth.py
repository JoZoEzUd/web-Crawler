import random
import time

UA = [
    "Mozilla/5.0", 
    "Chrome/120.0", 
    "Safari/605.1.15"
]

def stealth_delay():
    time.sleep(random.uniform(1.0, 3.0))

def stealth_headers():
    return {"User-Agent": random.choice(UA)}