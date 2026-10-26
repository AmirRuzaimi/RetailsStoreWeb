import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Retail Hub | Online Store",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for UI styling & smooth fade-in transitions
st.markdown(
    """
    <style>
    /* Global Page Fade-in Animation */
    .stApp {
        animation: fadeIn 0.8s ease-in-out;
    }

    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(10px); }
        100% { opacity: 1; transform: translateY(0); }
    }

    /* Modern Card Container */
    .product-card {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 16px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
        transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
        margin-bottom: 20px;
        border: 1px solid #eaeaea;
    }

    .product-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
    }

    /* Hero Banner */
    .hero-banner {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 40px 20px;
        border-radius: 16px;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 4px 15px rgba(118, 75, 162, 0.3);
    }

    .hero-banner h1 {
        margin: 0;
        font-size: 2.5rem;
        font-weight: 700;
        color: white;
    }

    .hero-banner p {
        font-size: 1.1rem;
        opacity: 0.9;
        margin-top: 8px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Initialize Session State for Cart
if "cart" not in st.session_state:
    st.session_state.cart = []

# Mock Product Database
PRODUCTS = [
    {
        "id": 1,
        "name": "Classic Cotton T-Shirt",
        "category": "Apparel",
        "price": 49.90,
        "image": "https://images.unsplash.com/photo-1521572267360-ee0c2909d518?w=500",
        "desc": "100% premium breathable cotton shirt.",
    },
    {
        "id": 2,
        "name": "Ergonomic Desk Lamp",
        "category": "Home & Living",
        "price": 89.00,
        "image": "https://images.unsplash.com/photo-1507473885765-e6ed057f782c?w=500",
        "desc": "Adjustable LED lamp with warm and cool modes.",
    },
    {
        "id": 3,
        "name": "Stainless Steel Water Bottle",
        "category": "Accessories",
        "price": 35.50,
        "image": "https://images.unsplash.com/photo-1602143407151-7111542de6e8?w=500",
        "desc": "Keeps drinks cold up to 24 hours.",
    },
    {
        "id": 4,
        "name": "Wireless Noise-Canceling Headphones",
        "category": "Electronics",
        "price": 299.00,
        "image": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500",
        "desc": "High-fidelity audio with active noise cancellation.",
    },
    {
        "id": 5,
        "name": "Minimalist Wristwatch",
        "category": "Accessories",
        "price": 149.90,
        "image": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=500",
        "desc": "Sleek analog watch with genuine leather strap.",
    },
    {
        "id": 6,
        "name": "Ceramic Coffee Mug Set",
        "category": "Home & Living",
        "price": 42.00,
        "image": "https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?w=500",
        "desc": "Handcrafted set of 2 ceramic mugs.",
    },
]

# Navigation Sidebar
st.sidebar.title("🛍️ Retail Store")
page = st.sidebar.radio("Navigate", ["Storefront", "Shopping Cart", "About Us"])

# --- PAGE 1: STOREFRONT ---
if page == "Storefront":
    # Hero Banner
    st.markdown(
        """
        <div class="hero-banner">
            <h1>Welcome to RetailHub</h1>
            <p>Your one-stop destination for quality everyday essentials.</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    # Filter by category
    categories = ["All"] + sorted(list(set(p["category"] for p in PRODUCTS)))
    selected_category = st.selectbox("Filter by Category", categories)

    filtered_products = (
        PRODUCTS
        if selected_category == "All"
        else [p for p in PRODUCTS if p["category"] == selected_category]
    )

    st.write("---")

    # Display Products in Grid
    cols = st.columns(3)
    for index, product in enumerate(filtered_products):
        col = cols[index % 3]
        with col:
            st.image(product["image"], use_container_width=True)
            st.subheader(product["name"])
            st.caption(f"Category: {product['category']}")
            st.write(f"**RM {product['price']:.2f}**")
            st.write(product["desc"])

            if st.button(
                f"Add to Cart 🛒", key=f"btn_{product['id']}"
            ):
                st.session_state.cart.append(product)
                st.toast(
                    f"Added **{product['name']}** to cart!", icon="✅"
                )

# --- PAGE 2: SHOPPING CART ---
elif page == "Shopping Cart":
    st.title("🛒 Your Shopping Cart")

    if not st.session_state.cart:
        st.info("Your cart is currently empty. Go back to the Storefront to add items!")
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
            st.success("Order placed successfully! Thank you for shopping with us.")
            st.session_state.cart = []

# --- PAGE 3: ABOUT US ---
elif page == "About Us":
    st.title("ℹ️ About RetailHub")
    st.write(
        """
        RetailHub is a modern retail shop focused on bringing top-quality everyday products right to your doorstep. 
        Whether you are looking for electronics, fashion, or home accessories, we ensure the best retail experience.
    """
    )
    st.subheader("Contact & Support")
    st.write("📧 Email: support@retailhub.com")
    st.write("📞 Phone: +60 12-345 6789")
    st.write("📍 Location: Kuala Lumpur, Malaysia")
