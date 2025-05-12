import random


def main():
    pilihan = ["batu", "gunting", "kertas"]
    print("=== Permainan Batu, Gunting, Kertas ===")

    while True:
        user_choice = input(
            "Pilih (batu/gunting/kertas) atau 'keluar' untuk berhenti: "
        ).lower()
        if user_choice == "keluar":
            print("Permainan selesai. Terima kasih sudah bermain!")
            break

        if user_choice not in pilihan:
            print("Pilihan tidak valid, silakan pilih batu, gunting, atau kertas.")
            continue

        komputer_choice = random.choice(pilihan)
        print(f"Komputer memilih: {komputer_choice}")

        if user_choice == komputer_choice:
            print("Hasil: Seri!")
        elif (
            (user_choice == "batu" and komputer_choice == "gunting")
            or (user_choice == "gunting" and komputer_choice == "kertas")
            or (user_choice == "kertas" and komputer_choice == "batu")
        ):
            print("Hasil: Anda menang!")
        else:
            print("Hasil: Komputer menang!")

        print()  # Baris kosong untuk jarak


if __name__ == "__main__":
    main()
