import os
import time

def run_hero():
    hero_path = r"C:\KiwoomGlobal\bin\NFStarter.exe"
    
    if os.path.exists(hero_path):
        print("✅ 영웅문을 실행합니다...")
        os.startfile(hero_path)
        
        print("로그인 창이 유지되는지 확인하세요. (이 창을 끄지 마세요)")
        # 파이썬이 종료되지 않도록 무한 대기합니다.
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("프로그램을 종료합니다.")
    else:
        print("❌ 경로를 찾을 수 없습니다.")

if __name__ == "__main__":
    run_hero()