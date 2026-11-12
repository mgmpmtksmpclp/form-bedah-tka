/**
 * Form Pendaftaran Bedah TKA 2026/2027 — Kelas 9 (Kab. Cilacap)
 * Backend Google Apps Script untuk index.html (Form Pendaftaran Bedah TKA 2026/2027).
 *
 * CARA PASANG (sekali saja):
 * 1. Buat Google Sheet baru (mis. "Pendaftaran TKA Kelas 9").
 * 2. Di Sheet itu: Extensions > Apps Script > hapus isi Code.gs lama >
 *    tempel seluruh isi file ini > simpan (ikon disket).
 * 3. Jalankan sekali fungsi siapkanSheet() (pilih di menu fungsi > Run)
 *    untuk membuat tab "Pendaftaran" + header. Beri izin saat diminta.
 * 4. Deploy > New deployment > type: Web app > Execute as: Me >
 *    Who has access: Anyone > Deploy. Salin URL Web App (.../exec).
 * 5. Tempel URL itu ke WEBAPP_URL di index.html (ganti yang berisi XXXX).
 *
 * ALUR DATA: form (index.html) --POST JSON--> doPost() --> simpan file
 * data murid ke folder Drive "Data Murid TKA" + tambah 1 baris PER
 * PESERTA ke tab "Pendaftaran" (satu sekolah boleh mengirim lebih dari
 * 1 orang per mata pelajaran). Satu NPSN hanya boleh terdaftar satu kali.
 */

/* ============================== KONFIG ============================== */

// Kosongkan (= pakai spreadsheet tempat script ini menempel) atau isi ID
// spreadsheet bila script berdiri sendiri.
var SPREADSHEET_ID = '';
var NAMA_SHEET = 'Pendaftaran';
var NAMA_FOLDER = 'Data Murid TKA';
var HEADER = ['Waktu Daftar', 'NPSN', 'Nama Sekolah', 'Kecamatan', 'Komda',
  'Mata Pelajaran', 'Nama Peserta', 'NIP Peserta',
  'Nama File Data Murid', 'Tautan File Data Murid'];

/* ============================== WEB APP ============================== */

function doGet(e) {
  return ContentService
    .createTextOutput(JSON.stringify({ ok: true, layanan: 'Form Pendaftaran Bedah TKA 2026/2027', waktu: new Date().toISOString() }))
    .setMimeType(ContentService.MimeType.JSON);
}

// Dipanggil form dengan fetch POST + Content-Type text/plain (tanpa
// preflight CORS). Body berupa JSON:
// {npsn, sekolah, kecamatan, komda,
//  peserta: [{mapel: 'Bahasa Indonesia'|'Matematika', nama, nip}],
//  fileNama, fileTipe, fileData (base64 tanpa prefix data:)}.
function doPost(e) {
  var hasil;
  try {
    var d = JSON.parse((e && e.postData && e.postData.contents) || '{}');
    hasil = daftar_(d);
  } catch (err) {
    hasil = { ok: false, pesan: 'Terjadi kesalahan: ' + err.message };
  }
  return ContentService
    .createTextOutput(JSON.stringify(hasil))
    .setMimeType(ContentService.MimeType.JSON);
}

/* ============================== INTI ============================== */

