## 가상환경에서 Flask와 Dockerfile로 Google Cloud Platform에 API 서버 구축하기

(주)인실리코젠에서 Front-End 개발자 PL로서 개발한 AI 식단 생성 솔루션([아이푸드 플랜](https://ifoodplan.insilicogen.com/))에서 실제 사용하는 API Response Dummy를 반환하는 [서버](https://flaskwithrestapi-wbrfc7jwpa-de.a.run.app/)를 구축하였습니다.

<img width="347" alt="image" src="https://github.com/pplm1042/flask_with_rest_api/assets/47880774/cf872cde-5a38-4c21-8d54-7d37a916ac25">

## 에러 로그

### Dockerfile의 이름 첫 글자가 소문자일 경우 도커파일을 인식하지 못하는 에러가 발생(2024.01.14.)

<img width="941" alt="image" src="https://github.com/pplm1042/flask_with_rest_api/assets/47880774/c38bc33a-27a5-4813-b8de-da08f5c00523">
