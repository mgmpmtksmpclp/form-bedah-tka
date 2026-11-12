# Form Pendaftaran Bedah TKA 2026/2027

Form pendaftaran Bedah TKA TP 2026/2027 Kabupaten Cilacap (Kelas 9).
Repo: https://github.com/mgmpmtksmpclp/form-bedah-tka
Tayang di https://tka.mgmpmtkcilacap.web.id (VPS).

## Isi form

- **NPSN** (8 digit) — begitu 8 digit, Nama Sekolah + Kecamatan + Komda
  terisi otomatis dari daftar 195 SMP Kab. Cilacap. Bila NPSN tidak
  ditemukan dalam daftar, ketiga field itu terbuka dan bisa diisi manual.
- **Data Peserta** — Nama + NIP Guru Bahasa Indonesia dan
  Guru Matematika. NIP boleh kosong bila guru honorer tanpa NIP;
  bila diisi harus 18 digit angka.
- **Data Murid Kelas 9** — unggah file CSV/Excel (template tersedia di
  form, kolom: No, Nama, NIS, NISN, Kelas).

Satu NPSN hanya boleh terdaftar satu kali. Data tersimpan di Google
Sheet (tab "Pendaftaran") dan file data murid tersimpan di folder
Drive "Data Murid TKA".

## Struktur situs

Situs ini nantinya berisi beberapa tautan — saat ini baru halaman
pendaftaran (`index.html`). Rencana berikutnya: halaman **cek peserta**.
Halaman baru ditambahkan sebagai file HTML terpisah di repo ini
(mis. `cek-peserta.html`) lalu ditautkan dari halaman utama.

## File

- `index.html` — form (satu file, sudah berisi data 195 sekolah).
- `Code.gs` — backend Google Apps Script.
- `Template-Data-Murid-Kelas-9.csv` — template data murid.
- `PANDUAN.txt` — panduan pasang lengkap (Sheet + Apps Script + VPS).
- `build_index.py` — pembangun `index.html` (baca `data-sekolah.csv`,
  sisipkan ke template).
- `data-sekolah.csv` — daftar 195 SMP Kab. Cilacap (sumber data NPSN).

## Cara update

1. Ubah `build_index.py` (atau `data-sekolah.csv`), lalu jalankan
   `python3 build_index.py` untuk membangun ulang `index.html`.
2. Commit + push ke repo ini.
3. Di VPS: `cd /home/ubuntu/form-bedah-tka && git pull && sudo chmod -R a+rX .`
