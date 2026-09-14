# 🎬 Movie Recommendation System

Hệ thống gợi ý phim dựa trên nội dung (**Content-Based Filtering**), sử dụng độ tương đồng cosine giữa các bộ phim để đề xuất những phim có nội dung/thể loại tương tự với phim người dùng chọn. Ứng dụng được xây dựng bằng **Streamlit**, mang lại giao diện web tương tác đơn giản, dễ sử dụng.

## 🖼️ Demo

![Demo](assets/web_demo.png)

Người dùng chọn phim từ dropdown → bấm **Show Recommend** → hệ thống hiển thị danh sách các phim tương tự kèm poster.

## 📌 Tính năng

- Tìm kiếm và chọn một bộ phim từ danh sách có sẵn
- Gợi ý các bộ phim tương tự dựa trên nội dung (tóm tắt, thể loại, diễn viên, đạo diễn...)
- Giao diện web trực quan, dễ thao tác nhờ Streamlit
- Giao diện được tùy chỉnh thêm bằng CSS riêng

## 🗂️ Cấu trúc project

```
Movie-Recommendation-System/
├── .streamlit/
│   └── secrets.toml          # Lưu các khóa API / thông tin nhạy cảm (không commit lên Git)
├── assets/
│   └── style.css             # CSS tùy chỉnh giao diện Streamlit
├── dataset/
│   └── movies.csv            # Dữ liệu gốc chứa thông tin phim
├── notebooks/
│   └── experiment.ipynb      # Notebook thử nghiệm, xử lý dữ liệu và xây dựng mô hình
├── src/
│   └── recommender.py        # Logic chính xử lý gợi ý phim
├── app.py                    # File chạy ứng dụng Streamlit
├── movies_list.pkl           # Danh sách phim đã xử lý (pickle)
├── similarity.pkl            # Ma trận độ tương đồng giữa các phim (pickle)
├── .gitignore
└── README.md
```

## ⚙️ Cài đặt

### 1. Clone repository

```bash
git clone https://github.com/<username>/Movie-Recommendation-System.git
cd Movie-Recommendation-System
```

### 2. Tạo môi trường ảo (khuyến nghị)

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

### 3. Cài đặt các thư viện cần thiết

```bash
pip install -r requirements.txt
```


## 🔑 Cấu hình

Nếu ứng dụng có gọi API bên ngoài (ví dụ TMDB API để lấy poster phim), tạo file `.streamlit/secrets.toml` với nội dung:

```toml
TMDB_API_KEY = "your_api_key_here"
```

## ▶️ Chạy ứng dụng

```bash
streamlit run app.py
```

Sau khi chạy, ứng dụng sẽ mở tại `http://localhost:8501`.

## 🧠 Cách hoạt động

1. **Tiền xử lý dữ liệu** (`notebooks/experiment.ipynb`): Dữ liệu từ `dataset/movies.csv` được làm sạch, trích xuất đặc trưng (thể loại, từ khóa, diễn viên, đạo diễn, tóm tắt...) và chuyển thành vector.
2. **Tính độ tương đồng**: Sử dụng **Cosine Similarity** để tính độ tương đồng giữa các phim, lưu kết quả vào `similarity.pkl`.
3. **Gợi ý phim** (`src/recommender.py`): Khi người dùng chọn một phim, hệ thống tra cứu ma trận tương đồng và trả về top các phim gần giống nhất.
4. **Giao diện** (`app.py`): Hiển thị danh sách phim, cho phép chọn phim và xem kết quả gợi ý trực quan.

## 📊 Dataset

File `dataset/movies.csv` chứa thông tin các bộ phim dùng để huấn luyện mô hình gợi ý (ví dụ: tiêu đề, thể loại, tóm tắt, diễn viên, đạo diễn...).

## 🛠️ Công nghệ sử dụng

- **Python**
- **Streamlit** – xây dựng giao diện web
- **Pandas / NumPy** – xử lý dữ liệu
- **Scikit-learn** – tính toán độ tương đồng (Cosine Similarity)
- **Pickle** – lưu trữ mô hình đã huấn luyện

## ⚠️ Xử lý sự cố (Troubleshooting)

### Poster phim không hiển thị / lỗi khi gọi TMDB API

Ở một số khu vực hoặc mạng ISP, các domain của TMDB (`api.themoviedb.org`, `image.tmdb.org`) có thể bị chặn, khiến ứng dụng không lấy được poster hoặc bị lỗi timeout/connection error khi gọi API.

**Cách khắc phục:**
- Bật **VPN** (đổi sang server ở nước khác) rồi chạy lại ứng dụng
- Hoặc đổi DNS (ví dụ dùng `1.1.1.1` hoặc `8.8.8.8`) trong một số trường hợp cũng giúp truy cập được
- Nếu deploy trên server/cloud, kiểm tra xem firewall/network của nhà cung cấp có chặn outbound request tới TMDB không

> Đây là hạn chế từ phía mạng/nhà cung cấp, không phải lỗi từ code của ứng dụng.

## 🚀 Hướng phát triển

- Thêm poster phim qua TMDB API
- Bổ sung gợi ý dựa trên đánh giá người dùng (Collaborative Filtering)
- Triển khai (deploy) ứng dụng lên Streamlit Cloud / Render / Heroku
- Thêm chức năng tìm kiếm nâng cao, lọc theo thể loại/năm phát hành


## 🙋‍♂️ Tác giả

- Phạm Trung Chính – [GitHub](https://github.com/chinh1809z)
