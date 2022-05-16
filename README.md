Cho thông tin file bảng điểm chi tiết của các học sinh trong lớp các môn học liên quan đến việc thi đại học như sau: Toán, Lý, Hóa, Sinh, Văn, Anh, Sử, Địa. Mỗi một môn học tự nhiên có 4 đầu điểm: Điểm kiểm tra miệng, kiểm tra 15 phút, kiểm tra 1 tiết, thi cuối kỳ (5/10/15/70). Mỗi 1 môn học xã hội có 5 đầu điểm: Điểm chuyên cần, điểm bài luận, kiểm tra 1 tiết, kiểm tra 2 tiết, thi cuối kỳ (5, 10, 10, 15, 60).

Hãy viết một chương trình thực hiện các nhiệm vụ sau:

- Load dữ liệu bảng điểm chi tiết vào.

- Tính điểm tổng kết trung bình cho từng môn.

- Xếp loại học lực của học sinh (trung bình, trung bình khá, khá, giỏi dựa vào điểm tổng kết trung bình của học sinh).

- Đưa ra đánh giá sơ bộ về kết quả thi đại học dự kiến của học sinh thuộc loại nào (loại 1, loại 2, loại 3) theo các khối: A, A1, B, C, D dựa trên điểm tổng kết trung bình cho từng môn.

***

Hướng dẫn

Bài 1:

Hãy viết 1 chương trình “tinhtoan_diemtongket.py” có các hàm sau:

a. Hàm tinhdiem_trungbinh: 

Yêu cầu: Tính toán toàn bộ điểm trung bình của sinh viên theo từng môn học.

Input: Đường dẫn bảng điểm chi tiết cho từng môn của tất cả học sinh lưu trong file “diem_chitiet.txt”.

Chi tiết:

- Load bảng điểm chi tiết vào. Định dạng bảng điểm chi tiết sau khi load vào: Tùy chọn.

- Hàng đầu tiên gồm các đề mục: “Mã HS, Toán , Lý, Hóa, Sinh, Văn, Anh, Sử, Địa”. Hàng thứ 2 trở đi là bảng điểm chi tiết cho từng sinh viên (tên sinh viên + điểm chi tiết). Mỗi môn học tự nhiên có 4 đầu điểm, mỗi môn học xã hội có 5 đầu điểm. Các điểm thành phần của 1 môn được phân cách bằng dấu phẩy, các môn được phân cách bằng dấu chấm phẩy.

- Tỉ lệ điểm thành phần cho các môn tự nhiên (Toán, Lý, Hóa, Sinh): Điểm kiểm tra miệng, kiểm tra 15 phút, kiểm tra 1 tiết, thi cuối kỳ (5%, 10%, 15%, 70%).

- Tỉ lệ điểm thành phần cho các môn xã hội (Anh, Văn, Sử, Địa): Điểm chuyên cần, điểm bài luận, kiểm tra 1 tiết, kiểm tra 2 tiết, thi cuối kỳ (5%, 10%, 10%, 15%, 60%).

- Điểm trung bình của từng môn sẽ được tính toán theo tỉ lệ điểm thành phần được quy định ở trên, kết quả làm tròn đến 2 chữ số. VD: Diem_TB_Toan_SVA = 5% * kiem_tra_mieng + 10% * kiem_tra_15 + 15% * kiem_tra_1tiet + 70% * thi_cuoi_ky.

Output: 1 dictionary  lớn theo format sau:

