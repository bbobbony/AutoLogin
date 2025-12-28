import os
import time
from pywinauto import Application, findwindows

def run_and_login_hero():
    hero_path = r"C:\KiwoomGlobal\bin\NFStarter.exe"
    password = "356890"
    window_title = ".*영웅문.*"

    app = None 

    # 창 중복 확인 및 연결/실행 로직
    try:
        # 1. 일단 이미 켜져 있는지 확인하고 '연결(connect)' 시도
        print("기존에 실행 중인 창이 있는지 확인합니다...")
        app = Application(backend="uia").connect(title_re=window_title, timeout=2)
        print("기존 창을 발견하여 연결했습니다.")
        # 여기서는 return 안함 그래야 아래 로그인 로직으로 간다

    except:
        # 2. 창이 없어서 연결에 실패하면 새로 실행
        print("창이 없습니다. 새로 실행합니다...")
        if os.path.exists(hero_path):
            os.startfile(hero_path)
            time.sleep(15) # 프로그램 로딩 대기
            # 새로 실행된 창에 연결
            app = Application(backend="uia").connect(title_re=window_title, timeout=20)
        else:
            print("경로를 찾을 수 없습니다.")
            return
    # -----------------------------------------------

    # 3. 로그인 로직 (기존 창이든 새 창이든 공통으로 실행)
    try:
        dlg = app.window(title_re=window_title)
        dlg.set_focus()

        print("-" * 60)
        print("[시스템 분석] 로그인 창 컨트롤 스캔...")
        # dlg.print_control_identifiers() # 필요할 때만 주석 해제
        print("-" * 60)

        print("비밀번호 칸에 입력 중...")
        pw_field = dlg.child_window(auto_id="1001", control_type="Edit")
        pw_field.click_input()
        time.sleep(0.5)
        pw_field.type_keys(password, with_spaces=True)
        
        print("로그인 버튼 클릭")
        login_btn = dlg.child_window(auto_id="1", control_type="Button")
        login_btn.click()
        
        print("성공적으로 로그인을 성공")

    except Exception as e:
        print(f"로그인 제어 중 오류 발생: {e}")

    # 프로그램 종료 방지 대기
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("프로그램 종료")

if __name__ == "__main__":
    run_and_login_hero()