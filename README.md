# SuwonHiTech-Bot
본 프로젝트는 수원하이텍고등학교 학교급식알리미입니다.
제작자도 파이썬을 하나도 모르는 상태에서 만든 프로젝트여서 어울리지 않는 부분과 자잘한 오류가 있을 수 있습니다.

텔레그램 봇 제작자 : 3학년 김민규\
플러스친구 봇 제작자 : 3학년 김민규, 3학년 김현수

텔레그램 급식알리미 : 
* 제작시작 - 2019.07.18
* 텔레그램 봇 생성 - 2019.07.22
* 알파버전 완성 - 2019.07.25
* 알파버전 테스트 - 2019.07.26
* 코드 간결화(일부) - 2019.08.01

카카오 플러스 친구 급식알리미 :
* kakao i developers 접근권한 신청 - 2019.07.25
* kakao i developers 접근권한 허가 - 2019.07.26
* 제작중...(2019.08.05 현재)

기능으로는 "그제, 어제, 오늘, 내일, 모레"와 "start"가 존재합니다.

* start명령어는 봇이 동작하는지 확인할 수 있습니다.
* 나머지 명령어는 각각 당일 기준으로 해당 날짜 수원하이텍고등학교의 급식표를 가져옵니다.(단, 아침 메뉴는 업체 미제공으로 지원 불가)

급식표 주소 : 'http://sht.hs.kr/?_page=41&_action=view&_view=view&yy=' + str(today.year) + '&mm=' + str(today.month) + '&dd=' + str(today.day)
