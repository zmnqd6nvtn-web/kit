import random


CHOICES = ("가위", "바위", "보")
WINNING_MATCHUPS = {
    ("가위", "보"),
    ("바위", "가위"),
    ("보", "바위"),
}


def determine_result(user_choice: str, computer_choice: str) -> str:
    if user_choice == computer_choice:
        return "비겼습니다!"
    if (user_choice, computer_choice) in WINNING_MATCHUPS:
        return "이겼습니다!"
    return "졌습니다!"


def prompt_choice() -> str:
    while True:
        user_input = input("가위, 바위, 보 중 하나를 입력하세요 (종료: q): ").strip()
        if user_input.lower() == "q":
            return "q"
        if user_input in CHOICES:
            return user_input
        print("잘못된 입력입니다. 다시 입력해주세요.")


def main() -> None:
    print("가위 바위 보 게임에 오신 것을 환영합니다!")
    while True:
        user_choice = prompt_choice()
        if user_choice == "q":
            print("게임을 종료합니다.")
            break
        computer_choice = random.choice(CHOICES)
        print(f"컴퓨터: {computer_choice}")
        print(determine_result(user_choice, computer_choice))


if __name__ == "__main__":
    main()
