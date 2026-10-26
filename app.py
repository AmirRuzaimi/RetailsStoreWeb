import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="RetailHub | Modern Lifestyle Store",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for Sleek Retail UI, Background Pattern & Smooth Animations
st.markdown(
    """
    <style>
    /* Global Page & Background Pattern (Subtle Tech Grid) */
    .stApp {
        background-color: #fafbfc;
        background-image: radial-gradient(#d1d5db 1px, transparent 1px);
        background-size: 28px 28px;
        animation: pageFadeIn 0.6s cubic-bezier(0.16, 1, 0.3, 1);
    }

    @keyframes pageFadeIn {
        0% { opacity: 0; transform: translateY(12px); }
        100% { opacity: 1; transform: translateY(0); }
    }

    /* Sleek Dark Minimalist Hero Banner */
    .hero-banner {
        background: linear-gradient(135deg, #0f172a 1e%, #1e293b 100%);
        color: white;
        padding: 55px 30px;
        border-radius: 16px;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 12px 32px rgba(15, 23, 42, 0.15);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }

    .hero-banner h1 {
        margin: 0;
        font-size: 2.8rem;
        font-weight: 800;
        letter-spacing: -0.5px;
        color: #ffffff;
    }

    .hero-banner p {
        font-size: 1.15rem;
        color: #94a3b8;
        margin-top: 10px;
    }

    /* Product Card with Smooth Directional Hover & Entrance */
    .product-card {
        background-color: #ffffff;
        border-radius: 14px;
        padding: 16px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.02);
        transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
        margin-bottom: 24px;
        animation: cardSlideUp 0.5s ease-out;
    }

    @keyframes cardSlideUp {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }

    .product-card:hover {
        transform: translateY(-6px) scale(1.01);
        box-shadow: 0 20px 30px -10px rgba(0, 0, 0, 0.08);
        border-color: #cbd5e1;
    }

    /* Custom Category Badges */
    .badge {
        display: inline-block;
        padding: 4px 12px;
        font-size: 0.75rem;
        font-weight: 600;
        color: #0f172a;
        background-color: #f1f5f9;
        border-radius: 20px;
        margin-bottom: 10px;
        border: 1px solid #e2e8f0;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Initialize Session State for Cart
if "cart" not in st.session_state:
    st.session_state.cart = []

# Expanded Retail Product Database (Properly Focused Product Images)
PRODUCTS = [
    {
        "id": 1,
        "name": "Heavyweight Oversized Tee",
        "category": "Apparel",
        "price": 69.90,
        "image": "https://images.unsplash.com/photo-1583743814966-8936f5b7be1a?w=500",
        "desc": "Premium streetwear fit crafted from heavy combed cotton.",
    },
    {
        "id": 2,
        "name": "Minimalist Ambient Desk Lamp",
        "category": "Home & Living",
        "price": 119.00,
        "image": "https://images.unsplash.com/photo-1507473885765-e6ed057f782c?w=500",
        "desc": "Touch-control dimmable LED light with sleek metallic finish.",
    },
    {
        "id": 3,
        "name": "Insulated Thermal Flask 750ml",
        "category": "Accessories",
        "price": 45.00,
        "image": "https://images.unsplash.com/photo-1602143407151-7111542de6e8?w=500",
        "desc": "Double-wall vacuum insulation keeps drinks cold for 24h.",
    },
    {
        "id": 4,
        "name": "Active ANC Wireless Headphones",
        "category": "Electronics",
        "price": 329.00,
        "image": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500",
        "desc": "Immersive studio-grade sound with hybrid noise cancellation.",
    },
    {
        "id": 5,
        "name": "Matte Black Chronograph Watch",
        "category": "Accessories",
        "price": 189.90,
        "image": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=500",
        "desc": "Sleek modern timepiece with scratch-resistant sapphire glass.",
    },
    {
        "id": 6,
        "name": "Handcrafted Ceramic Mug Trio",
        "category": "Home & Living",
        "price": 55.00,
        "image": "https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?w=500",
        "desc": "Matte-glazed artisanal mugs designed for daily coffee rituals.",
    },
    {
        "id": 7,
        "name": "Urban Utility Crossbody Bag",
        "category": "Apparel",
        "price": 85.00,
        "image": "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=500",
        "desc": "Water-resistant techwear pouch for your daily essentials.",
    },
    {
        "id": 8,
        "name": "Portable Mechanical Keyboard",
        "category": "Electronics",
        "price": 240.00,
        "image": "https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=500",
        "desc": "Compact wireless keyboard with tactile hot-swappable switches.",
    },
    {
        "id": 9,
        "name": "Scented Soy Wax Candle",
        "category": "Home & Living",
        "price": 38.00,
        "image": "https://images.unsplash.com/photo-1603006905003-be475563bc59?w=500",
        "desc": "Long-burning clean amber and sandalwood fragrance candle.",
    },
]

# Navigation Sidebar with Layered Filters
st.sidebar.title("🛍️ RetailHub")
page = st.sidebar.radio("Navigate", ["Storefront", "Shopping Cart", "About Us"])

# --- PAGE 1: STOREFRONT ---
if page == "Storefront":
    st.markdown(
        """
        <div class="hero-banner">
            <h1>Elevate Your Everyday</h1>
            <p>Curated modern essentials designed for contemporary lifestyle and retail.</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    # Layered Category Filter Options
    st.sidebar.markdown("---")
    st.sidebar.subheader("🗂️ Category Layers")
    categories = ["All"] + sorted(list(set(p["category"] for p in PRODUCTS)))
    selected_category = st.sidebar.selectbox("Filter Collection", categories)

    filtered_products = (
        PRODUCTS
        if selected_category == "All"
        else [p for p in PRODUCTS if p["category"] == selected_category]
    )

    st.write(f"Showing **{len(filtered_products)}** items in *{selected_category}*")
    st.write("")

    # Display Products in a clean 3-column Grid with Card Wrappers
    cols = st.columns(3)
    for index, product in enumerate(filtered_products):
        col = cols[index % 3]
        with col:
            st.markdown('<div class="product-card">', unsafe_allow_html=True)
            st.image(product["image"], use_container_width=True)
            st.markdown(f'<span class="badge">{product["category"]}</span>', unsafe_allow_html=True)
            st.subheader(product["name"])
            st.write(f"**RM {product['price']:.2f}**")
            st.caption(product["desc"])

            if st.button(f"Add to Cart 🛒", key=f"btn_{product['id']}"):
                st.session_state.cart.append(product)
                st.toast(f"Added **{product['name']}** to cart!", icon="✅")
            st.markdown("</div>", unsafe_allow_html=True)

# --- PAGE 2: SHOPPING CART ---
elif page == "Shopping Cart":
    st.title("🛒 Your Shopping Cart")

    if not st.session_state.cart:
        st.info("Your cart is currently empty. Head over to the Storefront to add items!")
    else:
        total_price = sum(item["price"] for item in st.session_state.cart)

        for idx, item in enumerate(st.session_state.cart):
            col1, col2, col3 = st.columns([1, 4, 1])
            with col1:
                st.image(item["image"], width=70)
            with col2:
                st.markdown(f"**{item['name']}**")
                st.caption(f"RM {item['price']:.2f}")
            with col3:
                if st.button("Remove", key=f"remove_{idx}"):
                    st.session_state.cart.pop(idx)
                    st.rerun()

        st.write("---")
        st.subheader(f"Total Amount: **RM {total_price:.2f}**")

        if st.button("Proceed to Checkout 💳", type="primary"):
            st.balloons()
            st.success("Order placed successfully! Thank you for shopping with RetailHub.")
            st.session_state.cart = []

# --- PAGE 3: ABOUT US ---
elif page == "About Us":
    st.title("ℹ️ About RetailHub")
    st.write(
        """
        RetailHub is a contemporary lifestyle and retail storefront inspired by clean aesthetics, premium product curation, and seamless user experiences. 
        We bridge the gap between quality everyday goods and effortless online shopping.
    """
    )
    st.subheader("Get in Touch")
    st.write("📧 Email: support@retailhub.com")
    st.write("📞 Phone: +60 12-345 6789")
    st.write("📍 Location: Kota Bharu, Kelantan, Malaysia")
