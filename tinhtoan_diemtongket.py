# Bài 1
import typing
"""
format file diem_chitiet.txt:
- Hàng đầu tiên: “Mã HS, Toán , Lý, Hóa, Sinh, Văn, Anh, Sử, Địa”
- Hàng thứ 2 trở đi là bảng điểm chi tiết cho từng sinh viên (tên sinh viên + điểm chi tiết). Các điểm thành phần
 của 1 môn được phân cách bằng dấu phẩy, các môn được phân cách bằng dấu chấm phẩy.
"""
# Params
TU_NHIEN = ['Toán', 'Lý', 'Hóa', 'Sinh']
XA_HOI = ['Văn', 'Anh', 'Sử', 'Địa']


def diemTB_mon(subject, grade):  
    he_so_TN = [.05, .1, .15, .7] 
    he_so_XH = [.05, .1, .1, .15, .6]
    numeric_grade = list(map(float, grade.split(',')))
    he_so_TB = he_so_TN if subject in TU_NHIEN else he_so_XH
    diemTB = sum(map(lambda x, y: x*y, he_so_TB, numeric_grade))
    return round(diemTB, 2)


# Tiêu chí 1
def tinhdiem_trungbinh(path: str) -> typing.Dict:
    output = dict()
    with open(path, encoding="utf-8") as f:
        first_line = next(f) 
        _, *subjects = first_line.replace('\n', '').split(',') # Tách chuỗi, đồng thời loại kí tự xuống dòng
        # Duyệt qua điểm số từng học sinh
        for student in f:
            name, *grades = student.split(';')
            for subject, grade in zip(subjects, grades):
                output[name] = output.get(name, dict()) # Lấy value của key=name, key chưa tồn tại thì mặc định là 1 dict
                output[name][subject] = diemTB_mon(subject, grade)
    return output


# Tiêu chí 2
def luudiem_trungbinh(dest: str, diemTB: typing.Dict) -> None:
    with open(dest, 'w', encoding='utf-8') as f:
        f.write('Mã HS,Toán,Lý,Hóa,Sinh,Văn,Anh,Sử,Địa\n')
        for name in diemTB:
            new_line = [name]
            for subject in TU_NHIEN + XA_HOI:
                new_line.append(diemTB[name][subject])
            f.write(';'.join(map(str, new_line)) + '\n')
    

# Tiêu chí 3
def main():
    path = 'diem_chitiet.txt'
    dest = 'diem_trungbinh.txt'
    diemTB = tinhdiem_trungbinh(path)
    luudiem_trungbinh(dest, diemTB)
    print('Bai 1: OK')
    
    
if __name__ == "__main__":
    main()
    