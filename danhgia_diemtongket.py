# Bài 2
import typing


def xeploai_hocsinh(path='diem_trungbinh.txt') -> typing.Dict:
    output = dict() # format {‘Ma HS’: Xep loai, ...}
    ma_xep_loai = {'Xuất sắc': [9., 8.], 'Giỏi': [8., 6.5], 'Khá': [6.5, 5.], 'TB Khá': [6., 4.5], 'TB': [-1., -1]}
    with open(path, encoding='utf-8') as f:
        next(f) # Bỏ qua dòng input đầu
        for student in f:
            name, *grades = student.split(';')
            numeric_grades = list(map(float, grades))
            dtb_chuan = sum([2. * s for s in numeric_grades[:3]] + numeric_grades[3:]) / 11.
            dk_xep_loai = lambda threshold: \
                [dtb_chuan > float(threshold[0]), all(map(lambda x: x >= float(threshold[1]), numeric_grades))]
            for xep_loai, threshold in ma_xep_loai.items():
                if (all(dk_xep_loai(threshold))):
                    output[name] = xep_loai
                    break           
    return output
                       

def xeploai_thidaihoc_hocsinh(path='diem_trungbinh.txt') -> typing.Dict:
    output = dict() # format {‘Ma HS: [Xep loai],...}
    khoi_thi = {'A': ['Toán', 'Lý', 'Hóa'], 
            'A1': ['Toán', 'Lý', 'Anh'], 
            'B': ['Toán', 'Hóa', 'Sinh'], 
            'C': ['Văn', 'Sử', 'Địa'], 
            'D': ['Toán', 'Văn', 'Anh']}
    with open(path, encoding='utf-8') as f:
        _, *subjects = next(f).replace('\n', '').split(',')
        for student in f:
            name, *grades = student.split(';')
            numeric_grades = list(map(float, grades))
            grades_dict = {subject: grade for subject, grade in zip(subjects, numeric_grades)}
            output[name] = list()
            for khoi, mon in khoi_thi.items():
                if khoi in ('A', 'A1', 'B'):
                    diemTB_khoi = sum([grades_dict[subject] for subject in mon])
                    loai_nang_luc = lambda x: [x >= 24, 18 <= x < 24, 12 <= x < 18, x < 12]
                elif khoi == 'C':
                    diemTB_khoi = sum([grades_dict[subject] for subject in mon])
                    loai_nang_luc = lambda x: [x >= 21, 15 <= x < 21, 12 <= x < 15, x < 12]
                elif khoi == 'D':
                    diemTB_khoi = sum([2.*grades_dict[subject] if subject == 'Anh' else grades_dict[subject]\
                                        for subject in mon])
                    loai_nang_luc = lambda x: [x >= 32, 24 <= x < 32, 20 <= x < 24, x < 20]
                output[name].append(loai_nang_luc(diemTB_khoi).index(True) + 1)
        return output


def main():
    path = 'diem_trungbinh.txt'
    dest = 'danhgia_hocsinh.txt'
    xeploai_TBchuan = xeploai_hocsinh(path)
    xeploai_khoithi = xeploai_thidaihoc_hocsinh(path)
    with open(dest, 'w', encoding='utf-8') as f:
        first_line = 'Ma HS,xeploai_TB chuan,xeploai_A,xeploai_A1,xeploai_B,xeploai_C,xeploai_D\n'
        f.write(first_line)
        for name in xeploai_TBchuan:
            new_line = [name, xeploai_TBchuan[name]] + xeploai_khoithi[name]
            f.write(';'.join(map(str, new_line)) + '\n')
    
    print('Bai 2: OK')


if __name__ == "__main__":
    main()