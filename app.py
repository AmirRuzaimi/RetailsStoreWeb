```python
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="RetailHub | Premium Streetwear & Modern Essentials",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for Dr. Mister Inspired Aesthetics & Smooth Directional Animations
st.markdown(
    """
    <style>
    /* Global Page & Subtle Tech Grid Pattern */
    .stApp {
        background-color: #0b0f19;
        background-image: 
            radial-gradient(rgba(255, 255, 255, 0.08) 1px, transparent 1px),
            radial-gradient(rgba(255, 255, 255, 0.04) 1px, transparent 1px);
        background-size: 32px 32px;
        background-position: 0 0, 16px 16px;
        color: #f1f5f9;
        animation: pageFadeIn 0.8s cubic-bezier(0.16, 1, 0.3, 1);
    }

    @keyframes pageFadeIn {
        0% { opacity: 0; transform: translateY(12px); }
        100% { opacity: 1; transform: translateY(0); }
    }

    /* High-End Dark Luxury Hero Banner */
    .hero-banner {
        background: linear-gradient(135deg, #020617 0%, #0f172a 60%, #1e1b4b 100%);
        border: 1px solid rgba(255, 255, 255, 0.12);
        padding: 50px 30px;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 35px;
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.6), inset 0 1px 0 rgba(255, 255, 255, 0.1);
        position: relative;
        overflow: hidden;
    }

    .hero-banner h1 {
        margin: 0;
        font-size: 3rem;
        font-weight: 900;
        letter-spacing: -1px;
        background: linear-gradient(180deg, #ffffff 0%, #cbd5e1 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero-banner p {
        font-size: 1.15rem;
        color: #94a3b8;
        margin-top: 12px;
        font-weight: 300;
        letter-spacing: 0.5px;
    }

    .hero-tag {
        display: inline-block;
        background: rgba(99, 102, 241, 0.15);
        color: #818cf8;
        border: 1px solid rgba(99, 102, 241, 0.3);
        padding: 6px 16px;
        border-radius: 30px;
        font-size: 0.8rem;
        font-weight: 700;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        margin-bottom: 15px;
    }

    /* Product Cards */
    .product-card {
        background: rgba(15, 23, 42, 0.7);
        border-radius: 16px;
        padding: 18px;
        border: 1px solid rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(10px);
        transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        margin-bottom: 20px;
    }

    .product-card:hover {
        transform: translateY(-8px);
        border-color: rgba(99, 102, 241, 0.5);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.5), 0 0 20px rgba(99, 102, 241, 0.2);
    }

    /* Badges & Tags */
    .badge {
        display: inline-block;
        padding: 4px 12px;
        font-size: 0.72rem;
        font-weight: 700;
        color: #e2e8f0;
        background: rgba(255, 255, 255, 0.06);
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 10px;
        letter-spacing: 0.5px;
    }

    /* Button Customization */
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        font-weight: 600;
        transition: all 0.2s ease-in-out;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Initialize Session State
if "cart" not in st.session_state:
    st.session_state.cart = []

# Detailed Product Catalogue with Comprehensive Specifications & Explanations
PRODUCTS = [
    {
        "id": 1,
        "name": "Heavyweight Oversized Tee",
        "category": "Apparel",
        "price": 69.90,
        "image": "https://images.unsplash.com/photo-1583743814966-8936f5b7be1a?w=500",
        "tagline": "280 GSM Heavyweight Streetwear Silhouette",
        "desc": "Engineered for maximum structure and drape. Double-needle stitched sleeve and bottom hems ensure durability.",
        "specs": {
            "Material": "100% Combed Compact Cotton (280 GSM)",
            "Fit": "Signature Boxy / Oversized Drop-Shoulder",
            "Care": "Machine wash cold inside out, tumble dry low",
            "Story": "Inspired by urban brutalism and vintage streetwear cuts."
        }
    },
    {
        "id": 2,
        "name": "Minimalist Ambient Desk Lamp",
        "category": "Home & Living",
        "price": 119.00,
        "image": "https://images.unsplash.com/photo-1507473885765-e6ed057f782c?w=500",
        "tagline": "Anodized Matte Aluminum with Touch Dimming",
        "desc": "Sleek architectural lighting designed to reduce eye strain during late-night creative sessions.",
        "specs": {
            "Material": "Aircraft-grade Anodized Aluminum",
            "Lighting": "Warm Warm-to-Cool White LED (2700K - 6500K)",
            "Power": "USB-C Fast Rechargeable (3000mAh Battery)",
            "Story": "Crafted for minimalist workspaces and clean aesthetic setups."
        }
    },
    {
        "id": 3,
        "name": "Insulated Thermal Flask 750ml",
        "category": "Accessories",
        "price": 45.00,
        "image": "https://images.unsplash.com/photo-1602143407151-7111542de6e8?w=500",
        "tagline": "Pro-Grade 18/8 Stainless Steel Vacuum Bottle",
        "desc": "Keeps beverages ice-cold for up to 24 hours or scalding hot for 12 hours without condensation.",
        "specs": {
            "Material": "BPA-Free 18/8 Food-Grade Stainless Steel",
            "Capacity": "750 ml / 25 oz",
            "Coating": "Scratch-Resistant Matte Powder Coat",
            "Story": "Built for long urban commutes and outdoor explorations."
        }
    },
    {
        "id": 4,
        "name": "Active ANC Wireless Headphones",
        "category": "Electronics",
        "price": 329.00,
        "image": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500",
        "tagline": "40mm Titanium Drivers with Hybrid Active Noise Cancellation",
        "desc": "Immerse yourself in acoustic perfection with lossless Bluetooth 5.3 audio and plush memory foam earcups.",
        "specs": {
            "Drivers": "40mm Custom Titanium Drivers",
            "Battery": "40 Hours Playtime with ANC On (USB-C Quick Charge)",
            "Connectivity": "Bluetooth 5.3 & 3.5mm AUX Cable Included",
            "Story": "Tune out city background noise and focus on deep workflow."
        }
    },
    {
        "id": 5,
        "name": "Matte Black Chronograph Watch",
        "category": "Accessories",
        "price": 189.90,
        "image": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=500",
        "tagline": "Sapphire Crystal Glass with Japanese Quartz Movement",
        "desc": "Monochromatic minimalist dial paired with a premium full-grain Italian leather strap.",
        "specs": {
            "Case": "42mm Matte Black Stainless Steel Case",
            "Glass": "Anti-Reflective Scratch-Resistant Sapphire Crystal",
            "Water Resistance": "5 ATM / 50 Meters Water Resistant",
            "Story": "Timeless utility meets modern stealth luxury."
        }
    },
    {
        "id": 6,
        "name": "Handcrafted Ceramic Mug Trio",
        "category": "Home & Living",
        "price": 55.00,
        "image": "https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?w=500",
        "tagline": "Speckled Stoneware Clay with Matte Glaze Finish",
        "desc": "Set of 3 unique artisan mugs handcrafted for espresso, pour-over coffee, and matcha rituals.",
        "specs": {
            "Material": "High-Fired Stoneware Clay",
            "Capacity": "320 ml per mug",
            "Safety": "Dishwasher and Microwave Safe",
            "Story": "Celebrating tactile design and slow morning routines."
        }
    },
    {
        "id": 7,
        "name": "Urban Utility Crossbody Bag",
        "category": "Apparel",
        "price": 85.00,
        "image": "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=500",
        "tagline": "Cordura Ballistic Nylon Techwear Pouch",
        "desc": "Weatherproof sling bag featuring YKK waterproof zippers and modular internal pockets.",
        "specs": {
            "Fabric": "1000D Cordura® Ballistic Nylon",
            "Hardware": "Fidlock® Magnetic Quick-Release Buckle",
            "Capacity": "3.5 Liters",
            "Story": "Designed for carry items: phone, wallet, keys, and compact camera."
        }
    },
    {
        "id": 8,
        "name": "Portable Mechanical Keyboard",
        "category": "Electronics",
        "price": 240.00,
        "image": "https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=500",
        "tagline": "Hot-Swappable Tactile Switches & South-Facing RGB",
        "desc": "Compact 75% layout keyboard with sound-dampening foam layers and factory-lubed switches.",
        "specs": {
            "Keycaps": "PBT Double-Shot OEM Profile Keycaps",
            "Connectivity": "Tri-Mode (Bluetooth 5.1 / 2.4GHz / USB-C Wired)",
            "Compatibility": "macOS, Windows, iOS, Android",
            "Story": "Tactile satisfaction engineered for desk purists and coders."
        }
    },
    {
        "id": 9,
        "name": "Scented Soy Wax Candle",
        "category": "Home & Living",
        "price": 38.00,
        "image": "https://images.unsplash.com/photo-1603006905003-be475563bc59?w=500",
        "tagline": "Hand-Poured 100% Natural Soy Wax in Amber Glass",
        "desc": "Infused with therapeutic essential oils: Cedarwood, Smoked Amber, and Bergamot notes.",
        "specs": {
            "Wax": "100% Organic Eco-Soy Wax (Clean Burning)",
            "Wick": "Natural Crackling Wooden Wick",
            "Burn Time": "Approx. 50 Hours",
            "Story": "Creating a calm and grounding atmosphere for modern living."
        }
    }
]

# Navigation Sidebar & Layered Category Controls
st.sidebar.title("🛍️ RetailHub")
st.sidebar.caption("Dr. Mister Inspired Collection")

page = st.sidebar.radio("Navigation", ["Storefront", "Shopping Cart", "Brand Story"])

# --- PAGE 1: STOREFRONT ---
if page == "Storefront":
    # Dark Luxury Hero Banner
    st.markdown(
        """
        <div class="hero-banner">
            <span class="hero-tag">NEW DROP 2026</span>
            <h1>URBAN ESSENTIALS & APPAREL</h1>
            <p>High-performance materials meets understated street luxury aesthetics.</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    # Layered Filtering System
    st.sidebar.markdown("---")
    st.sidebar.subheader("🗂️ Collection Layers")

    search_query = st.sidebar.text_input("🔍 Search Items", "")

    categories = ["All Categories"] + sorted(list(set(p["category"] for p in PRODUCTS)))
    selected_category = st.sidebar.selectbox("Category", categories)

    max_price = float(max(p["price"] for p in PRODUCTS))
    price_range = st.sidebar.slider("Price Filter (RM)", 0.0, max_price, max_price)

    # Filter Logic
    filtered_products = PRODUCTS
    if selected_category != "All Categories":
        filtered_products = [p for p in filtered_products if p["category"] == selected_category]
    if search_query:
        filtered_products = [p for p in filtered_products if search_query.lower() in p["name"].lower() or search_query.lower() in p["desc"].lower()]
    filtered_products = [p for p in filtered_products if p["price"] <= price_range]

    st.write(f"Displaying **{len(filtered_products)}** curated items")
    st.write("")

    # Display Product Grid
    cols = st.columns(3)
    for index, product in enumerate(filtered_products):
        col = cols[index % 3]
        with col:
            st.markdown('<div class="product-card">', unsafe_allow_html=True)
            st.image(product["image"], use_container_width=True)
            st.markdown(f'<span class="badge">{product["category"].upper()}</span>', unsafe_allow_html=True)
            st.subheader(product["name"])
            st.write(f"**RM {product['price']:.2f}**")
            st.caption(product["tagline"])

            # Expandable Product Details Section
            with st.expander("📖 Detailed Specifications & Story"):
                st.write(f"**Overview:** {product['desc']}")
                st.markdown("---")
                for key, val in product["specs"].items():
                    st.write(f"**{key}:** {val}")

            # Add to Cart Button
            if st.button(f"Add to Cart 🛒", key=f"btn_{product['id']}"):
                st.session_state.cart.append(product)
                st.toast(f"Added **{product['name']}** to cart!", icon="✅")
            st.markdown("</div>", unsafe_allow_html=True)

# --- PAGE 2: SHOPPING CART ---
elif page == "Shopping Cart":
    st.title("🛒 Shopping Cart & Checkout")

    if not st.session_state.cart:
        st.info("Your shopping cart is empty. Head back to the Storefront to explore items!")
    else:
        total_price = sum(item["price"] for item in st.session_state.cart)

        for idx, item in enumerate(st.session_state.cart):
            col1, col2, col3 = st.columns([1, 4, 1])
            with col1:
                st.image(item["image"], width=80)
            with col2:
                st.markdown(f"**{item['name']}**")
                st.caption(f"{item['category']} — RM {item['price']:.2f}")
            with col3:
                if st.button("Remove 🗑️", key=f"remove_{idx}"):
                    st.session_state.cart.pop(idx)
                    st.rerun()

        st.write("---")
        st.subheader(f"Total Amount: **RM {total_price:.2f}**")

        if st.button("Proceed to Checkout 💳", type="primary"):
            st.balloons()
            st.success("Order confirmed! Thank you for purchasing from RetailHub.")
            st.session_state.cart = []

# --- PAGE 3: BRAND STORY ---
elif page == "Brand Story":
    st.title("🏛️ About RetailHub")
    st.markdown(
        """
        RetailHub is built on the philosophy of **Functional Minimalism & Streetwear Aesthetics**. 
        Inspired by modern architectural design and refined utility, every item in our catalogue is chosen for its longevity, premium material composition, and timeless form factor.

        ### Quality Standard
        * **Apparel:** Heavyweight cotton fabrics designed to hold boxy structures over repeated washes.
        * **Hardware & Electronics:** Anodized metals, tactile switches, and high-fidelity sound components.
        * **Accessories:** High-grade stainless steel and water-resistant technical nylon.

        ### Support & Enquiries
        * 📧 Email: contact@retailhub.com
        * 📞 Hotline: +60 12-345 6789
        * 📍 Location: Kota Bharu, Kelantan, Malaysia
    """
    )
```

---

### What Was Updated:
1. **Dr. Mister Aesthetics & Hero Theme**: Applied dark luxury colors (`#0b0f19`, `#0f172a`, `#1e1b4b`) combined with a custom glowing tag and tech background dot grid.
2. **Item Specification Details**: Each item now includes an expandable **"Detailed Specifications & Story"** tab that breaks down materials (e.g., *280 GSM cotton*, *1000D Cordura Nylon*, *Titanium Drivers*), fit/care instructions, and brand story.
3. **Product #1 Image Fixed**: Replaced with a proper flat-lay streetwear t-shirt product photo instead of a portrait shot.
4. **Multi-layer Category Filtering**: Added live search bar, category selection, and price slider in the sidebar.
```
