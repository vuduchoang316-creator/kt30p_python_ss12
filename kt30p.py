max_id = 1
list_car = [
    {
        "id":1,
        "type":"Xe máy",
        "owner":"Vũ Đức Hoàng"
    }
]
while True:
    print("""
    QUẢN LÝ BÃI XE - SMART PARKING
=====================================
1. Thêm xe mới vào bãi
2. Hien thị danh sách xe trong bãi
3. Tim kiêm xe theo mã (id)
4. Xóa xe khỏi bãi (khi xe ra)
5. Thoát chương trình
""")
    choice = input("Lựa chọn chức năng: ")
    if not choice.isdigit():
        print("Lựa chọn không hợp lệ")
        continue
    choice = int(choice)
    match choice:
        case 1 :
            max_id += 1
            while True:
                input_type = input("Nhập loại xe: ").strip()
                if not input_type.strip() :
                    print("Loại xe không được để trống")
                    continue
                break
            while True: 
                input_owner = input("Nhập tên chủ xe: ").strip().title()
                if not input_owner.strip():
                    print("Lỗi chủ xe không được để trống")
                    continue
                break
            list_car.append({
                "id":max_id,
                "type":input_type,
                "owner":input_owner
            })
        case 2:
            if list_car == []:
                print("Danh sách hiện đang trống")
                continue
            print("Danh sách hiện tại:")
            print(f"{'ID' :<5} | {'Loại xe':<10} | {'Chủ xe' :<10}")
            for value in list_car:
                print(f"{value.get('id'):<5} | {value.get('type'):<10} | {value.get('owner')}")
        case 3:
            while True:
                check_id = False
                input_id = input("Nhập id cần tìm: ")
                if not input_id.isdigit():
                    print("Lỗi id không hợp lệ")
                    continue
                input_id = int(input_id)
                for i,value in enumerate(list_car):
                    if input_id == value.get('id'):
                        check_id = True
                        break
                if check_id:
                        print(list_car[i])
                        break
                else:
                    print(f"Không tìm thấy xe có id [{input_id}]")
                    continue
        case 4:
            while True:
                check_id = False
                input_id = input("Nhập id cần xóa: ")
                if not input_id.isdigit():
                    print("Lỗi id không hợp lệ")
                    continue
                input_id = int(input_id)
                for i,value in enumerate(list_car):
                    if input_id == value.get('id'):
                        check_id = True
                        break
                
                if check_id:
                        list_car.pop(i)
                        print(f"Đã xóa xe có ID [{input_id}] ra khỏi bãi")
                        break
                else:
                    print(f"Không tìm thấy xe có id [{input_id}] để xóa")
                    continue
        case 5:
            print("Thoát chương trình")
            break
        case _:
            print("Lựa chọn không hợp lệ vui lòng nhập lại!")
