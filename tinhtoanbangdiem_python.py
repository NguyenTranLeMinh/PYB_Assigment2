import os, psutil
process = psutil.Process(os.getpid())
memory1 = process.memory_info().rss / 1024 ** 2
print(memory1)  # in M bytes 

class BANGDIEM:
    def __init__(self):
        self.subjects = ['Toán','Lý','Hóa','Sinh','Văn','Anh','Sử','Địa']
        self.students = dict() # {name: {subject1: ..., subject2: ...}, ...}
        self.TB_mon = dict()
        #self.grades = ['Điểm chi tiết', 'Điểm TB môn']
        self.TN = ['Toán', 'Lý', 'Hóa', 'Sinh']
        self.XH = ['Văn', 'Anh', 'Sử', 'Địa']

    def load_dulieu(self, path: str):
        with open(path, encoding='utf-8') as f:
            next(f)
            for line in f:
                name, *grades = line.split(';')
                for subject, grade in zip(self.subjects, grades):
                    self.students[name] = self.students.get(name, dict())
                    self.students[name][subject] = list(map(float, grade.split(',')))
        
    def tinhdiem_trungbinh(self):
        he_so_TN = [.05, .1, .15, .7] 
        he_so_XH = [.05, .1, .1, .15, .6]
        for name in self.students:
            for subject in self.subjects:
                he_so = he_so_TN if subject in self.TN else he_so_XH
                info = self.students[name][subject]
                #info = round(sum(map(lambda x, y: x*y, he_so, info[self.grades[0]])), 2)
                diem_TB = round(sum(map(lambda x, y: x*y, he_so, info)), 2)
                self.TB_mon[name] = self.TB_mon.get(name, dict())
                self.TB_mon[name][subject] = diem_TB

    def luudiem_trungbinh(self, dest: str):
        with open(dest, 'w', encoding='utf-8') as f:
            f.write('Mã HS,' + ','.join(self.subjects) + '\n')
            for name in self.students:
                f.write(';'.join([name] + \
                    [str(self.TB_mon[name][subject]) for subject in self.subjects]) + '\n')

    def get_TB_mon(self):
        return self.TB_mon

class DANHGIA(BANGDIEM):
    def __init__(self):
        super().__init__()
        self.ma_xep_loai = {'Xuất sắc': [9., 8.], 'Giỏi': [8., 6.5], 'Khá': [6.5, 5.], 'TB Khá': [6., 4.5], 'TB': [-1., -1]}
        self.khoi_thi = {'A': ['Toán', 'Lý', 'Hóa'], 
                        'A1': ['Toán', 'Lý', 'Anh'], 
                        'B': ['Toán', 'Hóa', 'Sinh'], 
                        'C': ['Văn', 'Sử', 'Địa'], 
                        'D': ['Toán', 'Văn', 'Anh']}

    def xeploai_hocsinh(self):
        for name, info in self.students.items():
            TB_mon = []
            for subject in self.subjects:
                TB_mon.append(self.TB_mon[name][subject])
            dtb_chuan = sum([2. * s for s in TB_mon[:3]] + TB_mon[3:]) / 11.
            dk_xep_loai = lambda threshold: \
                [dtb_chuan > float(threshold[0]), all(map(lambda x: x >= float(threshold[1]), TB_mon))]
            for xep_loai, threshold in self.ma_xep_loai.items():
                if (all(dk_xep_loai(threshold))):
                    self.students[name]['Xếp loại'] = xep_loai
                    break   
    
    def get_Xeploai(self):
        return {name: self.students[name]['Xếp loại'] for name in self.students}

    def xeploai_thidaihoc_hocsinh(self):
        for name, info in self.students.items():
            self.students[name]['Xếp loại thi ĐH'] = list()
            #TB_mon = dict()
            #for subject in self.subjects:
            #    TB_mon[subject] = info[subject][self.grades[1]]     
            TB_mon = self.TB_mon[name]       
            for khoi, mon in self.khoi_thi.items():
                if khoi in ('A', 'A1', 'B'):
                    diemTB_khoi = sum([TB_mon[subject] for subject in mon])
                    loai_nang_luc = lambda x: [x >= 24, 18 <= x < 24, 12 <= x < 18, x < 12]
                elif khoi == 'C':
                    diemTB_khoi = sum([TB_mon[subject] for subject in mon])
                    loai_nang_luc = lambda x: [x >= 21, 15 <= x < 21, 12 <= x < 15, x < 12]
                elif khoi == 'D':
                    diemTB_khoi = sum([2.*TB_mon[subject] if subject == 'Anh' \
                                        else TB_mon[subject] for subject in mon])
                    loai_nang_luc = lambda x: [x >= 32, 24 <= x < 32, 20 <= x < 24, x < 20]
                self.students[name]['Xếp loại thi ĐH'].append(loai_nang_luc(diemTB_khoi).index(True) + 1)

    def luu_danhgia(self, dest: str):
        with open(dest, 'w', encoding='utf-8') as f:
            f.write('Ma HS,xeploai_TB chuan,xeploai_A,xeploai_A1,xeploai_B,xeploai_C,xeploai_D\n')
            for name, info in self.students.items():
                new_line = [name, info['Xếp loại']] + list(map(str, info['Xếp loại thi ĐH']))
                f.write(';'.join(new_line) + '\n')

