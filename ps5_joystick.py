from time import sleep
from dualsense_controller import DualSenseController

# 列出可用的 DualSense 設備，並檢查是否有連接的設備
device_infos = DualSenseController.enumerate_devices()
if len(device_infos) < 1:
    raise Exception("No DualSense Controller available.")

# 全域變數，控制程式運行
is_running = True

# 創建 DualSenseController 物件，使用第一個可用設備
controller = DualSenseController()
controller.lightbar.set_color_red()


controller.btn_square.on_change(
    lambda pressed: print("Square pressed") if pressed else print("Square released")
)
controller.btn_circle.on_change(
    lambda pressed: print("Circle pressed") if pressed else print("Circle released")
)
controller.btn_triangle.on_change(
    lambda pressed: print("Triangle pressed") if pressed else print("Triangle released")
)
controller.btn_l1.on_change(
    lambda pressed: print("L1 pressed") if pressed else print("L1 released")
)
controller.btn_r1.on_change(
    lambda pressed: print("R1 pressed") if pressed else print("R1 released")
)
controller.btn_l2.on_change(
    lambda pressed: print("L2 pressed") if pressed else print("L2 released")
)
controller.btn_r2.on_change(
    lambda pressed: print("R2 pressed") if pressed else print("R2 released")
)
# 偵測 L3 / R3
controller.btn_l3.on_change(
    lambda pressed: print("L3 pressed") if pressed else print("L3 released")
)
controller.btn_r3.on_change(
    lambda pressed: print("R3 pressed") if pressed else print("R3 released")
)
# 切換 `is_running`，停止程式
def stop():
    global is_running
    is_running = False


# === Cross 按鈕回調 ===
def on_cross_btn_pressed():
    print("Cross button pressed")
    controller.left_rumble.set(255)
    controller.right_rumble.set(255)


def on_cross_btn_released():
    print("Cross button released")
    controller.left_rumble.set(0)
    controller.right_rumble.set(0)


def on_cross_btn_changed(pressed):
    print(f"Cross button is pressed: {pressed}")


# === PlayStation 按鈕回調 ===
def on_ps_btn_pressed():
    print("PS button pressed -> stopping script")
    stop()


# === 發生錯誤時的回調 ===
def on_error(error):
    print(f"Oops! An error occurred: {error}")
    stop()


# 註冊 Cross 按鍵回調函數
controller.btn_cross.on_down(on_cross_btn_pressed)
controller.btn_cross.on_up(on_cross_btn_released)
controller.btn_cross.on_change(on_cross_btn_changed)

# 註冊 PS 按鈕回調函數
controller.btn_ps.on_down(on_ps_btn_pressed)

# 註冊錯誤處理回調
controller.on_error(on_error)

# 啟動 DualSense 控制器
controller.activate()

print("PS5 DualSense 控制器已連接！按下 PS 按鈕退出程式。")

# 持續運行，直到 `is_running` 為 False
while is_running:
    sleep(0.001)

# 停止 DualSense 控制器
controller.deactivate()
print("PS5 DualSense 控制器已斷開連接。")
