import time
import sys
from pywinauto import Application

WINDOW_TITLE = ".*영웅문.*"
PASSWORD = "356890"

def auto_login():
    print("영웅문 실행 여부 확인 중...")

    try:
        app = Application(backend="uia").connect(
            title_re=WINDOW_TITLE,
            timeout=30
        )
    except:
        print("영웅문이 실행되어 있지 않습니다. 종료합니다.")
        sys.exit(1)

    dlg = app.window(title_re=WINDOW_TITLE)
    dlg.set_focus()

    print("비밀번호 입력 중...")
    pw = dlg.child_window(auto_id="1001", control_type="Edit")
    pw.click_input()
    pw.type_keys(PASSWORD, with_spaces=True)

    print("로그인 버튼 클릭")
    login_btn = dlg.child_window(auto_id="1", control_type="Button")
    login_btn.click_input()

    print("로그인 시도 완료. 파이썬 종료")
    sys.exit(0)

if __name__ == "__main__":
    auto_login()
