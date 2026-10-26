import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="RetailHub | Modern Lifestyle Store",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for Pure Solid Dark Theme & High-Contrast Typography
st.markdown(
    """
    <style>
    /* Global Page & Main Background (Pure Solid Dark - No Dots) */
    .stApp {
        background-color: #0b0f17 !important;
        background-image: none !important;
        color: #f3f4f6 !important;
        animation: fadeIn 0.5s ease-in-out;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(8px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Force All Main Text & Headers to Bright High-Contrast White */
    h1, h2, h3, h4, h5, h6, p, span, label, div {
        color: #f9fafb !important;
    }

    /* Hero Banner (Sleek Dark Slate Gradient) */
    .hero-banner {
        background: linear-gradient(135deg, #111827 0%, #1f2937 100%);
        color: #ffffff !important;
        padding: 50px 30px;
        border-radius: 16px;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
        border: 1px solid #1f2937;
    }

    .hero-banner h1 {
        margin: 0;
        font-size: 2.7rem;
        font-weight: 800;
        color: #ffffff !important;
        letter-spacing: -0.5px;
    }

    .hero-banner p {
        font-size: 1.1rem;
        color: #9ca3af !important;
        margin-top: 10px;
    }

    /* Product Card Container (Clean Dark Surface) */
    .product-card {
        background-color: #111827 !important;
        border-radius: 14px;
        padding: 18px;
        border: 1px solid #1f2937;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
        transition: all 0.3s ease;
        margin-bottom: 20px;
    }

    .product-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 24px rgba(0, 0, 0, 0.7);
        border-color: #374151;
    }

    /* Product Subheaders & Prices */
    .product-title {
        font-size: 1.25rem;
        font-weight: 700;
        color: #ffffff !important;
        margin-top: 8px;
        margin-bottom: 4px;
    }

    .product-price {
        font-size: 1.1rem;
        font-weight: 600;
        color: #38bdf8 !important;
        margin-bottom: 8px;
    }

    .product-desc {
        font-size: 0.9rem;
        color: #d1d5db !important;
        line-height: 1.4;
        margin-bottom: 12px;
    }

    /* Custom Category Badges */
    .badge {
        display: inline-block;
        padding: 4px 12px;
        font-size: 0.75rem;
        font-weight: 700;
        color: #38bdf8 !important;
        background-color: #1e293b;
        border-radius: 20px;
        margin-bottom: 8px;
        border: 1px solid #334155;
    }

    /* Expandable Specification Box Fix for Dark Mode */
    .stExpander {
        background-color: #1f2937 !important;
        border-radius: 8px !important;
        border: 1px solid #374151 !important;
    }

    .stExpander p, .stExpander li {
        color: #e5e7eb !important;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Initialize Session State for Cart
if "cart" not in st.session_state:
    st.session_state.cart = []

# Product Database
PRODUCTS = [
    {
        "id": 1,
        "name": "Heavyweight Oversized Tee",
        "category": "Apparel",
        "price": 69.90,
        "image": "https://images.unsplash.com/photo-1583743814966-8936f5b7be1a?w=500",
        "desc": "Premium streetwear fit crafted from heavy combed cotton.",
        "specs": "• Material: 280 GSM Heavy Combed Cotton\n• Fit: Relaxed / Oversized Drop-Shoulder\n• Care: Machine wash cold, tumble dry low\n• Story: Engineered for supreme comfort and structured drape, inspired by urban minimalism."
    },
    {
        "id": 2,
        "name": "Minimalist Ambient Desk Lamp",
        "category": "Home & Living",
        "price": 119.00,
        "image": "https://images.unsplash.com/photo-1507473885765-e6ed057f782c?w=500",
        "desc": "Touch-control dimmable LED light with sleek metallic finish.",
        "specs": "• Material: Anodized Aluminum Alloy & Frosted Glass\n• Power: USB-C Rechargeable (5000mAh Battery)\n• Modes: 3 Color Temperatures (Warm, Neutral, Cool)\n• Story: Designed to declutter your workspace while providing warm, glare-free illumination."
    },
    {
        "id": 3,
        "name": "Insulated Thermal Flask 750ml",
        "category": "Accessories",
        "price": 45.00,
        "image": "https://images.unsplash.com/photo-1602143407151-7111542de6e8?w=500",
        "desc": "Double-wall vacuum insulation keeps drinks cold for 24h.",
        "specs": "• Material: 18/8 Food-Grade Stainless Steel\n• Capacity: 750ml (25 oz)\n• Performance: Keeps drinks cold 24 hrs / hot 12 hrs\n• Story: Built for the active commuter seeking sustainable, plastic-free hydration."
    },
    {
        "id": 4,
        "name": "Active ANC Wireless Headphones",
        "category": "Electronics",
        "price": 329.00,
        "image": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500",
        "desc": "Immersive studio-grade sound with hybrid noise cancellation.",
        "specs": "• Drivers: Custom 40mm Titanium Drivers\n• Battery Life: Up to 40 hours with ANC On\n• Connectivity: Bluetooth 5.3 & AUX support\n• Story: Tuned for audiophiles who demand complete acoustic isolation in noisy environments."
    },
    {
        "id": 5,
        "name": "Matte Black Chronograph Watch",
        "category": "Accessories",
        "price": 189.90,
        "image": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=500",
        "desc": "Sleek modern timepiece with scratch-resistant sapphire glass.",
        "specs": "• Movement: Japanese Quartz Chronograph\n• Glass: Scratch-Resistant Sapphire Crystal\n• Water Resistance: 5 ATM (50 meters)\n• Story: A bold statement piece blending tactical matte finishing with timeless elegance."
    },
    {
        "id": 6,
        "name": "Handcrafted Ceramic Mug Trio",
        "category": "Home & Living",
        "price": 55.00,
        "image": "https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?w=500",
        "desc": "Matte-glazed artisanal mugs designed for daily coffee rituals.",
        "specs": "• Material: High-fire stoneware ceramic\n• Capacity: 350ml per mug\n• Care: Microwave and dishwasher safe\n• Story: Hand-glazed by local artisans to bring tactile warmth to your morning brew."
    },
]

# Navigation Sidebar
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

    cols = st.columns(3)
    for index, product in enumerate(filtered_products):
        col = cols[index % 3]
        with col:
            st.markdown('<div class="product-card">', unsafe_allow_html=True)
            st.image(product["image"], use_container_width=True)
            st.markdown(f'<span class="badge">{product["category"]}</span>', unsafe_allow_html=True)
            st.markdown(f'<div class="product-title">{product["name"]}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="product-price">RM {product["price"]:.2f}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="product-desc">{product["desc"]}</div>', unsafe_allow_html=True)

            # Detailed specifications and story tab
            with st.expander("📖 Detailed Specifications & Story"):
                st.markdown(product["specs"])

            st.write("")
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
        RetailHub is a contemporary lifestyle and retail storefront inspired by clean dark-mode aesthetics, premium product curation, and seamless user experiences. 
        We bridge the gap between quality everyday goods and effortless online shopping.
    """
    )
    st.subheader("Get in Touch")
    st.write("📧 Email: support@retailhub.com")
    st.write("📞 Phone: +60 12-345 6789")
    st.write("📍 Location: Kota Bharu, Kelantan, Malaysia")
    
