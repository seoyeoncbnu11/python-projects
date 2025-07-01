import pyautogui
import time
import pyperclip

# while True:
#     print(pyautogui.position())
#     time.sleep(0.1)

# pyautogui.moveTo(843, 164, 0.2)
# pyautogui.click()
# time.sleep(0.5)

# pyperclip.copy("서울 날씨")
# pyautogui.hotkey("ctrl", "v")
# time.sleep(0.5)

# pyautogui.write(["enter"])
# time.sleep(1)

날씨 = ["서울 날씨", "시흥 날씨", "청주 날씨", "부산 날씨", "강원도 날씨"]

addr_x = 827
addr_y = 62
start_x = 723
start_y = 230
end_x = 1315
end_y = 603

# # pyautogui.screenshot(
# #     "./04-auto-projects/서울날씨.png",
# #     region=(start_x, start_y, end_x - start_x, end_y - start_y),
# # )

for 지역날씨 in 날씨:
    pyautogui.moveTo(addr_x, addr_y, 1)
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.write("www.naver.com", interval=0.1)
    pyautogui.write(["enter"])
    time.sleep(1)

    pyperclip.copy(지역날씨)

    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.5)
    pyautogui.write(["enter"])
    time.sleep(1)
    저장경로 = f"./04-auto-projects/{지역날씨}.png"
    pyautogui.screenshot(
        저장경로, region=(start_x, start_y, end_x - start_x, end_y - start_y)
    )
