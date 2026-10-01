import streamlit as st
from datetime import datetime

# =========================================================
# CẤU HÌNH TRANG
# =========================================================

st.set_page_config(
    page_title="Hóa Đơn Trà Sữa",
    page_icon="🧋",
    layout="centered"
)

# =========================================================
# HIỂN THỊ ẢNH
# =========================================================

try:
    st.image("TRASUA.jpg", use_container_width=True)
except Exception:
    pass

# =========================================================
# TIÊU ĐỀ ỨNG DỤNG
# =========================================================

st.markdown(
    """
    <h1 style="text-align: center;">
        🧋 HÓA ĐƠN TRÀ SỮA & TRỢ LÝ TƯ VẤN 🧋
    </h1>
    """,
    unsafe_allow_html=True
)

st.write("---")

# =========================================================
# DỮ LIỆU MENU
# =========================================================

MENU_TRASUA = {
    "Trà sữa truyền thống": 25000,
    "Trà sữa chân châu đường đen": 35000,
    "Trà sữa matcha": 30000,
    "Trà sữa khoai môn": 30000,
    "Trà sữa ô long": 28000,
    "Hồng trà sữa": 25000
}

MENU_TOPPING = {
    "Trân châu đen": 5000,
    "Trân châu trắng": 5000,
    "Thạch phô mai": 8000,
    "Pudding trứng": 8000,
    "Trân châu hoàng kim": 6000,
    "Sương sáo": 5000
}

# =========================================================
# KHỞI TẠO SESSION STATE
# =========================================================

if "cart" not in st.session_state:
    st.session_state.cart = []

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "Xin chào! 👋 Mình là trợ lý ảo của Quán Trà Sữa Happy. "
                "Bạn cần mình tư vấn chọn món hay loại topping nào ngon không?"
            )
        }
    ]

# =========================================================
# PHẦN 1: CHATBOT TƯ VẤN
# =========================================================

with st.expander(
    "💬 Trò chuyện với Trợ lý ảo tư vấn trà sữa",
    expanded=False
):

    st.write(
        "Hỏi trợ lý về món bán chạy, topping, giá hoặc mức độ đường:"
    )

    # -----------------------------------------------------
    # HIỂN THỊ LỊCH SỬ CHAT
    # -----------------------------------------------------

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # -----------------------------------------------------
    # NHẬN CÂU HỎI
    # -----------------------------------------------------

    user_prompt = st.chat_input(
        "Nhập câu hỏi cho bot (VD: Món nào bán chạy nhất?)..."
    )

    if user_prompt:

        # Thêm câu hỏi người dùng
        st.session_state.messages.append(
            {
                "role": "user",
                "content": user_prompt
            }
        )

        with st.chat_message("user"):
            st.markdown(user_prompt)

        # -------------------------------------------------
        # LOGIC CHATBOT
        # -------------------------------------------------

        prompt_lower = user_prompt.lower()

        bot_response = (
            "Xin lỗi bạn, mình chưa hiểu ý lắm. 🤔 "
            "Bạn có thể hỏi về menu, các loại topping, giá tiền "
            "hoặc mức độ đường nhé!"
        )

        # Món bán chạy / ngon
        if (
            "bán chạy" in prompt_lower
            or "ngon" in prompt_lower
            or "best" in prompt_lower
            or "recommend" in prompt_lower
            or "gợi ý" in prompt_lower
        ):

            bot_response = (
                "🌟 **Gợi ý món được yêu thích:**\n\n"
                "🧋 **Trà sữa chân châu đường đen** – đậm đà, "
                "thơm ngọt và có vị caramel đặc trưng.\n\n"
                "🍵 **Trà sữa Matcha** – thanh mát, thơm vị trà xanh.\n\n"
                "👉 Nếu bạn thích vị truyền thống, mình cũng "
                "gợi ý **Trà sữa truyền thống** nhé!"
            )

        # Topping
        elif "topping" in prompt_lower:

            bot_response = (
                "🧋 Quán có nhiều loại topping hấp dẫn:\n\n"
                "⚫ **Trân châu đen** – dai, thơm.\n"
                "⚪ **Trân châu trắng** – giòn nhẹ.\n"
                "🧀 **Thạch phô mai** – béo ngậy.\n"
                "🍮 **Pudding trứng** – mềm mịn.\n"
                "🟡 **Trân châu hoàng kim** – dai giòn.\n"
                "🌿 **Sương sáo** – thanh mát.\n\n"
                "👉 Bạn có thể chọn nhiều topping cùng lúc!"
            )

        # Đường
        elif (
            "đường" in prompt_lower
            or "ngọt" in prompt_lower
        ):

            bot_response = (
                "🍬 Quán có 3 mức đường:\n\n"
                "• **100% đường** – vị ngọt đậm.\n"
                "• **70% đường** – ngọt vừa, dễ uống.\n"
                "• **0% đường** – không thêm đường.\n\n"
                "👉 Nếu bạn không thích quá ngọt, mình gợi ý "
                "**70% đường**."
            )

        # Chào hỏi
        elif (
            "chào" in prompt_lower
            or "hi" in prompt_lower
            or "hello" in prompt_lower
        ):

            bot_response = (
                "Dạ chào bạn! 👋🥰 "
                "Chúc bạn một ngày tốt lành! "
                "Bạn muốn mình gợi ý một món trà sữa hôm nay không?"
            )

        # Giá / menu
        elif (
            "giá" in prompt_lower
            or "menu" in prompt_lower
            or "bao nhiêu" in prompt_lower
        ):

            bot_response = (
                "📋 **Giá trà sữa:** từ **25.000đ – 35.000đ**.\n\n"
                "🍮 **Giá topping:** từ **5.000đ – 8.000đ**.\n\n"
                "Bạn có thể xem danh sách món đầy đủ ở phần đặt hàng bên dưới."
            )

        # -------------------------------------------------
        # LƯU PHẢN HỒI
        # -------------------------------------------------

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": bot_response
            }
        )

        with st.chat_message("assistant"):
            st.markdown(bot_response)

