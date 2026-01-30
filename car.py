import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit.components.v1 import html

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Car Information System", layout="wide")

st.markdown(
    """
    <style>
    /* Hide GitHub / Source icon */
    header {visibility: hidden;}
    
    /* Optional: remove top padding left by header */
    .block-container {
        padding-top: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# ---------------- CUSTOM CSS (TITLE STYLING) ----------------
st.markdown(
    """
    <style>
    .main-title {
        text-align: center;
        font-size: 3.2rem;
        font-weight: 800;
        background: linear-gradient(90deg, #1f77b4, #2ca02c, #ff7f0e);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0;
        letter-spacing: 1px;
    }
    .subtitle {
        text-align: center;
        font-size: 1.4rem;
        color: #666;
        margin-top: -10px;
    }
    .emoji {
        text-align: center;
        font-size: 3rem;
        margin-top: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- TITLE ----------------
st.markdown("<div class='main-title'>Car Information System</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>360° Car Explorer • Sales Insights • India Market</div>", unsafe_allow_html=True)
st.markdown("<div class='emoji'>🏎️</div>", unsafe_allow_html=True)

# ---------------- CAR DATA ----------------
car_data = {
    "Maruti Suzuki": ["800", "Vitara Brezza", "WagonR"],
    "Tata": ["Nexon", "Tiago", "Sierra"],
    "Volvo": ["V60 Polestar", "V50", "V70", "XC90 Inscription", "240R Kombi"],
    "Skoda": ["Karoq", "Superb", "Kodiaq", "Rapid", "Octavia"]
}

# ---------------- CAR SPECS ----------------
car_specs = {
    "800": {"capacity": "4 Seater", "mileage": "22.0 km/l"},
    "WagonR": {"capacity": "5 Seater", "mileage": "23.5 km/l"},
    "Vitara Brezza": {"capacity": "5 Seater", "mileage": "19.8 km/l"},
    "Nexon": {"capacity": "5 Seater", "mileage": "17.3 km/l"},
    "Tiago": {"capacity": "5 Seater", "mileage": "20.1 km/l"},
    "Sierra": {"capacity": "5 Seater", "mileage": "N/A"},
    "V60 Polestar": {"capacity": "5 Seater", "mileage": "15.0 km/l"},
    "V50": {"capacity": "5 Seater", "mileage": "14.5 km/l"},
    "V70": {"capacity": "5 Seater", "mileage": "13.8 km/l"},
    "XC90 Inscription": {"capacity": "7 Seater", "mileage": "12.0 km/l"},
    "240R Kombi": {"capacity": "5 Seater", "mileage": "11.5 km/l"},
    "Karoq": {"capacity": "5 Seater", "mileage": "14.8 km/l"},
    "Superb": {"capacity": "5 Seater", "mileage": "15.1 km/l"},
    "Kodiaq": {"capacity": "7 Seater", "mileage": "13.3 km/l"},
    "Rapid": {"capacity": "5 Seater", "mileage": "16.2 km/l"},
    "Octavia": {"capacity": "5 Seater", "mileage": "15.8 km/l"}
}

# ---------------- CAR DESCRIPTION ----------------
car_description = {
    "800": "Launched in 1983, the Maruti 800 transformed the Indian automobile market by making car ownership affordable and reliable.",
    "WagonR": "Launched in 1999, the WagonR is known for its tall-boy design, spacious cabin, and excellent fuel efficiency.",
    "Vitara Brezza": "Launched in 2016, the Brezza became a top-selling compact SUV with bold design and strong reliability.",
    "Nexon": "Introduced in 2017, the Tata Nexon is India’s first 5-star Global NCAP-rated car, admired for safety and design.",
    "Tiago": "Launched in 2016, the Tiago offers solid build quality and great value in the hatchback segment.",
    "Sierra": "The Tata Sierra is an iconic SUV remembered for its unique design and futuristic revival concept.",
    "V60 Polestar": "A performance-oriented luxury wagon known for advanced safety and hybrid performance.",
    "V50": "A compact premium Volvo wagon with Scandinavian styling and comfort.",
    "V70": "A spacious estate car praised for durability, comfort, and safety.",
    "XC90 Inscription": "Launched in India in 2015, the XC90 represents Volvo’s luxury SUV segment.",
    "240R Kombi": "A classic Volvo wagon famous for durability and safety leadership.",
    "Karoq": "Launched in India in 2020, the Karoq offers solid European build quality and comfort.",
    "Superb": "Known for luxury, rear-seat comfort, and powerful engines.",
    "Kodiaq": "A premium full-size SUV with strong road presence and refined interiors.",
    "Rapid": "A compact sedan appreciated for sharp handling and solid build quality.",
    "Octavia": "An iconic sedan admired for performance, design, and driving dynamics."
}

# ---------------- 360° EMBEDS ----------------
car_360_embed = {
    "Maruti Suzuki": {
        "800": "https://sketchfab.com/models/adcc7ff83891422d9f3dcaf55debc073/embed",
        "Vitara Brezza": "https://sketchfab.com/models/1a5cbddc8acb457e9d896d7345fd07d8/embed",
        "WagonR": "https://sketchfab.com/models/71112627f42342099ff95b59e7532663/embed"
    },
    "Tata": {
        "Nexon": "https://sketchfab.com/playlists/embed?collection=877506d06f4e43c8bc2ddc8328ad02c1",
        "Tiago": "https://sketchfab.com/models/7ae10b287a184453b19a83ed5b37c007/embed",
        "Sierra": "https://sketchfab.com/models/c465e62e9e0f4802a1de528db756c106/embed"
    },
    "Volvo": {
        "V60 Polestar": "https://sketchfab.com/models/504ce39150fe49c7979f702d5f0f8580/embed",
        "V50": "https://sketchfab.com/models/34632915878c410fa1f5cbc8c820e4ba/embed",
        "V70": "https://sketchfab.com/models/61bb5ad577754b8ead80a85e94cbf644/embed",
        "XC90 Inscription": "https://sketchfab.com/models/e91e35e356ea456ca2c682efe36360b2/embed",
        "240R Kombi": "https://sketchfab.com/models/6ad5919e89a44775bc548d86cc241e9b/embed"
    },
    "Skoda": {
        "Karoq": "https://sketchfab.com/models/7e359874ebe744158eddc37c9da8f487/embed",
        "Superb": "https://sketchfab.com/models/9df2416b04b74bb2aea0ef49e3f363b3/embed",
        "Kodiaq": "https://sketchfab.com/models/ad0fb4edf2c245338ddfcc9639555584/embed",
        "Rapid": "https://sketchfab.com/models/40dc7c8a08e1479ba3bbd93d06744ede/embed",
        "Octavia": "https://sketchfab.com/models/747287e4d7a448948ae7a9ca873f2b4f/embed"
    }
}

# ---------------- SELECT SECTION ----------------
c1, c2, c3 = st.columns(3)
with c1:
    brand = st.selectbox("Brand", list(car_data.keys()))
with c2:
    model = st.selectbox("Model", car_data[brand])
with c3:
    fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "Electric", "Hybrid"])

# ---------------- 360° VIEW ----------------
embed_url = car_360_embed.get(brand, {}).get(model)
if embed_url:
    html(f"<iframe src='{embed_url}' width='100%' height='450' frameborder='0' allowfullscreen></iframe>", height=460)

# ---------------- REVIEW SECTION ----------------
if st.button("📝 Review Car"):

    left, right = st.columns([1, 2])
    specs = car_specs.get(model, {"capacity": "N/A", "mileage": "N/A"})

    with left:
        st.markdown("## 🚘 Car Details")
        st.write(f"**Brand:** {brand}")
        st.write(f"**Model:** {model}")
        st.write(f"**Fuel Type:** {fuel_type}")
        st.write(f"**Capacity:** {specs['capacity']}")
        st.write(f"**Mileage:** {specs['mileage']}")

    with right:
        st.markdown("## 📘 About This Car")
        st.write(car_description.get(model, "Description not available."))

    st.markdown("---")

    # ---------------- LINE GRAPH ----------------
    sales_data = {
        "WagonR": ([2019,2020,2021,2022,2023,2024,2025],[153000,148000,175000,181000,183000,180000,178000]),
        "Vitara Brezza": ([2019,2020,2021,2022,2023,2024,2025],[145000,130000,155000,167000,171000,170000,172000]),
        "Nexon": ([2019,2020,2021,2022,2023,2024,2025],[41600,44923,108577,172138,180000,175000,175000]),
        "Tiago": ([2019,2020,2021,2022,2023,2024,2025],[96400,75600,65000,67000,69000,68000,70000]),
        "800": ([2019,2020,2021,2022,2023,2024,2025],[0,0,0,0,0,0,0])
    }

    years, sales = sales_data.get(model, ([2019], [0]))
    df_line = pd.DataFrame({"Year": years, "Sales": sales})

    fig_line = px.line(
        df_line,
        x="Year",
        y="Sales",
        markers=True,
        title=f"📈 {model} Sales Trend in India",
        color_discrete_sequence=["#1f77b4"]
    )

    st.plotly_chart(fig_line, use_container_width=True)

    st.markdown("---")

    # ---------------- BAR GRAPH ----------------
    st.markdown("## 🏆 Top 10 Selling Cars in India (2026 – Estimated)")

    df_bar = pd.DataFrame({
        "Car Model": [
            "Maruti WagonR","Maruti Swift","Tata Nexon","Maruti Baleno",
            "Hyundai Creta","Maruti Brezza","Tata Punch",
            "Hyundai i20","Tata Tiago","Maruti Dzire"
        ],
        "Sales": [195000,188000,182000,176000,172000,168000,162000,156000,151000,146000]
    })

    fig_bar = px.bar(
        df_bar,
        x="Car Model",
        y="Sales",
        color="Car Model",
        text="Sales",
        color_discrete_sequence=px.colors.qualitative.Set2,
        title="📊 Top 10 Car Sales in India – 2026"
    )

    fig_bar.update_traces(textposition="outside")
    fig_bar.update_layout(showlegend=False)

    st.plotly_chart(fig_bar, use_container_width=True)

# ---------------- FOOTER ----------------
st.markdown("<br><hr>", unsafe_allow_html=True)
st.caption("🚀 Built with Streamlit & Python | 360° Car Visualization Project")












