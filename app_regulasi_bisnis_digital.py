import streamlit as st

st.set_page_config(
    page_title="Regulasi Bisnis Digital",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    .block-container {padding-top: 1.5rem; padding-bottom: 3rem;}
    .hero {
        padding: 1.5rem 1.6rem;
        border: 1px solid rgba(120,120,120,.24);
        border-radius: 18px;
        margin-bottom: 1.1rem;
    }
    .soft-card {
        padding: 1rem 1.1rem;
        border: 1px solid rgba(120,120,120,.22);
        border-radius: 14px;
        margin-bottom: .7rem;
        height: 100%;
    }
    .flow {
        padding: .8rem 1rem;
        border: 1px solid rgba(120,120,120,.22);
        border-radius: 12px;
        margin: .25rem 0;
        text-align: center;
        font-weight: 600;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

def section_title(title, subtitle=None):
    st.markdown(f"## {title}")
    if subtitle:
        st.caption(subtitle)

def card(title, body):
    st.markdown(
        f"""
        <div class="soft-card">
            <b>{title}</b><br>
            {body}
        </div>
        """,
        unsafe_allow_html=True,
    )

def takeaway(text):
    st.success(f"💡 Intinya: {text}")

st.sidebar.title("💻 Pertemuan 9")
st.sidebar.caption("Regulasi dan Hukum Bisnis")

nav_options = [
    "🏠 Beranda",
    "🌐 Dasar Regulasi Digital",
    "🧾 Peta Regulasi",
    "🔐 Data Pribadi & Keamanan",
    "🛒 Konsumen & Bisnis Digital",
    "📰 Kasus & Contoh",
    "🧠 Cara Analisis Kasus",
    "📝 Latihan Studi Kasus",
    "🎯 Kuis ",
    "📚 Referensi",
]

if "nav" not in st.session_state:
    st.session_state.nav = "🏠 Beranda"

menu = st.sidebar.radio("Pilih bagian", nav_options, key="nav")

st.sidebar.divider()
st.sidebar.info(
        "Aplikasi ini bukan nasihat hukum untuk kasus tertentu."
)

if menu == "🏠 Beranda":
    st.markdown(
        """
        <div class="hero">
            <h1>Regulasi Bisnis Digital</h1>
            <p>
            Pertemuan 9 • Regulasi dan Hukum Bisnis<br>
            Belajar tentang transaksi digital, sistem elektronik, data pribadi,
            keamanan, perlindungan konsumen, hingga kasus bisnis digital.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.info(
        "Bayangkan Anda mengunduh sebuah aplikasi. Saat mendaftar, aplikasi meminta nama, "
        "nomor HP, lokasi, foto KTP, bahkan akses kontak. Apakah perusahaan bebas menggunakan "
        "semua data itu hanya karena Anda menekan tombol 'Setuju'?"
    )

    section_title("Tujuan belajar")
    c1, c2, c3 = st.columns(3)
    with c1:
        card("1. Paham aturan digital",
             "Mahasiswa mampu menjelaskan mengapa bisnis digital tetap membutuhkan regulasi.")
    with c2:
        card("2. Paham data pribadi",
             "Mahasiswa mampu mengenali data pribadi, hak pengguna, dan kewajiban perusahaan.")
    with c3:
        card("3. Bisa analisis kasus",
             "Mahasiswa mampu menghubungkan masalah bisnis digital dengan aturan yang relevan.")

    section_title("Pertanyaan pembuka")
    answer = st.radio(
        "Apakah perusahaan bebas memakai semua data pengguna setelah pengguna menekan tombol 'Setuju'?",
        [
            "Ya, karena pengguna sudah menyetujui semuanya",
            "Tidak, penggunaan data tetap harus memiliki tujuan dan dasar yang sesuai",
            "Ya, selama aplikasinya gratis",
        ],
        index=None,
    )
    if answer:
        if answer == "Tidak, penggunaan data tetap harus memiliki tujuan dan dasar yang sesuai":
            st.success("Tepat. Persetujuan bukan berarti perusahaan bebas menggunakan data tanpa batas.")
        else:
            st.warning("Belum tepat. Persetujuan tidak otomatis membuat semua penggunaan data menjadi sah.")

    takeaway(
        "Bisnis digital bukan ruang tanpa hukum. Teknologi mengubah cara bisnis dilakukan, "
        "tetapi tidak menghapus hak, kewajiban, dan tanggung jawab."
    )

    
elif menu == "🌐 Dasar Regulasi Digital":
    section_title("1. Apa itu regulasi bisnis digital?")
    st.write(
        """
        Secara sederhana, **regulasi bisnis digital adalah aturan yang mengatur bagaimana
        bisnis menggunakan teknologi, melakukan transaksi elektronik, mengelola data,
        berinteraksi dengan konsumen, dan bertanggung jawab ketika terjadi masalah.**

        Ketika bisnis berpindah dari toko fisik ke website, aplikasi, marketplace,
        cloud, atau media sosial, masalah hukumnya ikut berpindah ke ruang digital.
        """
    )

    section_title("2. Contoh yang dekat dengan mahasiswa")
    st.table([
        {"Aktivitas": "Belanja marketplace", "Masalah hukum": "Barang tidak sesuai, refund, data konsumen"},
        {"Aktivitas": "Pesan makanan online", "Masalah hukum": "Transaksi, pembayaran, tanggung jawab platform"},
        {"Aktivitas": "PayLater", "Masalah hukum": "Kontrak elektronik, data, pembiayaan"},
        {"Aktivitas": "Media sosial", "Masalah hukum": "Konten, iklan, data pengguna"},
        {"Aktivitas": "Ride hailing", "Masalah hukum": "Transaksi, mitra, konsumen, data lokasi"},
        {"Aktivitas": "Aplikasi kesehatan", "Masalah hukum": "Data kesehatan dan keamanan"},
        {"Aktivitas": "AI recommendation", "Masalah hukum": "Profiling dan pemrosesan data"},
    ])

    section_title("3. Mengapa hukum digital cepat berubah?")
    st.write(
        """
        Dulu alur bisnis relatif sederhana:

        **Toko → Pembeli**

        Sekarang satu transaksi digital bisa melibatkan:

        **Seller → Marketplace → Payment System → Logistics → Cloud → Advertiser → Consumer**

        Karena model bisnis berubah, regulator juga harus menyesuaikan aturan.
        """
    )

    takeaway(
        "Saat model bisnis berubah, yang perlu dilihat bukan hanya teknologinya, "
        "tetapi juga siapa pihaknya, apa aktivitasnya, dan siapa yang menanggung risiko."
    )

elif menu == "🧾 Peta Regulasi":
    section_title("Peta hukum bisnis digital di Indonesia")
    st.write("Mahasiswa tidak perlu menghafal seluruh pasal. Yang penting memahami **fungsi setiap aturan**.")

    st.table([
        {"Regulasi": "UU ITE jo. UU No. 1 Tahun 2024",
         "Mudahnya mengatur": "Informasi elektronik dan transaksi elektronik"},
        {"Regulasi": "PP No. 71 Tahun 2019",
         "Mudahnya mengatur": "Penyelenggaraan sistem dan transaksi elektronik"},
        {"Regulasi": "UU No. 27 Tahun 2022 tentang PDP",
         "Mudahnya mengatur": "Pelindungan data pribadi"},
        {"Regulasi": "PP No. 80 Tahun 2019",
         "Mudahnya mengatur": "Perdagangan melalui sistem elektronik"},
        {"Regulasi": "Permendag No. 19 Tahun 2026",
         "Mudahnya mengatur": "Penyelenggaraan usaha perdagangan melalui sistem elektronik"},
        {"Regulasi": "UU No. 8 Tahun 1999",
         "Mudahnya mengatur": "Perlindungan konsumen"},
    ])

    st.warning(
        "Catatan penting: Permendag No. 19 Tahun 2026 merupakan regulasi PMSE terkini "
        "yang menggantikan Permendag No. 31 Tahun 2023."
    )

    section_title("Apa itu sistem elektronik?")
    st.write(
        """
        **Sistem elektronik** secara sederhana adalah sistem yang menggunakan perangkat
        dan teknologi elektronik untuk mengolah, menyimpan, menampilkan, mengirim,
        atau menyebarkan informasi.

        Contoh: marketplace, mobile banking, aplikasi kampus, sistem pembayaran,
        aplikasi HR, dan cloud storage.
        """
    )

    takeaway(
        "Jangan hanya bertanya 'aplikasinya apa?', tetapi juga 'siapa penyelenggaranya?' "
        "dan 'aturan apa yang mengatur aktivitas tersebut?'."
    )

elif menu == "🔐 Data Pribadi & Keamanan":
    section_title("1. Apa itu data pribadi?")
    st.write(
        """
        Secara sederhana, **data pribadi adalah data tentang seseorang yang dapat
        mengidentifikasi orang tersebut, baik secara langsung maupun melalui kombinasi informasi.**
        """
    )

    c1, c2 = st.columns(2)
    with c1:
        card("Contoh data pribadi umum",
             "Nama lengkap, jenis kelamin, kewarganegaraan, status perkawinan, atau kombinasi data yang dapat mengidentifikasi seseorang.")
    with c2:
        card("Contoh data pribadi spesifik",
             "Data kesehatan, biometrik, genetika, catatan kejahatan, data anak, dan data keuangan pribadi.")

    section_title("2. Bukan hanya KTP")
    st.table([
        {"Data": "Nama lengkap", "Potensi data pribadi": "Ya"},
        {"Data": "Nomor HP", "Potensi data pribadi": "Ya"},
        {"Data": "Email personal", "Potensi data pribadi": "Ya"},
        {"Data": "Nomor rekening", "Potensi data pribadi": "Ya"},
        {"Data": "Foto wajah", "Potensi data pribadi": "Ya"},
        {"Data": "Data biometrik", "Potensi data pribadi": "Ya"},
        {"Data": "Riwayat kesehatan", "Potensi data pribadi": "Ya"},
        {"Data": "Lokasi pengguna", "Potensi data pribadi": "Dapat terkait identitas"},
        {"Data": "Riwayat transaksi", "Potensi data pribadi": "Dapat terkait identitas"},
    ])

    section_title("3. Siapa siapa dalam pengelolaan data?")
    c1, c2, c3 = st.columns(3)
    with c1:
        card("👤 Subjek Data", "Orang yang datanya diproses. Contoh: pengguna yang mendaftar aplikasi.")
    with c2:
        card("🏢 Pengendali Data", "Pihak yang menentukan tujuan dan melakukan kendali atas pemrosesan data.")
    with c3:
        card("⚙️ Prosesor Data", "Pihak yang memproses data atas nama pengendali.")

    section_title("4. Klik 'Setuju' bukan berarti bebas")
    st.write(
        """
        Persetujuan bukan berarti:

        > “Perusahaan boleh memakai data saya untuk apa saja dan selamanya.”

        Penggunaan data tetap harus sesuai dengan tujuan, dasar pemrosesan,
        dan ketentuan pelindungan data pribadi.
        """
    )

    section_title("5. Prinsip sederhana")
    st.info("**Ambil seperlunya → gunakan sesuai tujuan → lindungi dengan baik.**")

    st.write(
        """
        Aplikasi pemesanan makanan membutuhkan nama, alamat, dan nomor telepon.
        Tetapi jika aplikasi yang sama meminta **riwayat kesehatan lengkap** tanpa alasan
        yang jelas, pengguna seharusnya bertanya: **untuk apa data tersebut diperlukan?**
        """
    )

    section_title("6. Kalau data bocor?")
    st.write(
        """
        Jika terjadi kegagalan pelindungan data pribadi, perusahaan tidak cukup hanya mengatakan:

        > “Maaf, sistem kami diretas.”

        UU PDP mengatur kewajiban pemberitahuan tertulis paling lambat **3 × 24 jam**
        setelah kegagalan pelindungan data diketahui, sesuai ketentuan yang berlaku.
        """
    )

    st.error(
        "Keamanan sistem dan kepatuhan pelindungan data adalah dua hal yang saling berhubungan, "
        "tetapi tidak sama."
    )

    takeaway(
        "Sistem yang aman belum tentu berarti penggunaan datanya sah. Sebaliknya, "
        "kebijakan privasi yang bagus juga tidak cukup jika sistem keamanannya lemah."
    )

elif menu == "🛒 Konsumen & Bisnis Digital":
    section_title("Perlindungan konsumen dalam bisnis digital")
    st.write(
        """
        Konsumen digital dapat mengalami masalah seperti:

        - barang berbeda dengan deskripsi;
        - pesanan tidak sampai;
        - refund tidak diproses;
        - tagihan/pembayaran bermasalah;
        - akun tidak dapat diakses;
        - layanan tidak sesuai dengan informasi yang diberikan.
        """
    )

    section_title("Contoh alur transaksi digital")
    for step in [
        "1️⃣ Konsumen memilih barang/jasa",
        "2️⃣ Platform menampilkan informasi produk",
        "3️⃣ Konsumen membuat pesanan",
        "4️⃣ Sistem pembayaran memproses transaksi",
        "5️⃣ Merchant menyiapkan barang",
        "6️⃣ Logistik mengirimkan barang",
        "7️⃣ Konsumen menerima dan mengevaluasi",
        "8️⃣ Jika bermasalah → pengaduan / refund / penyelesaian sengketa",
    ]:
        st.markdown(f'<div class="flow">{step}</div>', unsafe_allow_html=True)

    section_title("Siapa yang bertanggung jawab?")
    st.write(
        """
        Dalam satu transaksi digital bisa ada banyak pihak:
        konsumen, merchant, marketplace, penyedia pembayaran, perusahaan logistik,
        dan penyedia teknologi lain.

        Karena itu, jangan langsung bertanya **“siapa yang salah?”**.

        Pertanyaan pertama justru:

        > **“Siapa melakukan apa?”**
        """
    )

    takeaway("Tanggung jawab hukum perlu dilihat berdasarkan peran masing-masing pihak dalam transaksi.")

elif menu == "📰 Kasus & Contoh":
    section_title("Kasus dan perkembangan nyata", "Gunakan kasus ini untuk menghubungkan teori dengan praktik.")

    st.markdown("### Kasus 1 — PSE belum terdaftar")
    st.write(
        """
        Pada Juli 2026, Komdigi memberikan peringatan tertulis kepada sejumlah
        Penyelenggara Sistem Elektronik (PSE) Lingkup Privat yang belum memenuhi kewajiban pendaftaran.

        **Pelajaran:** beroperasi secara digital tidak berarti bebas dari kewajiban administratif
        dan regulasi di Indonesia.
        """
    )
    st.markdown("[Sumber Komdigi](https://portal.komdigi.go.id/kanal-publik/berita-kini/10379)")

    st.divider()

    st.markdown("### Kasus 2 — Perlindungan konsumen digital")
    st.write(
        """
        Pada 2026, Kemendag menindaklanjuti pengaduan konsumen terkait transaksi di platform digital.
        Jenis masalah yang dapat muncul antara lain ketidaksesuaian barang, retur/refund,
        tagihan atau pembayaran digital, pengiriman, dan akses akun.

        **Pelajaran:** bisnis digital harus memiliki mekanisme penyelesaian keluhan yang jelas.
        """
    )
    st.markdown(
        "[Sumber Kemendag](https://www.kemendag.go.id/berita/siaran-pers/fasilitasi-penyelesaian-pengaduan-konsumen-terhadap-tokopedia-dan-tiktok-shop-kemendag-perkuat-perlindungan-konsumen-digital)"
    )

    st.divider()

    st.markdown("### Kasus 3 — AI dan profiling")
    st.write(
        """
        Sebuah e-commerce menggunakan AI untuk menilai perilaku pengguna berdasarkan:
        barang yang dilihat, lokasi, riwayat transaksi, waktu belanja, dan jenis perangkat.

        Sistem kemudian menentukan penawaran yang berbeda untuk pengguna yang berbeda.

        **Pertanyaan kelas:** apakah karena keputusan dibuat oleh algoritma, berarti perusahaan
        tidak lagi bertanggung jawab?
        """
    )
    st.info(
        "Jawabannya tidak sesederhana itu. Pemrosesan otomatis tetap dapat menimbulkan "
        "persoalan hak subjek data, transparansi, dan akuntabilitas."
    )

elif menu == "🧠 Cara Analisis Kasus":
    section_title("Cara berpikir saat menemukan kasus digital")
    st.write("Gunakan formula sederhana **WHO – WHAT – DATA – RULE – RISK – SOLUTION**.")

    for title, body in [
        ("WHO", "Siapa pihaknya?"),
        ("WHAT", "Apa aktivitas bisnisnya?"),
        ("DATA", "Apakah ada data pribadi?"),
        ("RULE", "Aturan apa yang relevan?"),
        ("RISK", "Siapa yang dapat dirugikan?"),
        ("SOLUTION", "Apa penyelesaiannya?"),
    ]:
        card(title, body)

    section_title("Contoh")
    st.write(
        """
        **Kasus:** marketplace mengalami kebocoran akun.

        - **WHO:** platform + pengguna
        - **WHAT:** layanan perdagangan digital
        - **DATA:** email, nomor HP, riwayat transaksi
        - **RULE:** pelindungan data + sistem elektronik
        - **RISK:** penipuan, pencurian akun, penyalahgunaan identitas
        - **SOLUTION:** mitigasi, pemberitahuan, peningkatan keamanan, pengaduan
        """
    )

    section_title("Bisa juga memakai IRAC")
    st.write(
        """
        - **Issue** → apa masalah hukumnya?
        - **Rule** → aturan apa yang relevan?
        - **Application** → bagaimana aturan diterapkan pada fakta?
        - **Conclusion** → apa kesimpulan dan rekomendasinya?
        """
    )

    takeaway(
        "Jangan berhenti pada kalimat 'perusahaan salah'. Jelaskan salahnya di mana, "
        "aturan apa yang relevan, dan apa yang seharusnya dilakukan."
    )

elif menu == "📝 Latihan Studi Kasus":
    section_title("Latihan Studi Kasus")
    tab1, tab2, tab3 = st.tabs(["Kasus A — CampusFood", "Kasus B — Marketplace", "Kasus C — AI Profiling"])

    with tab1:
        st.markdown("### Kasus A — CampusFood")
        st.write(
            """
            Empat mahasiswa membuat aplikasi **CampusFood** untuk memesan makanan di sekitar kampus.
            Saat registrasi, aplikasi meminta nama, nomor mahasiswa, nomor HP, alamat, lokasi real-time,
            foto KTP, akses kontak, dan tanggal lahir.

            Setelah enam bulan, pengguna mencapai 50.000. Suatu hari diketahui bahwa data pelanggan
            dapat diakses melalui URL tanpa login. Manajemen mengetahui masalah tersebut tetapi
            memutuskan tidak memberi tahu pengguna karena belum ada yang komplain.
            """
        )
        st.markdown("**Pertanyaan:**")
        st.write(
            """
            1. Data mana yang termasuk data pribadi?
            2. Apakah semua data tersebut benar-benar diperlukan?
            3. Siapa subjek data pribadi?
            4. Siapa pengendali data pribadi?
            5. Apa masalah keamanan yang muncul?
            6. Apa kewajiban perusahaan setelah mengetahui adanya kegagalan pelindungan data?
            7. Apa risiko yang dapat dialami pengguna?
            8. Apa yang seharusnya dilakukan manajemen?
            """
        )
        st.text_area("Tulis analisis Anda", height=180, key="campusfood")
        with st.expander("Lihat arah pembahasan setelah mencoba"):
            st.write(
                """
                Fokus pada kebutuhan dan relevansi data, identifikasi subjek dan pengendali data,
                keamanan sistem, kewajiban menangani insiden, pemberitahuan sesuai ketentuan,
                risiko penyalahgunaan data, serta perbaikan teknis dan tata kelola.
                """
            )

    with tab2:
        st.markdown("### Kasus B — Barang tidak sesuai dan refund")
        st.write(
            """
            Seorang konsumen membeli smartphone seharga Rp8.000.000 melalui marketplace.
            Barang datang, tetapi spesifikasinya berbeda dari deskripsi. Konsumen mengajukan refund,
            merchant tidak merespons, sementara platform meminta konsumen menunggu.
            """
        )
        st.markdown("**Pertanyaan:**")
        st.write(
            """
            1. Siapa saja pihak yang terlibat?
            2. Apa masalah hukumnya?
            3. Apa hak konsumen yang harus diperhatikan?
            4. Apa tanggung jawab merchant?
            5. Apa peran platform dalam penyelesaian transaksi?
            """
        )
        st.text_area("Tulis analisis Anda", height=180, key="marketplace")
        with st.expander("Lihat arah pembahasan setelah mencoba"):
            st.write(
                """
                Mulailah dengan memetakan pihak dan peran: konsumen, merchant, marketplace,
                pembayaran, dan logistik jika relevan. Hubungkan dengan informasi produk,
                transaksi elektronik, perlindungan konsumen, refund, dan mekanisme pengaduan.
                """
            )

    with tab3:
        st.markdown("### Kasus C — AI Profiling")
        st.write(
            """
            Sebuah e-commerce menggunakan sistem otomatis untuk menilai pengguna berdasarkan
            riwayat transaksi, lokasi, waktu belanja, perangkat, dan barang yang sering dilihat.
            Sistem kemudian memberikan penawaran yang berbeda kepada tiap pengguna.
            """
        )
        st.markdown("**Pertanyaan:**")
        st.write(
            """
            1. Data apa saja yang diproses?
            2. Apa tujuan pemrosesannya?
            3. Apakah pengguna mengetahui adanya profiling?
            4. Apa risiko bagi pengguna?
            5. Mengapa perusahaan tetap harus bertanggung jawab walaupun keputusan dibuat algoritma?
            """
        )
        st.text_area("Tulis analisis Anda", height=180, key="ai_profiling")
        with st.expander("Lihat arah pembahasan setelah mencoba"):
            st.write(
                """
                Fokus pada transparansi, tujuan pemrosesan, hak pengguna, pemrosesan otomatis,
                serta akuntabilitas perusahaan.
                """
            )

elif menu == "🎯 Kuis ":
    section_title("Kuis Interaktif — 10 Soal")
    st.caption("Pilih satu jawaban paling tepat. Nilai dan pembahasan muncul setelah tombol Kirim ditekan.")

    questions = [
        {
            "q": "1. Tujuan utama regulasi bisnis digital adalah...",
            "options": [
                "Membatasi seluruh penggunaan internet",
                "Mengatur aktivitas digital agar hak dan kewajiban para pihak lebih jelas",
                "Menghapus bisnis konvensional",
                "Menggantikan seluruh hukum bisnis",
            ],
            "answer": "Mengatur aktivitas digital agar hak dan kewajiban para pihak lebih jelas",
            "explanation": "Regulasi digital membantu mengatur hak, kewajiban, transaksi, data, dan tanggung jawab dalam aktivitas bisnis berbasis teknologi.",
        },
        {
            "q": "2. Manakah yang paling tepat menggambarkan data pribadi?",
            "options": [
                "Semua informasi yang ada di internet",
                "Hanya nomor KTP",
                "Data tentang seseorang yang dapat mengidentifikasi orang tersebut secara langsung atau melalui kombinasi informasi",
                "Hanya password",
            ],
            "answer": "Data tentang seseorang yang dapat mengidentifikasi orang tersebut secara langsung atau melalui kombinasi informasi",
            "explanation": "Data pribadi tidak terbatas pada KTP atau password. Yang penting adalah keterkaitannya dengan identitas seseorang.",
        },
        {
            "q": "3. Perusahaan menemukan kebocoran data pelanggan. Tindakan yang paling tepat adalah...",
            "options": [
                "Menunggu sampai konsumen mengetahui sendiri",
                "Menyembunyikan kejadian agar reputasi aman",
                "Menghapus seluruh akun pelanggan",
                "Menangani kejadian dan memenuhi kewajiban pemberitahuan sesuai ketentuan",
            ],
            "answer": "Menangani kejadian dan memenuhi kewajiban pemberitahuan sesuai ketentuan",
            "explanation": "Insiden data perlu ditangani, didokumentasikan, dimitigasi, dan diberitahukan sesuai kewajiban hukum yang berlaku.",
        },
        {
            "q": "4. Pernyataan yang paling tepat mengenai keamanan sistem dan pelindungan data adalah...",
            "options": [
                "Sistem yang aman otomatis membuat semua penggunaan data sah",
                "Persetujuan membuat perusahaan bebas memakai data apa pun",
                "Keamanan teknologi dan kepatuhan pelindungan data berhubungan tetapi bukan hal yang sama",
                "Data digital tidak memiliki perlindungan hukum",
            ],
            "answer": "Keamanan teknologi dan kepatuhan pelindungan data berhubungan tetapi bukan hal yang sama",
            "explanation": "Sistem dapat aman tetapi pemrosesan datanya belum tentu sah; kebijakan privasi saja juga tidak cukup jika sistem keamanannya lemah.",
        },
        {
            "q": "5. Regulasi PMSE yang berlaku pada 2026 dan menggantikan Permendag No. 31 Tahun 2023 adalah...",
            "options": [
                "Permendag No. 19 Tahun 2026",
                "PP No. 71 Tahun 2019",
                "UU No. 27 Tahun 2022",
                "UU No. 8 Tahun 1999",
            ],
            "answer": "Permendag No. 19 Tahun 2026",
            "explanation": "Permendag No. 19 Tahun 2026 menjadi regulasi PMSE terkini dan menggantikan Permendag No. 31 Tahun 2023.",
        },
        {
            "q": "6. Sebuah aplikasi cuaca meminta akses seluruh kontak pengguna. Pertanyaan yang paling tepat adalah...",
            "options": [
                "Berapa banyak pengguna aplikasi?",
                "Apakah data tersebut benar-benar diperlukan dan digunakan untuk tujuan yang jelas?",
                "Siapa pembuat desain aplikasinya?",
                "Berapa harga aplikasinya?",
            ],
            "answer": "Apakah data tersebut benar-benar diperlukan dan digunakan untuk tujuan yang jelas?",
            "explanation": "Pengumpulan data harus dinilai berdasarkan kebutuhan, relevansi, dan tujuan pemrosesan.",
        },
        {
            "q": "7. Siapa yang disebut sebagai pengendali data pribadi?",
            "options": [
                "Orang yang sekadar memakai smartphone",
                "Semua karyawan perusahaan",
                "Pihak yang menentukan tujuan dan melakukan kendali atas pemrosesan data pribadi",
                "Hanya perusahaan penyedia internet",
            ],
            "answer": "Pihak yang menentukan tujuan dan melakukan kendali atas pemrosesan data pribadi",
            "explanation": "Pengendali data menentukan tujuan dan kendali atas pemrosesan data pribadi.",
        },
        {
            "q": "8. Aplikasi pemesanan makanan meminta data kesehatan lengkap tanpa tujuan yang jelas. Prinsip yang paling tepat adalah...",
            "options": [
                "Mengumpulkan seluruh data karena mungkin berguna suatu hari nanti",
                "Mengumpulkan data sebanyak mungkin selama pengguna punya akun",
                "Data konsumen tidak perlu dibatasi",
                "Mengumpulkan data yang relevan dan diperlukan untuk tujuan pemrosesan",
            ],
            "answer": "Mengumpulkan data yang relevan dan diperlukan untuk tujuan pemrosesan",
            "explanation": "Data sebaiknya dikumpulkan sesuai kebutuhan dan tujuan yang jelas, bukan sebanyak mungkin.",
        },
        {
            "q": "9. Menurut UU PDP, pemberitahuan tertulis atas kegagalan pelindungan data pribadi pada prinsipnya dilakukan paling lambat...",
            "options": [
                "3 × 24 jam setelah kegagalan pelindungan data diketahui",
                "30 hari",
                "14 hari",
                "Setelah ada konsumen yang mengadu",
            ],
            "answer": "3 × 24 jam setelah kegagalan pelindungan data diketahui",
            "explanation": "UU PDP mengatur batas pemberitahuan tertulis paling lambat 3 × 24 jam sesuai ketentuan.",
        },
        {
            "q": "10. Sebuah marketplace menggunakan sistem otomatis untuk menentukan penawaran berdasarkan profil pengguna. Hal yang penting diperhatikan adalah...",
            "options": [
                "Algoritma selalu benar sehingga tidak perlu dipertanyakan",
                "Pemrosesan otomatis tetap dapat menimbulkan persoalan hak subjek data dan akuntabilitas perusahaan",
                "AI tidak termasuk bagian dari aktivitas bisnis digital",
                "Perusahaan tidak perlu menjelaskan penggunaan data karena dilakukan komputer",
            ],
            "answer": "Pemrosesan otomatis tetap dapat menimbulkan persoalan hak subjek data dan akuntabilitas perusahaan",
            "explanation": "Keputusan otomatis tidak menghapus kebutuhan akan transparansi, perlindungan hak subjek data, dan tanggung jawab perusahaan.",
        },
    ]

    with st.form("quiz_form"):
        selected = {}
        for i, item in enumerate(questions):
            selected[i] = st.radio(
                item["q"],
                item["options"],
                index=None,
                key=f"quiz_{i}",
            )
            st.write("")
        submitted = st.form_submit_button("Kirim Jawaban", type="primary", use_container_width=True)

    if submitted:
        unanswered = sum(1 for i in range(len(questions)) if selected[i] is None)
        if unanswered:
            st.warning(
                f"Masih ada {unanswered} soal yang belum dijawab. "
                "Nilai tetap dihitung dari jawaban yang sudah dipilih."
            )

        score = sum(1 for i, item in enumerate(questions) if selected[i] == item["answer"])
        pct = round(score / len(questions) * 100)

        st.markdown("---")
        st.markdown(f"## Nilai: {score}/10 ({pct}%)")
        st.progress(score / len(questions))

        if score == 10:
            st.success("Sangat baik! Semua konsep utama sudah dipahami.")
        elif score >= 8:
            st.success("Bagus sekali. Pemahaman Anda sudah kuat.")
        elif score >= 6:
            st.info("Cukup baik. Coba perkuat bagian yang masih tertukar.")
        else:
            st.warning("Coba baca kembali materi sebelum mengulang kuis.")

        st.markdown("### Pembahasan")
        for i, item in enumerate(questions):
            if selected[i] == item["answer"]:
                st.success(f"Soal {i+1}: Benar — {item['explanation']}")
            else:
                st.error(
                    f"Soal {i+1}: Belum tepat. Jawaban yang tepat: **{item['answer']}**. "
                    f"{item['explanation']}"
                )

elif menu == "📚 Referensi":
    section_title("Referensi dan dasar materi")

    st.markdown(
        """
        ### Referensi utama sesuai RPS
        **Cheeseman, H. R. (2020). _Business Law: Legal Environment, Online Commerce,
        Business Ethics, and International Issues_ (10th Edition). Pearson.**

        ### Regulasi dan sumber resmi pendukung
        """
    )

    refs = [
        ("UU No. 1 Tahun 2024",
         "Perubahan kedua atas Undang-Undang Informasi dan Transaksi Elektronik",
         "https://peraturan.bpk.go.id/Details/274494/uu-no-1-tahun-2024"),
        ("PP No. 71 Tahun 2019",
         "Penyelenggaraan Sistem dan Transaksi Elektronik",
         "https://peraturan.bpk.go.id/Details/122030/pp-no-71-tahun-2019"),
        ("UU No. 27 Tahun 2022",
         "Pelindungan Data Pribadi",
         "https://peraturan.bpk.go.id/Details/229798/uu-no-27-tahun-2022"),
        ("PP No. 80 Tahun 2019",
         "Perdagangan Melalui Sistem Elektronik",
         "https://peraturan.bpk.go.id/Details/126143/pp-no-80-tahun-2019"),
        ("Permendag No. 19 Tahun 2026",
         "Penyelenggaraan Usaha Perdagangan Melalui Sistem Elektronik",
         "https://jdih.kemendag.go.id/peraturan/peraturan-menteri-perdagangan-republik-indonesia-nomor-19-tahun-2026-tentang-penyelenggaraan-usaha-perdagangan-melalui-sistem-elektronik-1"),
        ("UU No. 8 Tahun 1999",
         "Perlindungan Konsumen",
         "https://peraturan.bpk.go.id/Details/45288/uu-no-8-tahun-1999"),
        ("Komdigi — PSE 2026",
         "Peringatan terhadap PSE Lingkup Privat yang belum memenuhi kewajiban pendaftaran",
         "https://portal.komdigi.go.id/kanal-publik/berita-kini/10379"),
        ("Kemendag — Perlindungan Konsumen Digital 2026",
         "Fasilitasi penyelesaian pengaduan konsumen terhadap platform digital",
         "https://www.kemendag.go.id/berita/siaran-pers/fasilitasi-penyelesaian-pengaduan-konsumen-terhadap-tokopedia-dan-tiktok-shop-kemendag-perkuat-perlindungan-konsumen-digital"),
    ]

    for name, desc, url in refs:
        st.markdown(f"**[{name}]({url})**  \n{desc}")

    st.divider()
    st.warning(
        "Regulasi dapat berubah. Untuk penggunaan di luar pembelajaran kelas, "
        "cek kembali versi peraturan terbaru melalui situs resmi BPK, Komdigi, Kemendag, atau JDIH terkait."
    )

    st.markdown("### Ringkasan 5 hal yang wajib diingat")
    st.write(
        """
        1. **Bisnis digital bukan ruang tanpa hukum.**
        2. **Data pribadi bukan hanya KTP dan password.**
        3. **Persetujuan tidak berarti perusahaan bebas menggunakan data tanpa batas.**
        4. **Keamanan sistem dan pelindungan data sama-sama penting.**
        5. **Dalam kasus digital, selalu tanyakan: siapa pihaknya, apa aktivitasnya, data apa yang digunakan, aturan apa yang berlaku, dan siapa yang dapat dirugikan.**
        """
    )
