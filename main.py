import os
import time
from pywinauto import Application, findwindows #중복창을 찾는 라이브러리 추가

def run_and_login_hero():
    hero_path = r"C:\KiwoomGlobal\bin\NFStarter.exe"
    password = "356890"
    window_title = ".*영웅문.*" #찾고자 하는 창의 제목 패턴

    # 창 중복확인
    try:
        #해당 타이틀을 가진 창이 있는지 검색
        existing_window = findwindows.find_windows(title_re=window_title)
        if existing_window:
            print("이미 영웅문이 실행중입니다. 프로그램을 실행하지 않습니다.")
            return
    except findwindows.ElementNotFoundError:
        pass


    #1111이 눌리게 && 현재 창이 켜져있으면 따로 안나오게 && 하나증권도 열리게 && 직렬 및 병렬
    if os.path.exists(hero_path):
        print("영웅문을 실행합니다...")
        os.startfile(hero_path)
        
        # 창이 뜰 때까지 대기
        time.sleep(15) 

        try:
            # 1. 창 연결
            app = Application(backend="uia").connect(title_re=".*영웅문.*", timeout=20)
            dlg = app.window(title_re=".*영웅문.*")
            dlg.set_focus()

            # 1-1. 연결된 창에서 내부 구조 불러오기
            print("-" * 60)
            print("[시스템 분석] 영웅문 로그인 창의 내부 컨트롤 구조를 스캔...")
            dlg.print_control_identifiers()  # 터미널에 설계도를 출력하는 핵심 명령어
            print("-" * 60)


            # 2. 비밀번호 입력
            print("비밀번호 칸에 입력 중...")
            pw_field = dlg.child_window(auto_id="1001", control_type="Edit")
            
            # 직접 클릭 후 타이핑
            pw_field.click_input()
            time.sleep(0.5)
            pw_field.type_keys(password, with_spaces=True)
            
            # 3. 로그인 버튼 클릭
            print("로그인 버튼 클릭")
            login_btn = dlg.child_window(auto_id="1", control_type="Button")
            login_btn.click()
            
            print("성공적으로 로그인을 성공")

        except Exception as e:
            print(f"오류 발생: {e}")
            
        # 무한 대기 (프로그램 종료 방지)
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("프로그램 종료")
    else:
        print("경로를 찾을 수 없음")

if __name__ == "__main__":
    run_and_login_hero()