list_emp = [
    {
        "id": "NV001",
        "name": "Nguyen Van A",
        "salary_per_day": 400000,
        "work_day": 25,
        "benefit": 1500000,
        "total": 11500000,
        "type": "Trung bình"
    },
    {
        "id": "NV002",
        "name": "Nguyen Van B",
        "salary_per_day": 300000,
        "work_day": 26,
        "benefit": 1400000,
        "total": 12000000,
        "type": "Trung bình"
    }
]

def classify (salary_per_day: int, benefit:int, work_day:int):
    total = (salary_per_day * work_day) + benefit
    return total
def auto_update (list_emp):
    list_emp['total'] = classify(list_emp['salary_per_day'], list_emp['benefit'], list_emp['work_day'])
    
    if list_emp['total'] < 9000000:
        return "Thấp"
    
    if list_emp['total'] >= 9000000 and list_emp['total'] < 15000000:
        return "Trung bình"
    
    if list_emp['total'] >= 15000000 and list_emp['total'] < 30000000:
        return "Khá"
    
    if list_emp['total'] >= 30000000:
        return "Cao" 
    
def display_emp (list_emp):
    if not list_emp:
        print ("Hiện tại danh sách nhân viên đang bị trống")
        return
    print (f"{'Mã định danh nhân viên':<25} | {'Họ tên':<25} | {'Lương ngày':<15} | {'Tiền phụ cấp (VNĐ)':<18} | {'Tổng thu nhập':<18} | {'Phân loại thu nhập':<20}")
    for emp in list_emp:
        print (f"{emp['id']:<25} | {emp['name']:<25} | {emp['salary_per_day']:<15} | {emp['benefit']:<18} | {emp['total']:<18} | {emp['type']:<20}")

def add_emp ():
    while True:
        id = input ("Nhập vào mã nhân viên: ").strip().upper()
        if not id:
            print ("Mã nhân viên không được để trống")
            continue
        check = False
        for emp in list_emp:
            if id == emp['id']:
                check = True
                break
        
        if check:
            print ("Mã nhân viên đã có trong danh sách")
            continue
        else:
            break
        
    while True:
        name = input ("Nhập vào họ và tên: ").strip().title()
        if not name:
            print ("Họ và tên không được để trống. ")
            continue
        else:
            break
    
    while True:
        try:
            salary_per_day = int (input("Nhập vào lương cơ bản theo ngày: "))
            if salary_per_day <= 0:
                print ("Lương cơ bản phải lớn hơn 0. ")
                continue
            else:
                break
        except ValueError:
            print ("Lương cơ bản phải là số nguyên.")
            
    while True:
        try:
            benefit = int (input("Nhập vào tiền phụ cấp: "))
            if benefit <= 0:
                print ("Tiền phụ cấp phải lớn hơn 0. ")
                continue
            else:
                break
        except ValueError:
            print ("Tiền phụ cấp phải là số nguyên.")
        
    while True:
        try:
            work_day = int (input("Nhập vào số ngày công: "))
            if work_day <= 0:
                print ("Số ngày công phải lớn hơn 0. ")
                continue
            elif work_day > 31:
                print ("Số ngày công phải trong khoảng 1-31")
                continue
            else:
                break
        except ValueError:
            print ("Số ngày công phải là số nguyên.")
    
    new_emp = {
        "id": id,
        "name": name,
        "salary_per_day": salary_per_day,
        "work_day": work_day,
        "benefit": benefit,
        "total": 0,
        "type": ""
    }
    
    new_emp['type'] = auto_update(new_emp)
    list_emp.append(new_emp)
    print (f"Đã thêm thành công nhân viên với mã là {id}")

