import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set_style("whitegrid")
sns.set(rc={"axes.facecolor":"#FFF9ED","figure.facecolor":"#FFF9ED"})
palette = ["#682F2F", "#9E726F", "#D6B2B1", "#B9C0C9", "#9F8A78", "#F3AB60","#84596B","#917B99","#AE8CA3","#C4A7CB"]

st.title("Air Quality Public Dataset")
st.write("**Dashboard for analyzing Air Quality Public Dataset**")

all_data = pd.read_csv("https://raw.githubusercontent.com/juanvalno/Analisis-Dicoding/main/Dashboard/main_data.csv")

pal = ["#682F2F", "#9E726F", "#D6B2B1", "#B9C0C9", "#9F8A78", "#F3AB60", "#84596B", "#917B99", 
       "#AE8CA3", "#C4A7CB", "#6C8EAD", "#8AB8A8", "#72AD75", "#B5CC6A", "#F4E76E"]

st.write("**1. Dari tahun 2013 - 2017, perkembangan tren kualitas udara dari tahun ke tahun mengelami penurunan atau peningkatan?**")
st.write("**Tren Perkembangan Kualitas Udara 2013 - 2017**")

mean_kualitas = all_data.groupby(['year', 'month'])['Kualitas'].mean()
mean_kualitas.index = mean_kualitas.index.map(lambda x: f'{x[0]}-{x[1]:02d}')
plt.figure(figsize=(20, 7))
plt.plot(mean_kualitas.index, mean_kualitas.values, marker='o', linestyle='-', color="#84596B")
plt.xlabel('Year-Month', labelpad=20, fontsize=13)
plt.ylabel('Kualitas Udara', labelpad=20, fontsize=13)
plt.title('Tren Perkembangan Kualitas Udara', fontsize=25, pad=20, fontweight='bold')
plt.xticks(rotation=45)
plt.xlim(mean_kualitas.index[0], mean_kualitas.index[-1])
plt.grid(True)
plt.tight_layout()
st.pyplot(plt)

text_perkembangan = """
Analisis data menunjukkan bahwa kualitas udara mengalami penurunan dari Maret 2013 hingga Februari 2017, dengan fluktuasi yang signifikan dalam periode tersebut.

Desember 2015 menonjol sebagai bulan dengan kualitas udara terburuk di berbagai wilayah. Hal ini perlu menjadi perhatian serius dan perlu ditelusuri lebih lanjut untuk memahami faktor-faktor yang berkontribusi pada penurunan kualitas udara yang signifikan pada bulan tersebut.

Sebaliknya, Mei 2016 tercatat sebagai bulan dengan kualitas udara terbaik. Hal ini menunjukkan bahwa upaya untuk meningkatkan kualitas udara dapat menghasilkan hasil yang positif.

Secara keseluruhan, data menunjukkan bahwa masih banyak yang harus dilakukan untuk mencapai tingkat kualitas udara yang optimal. Diperlukan upaya berkelanjutan dari berbagai pihak untuk mengatasi berbagai faktor yang berkontribusi pada pencemaran udara.
"""
st.write(text_perkembangan)

yearly_means = all_data.groupby("year")[["PM2.5", "PM10", "SO2", "NO2", "O3"]].mean()
plt.figure(figsize=(10, 6))
for i, feature in enumerate(yearly_means.columns):
    plt.plot(yearly_means.index, yearly_means[feature], label=feature, marker='o', color=palette[i])
plt.xlabel('Tahun', labelpad=10, fontsize=13)
plt.ylabel('Indeks', labelpad=10, fontsize=13)
plt.title('Tren Perkembangan Polutan', fontsize=20, pad=20, fontweight='bold')
plt.xticks(range(2013, 2016))
plt.legend(loc='center left', bbox_to_anchor=(1, 0.88))
plt.grid(True)
plt.tight_layout()
st.pyplot(plt)

text_perkembangan_polutan = """
Analisis Tren Polutan Udara (Maret 2013 - Februari 2017)

Berdasarkan analisis data, rata-rata tingkat polutan menunjukkan pola yang beragam selama periode Maret 2013 hingga Februari 2017.

- PM10 dan PM2.5: Terjadi peningkatan rata-rata tingkat PM10 dan PM2.5, menunjukkan peningkatan risiko kesehatan masyarakat yang terkait dengan paparan partikel halus ini.
- O3: Rata-rata tingkat O3 mengalami penurunan, yang dapat berdampak negatif pada kesehatan manusia dan ekosistem.
- NO2: Terjadi peningkatan rata-rata tingkat NO2, yang merupakan gas beracun dan dapat memperburuk penyakit pernapasan.
- SO2: Rata-rata tingkat SO2 mengalami sedikit penurunan, menunjukkan adanya perbaikan dalam emisi sulfur dioksida.
"""
st.write(text_perkembangan_polutan)