st.write("---")

# =========================================================
# PHẦN 2: NHẬP THÔNG TIN VÀ CHỌN MÓN
# =========================================================

st.subheader("📝 Nhập thông tin đơn hàng")

# ---------------------------------------------------------
# TÊN KHÁCH HÀNG
# ---------------------------------------------------------

ten_khach = st.text_input(
    "Tên khách hàng:",
    placeholder="Nhập tên của bạn...",
    key="input_ten"
)

st.write("---")

st.subheader("🧋 Chọn món trà sữa")

# ---------------------------------------------------------
# CHỌN TRÀ SỮA
# ---------------------------------------------------------

chon_tra_sua = st.selectbox(
    "Chọn loại trà sữa:",
    list(MENU_TRASUA.keys())
)

# ---------------------------------------------------------
# SỐ LƯỢNG
# ---------------------------------------------------------

so_luong = st.number_input(
    "Số lượng:",
    min_value=1,
    max_value=100,
    value=1,
    step=1
)

# ---------------------------------------------------------
# MỨC ĐỘ ĐƯỜNG
# ---------------------------------------------------------

muc_duong = st.radio(
    "Mức độ đường:",
    [
        "100% đường",
        "70% đường",
        "0% đường (Không đường)"
    ],
    horizontal=True
)

# ---------------------------------------------------------
# TOPPING
# ---------------------------------------------------------

st.write("Chọn Topping thêm (tùy chọn):")

topping_duoc_chon = []

cols = st.columns(2)

for i, topping in enumerate(MENU_TOPPING.keys()):

    with cols[i % 2]:

        if st.checkbox(
            f"{topping} (+{MENU_TOPPING[topping]:,}đ)",
            key=f"top_{topping}"
        ):

            topping_duoc_chon.append(topping)

# ---------------------------------------------------------
# THÊM MÓN VÀO GIỎ
# ---------------------------------------------------------

if st.button(
    "➕ Thêm món này vào giỏ hàng",
    type="secondary"
):

    gia_tra_sua = MENU_TRASUA[chon_tra_sua]

    tien_ts = gia_tra_sua * so_luong

    tien_top_1_ly = sum(
        MENU_TOPPING[t]
        for t in topping_duoc_chon
    )

    tien_top = tien_top_1_ly * so_luong

    thanh_tien_item = tien_ts + tien_top

    # Thêm món vào giỏ
    st.session_state.cart.append(
        {
            "ten_mon": chon_tra_sua,
            "so_luong": so_luong,
            "muc_duong": muc_duong,
            "topping": topping_duoc_chon.copy(),
            "thanh_tien": thanh_tien_item
        }
    )

    st.success(
        f"✅ Đã thêm **{so_luong}x {chon_tra_sua}** vào giỏ hàng!"
    )

st.write("---")

# =========================================================
# PHẦN 3: HIỂN THỊ GIỎ HÀNG
# =========================================================

st.subheader(
    f"🛒 Giỏ hàng của bạn ({len(st.session_state.cart)} loại món)"
)

if len(st.session_state.cart) > 0:

    for idx, item in enumerate(st.session_state.cart):

        with st.container():

            st.markdown(
                f"### {idx + 1}. {item['ten_mon']} "
                f"(x{item['so_luong']})"
            )

            st.write(
                f"🍬 Đường: {item['muc_duong']}"
            )

            topping_text = (
                ", ".join(item["topping"])
                if item["topping"]
                else "Không có"
            )

            st.write(
                f"🍮 Topping: {topping_text}"
            )

            st.write(
                f"💰 Thành tiền: **{item['thanh_tien']:,}đ**"
            )

            if st.button(
                "🗑️ Xóa món này",
                key=f"del_{idx}"
            ):

                st.session_state.cart.pop(idx)

                st.rerun()

            st.write("---")

    # -----------------------------------------------------
    # XÓA TOÀN BỘ
    # -----------------------------------------------------

    if st.button(
        "🗑️ Xóa toàn bộ giỏ hàng",
        type="tertiary"
    ):

        st.session_state.cart = []

        st.rerun()

