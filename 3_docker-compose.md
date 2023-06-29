# 다중 컴포즈 도구를 이용한 다중 컨테이너 애플리케이션 서비스 배포
---

### 1. 도커 컴포즈

- 도커 컴포즈(docker-compose)는 공통성을 갖는 컨테이너 애플리케이션 스택은 YAML코드로 정의하고 그것을 실행하기 위한 다중 컨테이너 실행 도구
- 공통의 목적을 갖는 애플리케이션 스택을 정의하여 한 번에 서비스를 올리고 관리
- 컨테이너 간 쉬운 통신
- 다양한 관리 기능은 없어서 테스트나 개발환경 구성에 적합
- 운영 환경은 많은 관리 요소가 필요하기 때문에 쿠버네티스와 같은 오케스트레이션 도구와 함께 사용 권장

#### 1-1. 도커 컴포즈 야믈 코드 작성

- **버전 정의**: 도커 엔진 릴리즈에 적합한 버전 선택
    - **version**: '3.8'</br>
- **서비스 정의**: 도커 컴포즈를 통해 실행할 서비스, 컨테이너 개념
    - **image**: 도커 허브에서 제공하는 오피셜 이미지 사용하는 경우
    - **build**: Dockerfile을 작성하여 컨테이너 구성하는 경우
        - **context**: 작업파일 디렉토리 지정, 보통 '.'
        - **dockerfile**: Dockerfile 경로 지정
    - **container_name**: 컨테이너 이름, --name 옵션과 동일, 생략시 자동 부여
    - **ports**: 서비스 내부 포트와 외부 호스트 포트 지정, -p 옵션과 동일
    - **expose**: 서비스만 포트 노출
    - **networks**: 최상위 레벨의 networks에 정의된 네트워크 이름을 작성, --net 옵션과 동일
    - **volumes**: 도커 볼륨을 통한 데이터 지속성 설정, -v 옵션과 동일
    - **environment**: 서비스 내부 환경 변수 설정, -e 옵션과 동일
    - **command**: 서비스 구동 이후 실행할 명령어 작성
    - **restart**: 서비스 재시작 옵션 지정, --restart 옵션과 동일
    - **depends_on**: 서비스 간의 종속성, 먼저 실행해야 하는 서비스를 지정하여 순서 지정</br>
- **네트워크 정의**: 다중 컨테이너들이 사용할 최상위 네트워크 키 정의, 이하 하위 서비스 단위로 네트워크 선택 가능
    - 아무런 옵션도 지정하지 않으면 자체 기본 네트워크 자동 생성
    - 최상위 레벨에 networks 지정 시 해당 이름의 네트워크 생성, 대역은 172.x.x.x로 자동 할당, 기본 드라이버는 브리지
    - 도커에서 생성한 기존 네트워크를 지정하는 경우 external 옵션에 네트워크 이름 작성</br>
- **볼륨 정의**: 데이터 지속성을 유지하기 위해 최상위 레벨에 볼륨 정의, 서비스 레벨에서 볼륨명과 서비스 내부의 이렉터리 바인드
    - **docker volume ls** 명령을 통해 확인 가능

#### 1-2. 도커 컴포즈 명령어 (docker-compose -help)

 - **docker-compose up**: yaml 코드에 있는 이미지를 이용해 컨테이너 서비스 실행
    - **-d, --detach**: 백그라운드로 컨테이너 서비스 실행
    - **--build**: 컨테이너 서비스를 시작하기 전에 이미지 빌드
    - **--force-recreate**: 컨테이너 무조건 재생성
    - **-t, --timeout**: 컨테이너 종료시 타임아웃
    - **--scale SERVICE=NUM**: 컨테이너 서비스의 개수를 지정한 만큼 확장
 - **docker-compose down**: 정의된 서비스, 볼륨, 네트워크를 정지 후 삭제
 - **docker-compose stop 서비스명**: 특정 컨테이너를 중지시킬 경우 사용
 - **docker-compose start 서비스명**: 정지상태의 서비스 실행
 - **docker-compose logs**: 화면에 어플리케이션 로그 출력, -f 옵션을 줄 경우 실시간 접근 로그 출력
 - **docker-compose ps**: 도커 컴포즈에 정의된 모든 서비스 컨테이너 목록 조회
 - **docker-compose config**: yaml파일 설정을 확인
 - **docker-compose pause**: 컨테이너 일시 정지
 - **docker-compose unpause**: 일시 정지 상태의 서비스 동작
 - **docker-compose port 서비스명 포트**: 해당 컨테이너 서비스의 공개된 포트 정보 확인