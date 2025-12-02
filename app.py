import io

import pandas as pd
import streamlit as st


st.set_page_config(page_title="Tổng hợp 3 file Excel", layout="centered")

st.title("📊 Tổng hợp dữ liệu từ 3 file Excel")
st.write(
    "Tải lên **tối đa 3 file Excel** (cùng cấu trúc cột), ứng dụng sẽ gộp lại "
    "thành một bảng và cho phép tải về file `tong_hop.xlsx`."
)

uploaded_files = st.file_uploader(
    "Chọn 1–3 file Excel (.xlsx)",
    type=["xlsx"],
    accept_multiple_files=True,
)

if uploaded_files:
    if len(uploaded_files) > 3:
        st.warning("Chỉ xử lý tối đa **3 file**. Vui lòng chọn lại 1–3 file.")
    else:
        dfs = []
        for f in uploaded_files:
            try:
                df = pd.read_excel(f)
                dfs.append(df)
                st.success(f"Đã đọc file: `{f.name}` (số dòng: {len(df)})")
            except Exception as e:
                st.error(f"Lỗi khi đọc file `{f.name}`: {e}")

        if dfs:
            merged = pd.concat(dfs, ignore_index=True)

            st.subheader("Xem nhanh dữ liệu đã gộp")
            st.dataframe(merged)

            # Ghi ra buffer để cho tải về dạng Excel
            buffer = io.BytesIO()
            with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
                merged.to_excel(writer, index=False, sheet_name="TongHop")
            buffer.seek(0)

            st.download_button(
                label="⬇️ Tải file Excel đã tổng hợp (`tong_hop.xlsx`)",
                data=buffer,
                file_name="tong_hop.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            )
else:
    st.info("Hãy tải lên 1–3 file Excel để bắt đầu tổng hợp.")


