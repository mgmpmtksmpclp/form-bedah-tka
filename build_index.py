# -*- coding: utf-8 -*-
"""Bangun index.html Form Pendaftaran TKA (data 195 sekolah disisipkan)."""
import csv, json, os

SRC = os.path.dirname(os.path.abspath(__file__))
rows = list(csv.DictReader(open(os.path.join(SRC, 'data-sekolah.csv'), encoding='utf-8-sig')))
# format ringkas: [NPSN, Nama, Kecamatan, Komda]
data = [[r['NPSN'].strip(), r['Nama Satuan Pendidikan'].strip(), r['Kecamatan'].strip(), r['Komda'].strip()] for r in rows]
DATA_JSON = json.dumps(data, ensure_ascii=False, separators=(',', ':'))

HTML = r"""<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Form Pendaftaran Bedah TKA 2026/2027</title>
<style>
* { box-sizing: border-box; }
body { font-family: "Times New Roman", Times, serif; background: #fff8e1; margin: 0; padding: 18px 14px; color: #1f2937; }
.kartu { max-width: 620px; margin: 0 auto; background: #fff; border-radius: 18px; overflow: hidden; box-shadow: 0 10px 30px rgba(15,118,110,.18); }
.kepala { background: linear-gradient(90deg,#075985,#0369a1 50%,#0ea5e9); padding: 24px 24px 18px; color: #fff; }
.kepala-isi { display: flex; align-items: flex-start; gap: 10px; }
.kepala-ikon { font-size: 26px; line-height: 1.25; }
.kepala h1 { margin: 0; font-size: 26px; }
.kepala p { margin: 6px 0 0; font-size: 15px; opacity: .95; }
.isi { padding: 8px 24px 22px; }
label { display: block; font-size: 14px; font-weight: bold; color: #0f766e; margin: 18px 0 6px; }
label .wajib { color: #dc2626; }
input, select { width: 100%; padding: 12px 14px; border: 1.5px solid #d1d5db; border-radius: 10px; font-size: 15px; font-family: inherit; background: #fff; color: #1f2937; }
input:focus { outline: none; border-color: #0f766e; box-shadow: 0 0 0 3px rgba(15,118,110,.15); }
input[readonly] { background: #f3f4f6; color: #374151; }
input.galat { border-color: #dc2626; }
.hint { font-size: 13px; color: #6b7280; margin: 5px 0 0; }
.hint.galat { color: #dc2626; font-weight: bold; }
.hint.ok { color: #15803d; font-weight: bold; }
button.kirim { background: linear-gradient(180deg,#f97316,#ea580c); color: #fff; border: 0; border-radius: 12px; padding: 14px 20px; font-size: 16px; font-weight: bold; cursor: pointer; margin-top: 24px; width: 100%; box-shadow: 0 4px 14px rgba(234,88,12,.35); font-family: inherit; }
button.kirim:disabled { opacity: .55; box-shadow: none; cursor: wait; }
button.templat { background: #fff; color: #0f766e; border: 1.5px solid #0f766e; border-radius: 10px; padding: 10px 16px; font-size: 14px; font-weight: bold; cursor: pointer; margin-top: 8px; font-family: inherit; }
button.templat:hover { background: #f0fdfa; }
.pesan { margin-top: 16px; font-size: 14px; padding: 13px 15px; border-radius: 10px; display: none; line-height: 1.5; }
.pesan.ok { background: #dcfce7; border: 1px solid #86efac; display: block; }
.pesan.galat { background: #fee2e2; border: 1px solid #fca5a5; display: block; }
.fileinfo { font-size: 13px; color: #15803d; margin: 6px 0 0; font-weight: bold; }
.bagian { border-top: 2px solid #fde68a; margin-top: 22px; padding-top: 4px; }
.bagian h2 { font-size: 17px; color: #b45309; margin: 14px 0 0; }
.kaki { font-size: 12px; color: #9ca3af; text-align: center; margin: 18px 0 0; }
</style>
</head>
<body>
<div class="kartu">
  <div class="kepala">
    <div class="kepala-isi">
      <span class="kepala-ikon">📋</span>
      <div>
        <h1>Form Pendaftaran Bedah TKA 2026/2027</h1>
        <p>Panitia Bedah TKA TP 2026/2027 Kabupaten Cilacap</p>
      </div>
    </div>
  </div>
  <div class="isi">
    <form id="formTKA" novalidate>
      <div class="bagian"><h2>🏫 Data Sekolah</h2></div>

      <label for="npsn">NPSN <span class="wajib">*</span></label>
      <input id="npsn" inputmode="numeric" autocomplete="off" maxlength="8"
             placeholder="Contoh: 20331749">
      <p class="hint" id="npsnHint">Ketik 8 digit NPSN &mdash; nama sekolah dan Komda akan muncul otomatis.</p>

      <label for="sekolah">Nama Sekolah</label>
      <input id="sekolah" readonly placeholder="— terisi otomatis dari NPSN —">

      <label for="kecamatan">Kecamatan</label>
      <input id="kecamatan" readonly placeholder="— terisi otomatis dari NPSN —">

      <label for="komda">Komda</label>
      <input id="komda" readonly placeholder="— terisi otomatis dari NPSN —">

      <div class="bagian"><h2>👥 Data Peserta</h2></div>

      <label for="guruBindo">Nama Guru Bahasa Indonesia <span class="wajib">*</span></label>
      <input id="guruBindo" autocomplete="off" placeholder="Contoh: Siti Aminah, S.Pd.">

      <label for="nipBindo">NIP Guru Bahasa Indonesia</label>
      <input id="nipBindo" inputmode="numeric" autocomplete="off" maxlength="18"
             placeholder="Contoh: 198506122009032001 (18 digit)">
      <p class="hint">Kosongkan bila guru honorer tanpa NIP. Bila diisi, harus 18 digit angka.</p>

      <label for="guruMat">Nama Guru Mata Pelajaran Matematika <span class="wajib">*</span></label>
      <input id="guruMat" autocomplete="off" placeholder="Contoh: Budi Santoso, S.Pd.">

      <label for="nipMat">NIP Guru Mata Pelajaran Matematika</label>
      <input id="nipMat" inputmode="numeric" autocomplete="off" maxlength="18"
             placeholder="Contoh: 198803152010011002 (18 digit)">
      <p class="hint">Kosongkan bila guru honorer tanpa NIP. Bila diisi, harus 18 digit angka.</p>

      <div class="bagian"><h2>🧑‍🎓 Data Murid Kelas 9</h2></div>

      <label>Upload Data Murid Kelas 9 <span class="wajib">*</span></label>
      <button type="button" class="templat" id="btnTemplat">⬇ Unduh Template Data Murid (CSV)</button>
      <p class="hint">Unduh templatenya, isi data, lalu unggah kembali file-nya di bawah ini.</p>
      <input id="fileMurid" type="file" accept=".csv,.xls,.xlsx" style="margin-top:10px">
      <p class="hint">Format file: CSV atau Excel (.xls / .xlsx).</p>
      <p class="fileinfo" id="fileInfo" style="display:none"></p>

      <button type="submit" class="kirim" id="btnKirim">Kirim Pendaftaran</button>
      <p class="kaki">Satu pendaftaran per sekolah (satu NPSN). Bila sudah terdaftar, hubungi panitia untuk perubahan data.</p>
    </form>
    <div class="pesan" id="pesan"></div>
  </div>
</div>

<script>
// =====================================================================
// KONFIGURASI — GANTI SETELAH DEPLOY APPS SCRIPT:
// Tempel URL Web App (diakhiri /exec) dari Deploy > New deployment.
// =====================================================================
var WEBAPP_URL = "https://script.google.com/macros/s/AKfycbzxkADr1Zu5okSyLcuKqhd7OlYS1PO6s_yoYQpxyChmUc9iS3G4iMK8Do4AS96jVvaq/exec";

// Data sekolah (195 SMP Kab. Cilacap): [NPSN, Nama, Kecamatan, Komda]
var DATA_SEKOLAH = __DATA_JSON__;

var PETA = {};
DATA_SEKOLAH.forEach(function (r) { PETA[r[0]] = r; });

var el = function (id) { return document.getElementById(id); };
var fileMurid = null; // {nama, tipe, data (base64)}

function bersihAngka(s) { return (s || "").replace(/[^0-9]/g, ""); }

// Bila NPSN tidak ditemukan dalam daftar, ketiga field sekolah dibuka
// untuk diisi manual; bila ditemukan (atau NPSN dihapus) dikunci lagi.
function aturManualSekolah(bisa) {
  ["sekolah", "kecamatan", "komda"].forEach(function (id) { el(id).readOnly = !bisa; });
  el("sekolah").placeholder = bisa ? "Ketik nama sekolah" : "— terisi otomatis dari NPSN —";
  el("kecamatan").placeholder = bisa ? "Ketik kecamatan" : "— terisi otomatis dari NPSN —";
  el("komda").placeholder = bisa ? "Ketik Komda" : "— terisi otomatis dari NPSN —";
}

el("npsn").addEventListener("input", function () {
  var npsn = bersihAngka(this.value);
  this.value = npsn;
  var hint = el("npsnHint");
  if (npsn.length === 0) {
    hint.textContent = "Ketik 8 digit NPSN — nama sekolah dan Komda akan muncul otomatis.";
    hint.className = "hint";
    el("sekolah").value = ""; el("kecamatan").value = ""; el("komda").value = "";
    aturManualSekolah(false);
    this.classList.remove("galat");
    return;
  }
  if (npsn.length < 8) {
    hint.textContent = "NPSN masih " + npsn.length + " digit — lanjutkan sampai 8 digit.";
    hint.className = "hint";
    el("sekolah").value = ""; el("kecamatan").value = ""; el("komda").value = "";
    aturManualSekolah(false);
    this.classList.remove("galat");
    return;
  }
  var r = PETA[npsn];
  if (r) {
    el("sekolah").value = r[1];
    el("kecamatan").value = r[2];
    el("komda").value = r[3];
    aturManualSekolah(false);
    hint.textContent = "✓ Sekolah ditemukan: " + r[1] + " — Komda " + r[3] + ".";
    hint.className = "hint ok";
    this.classList.remove("galat");
  } else {
    el("sekolah").value = ""; el("kecamatan").value = ""; el("komda").value = "";
    aturManualSekolah(true);
    hint.textContent = "⚠ NPSN tidak ditemukan dalam daftar 195 SMP Kab. Cilacap. Silakan isi Nama Sekolah, Kecamatan, dan Komda di bawah ini secara manual.";
    hint.className = "hint";
    this.classList.remove("galat");
  }
});

["nipBindo", "nipMat"].forEach(function (id) {
  el(id).addEventListener("input", function () { this.value = bersihAngka(this.value); });
});

// ---- Template CSV data murid ----
var TEMPLATE_CSV =
  "No,Nama,NIS,NISN,Kelas\r\n" +
  "1,,,,\r\n" +
  "2,,,,\r\n" +
  "3,,,,\r\n";

el("btnTemplat").addEventListener("click", function () {
  var blob = new Blob(["\ufeff" + TEMPLATE_CSV], { type: "text/csv;charset=utf-8" });
  var a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = "Template-Data-Murid-Kelas-9.csv";
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  setTimeout(function () { URL.revokeObjectURL(a.href); }, 1000);
});

// ---- Pilih file data murid ----
el("fileMurid").addEventListener("change", function () {
  var f = this.files && this.files[0];
  var info = el("fileInfo");
  fileMurid = null;
  if (!f) { info.style.display = "none"; return; }
  var reader = new FileReader();
  reader.onload = function (ev) {
    var dataUrl = String(ev.target.result || "");
    fileMurid = { nama: f.name, tipe: f.type || "application/octet-stream", data: dataUrl.split(",")[1] || "" };
    info.style.display = "block";
    info.style.color = "#15803d";
    info.textContent = "✓ File dipilih: " + f.name + " (" + (f.size / 1024).toFixed(0) + " KB).";
  };
  reader.readAsDataURL(f);
});

function tampilPesan(ok, html) {
  var p = el("pesan");
  p.className = "pesan " + (ok ? "ok" : "galat");
  p.innerHTML = html;
  p.scrollIntoView({ behavior: "smooth", block: "center" });
}

el("formTKA").addEventListener("submit", function (ev) {
  ev.preventDefault();
  var npsn = el("npsn").value.trim();
  var sekolah = el("sekolah").value.trim();
  var kecamatan = el("kecamatan").value.trim();
  var komda = el("komda").value.trim();
  var guruBindo = el("guruBindo").value.trim();
  var nipBindo = el("nipBindo").value.trim();
  var guruMat = el("guruMat").value.trim();
  var nipMat = el("nipMat").value.trim();

  if (npsn.length !== 8) return tampilPesan(false, "<b>NPSN belum benar.</b> Isi 8 digit NPSN sekolah.");
  if (!sekolah) return tampilPesan(false, "<b>Nama Sekolah</b> wajib diisi — terisi otomatis dari NPSN, atau ketik manual bila NPSN tidak ditemukan.");
  if (!kecamatan) return tampilPesan(false, "<b>Kecamatan</b> wajib diisi.");
  if (!komda) return tampilPesan(false, "<b>Komda</b> wajib diisi.");
  if (!guruBindo) return tampilPesan(false, "<b>Nama Guru Bahasa Indonesia</b> wajib diisi.");
  if (nipBindo && !/^[0-9]{18}$/.test(nipBindo)) return tampilPesan(false, "<b>NIP Guru Bahasa Indonesia</b> harus 18 digit angka bila diisi.");
  if (!guruMat) return tampilPesan(false, "<b>Nama Guru Matematika</b> wajib diisi.");
  if (nipMat && !/^[0-9]{18}$/.test(nipMat)) return tampilPesan(false, "<b>NIP Guru Matematika</b> harus 18 digit angka bila diisi.");
  if (!fileMurid) return tampilPesan(false, "<b>File Data Murid Kelas 9</b> wajib diunggah. Unduh templatenya bila belum punya.");
  if (WEBAPP_URL.indexOf("XXXX") !== -1) return tampilPesan(false, "<b>Form belum terhubung ke server.</b> Panitia masih menyiapkan alamat pengiriman (WEBAPP_URL).");

  var btn = el("btnKirim");
  btn.disabled = true;
  btn.textContent = "Mengirim…";
  tampilPesan(true, "Mengirim pendaftaran… mohon tunggu.");

  fetch(WEBAPP_URL, {
    method: "POST",
    headers: { "Content-Type": "text/plain;charset=utf-8" },
    body: JSON.stringify({
      npsn: npsn, sekolah: sekolah, kecamatan: kecamatan, komda: komda,
      guruBindo: guruBindo, nipBindo: nipBindo, guruMat: guruMat, nipMat: nipMat,
      fileNama: fileMurid.nama, fileTipe: fileMurid.tipe, fileData: fileMurid.data
    })
  })
  .then(function (r) { return r.json(); })
  .then(function (hasil) {
    btn.disabled = false;
    btn.textContent = "Kirim Pendaftaran";
    if (hasil && hasil.ok) {
      tampilPesan(true, "<b>✓ Pendaftaran berhasil terkirim.</b><br>" +
        "Sekolah: <b>" + sekolah + "</b> (NPSN " + npsn + ", Komda " + komda + ")<br>" +
        "File data murid: <b>" + fileMurid.nama + "</b><br>" +
        "Simpan halaman ini sebagai bukti pendaftaran.");
      el("formTKA").reset();
      el("sekolah").value = ""; el("kecamatan").value = ""; el("komda").value = "";
      aturManualSekolah(false);
      el("npsnHint").textContent = "Ketik 8 digit NPSN — nama sekolah dan Komda akan muncul otomatis.";
      el("npsnHint").className = "hint";
      el("fileInfo").style.display = "none";
      fileMurid = null;
    } else {
      tampilPesan(false, "<b>✗ Pendaftaran gagal.</b> " + ((hasil && hasil.pesan) || "Terjadi kesalahan."));
    }
  })
  .catch(function (err) {
    btn.disabled = false;
    btn.textContent = "Kirim Pendaftaran";
    tampilPesan(false, "<b>✗ Tidak dapat terhubung ke server.</b> Periksa koneksi internet, lalu coba kirim lagi. (" + err.message + ")");
  });
});
</script>
</body>
</html>
"""

html = HTML.replace('__DATA_JSON__', DATA_JSON)
out = os.path.join(SRC, 'index.html')
open(out, 'w', encoding='utf-8').write(html)
print('index.html:', len(html), 'byte, sekolah:', len(data))
