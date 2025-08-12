ỨNG DỤNG QUẢN LÝ SINH VIÊN VÀ LỚP HỌC
Giới thiệu
Đây là một ứng dụng web cho phép quản lý thông tin sinh viên và lớp học. Hệ thống cung cấp API RESTful để thêm, sửa, xóa, và lấy danh sách dữ liệu từ cơ sở dữ liệu SQL Server. Ứng dụng có thể truy cập qua mạng LAN, hỗ trợ giao tiếp giữa backend Python và frontend HTML/JS.

Công nghệ và thuật toán sử dụng
Python FastAPI – Backend xử lý API server

HTML/CSS/JavaScript – Giao diện người dùng

SQL Server – Lưu trữ dữ liệu sinh viên và lớp

PyODBC – Kết nối và truy vấn dữ liệu

CORS Middleware – Cho phép giao tiếp giữa các domain khác nhau

Luồng xử lý hệ thống
Frontend gửi yêu cầu HTTP (GET/POST/PUT/DELETE) đến API.

Backend nhận request, truy vấn hoặc cập nhật dữ liệu trong SQL Server qua pyodbc.

API trả dữ liệu JSON về cho frontend.

Giao diện hiển thị danh sách sinh viên, lớp học hoặc thông báo kết quả thao tác.

Các chức năng nổi bật
Lấy danh sách tất cả sinh viên và lớp học.

Thêm mới sinh viên.

Tra cứu sinh viên theo mã số.

Hỗ trợ kết nối qua địa chỉ IP trong mạng nội bộ

Giao diện minh họa
GIao diện thêm sinh viên, hiển thị danh sách lớp, danh sách sinh viên
<img width="1821" height="749" alt="image" src="https://github.com/user-attachments/assets/826130db-47b2-4cf7-aedd-4d35881f3235" />
<img width="1835" height="286" alt="image" src="https://github.com/user-attachments/assets/4908a755-6a49-46ef-aeb7-587a1103f4a4" />

Giao diện hiển thị đã thêm sinh viên
<img width="1817" height="580" alt="image" src="https://github.com/user-attachments/assets/14b3d333-e10f-4444-934c-e57a73dea22c" />

Giao diện tra cứu sinh viên
<img width="953" height="456" alt="image" src="https://github.com/user-attachments/assets/7c34fff6-1b21-4b16-869d-fc238171d7b3" />

<img width="875" height="551" alt="image" src="https://github.com/user-attachments/assets/3b90dd2c-f6eb-4c3e-a8fd-0115aa665a2d" />
