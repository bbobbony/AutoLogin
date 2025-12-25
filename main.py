import os
import time

def run_hero():
    # 영웅문 Global의 실행파일 경로
    hero_path = r"C:\KiwoomGlobal\bin\NFStarter.exe"
    
    if os.path.exists(hero_path):
        print("영웅문을 실행")
        os.startfile(hero_path)
        
        print("로그인 창 유지 확인")
        # 파이썬이 종료되지 않도록 무한 대기합니다.
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("프로그램 종료")
    else:
        print("경로를 찾을 수 없음")

#메인함수
if __name__ == "__main__":
    # 함수호출
    run_hero()