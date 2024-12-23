from icrawler.builtin import GoogleImageCrawler
import sys

num = int(sys.argv[1])
tag = sys.argv[2]
folder = sys.argv[3]

google_crawler = GoogleImageCrawler(
    parser_threads=2,
    downloader_threads=4,
    storage={'root_dir': folder})

google_crawler.crawl(
    keyword=tag,
    max_num=num, )
