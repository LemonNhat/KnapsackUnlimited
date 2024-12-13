import tkinter as tk
from tkinter import messagebox


def information():
    tk.messagebox.showinfo(title="Thông tin", message="Nhóm: 10 nụ cười bằng 1 thang thuốc bổ\nThành viên:\nVõ Thị Minh Tâm           2313044\nLý Quang Huy                2311168\nLê Minh Nhật                2312471\nVũ Hoàng Thiên Phú   2312662\nLê Anh Thư                   2313382\n")


def calculate():
    try:
        # Lấy giá trị đầu vào từ giao diện
        max_weight = int(ent_MaxWeight.get())
        value = [int(ent_Value1.get()), int(ent_Value2.get()), int(ent_Value3.get())]
        weight = [int(ent_Weight1.get()), int(ent_Weight2.get()), int(ent_Weight3.get())]

        k = len(value)
        # Khởi tạo bảng kết quả
        table = [0 for _ in range(max_weight + 1)]
        chosen_items = [{} for _ in range(max_weight + 1)]

        # Tính toán tối ưu cho từng trọng lượng từ 0 đến max_weight
        for j in range(max_weight + 1):
            for i in range(k):
                if weight[i] <= j:
                    tempt = table[j - weight[i]] + value[i]
                    if tempt > table[j]:
                        table[j] = tempt
                        # Cập nhật truy vết
                        chosen_items[j] = chosen_items[j - weight[i]].copy()
                        chosen_items[j][i] = chosen_items[j].get(i, 0) + 1

        # Hiển thị tổng doanh thu tối ưu
        lbl_Result.config(text=f"Tổng lợi nhuận tối đa là: {table[max_weight]} triệu đồng")

        # Hiển thị chi tiết vật phẩm được chọn
        detailed_result = "Các vật phẩm được chọn và số lần chọn:\n"
        for n, count in chosen_items[max_weight].items():
            detailed_result += f"Vật phẩm {n + 1} (Doanh thu: {value[n]} triệu, Trọng lượng: {weight[n]} tấn): {count} lần\n"

        # Xóa nội dung cũ và hiển thị kết quả chi tiết
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, detailed_result)

    except ValueError:
        lbl_Result.config(text="Vui lòng nhập số hợp lệ!")
        result_text.delete(1.0, tk.END)


# Tạo cửa sổ giao diện
window = tk.Tk()
window.title("Chương trình giải bài toán sắp xếp hàng hóa")
window.geometry("640x480")

# Thanh menu
MenuBar = tk.Menu(window)
MenuFunction = tk.Menu(MenuBar, tearoff=0)
MenuFunction.add_command(label="Thoát", command=window.quit)
MenuHelp = tk.Menu(MenuBar, tearoff=0)
MenuHelp.add_command(label="Thông tin", command=information)
MenuBar.add_cascade(label="Công cụ", menu=MenuFunction)
MenuBar.add_cascade(label="Trợ giúp", menu=MenuHelp)
window.config(menu=MenuBar)

# Khung chính
MainFrame = tk.Frame(window)
MainFrame.pack(pady=10)

# Nhãn và ô nhập liệu
lbl_Items = tk.Label(MainFrame, text="Hàng hóa")
lbl_Items.grid(row=0, column=0, padx=10, pady=10)
lbl_Type1 = tk.Label(MainFrame, text="Loại 1")
lbl_Type1.grid(row=0, column=1, padx=10, pady=10)
lbl_Type2 = tk.Label(MainFrame, text="Loại 2")
lbl_Type2.grid(row=0, column=2, padx=10, pady=10)
lbl_Type3 = tk.Label(MainFrame, text="Loại 3")
lbl_Type3.grid(row=0, column=3, padx=10, pady=10)

lbl_Weight = tk.Label(MainFrame, text="Trọng lượng (Tấn):")
lbl_Weight.grid(row=1, column=0, padx=10, pady=10)
ent_Weight1 = tk.Entry(MainFrame, width=5)
ent_Weight1.grid(row=1, column=1, padx=10, pady=10)
ent_Weight2 = tk.Entry(MainFrame, width=5)
ent_Weight2.grid(row=1, column=2, padx=10, pady=10)
ent_Weight3 = tk.Entry(MainFrame, width=5)
ent_Weight3.grid(row=1, column=3, padx=10, pady=10)

lbl_Value = tk.Label(MainFrame, text="Doanh thu (Triệu Đồng):")
lbl_Value.grid(row=2, column=0, padx=10, pady=10)
ent_Value1 = tk.Entry(MainFrame, width=5)
ent_Value1.grid(row=2, column=1, padx=10, pady=10)
ent_Value2 = tk.Entry(MainFrame, width=5)
ent_Value2.grid(row=2, column=2, padx=10, pady=10)
ent_Value3 = tk.Entry(MainFrame, width=5)
ent_Value3.grid(row=2, column=3, padx=10, pady=10)

Frame2 = tk.Frame(window)
Frame2.pack(pady=10)
lbl_MaxWeight = tk.Label(Frame2, text="Tải trọng tối đa (Tấn):")
lbl_MaxWeight.grid(row=0, column=0, padx=10, pady=0)
ent_MaxWeight = tk.Entry(Frame2, width=16)
ent_MaxWeight.grid(row=0, column=1, padx=10, pady=0)

ConfirmButton = tk.Button(window, text="Tính toán kết quả", command=calculate)
ConfirmButton.pack(pady=20)

# Khung kết quả
ResultFrame = tk.LabelFrame(window, text="Kết quả")
ResultFrame.pack(fill="both", padx=10, pady=10)
lbl_Result = tk.Label(ResultFrame, text="", font=("Times New Roman", 11))
lbl_Result.pack()
result_text = tk.Text(ResultFrame, width=70, height=10, font=("Times New Roman", 11))
result_text.pack(pady=5)

# Vòng lặp chính
window.mainloop()
