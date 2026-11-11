# Form Pendaftaran Bedah TKA 2026/2027

Form pendaftaran Bedah TKA TP 2026/2027 Kabupaten Cilacap (Kelas 9).
Repo: https://github.com/mgmpmtksmpclp/form-tka
Tayang di https://tka.mgmpmtkcilacap.web.id (VPS).

## Isi form

- **NPSN** (8 digit) — begitu 8 digit, Nama Sekolah + Kecamatan + Komda
  terisi otomatis dari daftar 195 SMP Kab. Cilacap.
- **Data Peserta** — Nama + NIP (18 digit) Guru Bahasa Indonesia dan
  Guru Matematika.
- **Data Murid Kelas 9** — unggah file CSV/Excel (template tersedia di
  form, kolom: No, Nama, NIS, NISN, Kelas).

Satu NPSN hanya boleh terdaftar satu kali. Data tersimpan di Google
Sheet (tab "Pendaftaran") dan file data murid tersimpan di folder
Drive "Data Murid TKA".

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
3. Di VPS: `cd /home/ubuntu/form-tka && git pull && sudo chmod -R a+rX .`