def update_salary():
    id = input ("Nhập vào mã nhân viên cần cập nhật: ").strip().upper()
    found_emp = None
    for emp in list_emp:
        if id == emp ['id']:
            found_emp = emp
            break
    if not found_emp:
        print (f"Không có mã nhân viên {id} trong danh sách")
        return
    else:
        while True:
            try:
                salary_per_day = int (input ("Nhập vào lương cơ bản theo ngày muốn cập nhật: "))
                if salary_per_day <= 0:
                    print ("Lương cơ bản phải lớn hơn 0. ")
                    continue
                else:
                    break
            except ValueError:
                print ("Lương cơ bản phải là số nguyên. ")
                
        while True:
            try:
                benefit = int (input("Nhập vào tiền phụ cấp: "))
                if benefit <= 0:
                    print ("Tiền phụ cấp phải lớn hơn 0. ")
                    continue
                else:
                    break
            except ValueError:
                print ("Tiền phụ cấp phải là số nguyên.")
            
        while True:
            try:
                work_day = int (input("Nhập vào số ngày công: "))
                if work_day <= 0:
                    print ("Số ngày công phải lớn hơn 0. ")
                    continue
                elif work_day > 31:
                    print ("Số ngày công phải trong khoảng 1-31")
                    continue
                else:
                    break
            except ValueError:
                print ("Số ngày công phải là số nguyên.")    
        found_emp['salary_per_day'] = salary_per_day
        found_emp['work_day'] = work_day
        found_emp['benefit'] = benefit
        found_emp['type'] = auto_update(found_emp)
        print ("Cập nhật thành công")
        
def delete_emp ():
    id = input ("Nhập vào mã nhân viên cần xóa: ").strip().upper()
    found_emp = None
    for emp in list_emp:
        if emp ['id'] == id:
            found_emp = emp
            break
    
    if not found_emp:
        print (f"Không tìm thấy nhân viên có mã {id} trong danh sách")
        return
    else:
        while True:
            choice = input("Bạn có muốn xóa nhân viên này không? (Y/N)").strip().upper()
            match choice:
                case "Y":
                    print ("Xóa thành công")
                    list_emp.remove(found_emp)
                    return
                case "N":
                    print (f"Bạn đã hủy thao tác xóa nhân viên {id}")
                    return
                case _:
                    print ("Lựa chọn của bạn không hợp lệ")
            
def find_emp():
    while True:
        print ("1. Tìm theo mã nhân viên")
        print ("2. Tìm gần đúng theo tên nhân viên")
        print ("3. Thoát tìm kiếm")
        choice = input ("Nhập vào lựa chọn của bạn: ")
        match choice:
            case "1":
                id = input ("Nhập vào mã nhân viên bạn cần tìm: ").strip().upper()
                found_emp = None
                for emp in list_emp:
                    if emp['id'] == id:
                        found_emp = emp
                        break
                if not found_emp:
                    print (f"Không tìm được nhân viên theo mã {id} trong danh sách")
                    return
                display_emp(found_emp)
                return
            case "2":
                name = input ("Nhập tên nhân viên cần tìm: ").strip().lower()
                found_emp = []
                for emp in list_emp:
                    if name == emp['name'].lower():
                        found_emp.append(emp)
                if not found_emp:
                    print (f"Không tìm được tên nhân viên trong danh sách")
                    return
                display_emp(found_emp)
                return
            case "3":
                print ("Thoát chương trình thành công.")
                break
            case _:
                print ("Lựa chọn của bạn không hợp lệ.")
                
def stat ():
    data = {
        "Cao": 0,
        "Khá": 0,
        "Trung bình": 0,
        "Thấp": 0
    }           
    
    for emp in list_emp:
        tt = emp['type']
        if tt in data:
            data[tt] +=1
    
    print (f"{'\nNhóm nhân viên theo mức':<26} | {'Số lượng':<10}")
    print (f"{'Cao':<25} | {data['Cao']:<10}") 
    print (f"{'Khá':<25} | {data['Khá']:<10}") 
    print (f"{'Trung bình':<25} | {data['Trung bình']:<10}") 
    print (f"{'Thấp':<25} | {data['Thấp']:<10}") 
                
def main ():
    while True:
        print ('''
Quản lý lương của nhân viên
1. Hiển thị danh sách nhân viên
2. Tiếp nhận nhân viên mới
3. Cập nhật thông tin và ngày công
4. Xóa nhân viên
5. Tìm kiếm nhân viên
6. Thống kê quỹ lương
7. Thoát chương trình''')
        choice = input ("Nhập vào lựa chọn của bạn: ")
        match choice:
            case "1":
                display_emp(list_emp)
            case "2":
                add_emp ()
            case "3":
                update_salary()
            case "4":
                delete_emp ()
            case "5":
                find_emp()
            case "6":
                stat ()
            case "7":
                print ("Thoát chương trình thành công")
                break
            case _:
                print ("Lựa chọn của bạn không hợp lệ")
                

if __name__ == "__main__":
    main()