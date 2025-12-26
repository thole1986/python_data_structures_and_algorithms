import requests
import re
from collections import deque

class WebCrawler:
    def __init__(self, max_pages=50):
        """
        max_pages: số lượng trang tối đa được phép crawl
        """
        # Set dùng để lưu các website đã crawl (tránh trùng lặp, rất nhanh)
        self.visited_urls = set()

        # Giới hạn số trang crawl
        self.max_pages = max_pages

        # Header giả lập trình duyệt thật để tránh bị chặn
        self.headers = {
            "User-Agent": "Mozilla/5.0 (compatible; SimpleCrawler/1.0)"
        }

    def crawl(self, start_url):
        """
        Crawl website theo thuật toán BFS (Breadth-First Search)
        """
        # Hàng đợi BFS (deque nhanh hơn list)
        queue = deque([start_url])

        # Đánh dấu URL đầu tiên đã được visit
        self.visited_urls.add(start_url)

        # Lặp cho đến khi:
        # - Hết URL để crawl
        # - Hoặc đạt giới hạn max_pages
        while queue and len(self.visited_urls) < self.max_pages:
            # Lấy URL đầu tiên trong hàng đợi
            current_url = queue.popleft()
            print(f"Crawling: {current_url}")

            # Đọc HTML của trang hiện tại
            html = self.read_raw_html(current_url)
            if not html:
                continue

            # Lấy tất cả link từ HTML
            links = self.get_links_from_html(html)

            for link in links:
                # Nếu link chưa từng crawl và chưa vượt giới hạn
                if link not in self.visited_urls:
                    self.visited_urls.add(link)
                    queue.append(link)

                    # Nếu đã đạt giới hạn thì dừng luôn
                    if len(self.visited_urls) >= self.max_pages:
                        break

    def get_links_from_html(self, html):
        """
        Trích xuất tất cả URL (http/https) từ HTML bằng regex
        """
        url_pattern = r"https?://[^\s\"\'<>]+"
        return re.findall(url_pattern, html)

    def read_raw_html(self, url):
        """
        Gửi HTTP GET request và trả về HTML
        """
        try:
            response = requests.get(
                url,
                headers=self.headers,
                timeout=5  # tránh treo chương trình
            )

            # Chỉ xử lý khi request thành công
            if response.status_code == 200:
                return response.text

        except requests.exceptions.RequestException as e:
            # Có thể log lỗi nếu muốn
            print(f"  Lỗi khi truy cập {url}")
            return None

        return None


if __name__ == "__main__":
    # Tạo crawler với giới hạn 30 trang
    crawler = WebCrawler(max_pages=30)
    # Bắt đầu crawl
    crawler.crawl("https://www.cnn.com")
