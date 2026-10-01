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
# TIÊU ĐỀ
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

MUC_DUONG = [
    "100% đường",
    "70% đường",
    "0% đường (Không đường)"
]

MUC_DA = [
    "Nhiều đá",
    "Đá bình thường",
    "Ít đá",
    "Không đá"
]

# =========================================================
# SESSION STATE
# =========================================================

if "cart" not in st.session_state:
    st.session_state.cart = []

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "Xin chào! 👋 Mình là trợ lý ảo của Quán Trà Sữa Happy. "
                "Bạn cần mình tư vấn chọn món, topping, mức đường hay mức đá không?"
            )
        }
    ]

if "order_key" not in st.session_state:
    st.session_state.order_key = 0

# =========================================================
# PHẦN 1: CHATBOT
# =========================================================

with st.expander(
    "💬 Trò chuyện với Trợ lý ảo tư vấn trà sữa",
    expanded=False
):
    st.write(
        "Hỏi trợ lý về món bán chạy, topping, giá, mức độ đường hoặc mức đá:"
    )

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    user_prompt = st.chat_input(
        "Nhập câu hỏi cho bot..."
    )

    if user_prompt:
        st.session_state.messages.append(
            {
                "role": "user",
                "content": user_prompt
            }
        )

        with st.chat_message("user"):
            st.markdown(user_prompt)

        prompt_lower = user_prompt.lower()

        bot_response = (
            "Xin lỗi bạn, mình chưa hiểu ý lắm. 🤔 "
            "Bạn có thể hỏi về menu, các loại topping, giá, "
            "mức độ đường hoặc mức đá nhé!"
        )

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

        elif "topping" in prompt_lower:
            bot_response = (
                "🧋 **Quán có nhiều loại topping:**\n\n"
                "⚫ Trân châu đen – 5.000đ\n"
                "⚪ Trân châu trắng – 5.000đ\n"
                "🧀 Thạch phô mai – 8.000đ\n"
                "🍮 Pudding trứng – 8.000đ\n"
                "🟡 Trân châu hoàng kim – 6.000đ\n"
                "🌿 Sương sáo – 5.000đ\n\n"
                "👉 Mỗi món có thể chọn nhiều topping cùng lúc!"
            )

        elif "đá" in prompt_lower:
            bot_response = (
                "🧊 **Quán có 4 mức đá:**\n\n"
                "• Nhiều đá – nhiều đá, mát lạnh.\n"
                "• Đá bình thường – mức đá tiêu chuẩn.\n"
                "• Ít đá – phù hợp nếu bạn thích nhiều vị trà sữa hơn.\n"
                "• Không đá – không thêm đá.\n\n"
                "👉 Bạn có thể chọn mức đá riêng cho từng món."
            )

        elif (
            "đường" in prompt_lower
            or "ngọt" in prompt_lower
        ):
            bot_response = (
                "🍬 **Quán có 3 mức đường:**\n\n"
                "• 100% đường – vị ngọt đậm.\n"
                "• 70% đường – ngọt vừa, dễ uống.\n"
                "• 0% đường – không thêm đường.\n\n"
                "👉 Bạn có thể chọn mức đường riêng cho từng món."
            )

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

        elif (
            "giá" in prompt_lower
            or "menu" in prompt_lower
            or "bao nhiêu" in prompt_lower
        ):
            bot_response = (
                "📋 **Giá trà sữa:** từ **25.000đ – 35.000đ**.\n\n"
                "🍮 **Giá topping:** từ **5.000đ – 8.000đ**.\n\n"
                "🧊 **Mức đá:** Nhiều đá, Đá bình thường, Ít đá, Không đá.\n\n"
                "Bạn có thể chọn nhiều món nước cùng một lần đặt hàng."
            )

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
# PHẦN 2: THÔNG TIN KHÁCH HÀNG
# =========================================================

st.subheader("📝 Thông tin đơn hàng")