{‘Ma HS’: {‘Mon hoc’: Điểm TB} (‘Ma HS’ thay bằng mã học sinh, ‘Mon hoc’ thay thế bằng tên môn học, Điểm TB thay thế bằng điểm TB của môn đấy).

VD: {‘Nguyen Hai Nam’: {‘Toan’: 9.00; ‘Ly’: 8.55, …}, ‘Ha Thi Hoa’: {…‘Su’: 9.00; ‘Dia’: 8.55}}

- Điểm TB được làm tròn đến 2 chữ số.

- Mỗi học sinh (trong các dictionary nhỏ) phải có điểm của tất cả 8 môn học.

b. Ham luudiem_trungbinh: 

Yêu cầu: Lưu điểm trung bình ra 1 file có tên là “diem_trungbinh.txt” theo đường dẫn có sẵn.

Input: 

- Output dictionary của hàm tinhdiem_trungbinh.

- Đường dẫn thư mục của bảng điểm trung bình.

Chi tiết: 

- Các điểm thành phần sẽ được thay thế bằng điểm trung bình, các điểm trung bình của các môn khác nhau được phân cách nhau bằng dấu chấm phẩy.

- Chú ý: Hàng đầu tiên của file “diem_trungbinh.txt” giữ nguyên như của “diem_chitiet.txt”, các điểm TB cho mỗi học sinh phải được sắp xếp theo trình tự các môn học của hàng đầu tiên.

Output: Lưu bảng điểm ra 1 file “diem_trungbinh.txt” theo đường dẫn input, format giống với “diem_chitiet.txt”

c. Hàm main():

Yêu cầu:

- Khai báo đường dẫn cho input file – “diem_chitiet.txt”.

- Khai báo đường dẫn cho output file – “diem_trungbinh.txt”.

- Chạy hàm tinhdiem_trungbinh.

- Chạy hàm luudiem_trungbinh.

- Chú ý: Hàm main cần được chạy khi gọi đến chương trình “tinhtoan_diemtongket.py”.

Bài 2: 

Hãy viết 1 chương trình “danhgia_diemtongket.py” có các hàm sau:

a. Hàm xeploai_hocsinh:

Yêu cầu: Xếp loại học lực chuẩn của học sinh dựa vào điểm tổng kết trung bình chuẩn.

Input: 

- Đường dẫn file “diem_trungbinh.txt”.

Output:

- 1 dictionary  lớn theo format sau: {‘Ma HS’: Xep loai} (‘Ma HS’ thay bằng mã học sinh, Xep loai thay thế bằng xếp loại cho học sinh đấy – “Xuat sac/Gioi/Kha/TB kha/TB).

Chi tiết: 

Điểm tổng kết trung bình chuẩn được tính như sau:

- Các môn toán, văn, anh hệ số 2.0, các môn lý, hóa, sinh, sử, địa hệ số 1.0.

 Công thức tính: dtb_chuan = ((dtb_toán + dtb_văn + dtb_anh) * 2.0 + (dtb_ly + dtb_hoa + dtb_sinh + dtb_su + dtb_dia) * 1.0) / 11.0

Học viên được xếp loại học lực chuẩn như sau:

- Học sinh xuất sắc: Điểm TB chuẩn trên 9.0, không có môn nào điểm TB thấp hơn 8.0.

 Mã xếp loại: Xuat sac.

- Học sinh giỏi: Điểm TB chuẩn trên 8.0, không có môn nào điểm TB thấp hơn 6.5.

 Mã xếp loại: Gioi.

- Học sinh khá: Điểm TB chuẩn trên 6.5, không có môn nào điểm TB thấp hơn 5.0.

 Mã xếp loại: Kha.

- Học sinh  trung bình khá: Điểm TB chuẩn trên 6.0, không có môn nào điểm TB thấp hơn 4.5.

 Mã xếp loại: TB kha.

- Học sinh trung bình: Các trường hợp còn lại.

 Mã xếp loại: TB.

b. Hàm xeploai_thidaihoc_hocsinh:

Yêu cầu: Phân loại năng lực các học sinh theo khối thi đại học dựa vào điểm tổng kết trung bình.

Input: 

- Đường dẫn thư mục “diem_trungbinh.txt”.

Output:

- 1 dictionary  lớn theo format sau: {‘Ma HS: [Xep loai]} (‘Ma HS’ thay bằng mã học sinh, Xep loai là một list thay thế bằng xếp loại cho học sinh đấy ở từng khối theo trình tự [A, A1, B, C, D]). VD: {‘Nguyen Hai Nam’: [1, 1, 1, 3, 2]}

Chi tiết:

- Có tất cả 5 khối: A (Toán, Lý Hóa), A1(Toán, Lý, Anh),  B(Toán, Hóa, Sinh), C(Văn, Sử Địa), D(Toán, Văn, Anh).

- Ở khối tự nhiên (A, A1, B), sinh viên sẽ được xếp thành 4 loại năng lực:

+ Loại 1: Tổng điểm TB môn của 3 môn trong khối >= 24.

+ Loại 2: Tổng điểm TB môn của 3 môn trong khối < 24 và >= 18.

+ Loại 3: Tổng điểm TB môn của 3 môn trong khối < 18 và >= 12.

+ Loại 4: Tổng điểm TB môn của 3 môn trong khối < 12.

- Ở khối xã hội (C), 4 loại năng lực sẽ được xếp tương tự như các khối tự nhiên nhưng ở các mức điểm khác: Loại 1 (>=21), loại 2(<21 và >=15), loại 3(<15 và >=12), loại 4(<12).

- Ở khối cơ bản (D): Loại 1(>=32), loại 2(<32 và >=24), loại 3(<24 và >=20), loại 4(<20) với điểm tiếng Anh có hệ số nhân đôi.

c. Hàm main:

Output: Lưu bảng điểm ra 1 file “danhgia_hocsinh.txt”.

Yêu cầu: Khai báo đường dẫn input cho file “diem_ trungbinh.txt” và output cho file “danhgia_hocsinh.txt”, thực thi 2 hàm ở trên và lưu kết quả vào file  “danhgia_hocsinh.txt”.

Chi tiết:

- Thực thi 2 hàm xeploai_hocsinh và xeploai_thidaihoc_hocsinh.

- Hàng đầu tiên của file “danhgia_hocsinh.txt” gồm các trường: “Ma HS”, “xeploai_TB chuan”, “xeploai_A”, “xeploai_A1”, “xeploai_B ”, “xeploai_C”, xeploai_D”. Hàng thứ 2 theo VD sau: “Nguyen Hai Nam; Gioi; 1; 1; 1; 3; 2”.

- Chú ý: Hàm main cần được chạy khi gọi đến chương trình “danhgia_diemtongket.py”.


