# 핵심로직
# 이파일의 백엔드 서버이자 매크로 본체

import time
import win32gui, win32api, win32con # 윈도우 제어용 모듈 (pip install pywin32)

def run_macro():
    # 1단계: 타겟 프로그램의 ID(핸들)를 찾기 (비활성 제어의 핵심)
    # 특정 창의 고유 번호를 알아내서 "그 창에만" 신호를 보냅니다.
    hwnd = win32gui.FindWindow(None, "매매프로그램이름")
    
    if hwnd:
        print("프로그램 발견! 작업을 시작합니다.")
        
        # 2단계: 비활성 클릭 (마우스를 움직이지 않고 신호만 보냄)
        # (hwnd: 대상창, WM_LBUTTONDOWN: 마우스 왼쪽 클릭 신호, 좌표)
        lparam = win32api.MAKELONG(100, 200) # 버튼이 있는 좌표 (x=100, y=200)
        win32gui.PostMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lparam)
        win32gui.PostMessage(hwnd, win32con.WM_LBUTTONUP, 0, lparam)
        
        print("클릭 신호를 보냈습니다.")
    else:
        print("프로그램이 켜져 있지 않습니다.")

# 3단계: 무한 루프 (스케줄러 역할)
while True:
    current_time = time.strftime("%H:%M:%S")
    if current_time == "08:30:00":
        run_macro()
        break # 실행 후 종료하거나 대기
    
    print(f"현재 시간: {current_time} - 대기 중...")
    time.sleep(1) # 1초마다 체크