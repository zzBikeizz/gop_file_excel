import pandas as pd


def tong_hop_3_file(
    file1: str = "demo_file_1.xlsx",
    file2: str = "demo_file_2.xlsx",
    file3: str = "demo_file_3.xlsx",
    output: str = "tong_hop.xlsx",
) -> None:
    """
    Tổng hợp dữ liệu từ 3 file Excel thành 1 file.

    Mặc định dùng:
      - demo_file_1.xlsx
      - demo_file_2.xlsx
      - demo_file_3.xlsx
    và ghi ra: tong_hop.xlsx

    Các file nên có cùng cấu trúc cột để nối theo chiều dọc.
    """
    files = [file1, file2, file3]

    dfs = []
    for f in files:
        try:
            df = pd.read_excel(f)
            dfs.append(df)
            print(f"Đã đọc file: {f} (số dòng: {len(df)})")
        except FileNotFoundError:
            print(f"[Cảnh báo] Không tìm thấy file: {f} -> bỏ qua")
        except Exception as e:
            print(f"[Lỗi] Không đọc được file {f}: {e} -> bỏ qua")

    if not dfs:
        print("Không có dữ liệu nào để tổng hợp.")
        return

    tong_hop = pd.concat(dfs, ignore_index=True)
    tong_hop.to_excel(output, index=False)
    print(f"Đã tạo file tổng hợp: {output} (tổng số dòng: {len(tong_hop)})")


if __name__ == "__main__":
    # Chỉ cần chạy file này:
    #   python tong_hop_excel.py
    # Nếu muốn đổi tên file, có thể sửa tham số dưới đây.
    tong_hop_3_file()


