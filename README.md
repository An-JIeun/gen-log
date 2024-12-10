# 📊 피드백 자동 요약 서비스
---

- 최종 수정일 : 2024-12-10

---

## 실행 전 준비 사항
### 1. 구글 스프레드 시트 API 발급
- 참고 : [파이썬을 이용한 구글 스프레드시트 연동 및 자동화 방법](https://develop-davi-kr.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9D%84-%EC%9D%B4%EC%9A%A9%ED%95%9C-%EA%B5%AC%EA%B8%80-%EC%8A%A4%ED%94%84%EB%A0%88%EB%93%9C%EC%8B%9C%ED%8A%B8-%EC%97%B0%EB%8F%99-%EB%B0%8F-%EC%9E%90%EB%8F%99%ED%99%94-%EB%B0%A9%EB%B2%95)
- 사용할 google spreadsheet 생성

### 2. OPEN AI Key 발급
- 참고 : [파이썬 OpenAI API key 숨기기: env파일, 환경변수 설정](https://simpleuse.tistory.com/entry/howtousekey)
- .env.example 파일과 같이 작성한 후, '.env' 형식으로 저장합니다.


## 설치 및 실행

### 1. 필요 라이브러리 다운

```bash
pip install -r requirements.txt
```

### 2. main.py 파일 수정

```python
#json 파일 명으로 수정
json_file_path = "{google api에서 다운받은 json 파일명}.json"
# url 수정
spreadsheet_url = "https://docs.google.com/spreadsheets/d/{자신의 스프레드 시트 url로 수정}"
```

### 3. streamlit 실행

```bash
streamlit run main.py
```