st.write("**2. Apakah kualitas udara semakin baik pada malam hari? Untuk menunjang keaktifan produktivitas.**")

waktu_means = all_data.groupby("Waktu")["Kualitas"].mean()
plt.figure(figsize=(10, 6))
waktu_means.plot(kind="bar", stacked=False, color=palette)
plt.xlabel('Waktu', labelpad=10, fontsize=13)
plt.ylabel('Indeks', labelpad=10, fontsize=13)
plt.title('Kualitas Udara Pagi & Malam', fontsize=20, pad=20, fontweight='bold')
plt.xticks(rotation=0)
plt.grid(True)
plt.tight_layout()
st.pyplot(plt)

st.write("**Pada malam hari kualitas udara memburuk, maka disarankan untuk tidak terlalu sering beraktifitas di malam hari.**")

waktu_means = all_data.groupby("Waktu")[["PM10", "PM2.5", "NO2", "O3", "SO2"]].mean()
plt.figure(figsize=(10, 6))
waktu_means.plot(kind="bar", stacked=False, color=palette)
plt.xlabel('Waktu', labelpad=10, fontsize=13)
plt.ylabel('Indeks', labelpad=10, fontsize=13)
plt.title('Molekul Polutan Pagi & Malam', fontsize=20, pad=20, fontweight='bold')
plt.xticks(rotation=0)
plt.legend(title="Polutan", loc="upper left", bbox_to_anchor=(1, 1))
plt.grid(True)
plt.tight_layout()
st.pyplot(plt)

text_malam_pagi = """
Kualitas Udara Malam Hari dan Saran Aktivitas

Analisis data menunjukkan bahwa kualitas udara di malam hari umumnya lebih buruk dibandingkan dengan siang hari. Hal ini disebabkan oleh beberapa faktor, seperti:

- Inversi suhu: Pada malam hari, suhu udara di permukaan bumi lebih dingin daripada di lapisan atas. Hal ini menyebabkan udara terperangkap di dekat permukaan bumi, sehingga polutan tidak dapat terdispersi dengan baik.
- Aktivitas kendaraan: Aktivitas kendaraan yang berkurang di malam hari dapat menyebabkan emisi tertahan di dekat permukaan bumi.
- Emisi industri: Beberapa industri beroperasi di malam hari, dan emisi dari industri ini dapat berkontribusi pada penurunan kualitas udara.
"""
st.write(text_malam_pagi)

st.write("**3. Bagaimana kualitas udara pada beberapa Station. Apakah terdapat variasi bedasarkan local geografis?**")

data_3 = all_data.groupby(["year", "station"])[["PM10", "PM2.5", "NO2", "O3", "SO2"]].mean().reset_index()
data_2013 = data_3[data_3['year'] == 2013]
data_2014 = data_3[data_3['year'] == 2014]
data_2015 = data_3[data_3['year'] == 2015]
data_2016 = data_3[data_3['year'] == 2016]
data_2017 = data_3[data_3['year'] == 2017]

def plot_yearly_data(data, year):
    fig, axes = plt.subplots(6, 2, figsize=(20, 18))
    fig.suptitle(f'Kualitas Udara bedasarkan Stations ({year})', fontsize=30, fontweight='bold', y=1)    

    color_iter = iter(palette)

    for ax, (_, row) in zip(axes.flat, data.iterrows()):
        station = row['station']
        color = next(color_iter, '#000000')
        ax.bar(data.columns[2:], row[2:], color=color)
        ax.set_title(station, fontsize=20, pad=5)
        ax.set_xlabel('Polutan', labelpad=5, fontsize=13)
        ax.set_ylabel('Indeks', labelpad=10, fontsize=13)
        ax.set_yticks(range(0, 121, 20))
        ax.grid(True)
    
    plt.tight_layout()
    st.pyplot(fig)

for year in range(2013, 2018):
    data_year = data_3[data_3['year'] == year]
    plot_yearly_data(data_year, year)