function daftar_(d) {
  var npsn = bersih_(d.npsn);
  var sekolah = bersih_(d.sekolah);
  var kecamatan = bersih_(d.kecamatan);
  var komda = bersih_(d.komda);
  // Peserta: array [{mapel, nama, nip}] (format baru). Kompatibel mundur:
  // bila tidak ada, rakit dari field lama guruBindo/nipBindo/guruMat/nipMat.
  var peserta = [];
  if (d.peserta && d.peserta.length) {
    for (var i = 0; i < d.peserta.length; i++) {
      peserta.push({ mapel: bersih_(d.peserta[i].mapel), nama: bersih_(d.peserta[i].nama), nip: bersih_(d.peserta[i].nip) });
    }
  } else {
    if (bersih_(d.guruBindo)) peserta.push({ mapel: 'Bahasa Indonesia', nama: bersih_(d.guruBindo), nip: bersih_(d.nipBindo) });
    if (bersih_(d.guruMat)) peserta.push({ mapel: 'Matematika', nama: bersih_(d.guruMat), nip: bersih_(d.nipMat) });
  }

  if (!/^[0-9]{8}$/.test(npsn)) return { ok: false, pesan: 'NPSN harus 8 digit angka.' };
  if (!sekolah) return { ok: false, pesan: 'Nama sekolah kosong.' };
  if (!kecamatan) return { ok: false, pesan: 'Kecamatan kosong.' };
  if (!komda) return { ok: false, pesan: 'Komda kosong.' };
  if (!peserta.length) return { ok: false, pesan: 'Isi minimal 1 peserta.' };
  for (var j = 0; j < peserta.length; j++) {
    if (peserta[j].mapel !== 'Bahasa Indonesia' && peserta[j].mapel !== 'Matematika') return { ok: false, pesan: 'Mata pelajaran peserta ke-' + (j + 1) + ' tidak dikenal.' };
    if (!peserta[j].nama) return { ok: false, pesan: 'Nama peserta ke-' + (j + 1) + ' wajib diisi.' };
    if (peserta[j].nip && !/^[0-9]{18}$/.test(peserta[j].nip)) return { ok: false, pesan: 'NIP peserta ke-' + (j + 1) + ' harus 18 digit angka bila diisi.' };
  }
  if (!d.fileData) return { ok: false, pesan: 'File Data Murid Kelas 9 wajib diunggah.' };

  var sheet = sheet_();
  // Satu NPSN satu pendaftaran — tolak bila sudah ada.
  var data = sheet.getDataRange().getValues();
  for (var i = 1; i < data.length; i++) {
    if (String(data[i][1]) === npsn) {
      return { ok: false, pesan: 'NPSN ' + npsn + ' (' + sekolah + ') sudah terdaftar. Hubungi panitia bila ada perubahan data.' };
    }
  }

  var tautanFile = simpanFile_(d, npsn, sekolah);
  var waktu = Utilities.formatDate(new Date(), 'Asia/Jakarta', 'yyyy-MM-dd HH:mm:ss');
  for (var k = 0; k < peserta.length; k++) {
    sheet.appendRow([waktu, "'" + npsn, sekolah, kecamatan, komda,
      peserta[k].mapel, peserta[k].nama, peserta[k].nip ? "'" + peserta[k].nip : '',
      String(d.fileNama || ''), tautanFile]);
  }
  return { ok: true, pesan: 'Pendaftaran tersimpan (' + peserta.length + ' peserta).', tautanFile: tautanFile };
}

// Simpan file data murid ke folder Drive, kembalikan tautannya.
function simpanFile_(d, npsn, sekolah) {
  var folder = folder_();
  var waktu = Utilities.formatDate(new Date(), 'Asia/Jakarta', 'yyyyMMdd-HHmm');
  var namaBersih = sekolah.replace(/[^a-zA-Z0-9]+/g, '-').replace(/^-+|-+$/g, '') || 'Sekolah';
  var namaAsli = String(d.fileNama || 'data-murid');
  var ekst = namaAsli.indexOf('.') !== -1 ? namaAsli.slice(namaAsli.lastIndexOf('.')) : '.csv';
  var nama = 'Data-Murid-Kelas9-' + npsn + '-' + namaBersih + '-' + waktu + ekst;
  var tipe = String(d.fileTipe || 'application/octet-stream');
  var bytes = Utilities.base64Decode(String(d.fileData));
  var file = folder.createFile(Utilities.newBlob(bytes, tipe, nama));
  return file.getUrl();
}

/* ============================== PEMBANTU ============================== */

function bersih_(s) { return String(s === undefined || s === null ? '' : s).trim(); }

function buku_() {
  return SPREADSHEET_ID
    ? SpreadsheetApp.openById(SPREADSHEET_ID)
    : SpreadsheetApp.getActiveSpreadsheet();
}

function sheet_() {
  var buku = buku_();
  var sheet = buku.getSheetByName(NAMA_SHEET);
  if (!sheet) {
    sheet = buku.insertSheet(NAMA_SHEET);
    sheet.getRange(1, 1, 1, HEADER.length).setValues([HEADER]);
    sheet.getRange(1, 1, 1, HEADER.length).setFontWeight('bold');
    sheet.setFrozenRows(1);
  }
  return sheet;
}

function folder_() {
  var cari = DriveApp.getFoldersByName(NAMA_FOLDER);
  if (cari.hasNext()) return cari.next();
  return DriveApp.createFolder(NAMA_FOLDER);
}

// Jalankan sekali dari editor Apps Script untuk menyiapkan tab + header.
// Bila header lama berbeda (mis. habis ganti format kolom), baris 1
// dibersihkan dulu lalu ditulis header baru.
function siapkanSheet() {
  var sheet = sheet_();
  var kepala = sheet.getRange(1, 1, 1, HEADER.length).getValues()[0];
  if (kepala.join('|') !== HEADER.join('|')) {
    sheet.getRange(1, 1, 1, 20).clearContent();
    sheet.getRange(1, 1, 1, HEADER.length).setValues([HEADER]);
    sheet.getRange(1, 1, 1, HEADER.length).setFontWeight('bold');
    sheet.setFrozenRows(1);
  }
  return 'Tab "' + NAMA_SHEET + '" siap. Header: ' + HEADER.join(' | ');
}