class TUNHIEN(DANHGIA):
    def __init__(self, TBmon):
        super().__init__()
        self.TB_mon = TBmon
        self.xeploai_khoithi = dict()
        self.khoi_TN = {'A': self.khoi_thi['A'], 
                        'A1': self.khoi_thi['A1'], 
                        'B': self.khoi_thi['B']}
        self.loai_nang_luc = lambda x: [x >= 24, 18 <= x < 24, 12 <= x < 18, x < 12]
    
    def xeploai_thidaihoc_hocsinh(self):
        for name, grades in self.TB_mon.items():
            #self.students[name]['Xếp loại thi ĐH'] = list()
            for khoi, cac_mon in self.khoi_TN.items():
                diemTB_khoi = sum([grades[subject] for subject in cac_mon])
                self.xeploai_khoithi[name] = self.xeploai_khoithi.get(name, list())
                self.xeploai_khoithi[name].append(self.loai_nang_luc(diemTB_khoi).index(True) + 1)

    def get_Xeploai_khoithi(self):
        return self.xeploai_khoithi

class XAHOI(DANHGIA):
    def __init__(self, TBmon):
        super().__init__()
        self.TB_mon = TBmon
        self.xeploai_khoithi = dict()
        self.khoi_XH = {'C': self.khoi_thi['C']}
        self.loai_nang_luc = lambda x: [x >= 21, 15 <= x < 21, 12 <= x < 15, x < 12]
    
    def xeploai_thidaihoc_hocsinh(self):
        for name, grades in self.TB_mon.items():
            #self.students[name]['Xếp loại thi ĐH'] = list()
            for khoi, cac_mon in self.khoi_XH.items():
                diemTB_khoi = sum([grades[subject] for subject in cac_mon])
                self.xeploai_khoithi[name] = self.xeploai_khoithi.get(name, list())
                self.xeploai_khoithi[name].append(self.loai_nang_luc(diemTB_khoi).index(True) + 1)

    def get_Xeploai_khoithi(self):
        return self.xeploai_khoithi


class COBAN(DANHGIA):
    def __init__(self, TBmon):
        super().__init__()
        self.TB_mon = TBmon
        self.xeploai_khoithi = dict()
        self.khoi_CB = {'D': self.khoi_thi['D']}
        self.loai_nang_luc = lambda x: [x >= 32, 24 <= x < 32, 20 <= x < 24, x < 20]
    
    def xeploai_thidaihoc_hocsinh(self):
        for name, grades in self.TB_mon.items():
            #self.students[name]['Xếp loại thi ĐH'] = list()
            for khoi, cac_mon in self.khoi_CB.items():
                diemTB_khoi = sum([2.*grades[subject] if subject == 'Anh' \
                                        else grades[subject] for subject in cac_mon])
                self.xeploai_khoithi[name] = self.xeploai_khoithi.get(name, list())
                self.xeploai_khoithi[name].append(self.loai_nang_luc(diemTB_khoi).index(True) + 1)
    
    def get_Xeploai_khoithi(self):
        return self.xeploai_khoithi





if __name__ == "__main__":
    # paths
    path = 'diem_chitiet.txt'
    dest_diem = 'diem_trungbinh.txt'
    dest_danhgia = 'danhgia_hocsinh.txt'
    
    # ĐIểm TB và Xếp loại học lực
    obj = DANHGIA()
    obj.load_dulieu(path)
    obj.tinhdiem_trungbinh()
    obj.luudiem_trungbinh(dest_diem)
    obj.xeploai_hocsinh()
    #obj.xeploai_thidaihoc_hocsinh()
    #obj.luu_danhgia(dest_danhgia)

    TB = obj.get_TB_mon()

    # Xếp loại thi ĐH
    khoi_TN = TUNHIEN(TB)
    khoi_TN.xeploai_thidaihoc_hocsinh()

    khoi_XH = XAHOI(TB)
    khoi_XH.xeploai_thidaihoc_hocsinh()

    khoi_CB = COBAN(TB)
    khoi_CB.xeploai_thidaihoc_hocsinh()

    # Lưu xếp loại thi ĐH
    with open(dest_danhgia, 'w', encoding='utf-8') as f:
        f.write('Ma HS,xeploai_TB chuan,xeploai_A,xeploai_A1,xeploai_B,xeploai_C,xeploai_D\n')
        for name, grades in khoi_TN.get_Xeploai_khoithi().items():
            new_line = [name, obj.get_Xeploai()[name]] + grades + khoi_XH.get_Xeploai_khoithi()[name] + khoi_CB.get_Xeploai_khoithi()[name]
            f.write(';'.join(map(str, new_line)) + '\n')
    
    print('OK')
    #process = psutil.Process(os.getpid())
    memory2 = process.memory_info().rss / 1024 ** 2
    print(memory2)  # in M bytes 
    print('Diff: ', memory2 - memory1)
    