import random
def get_computer_choice():
    choices = ["batu", "gunting", "kertas"]
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Seri"
    elif (player_choice == "batu" and computer_choice == "gunting") or \
         (player_choice == "gunting" and computer_choice == "kertas") or \
         (player_choice == "kertas" and computer_choice == "batu"):
        return "Pemain menang"
    else:
        return "Komputer menang"

def main():
    player_score = 0
    computer_score = 0
    rounds = 0

    while True:
        player_choice = input("Masukkan pilihan Anda (batu, gunting, kertas) atau 'keluar' untuk mengakhiri: ").lower()
        if player_choice == "keluar":
            break
        if player_choice not in ["batu", "gunting", "kertas"]:
            print("Pilihan tidak valid. Silakan coba lagi.")
            continue

        computer_choice = get_computer_choice()
        print(f"Komputer memilih: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)
        print(result)

        if result == "Pemain menang":
            player_score += 1
        elif result == "Komputer menang":
            computer_score += 1

        rounds += 1
        print(f"Skor setelah {rounds} ronde: Pemain {player_score} - Komputer {computer_score}")

if __name__ == "__main__":
    main()