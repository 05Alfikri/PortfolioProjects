# Panduan Git Dasar

Dokumentasi ini berisi kumpulan perintah Git yang sering digunakan dalam pengembangan proyek sehari-hari, lengkap dengan penjelasan singkat.

---

## Persiapan & Inisialisasi

| Perintah | Penjelasan |
|----------|------------|
| `git init` | Membuat repository Git lokal di folder saat ini. |
| `git clone <url>` | Mengunduh repository dari GitHub ke lokal. |
| `git remote add origin <url>` | Menambahkan remote bernama `origin` (biasanya GitHub). |

---

## Pekerjaan Harian (Edit → Commit → Push)

| Perintah | Penjelasan |
|----------|------------|
| `git status` | Menampilkan status file: perubahan, file baru, dsb. |
| `git add .` | Menambahkan semua file ke staging area. |
| `git add <nama_file>` | Menambahkan file tertentu ke staging area. |
| `git commit -m "pesan"` | Menyimpan snapshot perubahan dengan pesan. |
| `git push origin main` | Mengirim commit ke GitHub (branch `main`). |

---

## Sinkronisasi dengan Remote (GitHub)

| Perintah | Penjelasan |
|----------|------------|
| `git pull origin main` | Menarik update dari GitHub dan menggabungkannya. |
| `git pull origin main --rebase` | Menarik update dan menyusunnya ulang agar lebih rapi. |

---

## Branching (Cabang)

| Perintah | Penjelasan |
|----------|------------|
| `git branch` | Melihat daftar branch. |
| `git branch <nama>` | Membuat branch baru. |
| `git checkout <nama>` | Berpindah ke branch lain. |
| `git checkout -b <nama>` | Membuat dan langsung berpindah ke branch. |
| `git merge <branch>` | Menggabungkan branch ke branch aktif. |

---

## Lain-lain

| Perintah | Penjelasan |
|----------|------------|
| `git log --oneline` | Melihat riwayat commit secara ringkas. |
| `git remote -v` | Menampilkan remote yang terhubung. |
| `git config --global user.name "Nama"` | Menyetel nama global untuk Git. |
| `git config --global user.email "email@example.com"` | Menyetel email global untuk Git. |

---

## Error Umum dan Solusi

| Kasus | Solusi |
|-------|--------|
| `non-fast-forward` | Jalankan `git pull --rebase` sebelum push. |
| `origin does not appear to be a git repository` | Tambahkan remote: `git remote add origin <url>` |
| Push pertama kali | Gunakan: `git push -u origin main` |

---

## Catatan Tambahan

- Gunakan commit message yang jelas dan deskriptif.
- Lakukan `git pull` sebelum `git push` jika bekerja dalam tim.
- Hindari `git push --force` kecuali benar-benar paham dampaknya.

---

> Disusun oleh: Muh. Alfikri Tri Anggoro Pamungkas