text_stasiun = """
Analisis Kualitas Udara di Berbagai Stasiun (2013-2017)

Analisis data menunjukkan variasi kualitas udara di beberapa stasiun di periode 2013-2017:

1. Stasiun dengan Kualitas Udara Baik (2016-2017):
Stasiun Aotizhongxin, Changping, Dongsi, Guanyuan, Gucheng, Huairou, Nongzhanguan, Shunyi, Tiantan, Wanliu, dan Wanshouxigong di 2016 memiliki PM10 dan PM2.5 rendah mengartikan bahwa kualitas udara pada waktu itu baik, namun ketika 2017 mengalami peningkatan PM10 dan PM2.5 yang signifikan yang berarti kualitas udara memburuk.

2. Station **Dingling** mengalami signifikan kualitas udara yang sangat stabil di 2013 - 2017

3. Penurunan Kualitas Udara (2017):
Pada tahun 2017, terjadi peningkatan signifikan pada tingkat PM10 dan PM2.5 di semua stasiun, menandakan penurunan kualitas udara sehat secara keseluruhan.

4. Fluktuasi Kualitas Udara:
Stasiun Dingling mengalami fluktuasi kualitas udara yang signifikan selama periode 2013-2017.
Stasiun Gucheng dan Wanliu menunjukkan fluktuasi polusi PM10 dan PM2.5 tertinggi dalam data pada tahun 2014, dengan sedikit penurunan di tahun-tahun berikutnya..
"""
st.write(text_stasiun)

st.title('Kesimpulan')

text_kesimpulan="""
Berdasarkan analisis data kualitas udara dari tahun 2013 hingga 2017, dapat ditarik kesimpulan sebagai berikut:

**Pertanyaan 1: Tren Kualitas Udara**

1. Secara umum, kualitas udara mengalami peningkatan buruk dari tahun 2013 hingga 2017.

2. Terdapat fluktuasi kualitas udara yang signifikan dalam periode tersebut, dengan bulan Desember 2015 sebagai bulan dengan kualitas udara terburuk dan Mei 2016 sebagai bulan terbaik.

**Pertanyaan 2: Kualitas Udara Malam Hari**

1. Pada malam hari, kualitas udara umumnya lebih buruk dibandingkan dengan siang hari.

2. Hal ini disebabkan oleh beberapa faktor, seperti inversi suhu, berkurangnya aktivitas kendaraan, dan emisi industri.
Oleh karena itu, disarankan untuk tidak terlalu sering beraktivitas di luar ruangan pada malam hari, terutama bagi orang-orang yang memiliki masalah kesehatan pernapasan.

**Pertanyaan 3: Kualitas Udara di Berbagai Stasiun**

1. Terdapat variasi kualitas udara di beberapa stasiun.

2. Stasiun Aotizhongxin, Changping, Dongsi, Guanyuan, Gucheng, Huairou, Nongzhanguan, Shunyi, Tiantan, Wanliu, dan Wanshouxigong menunjukkan kualitas udara yang baik pada tahun 2016, namun mengalami penurunan pada tahun 2017.

3. Stasiun Dingling mengalami fluktuasi kualitas udara yang signifikan stabil selama periode 2013-2017.

4. Stasiun Gucheng dan Wanliu menunjukkan fluktuasi polusi PM10 dan PM2.5 tertinggi dalam data pada tahun 2014, dengan sedikit penurunan di tahun-tahun berikutnya.

Kesimpulan:

Kualitas udara di berbagai wilayah perlu mendapat perhatian serius dan upaya berkelanjutan dari berbagai pihak untuk meningkatkannya. Upaya ini dapat dilakukan dengan berbagai cara, seperti:
- Mengurangi emisi gas buang kendaraan dengan menerapkan standar emisi yang lebih ketat dan mendorong penggunaan kendaraan ramah lingkungan.
- Mengurangi emisi industri dengan menerapkan teknologi yang lebih bersih dan efisien.
- Meningkatkan kesadaran masyarakat tentang pentingnya menjaga kualitas udara dan mendorong mereka untuk berperilaku ramah lingkungan.
- Masyarakat perlu diimbau untuk mengurangi aktivitas di luar ruangan pada malam hari dan saat kualitas udara sedang buruk. Hal ini untuk menghindari paparan terhadap polutan udara yang dapat membahayakan kesehatan.

Upaya bersama dari berbagai pihak sangatlah penting untuk menciptakan lingkungan yang bersih dan sehat bagi semua orang.
"""

st.write(text_kesimpulan)