else:

    st.info(
        "🛒 Giỏ hàng của bạn đang trống. "
        "Hãy chọn món và bấm 'Thêm món này vào giỏ hàng'."
    )

# =========================================================
# PHẦN 4: THANH TOÁN VÀ XUẤT HÓA ĐƠN
# =========================================================

st.write("---")

st.subheader("💰 Thanh toán")

if st.button(
    "🧾 Tính Tiền và Xuất Hóa Đơn Chung",
    type="primary"
):

    # -----------------------------------------------------
    # KIỂM TRA TÊN
    # -----------------------------------------------------

    if not ten_khach.strip():

        st.warning(
            "⚠️ Vui lòng nhập tên khách hàng trước khi tính tiền!"
        )

    # -----------------------------------------------------
    # KIỂM TRA GIỎ HÀNG
    # -----------------------------------------------------

    elif len(st.session_state.cart) == 0:

        st.warning(
            "⚠️ Giỏ hàng đang trống, vui lòng thêm ít nhất một món!"
        )

    else:

        # -------------------------------------------------
        # TÍNH TỔNG
        # -------------------------------------------------

        tong_thanh_toan = sum(
            item["thanh_tien"]
            for item in st.session_state.cart
        )

        thoi_gian = datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )

        st.success(
            "✅ Đã tạo hóa đơn thành công cho tất cả các món!"
        )

        st.markdown(
            "### 📋 KẾT QUẢ HÓA ĐƠN CHI TIẾT"
        )

        # -------------------------------------------------
        # TẠO DANH SÁCH HTML
        # -------------------------------------------------

        danh_sach_html = ""

        for idx, item in enumerate(
            st.session_state.cart,
            1
        ):

            topping_str = (
                ", ".join(item["topping"])
                if item["topping"]
                else "Không có"
            )

            danh_sach_html += f"""
            <p>
                <b>{idx}. {item['ten_mon']}</b>
                (x{item['so_luong']})<br>

                &nbsp;&nbsp;&nbsp;&nbsp;
                + Đường: {item['muc_duong']}<br>

                &nbsp;&nbsp;&nbsp;&nbsp;
                + Topping: {topping_str}<br>

                &nbsp;&nbsp;&nbsp;&nbsp;
                <b>
                    Thành tiền: {item['thanh_tien']:,}đ
                </b>
            </p>
            """

        # -------------------------------------------------
        # TẠO HÓA ĐƠN HTML
        # -------------------------------------------------

        hoa_don_html = f"""
        <div style="
            background-color: #f9f9f9;
            padding: 20px;
            border-radius: 10px;
            border: 1px solid #ddd;
            color: #333;
        ">

            <h2 style="text-align: center;">
                🧋 QUÁN TRÀ SỮA HAPPY 🧋
            </h2>

            <p>
                <b>Địa chỉ:</b>
                123 Đường Sữa, TP. Hồ Chí Minh
            </p>

            <p>
                <b>Thời gian:</b>
                {thoi_gian}
            </p>

            <p>
                <b>Tên khách hàng:</b>
                {ten_khach}
            </p>

            <hr>

            <h3>📋 DANH SÁCH CÁC MÓN ĐÃ ĐẶT</h3>

            {danh_sach_html}

            <hr>

            <h2 style="text-align: right;">
                💰 TỔNG THANH TOÁN:
                {tong_thanh_toan:,}đ
            </h2>

            <p style="text-align: center;">
                ❤️ Cảm ơn quý khách và hẹn gặp lại!
            </p>

        </div>
        """

        st.markdown(
            hoa_don_html,
            unsafe_allow_html=True
        )

        # =================================================
        # TẠO FILE TXT
        # =================================================

        noi_dung_file = f"""
========================================
          QUÁN TRÀ SỮA HAPPY
========================================

Địa chỉ:
123 Đường Sữa, TP. Hồ Chí Minh

Thời gian: {thoi_gian}

Tên khách hàng: {ten_khach}

========================================
DANH SÁCH MÓN ĐÃ ĐẶT
========================================

"""

        for idx, item in enumerate(
            st.session_state.cart,
            1
        ):

            topping_str = (
                ", ".join(item["topping"])
                if item["topping"]
                else "Không có"
            )

            noi_dung_file += f"""
{idx}. {item['ten_mon']}
Số lượng: {item['so_luong']}
Mức đường: {item['muc_duong']}
Topping: {topping_str}
Thành tiền: {item['thanh_tien']:,} VNĐ

----------------------------------------
"""

        noi_dung_file += f"""
========================================
TỔNG THANH TOÁN: {tong_thanh_toan:,} VNĐ
========================================

Cảm ơn quý khách!
Hẹn gặp lại!
"""

        # -------------------------------------------------
        # NÚT TẢI HÓA ĐƠN
        # -------------------------------------------------

        st.download_button(
            label="📥 Tải xuống file hóa đơn (.txt)",
            data=noi_dung_file,
            file_name=(
                f"HoaDon_"
                f"{ten_khach.strip().replace(' ', '_')}.txt"
            ),
            mime="text/plain"
        )
