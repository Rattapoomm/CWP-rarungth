import sys
from checkmate import checkmate_from_str

def main():
    if len(sys.argv) < 2:
        return

    for file_path in sys.argv[1:]:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                board_content = f.read()
                result = checkmate_from_str(board_content)
                print(result)
        except Exception:
            print("Error")

if __name__ == "__main__":
    main()