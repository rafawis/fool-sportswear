# https://rafa-pradipta-foolsportswear.pbp.cs.ui.ac.id/

Tugas 2:

1. Membuat sebuah proyek Django baru
    Untuk step ini, kita harus membuat direktori baru dan memasukkan text file requirements yang diisi dengan semua dependencies yang akan dibutuh, selanjutnya kita bikin project django di direktori tersebut, selanjutnya kita membuat file env dan env.prod untuk set variabel environment untuk set konfigurasi, kredensial database, API keys, dll, ini memungkinkan kita untuk menjalankan kode di environment tanpa harus mengubah kode kita. .env akan dipakai buat testing dan development, ini akan pakai SQLite, tetapi .env.prod dipakai untuk deployment, ini akan memakai PostgreSQL.

    Di file settings.py kita harus memastikan variabel environment dibaca, maka kita akan import dotenv untuk membaca isi .env. Selain itu kita juga harus menambah "localhost","127.0.0.1", dan link PWS PBP. Dua host pertama ditambahkan agar bisa mengakses aplikasi secara lokal, dan host terakhir dipakai agar bisa membuka aplikasi dari website PWS.

    Setelah kita git add, commit, dan push ke origin master dan pws, kita bisa ngecek kalau aplikasi kita bisa diakses secara lokal dan lewat PWS. Setelah dikonfirmasi bekerja, kita akan modifikasi aplikasi kita untuk menunjukkan sesuatu agar tidak kosong. Untuk itu kita menjalankan "python manage.py startapp main" untuk membuat aplikasi baru dalam proyek kita, dalamnya kita akan buat model Product, yang memiliki beberapa field.
    Charfield -> untuk menyimpan teks pendek
        - name: untuk menyimpan nama produk
        - category: untuk menyimpan kategori produk, atribut ini akan mengambil dari CATEGORY_CHOICES yg berupa kategori dari produk, seperti jersey, celana, sepatu, dll.
    IntegerField -> menyimpan nomor bulat
        - price: untuk menyimpan harga produk
    TextField -> untuk menyimpan teks panjang
        - description: untuk keterangan dari produk
    URLField -> menyimpan link
        - thumbnail: untuk menyimpan foto produk
    BooleanField -> menyimpan true or false
        - isFeatured: untuk liat status unggulan produk

    Setelah setup model, kita membuat direktori templates yang mempunyai main.html didalamnya, disini kita menunjukkan nama aplikasi, nama, dan kelas. Untuk isinya, kita akan memakai placeholder, misalnya {{ name }}, ini berarti isi dari placeholder-placeholder akan bergantung dari input di file views, di file views kita membuat function show_main(request) yang memiliki dictionary context yang akan dipakai untuk memiliki key "name", "kelas", dan "nama_aplikasi" dan memilki value nama kita, kelas kita, dan nama aplikasi kita. Selanjutnya kita akan mengganti file urls.py jadi ketika main.urls dipanggil, akan memanggil show_main jadi placeholder diganti dengan value yang ingin ditampilkan. Agar main.urls dipanggil, kita juga membuat agar ketika URL proyek dipanggil, akan membuka main.urls.

    Setelah melakukan semua ini kita akan melakukan git add, commit, dan push terakhir untuk menyelesaikan tugas 2. Setelah di push kalau kita cek aplikasi kita, placeholder akan sukses diganti dengan value yang ingin ditunjukkan.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

    User akan mengirim request ke internet, yang akan mengirim request itu ke aplikasi kita, selanjutnya akan memasuki urls.py untuk mengecek mau dirutekan kemana, dari urls.py akan masuk ke views.py, file ini akan interaksi dengan models.py dan templates.py:
        models.py: membaca dan manipulasi database
        templates.py: tampilan website
    views.py akan mengambil data dari models.py dan modifikasi dan memilih tampilan dari templates.py untuk menampilkan websitenya. Yang ditunjuk di templates akan ditampilkan di web page.

3. Peran settings.py
    settings.py adalah file yang mengkonfigurasikan proyek kita, perilaku yang akan dilakukan proyek kita akan dikonfigurasi di settings.py, contoh darinya adalah ALLOWED_HOSTS agar kita bisa membuka proyek di web page, selain itu ada konfigurasi settings database, penggunaan .env, aplikasi yang dipakai, dll.

4. Cara kerja migrasi database
Django memakai migrasi untuk mencocokan perubahan di models.py kepada database

manage.py makemigrations -> membuat file migration yang menunjukkan apa yang diganti di models.py, disini kita harus memastikan apa yang digganti disini sesuai dengan apa yang diinginkan

