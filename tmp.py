import tqdm
from bs4 import BeautifulSoup, NavigableString, Tag
import requests

type_dict = {'thoi-su': ['chinh-tri', 'dan-sinh', 'lao-dong-viec-lam', 'giao-thong', 'mekong', 'quy-hy-vong'],
             'goc-nhin': ['binh-luan-nhieu', 'chinh-tri-chinh-sach', 'y-te-suc-khoe', 'kinh-doanh-quan-tri', 'giao-duc-tri-thuc', 'moi-truong', 'van-hoa-doi-song', 'covid-19', 'tac-gia'],
             'the-gioi': ['tu-lieu', 'phan-tich', 'nguoi-viet-5-chau', 'cuoc-song-do-day', 'quan-su'],
             'kinh-doanh': ['net-zero', 'quoc-te', 'doanh-nghiep', 'chung-khoan', 'ebank', 'vi-mo', 'tien-cua-toi', 'hang-hoa'],
             'bat-dong-san': ['chinh-sach', 'thi-truong', 'du-an', 'khong-gian-song', 'tu-van'],
             'khoa-hoc': ['khoa-hoc-trong-nuoc', 'pii-doi-moi-sang-tao', 'tin-tuc', 'phat-minh', 'ung-dung', 'the-gioi-tu-nhien', 'thuong-thuc'],
             'giai-tri': ['gioi-sao', 'sach', 'video', 'phim', 'nhac', 'thoi-trang', 'lam-dep', 'san-khau-my-thuat'],
             'the-thao': ['bong-da', 'du-lieu-bong-da', 'marathon', 'tennis', 'cac-mon-khac', 'hau-truong'],
             'phap-luat': ['ho-so-pha-an', 'tu-van'],
             'giao-duc': ['tin-tuc', 'tuyen-sinh', 'chan-dung', 'du-hoc', 'thao-luan', 'hoc-tieng-anh', 'giao-duc-40'],
             'suc-khoe': ['tin-tuc', 'cac-benh', 'song-khoe', 'vaccine'],
             'doi-song': ['nhip-song', 'to-am', 'bai-hoc-song', 'cooking', 'tieu-dung'],
             'du-lich': ['diem-den', 'am-thuc', 'dau-chan', 'tu-van', 'cam-nang'],
             'so-hoa': ['cong-nghe', 'san-pham', 'blockchain'],
             'xe': ['thi-truong', 'dien-dan'],
             'y-kien': ['thoi-su', 'doi-song']}

total_page = 1
type = 'so-hoa'
sub_type = ''
i = 1
url = f"https://vnexpress.net/{type}-p{i}" if sub_type == '' else f"https://vnexpress.net/{type}/{sub_type}-p{i}"

content = requests.get(url).content
soup = BeautifulSoup(content, "html.parser")

title_list = soup.find_all(class_="title-news")
print(title_list[0].find_all('a')[0].get("title"))