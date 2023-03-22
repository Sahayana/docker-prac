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


##### 3-1-4 도커 이미지 파일 관리: tar(Tape ARchiver) 파일로 이미지 관리

 - 도커 허브로부터 이미지를 내려받아 내부망으로 이전하는 경우
 - 신규 서비스를 위해 Dockerfile로 새롭게 생성한 이미지를 저장 및 배포하는 경우
 - 컨테이너를 완료하여 생성한 이미지를 저장하는 경우

 - **docker image save 옵션 파일명 이미지명**: 도커 이미지를 tar 파일로 저장
 - **docker image load 옵션**: 저장한 tar 이미지 파일 로드


##### 3-1-5 도커 이미지 삭제

 - **docker image rm 옵션 이미지이름<:태그>**: 하나 이상의 도커 이미지 삭제 (컨테이너 실행중인 이미지는 삭제 불가능)
 - **docker rmi 옵션 이미지이름<:태그>**: 단축 명령
 - **docker image prune -a**: 컨테이너로 연결되지 않은 모든 이미지 제거




#### 3-2 도커 컨테이너 명령어

다운로드한 이미지를 바탕으로 도커 엔진은 컨테이너를 생성한다.</br>
이미지와 함께 읽고 쓰기가 가능한 레이어를 추가하여 만들어지는 것이 컨테이너다.


##### 3-2-1 컨테이너는 프로세스다.

- **도커 컨테이너는 도커 이미지 기반의 스냅숏이다. (읽기전용의 도커 이미지 레이어를 복제)**
- **컴퓨터 application의 동작은 프로세스를 통해 이루어지며 컨테이너는 격리된 공간에서 프로세스가 동작하는 기술이다.**
- **docker run**: 컨테이너 동작 명령, 가상의 격리 환경에 독립된 프로세스가 동작

##### 3-2-2 컨테이너 실행 (nginx 예시)

- **docker run**: docker pull + create + start 가 합쳐진 명령어라고 볼 수 있다.
- **docker run --name webserver1 -d -p 8001:80 nginx:1.18**: 컨테이너 이름: webserver1, -d: 백그라운드 실행, -p: 컨테이너의 80포트를 호스트의 8001포트와 연결
- **docker stats webserver1**: 컨테이너의 리소스 사용량
- **docker top webserver1**: 컨테이너의 실행 중인 프로세스 표시
- **docker logs -f webserver1**: 컨테이너 접근 로그를 확인 (-f: 실시간, -t: 마지막로그까지)
- **docker stop webserver1**: 컨테이너 중지
- **docker pause webserver1**: 컨테이너 일시중지
- **docker unpause webserver1**: 컨테이너 일시중지 해제
- **docker restart webserver1**: 컨테이너 재시작
- **docker cp webserver1:/etc/nginx/nginx.conf ./nginx.conf**: 컨테이너의 파일을 복사
- **docker rename 현재이름 바꿀이름**: 컨테이너 이름 변경
- **docker commit -a "gs" webserver1 web:1.0**: 컨테이너 이미지의 저장된 변경과 함께 새로운 이미지를 생성(-a: author)


#### 3-3 도커 볼륨 활용

 - 도커는 유니언 파일 시스템을 사용한다. 이는 하나의 이미지로부터 여러 컨테이너를 만들 수 있게 한다.
 - 컨테이너는 휘발상 프로세스이기 때문에 데이터가 보존되지 않는다.
 - 컨테이너에서 생성된 데이터를 유지하고, 컨테이너간 파일 시스템을 쉽게 공유할 수 있는 매커니즘이 **도커 볼륨**이다.

##### 3-3-1 도커 볼륨 타입
 
 - **docker volume create 볼륨이름**: 볼륨 생성
 - **docker volume ls**: 볼륨 조회
 - **docker volume inspect 볼륨이름**: 볼륨 검사 및 확인
 - **docker volume create 볼륨이름**: 볼륨 생성
 - **docker run -d 컨테이너이름 -v 볼륨이름:타겟경로 이미지**: -v 혹은 --mount 옵션을 통해 볼륨 지정 가능
 - **docker volume rm 볼륨이름**: 볼륨 제거, 마찬가지로 연결된 컨테이너가 있으면 불가능
 - **docker run -d 컨테이너이름 --mount type=bind source=경로 target=타겟경로 이미지**: Bind mount
    - 도커 볼륨 기법에 비해 제한적 사용
    - 호스트 파일 시스템 절대경로 : 컨테이너 내부경로를 직접 마운트
    - 사용자가 파일 또는 디렉토리를 생성하면 해당 호스트 파일 시스템의 소유자 권한으로 연결
    - 컨테이너 실행 시 지정하여 사용, 제거 시 마운트는 해제되지만 호스트 디렉토리 유지
 - **docker run -d 컨테이너이름 --mount type=tmpfs destination=타겟경로**: tmpfs mount
    - 임시적인 데이터 유지 기법 (호스트 메모리에서만 지속)
    - 중요한 파일을 임시로 사용 할 때 좋음
    - 컨테이너 실행 시 지정하여 사용하고, 컨테이너 제거 시 자동 해제


##### 3-3-2 컨테이너 리소스 런타임 제약 옵션
 
 - **--cpus**: 컨테이너가 사용 가능한 CPU 리소스 지정 (--cpus=1.5)
 - **--cpu-period**: CPU CFS(프로세스 공정 스케쥴러) 기간 제한 옵션, 보통 변경하지 않음
 - **--cpu-quota**: period 옵션에 설정된 기간을 CPU 스케쥴링에 얼마나 할당할지를 설정
 - **--cpuset-cpus**: 호스트 운영체제에서 멀티 코어 CPU인 경우 특정 코어 번호 지정 (--cpuset-cpus="0-2": 1,2,3 번째 CPU 지정)
 - **--cpuset-shares**: CPU 타임 스케쥴링 기법, 모든 컨테이너는 동일한 비율의 CPU주기를 갖고, 이 비율은 실행 중인 다른 모든 컴테이너의 가중치를 기준으로 컨테이너이 CPU 공유 가중치를 변경하여 적용. 기본값 1024
 - **--memory 혹은 -m**: 컨테이너가 사용하는 최대 메모리 크기 설정 (최소 4mb)
 - **--memory-swap**: 컨테이너가 디스크로 스왑할 수 있는 메모리양 지정 (0이면 스왑 해제 ,-1이면 무제한)
 - **--kernel-memory**: 최대 커널 메모리양 지정


##### 3-3-3 도커 네트워크



##### 3-3-4 도커 Kill 명령과 초기화

 - **docker kill**: 강제 종료 명령, 비정상적 종료 처리