manage.py migrate -> membaca file migration dan apply perubahan kepada skema database.

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
    - Django memiliki library yang besar dan ekstensif jadi developer tidak harus import/download banyak library lain
    - Django sangat aman dan membantu melindungi dari banyak serangan cyber seperti SQL injection, CSRF, dll.
    - Django sudah memiliki banyak fitur dan komponen yang umum dibutuhkan di web sehingga developer tidak butuh membuat ulang
    - Memakai language python yang mudah dipakai dan jelas
    - Framework memiliki skalabilitas yang kuat sehingga sering dipakai perusahaan jadi apa yang dipelajari disini akan dipakai di masa depan.

6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
    Tutorial jelas dan mudah dilakukan.



Tugas 3:
1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Agar platform kita bisa menerima data dari input user dan bisa mengirim data agar bisa menampilkan data

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
    Json lebih baik dan populer dari JSON
    - JSON memakai javascript yang lebih umum dipakai
    - Lebih mudah untuk dilihat/dibaca
    - Parsing yang lebih cepat dan bisa dilakukan dengan fungsi javascript
    - memakai mapping yang menunjukkan key-value pairing yang lebih mudah dibaca 

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Ngecek input user/form dan memastikan kalau input benar dan gaada error, kalau inputnya udah valid baru akan disave ke database, tapi kalau invalid data yang memilki error tidak akan di save di database

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
Menjaga dari CSRF attack, dimana penyerang bisa membuat request menggunakan kredensial user lain. Dengan CSRF, website akan ngecek kalau request yang dikirim memilki token, kalau tidak memilki token tsb, request tidak akan diterima

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- Menyalakan virtual environment
- mengganti dirs menjadi base dir/templates agar memakai base.html sebagai basis/template utama untuk html kita
- membuat file baru forms.py di main yang membuat form yang menerima product baru
- membuat beberapa fungsi baru di views.py, ada yang untuk membuat form baru, menampilkan form, dan untuk melihat xml/json dan filter darinya dengan primary key
- mengganti urls.py untuk menambahkan path yang mengakses fungsi baru yang kita buat
- cek dengan runserver di localhost kalau semua yang digganti bekerja dengan benar
- push ke pws dan repository git

6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
bagus dan jelas.

Tugas 4:
1.  Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.

2. Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
Authentikasi adalah ketika kita ngecek kalau user yang lagi login adalah user benerannya, bukan penyerang.
Otorisasi adalah ketika kita memilih apa saja yang bisa dilakukan oleh suatu user/role.

3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?

Cookies:
- Lebih ringan
- Cepat diakses
- Disimpan sampai expire atau didelete

Cons:
- Bisa dimodify user
- Mudah dipakai penyerang untuk hijack, XSS, CSRF, etc.

Session:
Pros:
- Bisa menyimpan banyak tipe data dan
- Data disimpan di server sehingga lebih aman
- Langsung dihapus ketika user logout/tutup browser

Cons:
- Berat di server untuk load dan storage karena

4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
Ada risiko, misalnya XSS attack, di attack ini, penyerang akan exploit situs web untuk mengambil cookie dari user dan memakai cookie tsb untuk mengakses data sensitif user dan hal-hal lain. Untuk ini, django memiliki beberapa cara untuk menangani penyerangan, ada CSRF token yang membantu authentikasi kalau yang mengirim request dari user asli, bukan dari penyerang.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Step pertama adalah untuk membuat fungsi registrasi, fungsi ini membuat form dan meminta user untuk mengisi untuk membuat user baru, jika semua yang diisi udah benar, form dan user akan disave. Setelah membuat fungsi kita juga harus membuat html baru khusus untuk registrasi dan masukkan ke urls. Disini kita harus mengimpor messages dan UserCreationForm dari library Django


step kedua adalah untuk membuat fungsi login, disini kita meminta login info user dan akan cek di database kalau ada usernya, disini kita juga harus membuat url dan html baru. Untuk ini kita harus mengimpor AuthenticationForm, authenticate, dan login dari django.contrib.auth

step ketiga untuk membuat fungsi logout, fungsi ini akan logout user, dan unutk ini kita hanya butuh membuat button untuk logout di halaman main.html. disini kita harus mengimpor logout

step keempat adalah authentikasi, disini kita mengimpor login_required jadi untuk akses main dan untuk melihat product, user harus login dulu. 

Step kelima kita menyimpan cookies user, untuk ini kita mengimpor  datetime, HttpResponseRedirect dan menyimpan kapan user login ke web kita. Browser akan menyimpan kapan kita login dan akan ditampilkan di web.

Step keenam adalah untuk menggabungkan user dan product, disini kita akan mengubah class Product untuk menyimpan user dan akan menampilkan user yang membuat post/listing. Disini kita harus mengimpor User ke models, dan membuat user jadi atribut model Product. Selanjutnya kita di views akan menyimpan user yang create product baru, terus kita menambah filtering ke show product agar user bisa memilih antara melihat semua produk atau hanya yang dibuat user. Terakhir kita harus mengubah html main untuk menampilkan filtering tsb dan mengubah product_detail untuk menampilkan author/seller.

Step terakhir adalah untuk push ke git dan pws.

