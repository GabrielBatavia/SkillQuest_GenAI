# SkillQuest_GenAI: AI-Powered Question Answering System

## 🚀 Overview

**SkillQuest_GenAI** adalah sebuah proyek **AI Question Answering System** yang dikembangkan untuk meningkatkan kemampuan pembelajaran interaktif. Sistem ini dibangun menggunakan model **SkillQuest-Nusantara-2.7b-Indo-Chat**, sebuah model bahasa yang telah di-*fine-tune* khusus untuk menghasilkan jawaban yang relevan dalam bahasa Indonesia. Dengan memanfaatkan kecerdasan buatan (AI) berbasis transformer, proyek ini bertujuan untuk menciptakan lingkungan belajar yang adaptif dan responsif terhadap kebutuhan pengguna.

Model ini dapat digunakan untuk berbagai aplikasi, seperti:
- **Chatbot Pendidikan**: Membantu siswa dan pengguna umum untuk mendapatkan jawaban dari pertanyaan mereka dengan cepat.
- **Asisten Virtual**: Melayani sebagai asisten AI yang menjawab pertanyaan seputar berbagai topik dalam bahasa Indonesia.
- **Pembelajaran Interaktif**: Dapat digunakan oleh pengembang dalam aplikasi pendidikan berbasis AI.

## 🛠 Fitur Utama
- **Real-time Question Answering**: Memanfaatkan kekuatan dari model **Nusantara-2.7b** untuk menjawab pertanyaan dalam bahasa Indonesia.
- **Pembangkitan Teks Berkualitas**: Menghasilkan jawaban yang kohesif, alami, dan relevan.
- **Model Bahasa Indonesia**: Menggunakan bahasa Indonesia dengan baik untuk berbagai konteks percakapan, dari pembelajaran hingga layanan pelanggan.
- **Integrasi Mudah**: Dapat digunakan dalam berbagai aplikasi berbasis **Flask**, **FastAPI**, atau **Django** sebagai backend AI.

## 🔗 Model Hugging Face
Model utama yang digunakan dalam proyek ini tersedia di Hugging Face. Anda bisa mengunduh atau mencobanya langsung:

[SkillQuest-Nusantara-2.7b-Indo-Chat](https://huggingface.co/gabrielb/SkillQuest-Nusantara-2.7b-Indo-Chat)

## 📂 Struktur Proyek
Berikut adalah struktur folder dalam repositori ini:
- **config/**: Berisi konfigurasi model, hyperparameters, dan pipeline AI.
- **data/**: Dataset atau contoh data yang digunakan untuk melatih model.
- **evaluation/**: Kode untuk mengevaluasi performa model menggunakan metrik seperti F1-Score dan BLEU-Score.
- **training/**: Skrip yang digunakan untuk melatih model menggunakan framework PyTorch.
- **utils/**: Berbagai utilitas untuk preprocessing, postprocessing, dan lainnya.
- **visualization/**: Skrip untuk memvisualisasikan hasil evaluasi atau training model (misalnya, grafik learning curve).
- **main.py**: File utama untuk menjalankan aplikasi AI Question Answering.
- **requirements.txt**: File berisi dependensi yang diperlukan untuk menjalankan proyek ini.


## ⚠️ Risiko, Keterbatasan, dan Bias
Walaupun model ini dirancang untuk menghasilkan jawaban yang relevan dalam konteks pendidikan dan layanan pelanggan, ada beberapa keterbatasan dan risiko:
- Bias Data: Model ini dilatih menggunakan dataset publik, sehingga mungkin terdapat bias atau stereotip yang ada dalam data tersebut.
- Konten Tidak Sesuai: Model mungkin menghasilkan konten yang tidak sesuai atau tidak akurat dalam konteks tertentu. Pengguna disarankan untuk selalu mengevaluasi hasil dari model ini.

## 🤝 Kontribusi
Kami terbuka untuk kontribusi! Jika Anda ingin berkontribusi pada proyek ini, silakan fork repositori ini dan ajukan Pull Request dengan perubahan yang Anda usulkan.

## 📄 Lisensi
Proyek ini dilisensikan di bawah Apache License 2.0.
