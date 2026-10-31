import urllib.request
from urllib.error import URLError, HTTPError

URL = "http://127.0.0.1:5000/"

REQUIRED_HEADERS = {
    "Content-Security-Policy": "Restricts which resources the page may load.",
    "X-Content-Type-Options": "Helps prevent MIME-type sniffing.",
    "X-Frame-Options": "Helps prevent the page from being framed.",
    "Referrer-Policy": "Controls referrer information sent by the browser.",
    "Permissions-Policy": "Restricts access to selected browser features.",
}

def main():
    print("DEFENSIVE SECURITY ASSESSMENT")
    print("Target:", URL)
    print("-" * 45)

    request = urllib.request.Request(URL, method="GET")

    try:
        with urllib.request.urlopen(request, timeout=5) as response:
            headers = response.headers
            print("HTTP status:", response.status)
            passed = 0

            for header, purpose in REQUIRED_HEADERS.items():
                if header in headers:
                    print("[PASS]   ", header)
                    passed += 1
                else:
                    print("[REVIEW] ", header, "- not present")
                print("         ", purpose)

            print("-" * 45)
            print(f"Header checks passed: {passed}/{len(REQUIRED_HEADERS)}")
            print("Assessment completed.")
            print("Note: This checks response headers only; it is not a full penetration test.")

    except (URLError, HTTPError, TimeoutError) as error:
        print("Could not reach the local demo application.")
        print("Start app.py first, then run this script.")
        print("Technical detail:", error)

if __name__ == "__main__":
    main()
