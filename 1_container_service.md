# 컨테이너 서비스
---

### 1. 컨테이너 서비스


- 컨테이너 서비스 환경 도입의 이유:
개발, 테스트, 배포, 운영의 컴퓨팅 환경을 일관적으로 제공함


### 2. 도커 서비스의 과정

- 1. 어플리케이션 코드 개발:

- 2. 베이스 이미지를 이용한 Dockerfile 작성:
    - 개발에 필요한 인프라 구성 요소를 Dockerfile에 작성

- 3. Dockerfile build를 통한 새로운 이미지 생성:
    - 작성한 도커 파일을 단계(step)별로 실행

- 4. 컨테이너 실행 혹은 Docker compose를 이용한 다중 컨테이너 실행

- 5. 컨테이너 어플리케이션 서비스 테스트

- 6. 로컬 및 원격 저장소에 이미지 저장하여 관리

- 7. Docker file 등을 깃헙등의 원격 리포지토리에 관리

- 8. 위 단계를 통한 일관성 있는 환경에서 지속적인 어플리케이션 개발 및 유지보수




### 3. 도커 명령어 활용



#### 3-1 도커 이미지 명령어


##### 3-1-1 도커 이미지 내려받기

- **docker pull**: 도커 허브 레지스트리에서 로컬로 도커 이미지 내려받기
- **docker push**: 로컬에 있는 도커 이미지를 허브 레지스트리에 업로드
- **docker login**: 도커 허브 로그인
- **docker logout**: 도커 허브 로그아웃

**_ 구문: docker IMAGE pull OPTIONS name[:tag | @IMAGE_DIGEST] _**


**명령 옵션**
- **all-tags, -a**: 저장소에 태그로 지저오딘 여러 이미지를 모두 다운
- **disable-content-trust**: 이미지 검증 작업 건너뛰기
- **platform**: 플랫폼 지정  ex. --platform=linux
- **quiet, -q**: 이미지 다운로드 과정의 상세 출력 생략




##### 3-1-2 도커 이미지 세부 정보 조회



- **docker image inspect OPTIONS IMAGE**: 다운로드한 이미지 세부 정보 조회
- **docker image history OPTIONS IMAGE**: 현재 이미지 구성을 위해 사용된 레이블 정보 및 명령, 크기 조회


##### 3-1-3 도커 이미지 태그 설정

- **docker image inspect OPTIONS IMAGE**: 다운로드한 이미지 세부 정보 조회
- **docker image history OPTIONS IMAGE**: 현재 이미지 구성을 위해 사용된 레이블 정보 및 명령, 크기 조회