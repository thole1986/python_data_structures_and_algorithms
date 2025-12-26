import requests
import re

class WebCrawler:
    def __init__(self):
        # Danh sách lưu tất cả website đã được phát hiện
        self.discovered_websites = []

    def crawl(self, start_url):
        # Hàng đợi dùng cho BFS (Breadth-First Search)
        queue = [start_url]

        # Đánh dấu website đầu tiên là đã phát hiện
        self.discovered_websites.append(start_url)

        # Lặp cho đến khi hàng đợi rỗng
        while queue:
            # Lấy URL đầu tiên trong hàng đợi
            actual_url = queue.pop(0)

            # In ra URL đang crawl
            print(actual_url)

            # Đọc HTML của trang web hiện tại
            actual_url_html = self.read_raw_html(actual_url)

            # Lấy tất cả link trong HTML
            for url in self.get_links_from_html(actual_url_html):
                # Nếu link chưa từng được phát hiện
                if url not in self.discovered_websites:
                    # Thêm vào danh sách đã phát hiện
                    self.discovered_websites.append(url)

                    # Thêm vào hàng đợi để crawl sau
                    queue.append(url)

    def get_links_from_html(self, raw_html):
        # Dùng regex để tìm tất cả URL trong HTML
        return re.findall(
            r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+",
            raw_html
        )

    def read_raw_html(self, url):
        raw_html = ''
        try:
            # Gửi request GET và lấy nội dung HTML
            raw_html = requests.get(url).text
        except Exception:
            # Nếu có lỗi (timeout, SSL, 403...)
            pass
        return raw_html

if __name__ == '__main__':
    # Tạo đối tượng crawler
    crawler = WebCrawler()

    # Bắt đầu crawl từ CNN
    crawler.crawl('https://www.cnn.com')