ten_khach = st.text_input(
    "Tên khách hàng:",
    placeholder="Nhập tên của bạn...",
    key="input_ten"
)

st.write("---")

# =========================================================
# PHẦN 3: CHỌN NHIỀU MÓN NƯỚC TRONG MỘT LẦN
# =========================================================

st.subheader("🧋 Chọn nhiều món nước")

st.info(
    "💡 Bạn có thể chọn **nhiều món cùng lúc**. "
    "Mỗi món được cài riêng **số lượng, mức đường, mức đá và topping**."
)

chon_nhieu_mon = st.multiselect(
    "Chọn các món nước muốn đặt:",
    list(MENU_TRASUA.keys()),
    key="chon_nhieu_mon"
)

# Lưu cấu hình món đang chọn để thêm vào giỏ
order_items = []

if chon_nhieu_mon:
    st.markdown("### ⚙️ Tùy chỉnh từng món")

    for i, ten_mon in enumerate(chon_nhieu_mon):
        with st.container(border=True):
            st.markdown(
                f"### 🧋 {i + 1}. {ten_mon}"
            )

            col1, col2 = st.columns(2)

            with col1:
                so_luong_mon = st.number_input(
                    f"Số lượng – {ten_mon}",
                    min_value=1,
                    max_value=100,
                    value=1,
                    step=1,
                    key=f"qty_{ten_mon}"
                )

                muc_duong_mon = st.radio(
                    f"🍬 Mức đường – {ten_mon}",
                    MUC_DUONG,
                    horizontal=True,
                    key=f"sugar_{ten_mon}"
                )

            with col2:
                muc_da_mon = st.radio(
                    f"🧊 Mức đá – {ten_mon}",
                    MUC_DA,
                    horizontal=True,
                    key=f"ice_{ten_mon}"
                )

                topping_mon = st.multiselect(
                    f"🍮 Topping – {ten_mon}",
                    list(MENU_TOPPING.keys()),
                    key=f"topping_{ten_mon}"
                )

            gia_mon = MENU_TRASUA[ten_mon]

            tien_tra_sua_mon = gia_mon * int(so_luong_mon)

            tien_topping_moi_ly = sum(
                MENU_TOPPING[topping]
                for topping in topping_mon
            )

            tien_topping_mon = (
                tien_topping_moi_ly * int(so_luong_mon)
            )

            thanh_tien_mon = (
                tien_tra_sua_mon + tien_topping_mon
            )

            st.caption(
                f"💰 Đơn giá: {gia_mon:,}đ/ly | "
                f"Topping: {tien_topping_moi_ly:,}đ/ly | "
                f"Thành tiền: {thanh_tien_mon:,}đ"
            )

            order_items.append(
                {
                    "ten_mon": ten_mon,
                    "don_gia": gia_mon,
                    "so_luong": int(so_luong_mon),
                    "muc_duong": muc_duong_mon,
                    "muc_da": muc_da_mon,
                    "topping": list(topping_mon),
                    "tien_topping": tien_topping_moi_ly,
                    "thanh_tien": thanh_tien_mon
                }
            )

    # Tổng tiền của toàn bộ món đang chọn
    tong_mon_dang_chon = sum(
        item["thanh_tien"]
        for item in order_items
    )

    tong_ly_dang_chon = sum(
        item["so_luong"]
        for item in order_items
    )

    st.markdown(
        f"""
        <div style="
            padding:18px;
            border-radius:12px;
            background-color:#fff8e1;
            border:2px solid #ffca28;
        ">
            <h3 style="text-align:center;">
                🧾 TỔNG MÓN ĐANG CHỌN
            </h3>
            <p style="text-align:center;">
                🥤 Tổng số ly: <b>{tong_ly_dang_chon}</b>
            </p>
            <h2 style="text-align:center;">
                💰 {tong_mon_dang_chon:,}đ
            </h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    # -----------------------------------------------------
    # THÊM TẤT CẢ MÓN VÀO GIỎ CHỈ VỚI 1 LẦN BẤM
    # -----------------------------------------------------

    if st.button(
        "➕ THÊM TẤT CẢ MÓN ĐÃ CHỌN VÀO GIỎ",
        type="primary",
        use_container_width=True
    ):
        for item in order_items:
            st.session_state.cart.append(item)

        st.success(
            f"✅ Đã thêm **{len(order_items)} loại món / "
            f"{tong_ly_dang_chon} ly** vào giỏ hàng!"
        )

        # Xóa lựa chọn sau khi thêm để có thể tạo lượt đặt mới
        st.session_state.chon_nhieu_mon = []
        st.rerun()

else:
    st.info(
        "👆 Hãy chọn một hoặc nhiều món nước ở phía trên."
    )

st.write("---")

# =========================================================
# PHẦN 4: GIỎ HÀNG
# =========================================================

st.subheader(
    f"🛒 GIỎ HÀNG ({len(st.session_state.cart)} loại món)"
)

if len(st.session_state.cart) > 0:

    tong_tam_tinh = 0

    for idx, item in enumerate(st.session_state.cart):

        with st.container(border=True):

            st.markdown(
                f"### 🧋 {idx + 1}. {item['ten_mon']}"
            )

            col1, col2 = st.columns(2)

            with col1:
                st.write(
                    f"💵 Đơn giá: **{item['don_gia']:,}đ**"
                )

                st.write(
                    f"🔢 Số lượng: **{item['so_luong']}**"
                )

                st.write(
                    f"🍬 Đường: **{item['muc_duong']}**"
                )

            with col2:
                st.write(
                    f"🧊 Đá: **{item.get('muc_da', 'Đá bình thường')}**"
                )

                topping_text = (
                    ", ".join(item["topping"])
                    if item["topping"]
                    else "Không có"
                )

                st.write(
                    f"🍮 Topping: **{topping_text}**"
                )

            st.markdown(
                f"💰 **Thành tiền: {item['thanh_tien']:,}đ**"
            )

            tong_tam_tinh += item["thanh_tien"]

            if st.button(
                f"🗑️ Xóa món {idx + 1}",
                key=f"delete_{idx}",
                use_container_width=True
            ):
                st.session_state.cart.pop(idx)
                st.rerun()

    # =====================================================
    # TỔNG GIỎ HÀNG
    # =====================================================

    st.markdown("---")

    st.markdown(
        f"""
        <div style="
            padding:20px;
            border-radius:12px;
            background-color:#f1f8e9;
            border:2px solid #8bc34a;
        ">
            <h2 style="text-align:center;">
                🧾 TỔNG GIỎ HÀNG
            </h2>
            <h1 style="text-align:center;">
                {tong_tam_tinh:,}đ
            </h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    # =====================================================
    # XÓA TOÀN BỘ
    # =====================================================

    if st.button(
        "🗑️ XÓA TOÀN BỘ GIỎ HÀNG",
        type="secondary",
        use_container_width=True
    ):
        st.session_state.cart = []
        st.success("✅ Đã xóa toàn bộ giỏ hàng.")
        st.rerun()

else:

    st.info(
        "🛒 Giỏ hàng đang trống.\n\n"
        "Hãy chọn một hoặc nhiều món ở phía trên và bấm "
        "**THÊM TẤT CẢ MÓN ĐÃ CHỌN VÀO GIỎ**."
    )

# =========================================================
# PHẦN 5: THANH TOÁN
# =========================================================

st.write("---")

st.subheader("💰 Thanh toán")

if st.button(
    "🧾 TÍNH TIỀN & XUẤT HÓA ĐƠN",
    type="primary",
    use_container_width=True
):

    # -----------------------------------------------------
    # KIỂM TRA TÊN
    # -----------------------------------------------------

    if not ten_khach.strip():

        st.warning(
            "⚠️ Vui lòng nhập tên khách hàng trước khi thanh toán!"
        )

    # -----------------------------------------------------
    # KIỂM TRA GIỎ
    # -----------------------------------------------------

    elif len(st.session_state.cart) == 0:

        st.warning(
            "⚠️ Giỏ hàng đang trống. "
            "Vui lòng thêm ít nhất một món!"
        )

    else:

        # -------------------------------------------------
        # TÍNH TỔNG
        # -------------------------------------------------

        tong_thanh_toan = sum(
            item["thanh_tien"]
            for item in st.session_state.cart
        )

        tong_so_ly = sum(
            item["so_luong"]
            for item in st.session_state.cart
        )

        thoi_gian = datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )

        st.success(
            "✅ Đã tạo hóa đơn thành công!"
        )

        # -------------------------------------------------
        # HIỂN THỊ HÓA ĐƠN
        # -------------------------------------------------

        st.markdown(
            "## 📋 HÓA ĐƠN CHI TIẾT"
        )

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

            muc_da = item.get(
                "muc_da",
                "Đá bình thường"
            )

            danh_sach_html += f"""
            <div style="
                padding:12px;
                margin-bottom:10px;
                border-bottom:1px dashed #aaa;
            ">

                <b>{idx}. {item['ten_mon']}</b>

                <br>
                🔢 Số lượng: {item['so_luong']}

                <br>
                💵 Đơn giá: {item['don_gia']:,}đ

                <br>
                🍬 Đường: {item['muc_duong']}

                <br>
                🧊 Đá: {muc_da}

                <br>
                🍮 Topping: {topping_str}

                <br>
                💰 <b>Thành tiền: {item['thanh_tien']:,}đ</b>

            </div>
            """

        hoa_don_html = f"""
        <div style="
            background-color:#ffffff;
            padding:25px;
            border-radius:15px;
            border:2px solid #ddd;
            color:#222;
        ">

            <h2 style="text-align:center;">
                🧋 QUÁN TRÀ SỮA HAPPY 🧋
            </h2>

            <p style="text-align:center;">
                HÓA ĐƠN THANH TOÁN
            </p>

            <hr>

            <p>
                <b>📍 Địa chỉ:</b>
                123 Đường Sữa, TP. Hồ Chí Minh
            </p>

            <p>
                <b>⏰ Thời gian:</b>
                {thoi_gian}
            </p>

            <p>
                <b>👤 Khách hàng:</b>
                {ten_khach}
            </p>

            <p>
                <b>🥤 Tổng số ly:</b>
                {tong_so_ly}
            </p>

            <hr>

            <h3>📋 DANH SÁCH MÓN</h3>

            {danh_sach_html}

            <hr>

            <h2 style="text-align:right;">
                💰 TỔNG THANH TOÁN:
                {tong_thanh_toan:,}đ
            </h2>

            <p style="text-align:center;">
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

Tổng số ly: {tong_so_ly}

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

            muc_da = item.get(
                "muc_da",
                "Đá bình thường"
            )

            noi_dung_file += f"""

{idx}. {item['ten_mon']}
----------------------------------------
Đơn giá: {item['don_gia']:,} VNĐ
Số lượng: {item['so_luong']}
Mức đường: {item['muc_duong']}
Mức đá: {muc_da}
Topping: {topping_str}
Thành tiền: {item['thanh_tien']:,} VNĐ

"""

        noi_dung_file += f"""
========================================
TỔNG THANH TOÁN:
{tong_thanh_toan:,} VNĐ
========================================

Cảm ơn quý khách!
Hẹn gặp lại!
"""

        # =================================================
        # NÚT TẢI HÓA ĐƠN
        # =================================================

        st.download_button(
            label="📥 TẢI HÓA ĐƠN (.TXT)",
            data=noi_dung_file,
            file_name=(
                f"HoaDon_"
                f"{ten_khach.strip().replace(' ', '_')}.txt"
            ),
            mime="text/plain",
            use_container_width=True
        )
