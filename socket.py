import tkinter as tk

def send_message():
    message = entry.get()
    # 메시지를 처리하고 전송하는 로직을 추가할 수 있습니다.
    print(f"Sent: {message}")
    entry.delete(0, tk.END)

# Tkinter 윈도우 생성
root = tk.Tk()
root.title("Messenger")

# 채팅 표시 영역
text_area = tk.Text(root, height=10, width=50)
text_area.pack()

# 메시지 입력 창
entry = tk.Entry(root, width=50)
entry.pack()

# 전송 버튼
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

# 윈도우 실행
root.mainloop()
