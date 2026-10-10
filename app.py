import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

du_lieu={
    "Họ Tên":["Nguyễn Ngọc Thế Vinh","Nguyễn Minh Sơn","Phan Nhật Thành","Lê Phan Quốc Thiện","Phan Minh Nhật",
              "Nguyễn Văn Đại Dương","Lê Văn Thắng","Võ Thị Sao Mai","Nguyễn Huyền Linh","Nguyễn Trần Gia An"],
    "Chuyên Cần":[10,8,8,2,2,8,1,8,9,9],
    "Giữa Kỳ":[10,5,5,1,3,7,6,8,9,8],
    "Cuối Kỳ":[9,8,5,4,8,4,8,9,8,10],
}
df=pd.DataFrame(du_lieu)

df["Điểm Tổng Kết"]=0.2 * df["Chuyên Cần"]+ 0.3 * df["Giữa Kỳ"]+ 0.5 * df["Cuối Kỳ"]

df["Xếp Loại"]=""                                                                                     
for i,diem in enumerate(df["Điểm Tổng Kết"]):
  if diem >=8.5:
    df.loc[i,"Xếp Loại"]="Giỏi"
  elif 7.0 <=diem< 8.5:
    df.loc[i,"Xếp Loại"]="Khá"
  elif 5.0 <=diem<7.0:
    df.loc[i,"Xếp Loại"]="Trung Bình"
  else:
    df.loc[i,"Xếp Loại"]="Yếu"

st.set_page_config(
    page_title="QUẢN LÝ SINH VIÊN",
    layout="wide"
)
st.title("WEBSITE QUẢN LÝ SINH VIÊN")
st.write("quản lý thông tin và điểm số sinh viên")
st.subheader("Bảng điểm sinh viên")
st.dataframe(df, use_container_width=True)

st.markdown("---")
st.subheader("Thống kê kết quả học tập")
dtb_lop=df["Điểm Tổng Kết"].mean()
sv_dat=len(df[df["Điểm Tổng Kết"]>=5])
diem_max=df["Điểm Tổng Kết"].max()
diem_min=df["Điểm Tổng Kết"].min()
sv_max=df[df["Điểm Tổng Kết"]==diem_max]["Họ Tên"].values
sv_min=df[df["Điểm Tổng Kết"]==diem_min]["Họ Tên"].values
cot1, cot2 = st.columns(2)
cot1.metric(label="Điểm trung bình của lớp",value=round(dtb_lop, 2))
cot2.metric(label="Số sinh viên đạt >= 5",value=f"{sv_dat}/{len(df)}")
st.write(
  f" Sinh viên đạt điểm cao nhất {', '.join(sv_max)} ({diem_max} điểm)"
)
st.write(
  f" Sinh viên đạt điểm thấp nhất {', '.join(sv_min)} ({diem_min} điểm)"
)
st.markdown("---")
st.subheader("Tra cứu sinh viên")
chon_sv= st.selectbox("Tên Sinh Viên",df["Họ Tên"])
thong_tin=df[df["Họ Tên"]==chon_sv].iloc[0]
c1,c2 ,c3 ,c4 ,c5 = st.columns(5)
c1.metric("Chuyên cần", thong_tin["Chuyên Cần"])
c2.metric("Giữa Kỳ", thong_tin["Giữa Kỳ"])
c3.metric("Cuối Kỳ", thong_tin["Cuối Kỳ"])
c4.metric("Tổng Kết", thong_tin["Điểm Tổng Kết"])
c5.metric("Xếp Loại", thong_tin["Xếp Loại"])
st.markdown("---")
st.subheader("Biểu đồ cột của 10 Sinh Viên")
plt.figure(figsize=(12, 6))
plt.bar(df["Họ Tên"],df["Điểm Tổng Kết"])
plt.xlabel("Tên")
plt.ylabel("Điểm")
plt.ylim(0,10)
plt.xticks(rotation=30, fontsize=8, ha="right")
plt.title("Điểm của 10 Sinh Viên")
st.pyplot(plt)
st.markdown(
  "<h3 style='font-size: 11px;'>Nguyễn Ngọc Thế Vinh_060208010510</h3>",
    unsafe_allow_html=True,)

