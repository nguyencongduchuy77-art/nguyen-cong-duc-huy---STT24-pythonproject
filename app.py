
# 1. Import thư viện
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 2. Tạo dữ liệu 10 sinh viên
data = {
    "Ho_ten": [
        "Nguyen Van An", "Tran Thi Binh", "Le Hoang Nam",
        "Pham Minh Anh", "Hoang Van Hung", "Vo Thi Lan",
        "Dang Quoc Bao", "Bui Ngoc Mai", "Do Thanh Cong",
        "Nguyen Thi Hoa"
    ],
    "Chuyen_can": [9, 8, 10, 7, 8, 9, 7, 10, 8, 9],
    "Giua_ky":    [8, 7, 9, 6, 7, 8, 6, 9, 7, 8],
    "Cuoi_ky":    [8.5, 7.5, 9, 6.5, 8, 8.5, 7, 9.5, 7.5, 8]
}

df = pd.DataFrame(data)

# 3. Tính điểm tổng kết
df["Tong_ket"] = (
    df["Chuyen_can"] * 0.2
    + df["Giua_ky"] * 0.3
    + df["Cuoi_ky"] * 0.5
)

# 4. Xếp loại
def xep_loai(diem):
    if diem >= 8.5:
        return "Gioi"
    elif diem >= 7:
        return "Kha"
    elif diem >= 5:
        return "Trung binh"
    return "Yeu"

df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)

# 5. Giao diện ứng dụng
st.title("QUẢN LÝ ĐIỂM SINH VIÊN-")
st.subheader("Bảng điểm của 10 sinh viên")

st.dataframe(
    df.rename(columns={
        "Ho_ten": "Họ tên",
        "Chuyen_can": "Chuyên cần",
        "Giua_ky": "Giữa kỳ",
        "Cuoi_ky": "Cuối kỳ",
        "Tong_ket": "Tổng kết",
        "Xep_loai": "Xếp loại"
    }),
    use_container_width=True
)

# 6. Thống kê lớp
st.subheader("Thống kê kết quả học tập")
st.write(f"Điểm trung bình lớp: {df['Tong_ket'].mean():.2f}")

cao_nhat = df.loc[df["Tong_ket"].idxmax()]
thap_nhat = df.loc[df["Tong_ket"].idxmin()]

st.write(
    f"Sinh viên điểm cao nhất: {cao_nhat['Ho_ten']} "
    f"({cao_nhat['Tong_ket']:.2f})"
)
st.write(
    f"Sinh viên điểm thấp nhất: {thap_nhat['Ho_ten']} "
    f"({thap_nhat['Tong_ket']:.2f})"
)
st.write(f"Số sinh viên đạt từ 5 điểm: {(df['Tong_ket'] >= 5).sum()}/10")

# 7. Chọn sinh viên xem chi tiết
st.subheader("Tra cứu điểm sinh viên")
ten = st.selectbox("Chọn sinh viên", df["Ho_ten"])
sv = df[df["Ho_ten"] == ten].iloc[0]

st.write(f"Họ tên: {sv['Ho_ten']}")
st.write(f"Chuyên cần: {sv['Chuyen_can']}")
st.write(f"Giữa kỳ: {sv['Giua_ky']}")
st.write(f"Cuối kỳ: {sv['Cuoi_ky']}")
st.write(f"Tổng kết: {sv['Tong_ket']:.2f}")
st.write(f"Xếp loại: {sv['Xep_loai']}")

# 8. Biểu đồ điểm tổng kết
st.subheader("Biểu đồ điểm tổng kết")
fig, ax = plt.subplots()
ax.bar(df["Ho_ten"], df["Tong_ket"])
ax.set_title("Điểm tổng kết của 10 sinh viên")
ax.set_xlabel("Họ tên")
ax.set_ylabel("Điểm tổng kết")
ax.tick_params(axis="x", rotation=70)
fig.tight_layout()
st.pyplot(fig)

# 9. Thông tin sinh viên thực hiện
st.caption("Người thực hiện: [Nhập họ tên của bạn] - MSSV: [Nhập MSSV]")
