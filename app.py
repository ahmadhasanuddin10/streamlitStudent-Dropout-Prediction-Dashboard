import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Konfigurasi halaman Streamlit
st.set_page_config(
    page_title="Student Dropout Prediction Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Menambahkan header
st.title("🎓 Student Dropout Prediction Dashboard")
st.markdown("""
    Selamat datang di dashboard prediksi dropout siswa. 
    Dashboard ini dirancang untuk memberikan insight tentang status siswa berdasarkan prediksi model.
""")

# Memuat data dari CSV
data = pd.read_csv('student_dropout_predictions.csv')

# Sidebar untuk navigasi
st.sidebar.header("📊 Filter Data")
status_filter = st.sidebar.multiselect(
    "Pilih Status Prediksi:", 
    options=data['Predicted_Status'].unique(), 
    default=data['Predicted_Status'].unique()
)
st.sidebar.markdown("---")
st.sidebar.header("📈 Analisis Data")
visual_choice = st.sidebar.radio(
    "Pilih Visualisasi:", 
    options=["Distribusi Status", "Probabilitas Dropout vs Graduate"]
)

# Filter data berdasarkan pilihan pengguna
filtered_data = data[data['Predicted_Status'].isin(status_filter)]

# Menampilkan DataFrame
st.subheader("📄 Data Siswa dan Prediksi Dropout")
st.write("Tabel berikut menunjukkan data siswa dengan filter berdasarkan status prediksi yang dipilih.")
st.dataframe(filtered_data)

# Insight Statistik Dasar
st.subheader("📊 Statistik Deskriptif")
col1, col2 = st.columns(2)
with col1:
    st.write("Statistik Probabilitas Dropout:")
    st.write(filtered_data['Probability_of_Dropout'].describe())
with col2:
    st.write("Statistik Probabilitas Graduate:")
    st.write(filtered_data['Probability_of_Graduate'].describe())

# Visualisasi Data
st.subheader("📈 Visualisasi Data")
if visual_choice == "Distribusi Status":
    st.write("Distribusi Prediksi Status Siswa:")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(x='Predicted_Status', data=filtered_data, ax=ax, palette="viridis")
    ax.set_title('Distribusi Prediksi Status Siswa', fontsize=16)
    ax.set_xlabel('Predicted Status', fontsize=12)
    ax.set_ylabel('Jumlah', fontsize=12)
    st.pyplot(fig)
elif visual_choice == "Probabilitas Dropout vs Graduate":
    st.write("Hubungan Probabilitas Dropout dan Graduate:")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(
        x='Probability_of_Dropout', 
        y='Probability_of_Graduate', 
        hue='Predicted_Status',
        data=filtered_data, 
        palette="viridis",
        ax=ax
    )
    ax.set_title('Probabilitas Dropout vs Graduate', fontsize=16)
    ax.set_xlabel('Probabilitas Dropout', fontsize=12)
    ax.set_ylabel('Probabilitas Graduate', fontsize=12)
    st.pyplot(fig)

# Insight Berdasarkan Status Prediksi
st.subheader("🔍 Insight Berdasarkan Status Prediksi")
if "Dropout" in filtered_data['Predicted_Status'].values:
    dropout_rate = filtered_data['Predicted_Status'].value_counts(normalize=True).get("Dropout", 0) * 100
    st.warning(f"⚠️ **{dropout_rate:.2f}% siswa dalam data ini diprediksi mengalami dropout.**")
else:
    st.success("Tidak ada siswa yang diprediksi dropout pada filter ini!")

if "Graduate" in filtered_data['Predicted_Status'].values:
    graduate_rate = filtered_data['Predicted_Status'].value_counts(normalize=True).get("Graduate", 0) * 100
    st.info(f"🎓 **{graduate_rate:.2f}% siswa diprediksi akan lulus.**")

# Penutup
st.markdown("---")
st.write("**💡 Rekomendasi Aksi:**")
st.markdown("""
1. Monitor siswa dengan probabilitas tinggi untuk **dropout** secara lebih intensif.
2. Berikan dukungan tambahan kepada siswa yang memiliki probabilitas **dropout** di atas rata-rata.
3. Perkuat sistem mentoring untuk membantu siswa dengan status **Enrolled** agar tetap dalam jalur menuju kelulusan.
4. Lakukan analisis lebih mendalam pada faktor-faktor yang memengaruhi probabilitas dropout, seperti kinerja akademik atau kehadiran.
""")
