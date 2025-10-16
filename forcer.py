import requests
import concurrent.futures

BASE_URL = "PASTE YOUR LINK HERE / REMOVED FOR SAFETY REASONS"
WORDLIST_FILE = "list.txt"
THREADS = 20  # Number of concurrent threads

def scan_url(word):
	word = word.strip()
	if not word:
		return

	urls = {
		f"{BASE_URL}{word}/",
		f"{BASE_URL}{word}"
	}
	
	for url in urls:

		try:
			response = requests.get(url, timeout=5)
			status = response.status_code
			if status in (200, 401, 403):  # Only print correct pages
				print(f"[{status}] {url}")
		except requests.RequestException:
			pass  # Ignore errors

def main():
	with open(WORDLIST_FILE, 'r') as file:
		words = file.readlines()

	with concurrent.futures.ThreadPoolExecutor(max_workers=THREADS) as executor:
		executor.map(scan_url, words)  # Scan URLs

if __name__ == "__main__":
	main()
