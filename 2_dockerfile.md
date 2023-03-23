# 컨테이너 환경 구성을 위한 Dockerfile 구성
---

### 1. 코드로 개발하는 컨테이너 인프라, Dockerfile



#### 1-1 IaC와 Dockerfile

 - **IaC (Infrastructure as Code, 인프라 구축을 코드화하여 개발)의 필요성**
    - 커맨드 기반의 인프라 구성시 실수 가능성 줄이기
    - 설치 순서, 상호 연관, 라이브러리 의존성 및 명령어들의 효율적인 관리
    - 각종 환경 설정 관리 효율
    - 높은 유지보수성
    - 도커, 앤서블, 쿠버네티스등이 IaC를 지원하는 도구

 - **Dockerfile**
    - 어플리케이션에 적용되는 새로운 환경을 사용자가 직접 프로비저닝하는 도구


#### 1-2 최적의 Dockerfile 만들기

 - **경량의 컨테이너 서비스 제공**: 빠른 컨테이너 배포를 위한 최소한의 설정과 구성
 - **dockerfile에 담기는 레이어 최소화**: 올바른 명령어 사용으로 레이어 수 줄이기
 - **하나의 어플리케이션은 하나의 컨테이너**: 컨테이너간 독립성 보장하기
 - **캐시 활용하기**: 캐싱을 통한 빌드 속도 향상
 - **IaC 환경 개발은 디렉토리 단위**: 올바른 빌드 컨텍스트
 - **서버리스 환경 개발**



### 2. Dockerfile 명령어와 이미지 빌드


#### 2-1 Dockerfile 명령어

 - **FROM**: 생성하려는 이미지의 베이스 이미지 지정
    - FROM ubuntu:20.04
    - FROM python:3.9<br>
 - **MAINTAINER**: 이미지를 빌드한 작성자 이름과 이메일 작성
    - MAINTAINER sahayana <sahayanayang@gmail.com><br>
 - **LABEL**: 이미지 작성 목적으로 버전, 타이틀, 설명등을 작성, 1개 이상 작성 가능
    - LABEL purpose = "Webserver for testing"
    - LABEL version - '1.0'<br>
 - **RUN**: 설정된 기본 이미지에 패키지 업데이트, 설치, 명령 실행 등을 작성, apt, yum 방법과 동일, 1개 이상 작성 가능
    - RUN apt update && apt install -y nginx git vim curl<br>
 - **CMD**: 생성된 이미지를 컨테이너로 실행할 때 쓰는 명령, ENTRYPOINT 명령으로 지저오딘 커맨드에 디폴트로 넘길 파라미터 지정, 마지막 CMD명령 1개만 처리됨
    - CMD apachectl -D FOREGROUND<br>
 - **ENTRYPOINT**: CMD와 비슷하지만 컨테이너가 실행될 때 명령어 및 인자 값을 전달, 여러개의 CMD를 사용하는 경우 함께 적용
    - ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]
    - 컨테이너 실행 시 항상 수행해야 하는 명령어를 지정
    - CMD는 컨테이너 실행 시 다양한 명령어를 지정하는 경우 유용<br>
 - **COPY**: 호스트 환경의 파일, 디렉토리를 이미지 안에 단순 복사
    - COPY ./app.py /user/services<br>
 - **ADD**: 호스트 환경의 파일, 디렉토리를 복사 및 URL주소에서 다운로드, 압축파일(tar, tar.gz) 해제 
    - ADD index.html /user/share/nginx/html
    - ADD http://example.com/view/customer.tar.gz /workspace/data/<br>
 - **ENV**: 이미지 안에 각종 환경 변수를 지정(PATH, 버전, 디렉토리 주소 등), RUN 혹은 WORKDIR 등에서 환경 변수를 사용해 반복을 피함
    - ENV python 3.9
    - ENV PATH /usr/local/nginx/bin:$PATH
    - ENV JAVA_HOME /user/lib/jvm/java-8-oracle<br>
 - **EXPOSE**: 컨테이너가 호스트 네트워크를 통해 들어오는 트래픽을 리스닝하는 포트와 프로토콜 지정
    - EXPOSE 80
    - EXPOSE 443/tcp<br>
 - **VOLUME**: 도커 볼륨을 이미지 빌드에 미리 설정
    - VOLUME /var/log
    - VOLUME /etx/nginx<br>
 - **USER**: USER 변경, 기본 사용자는 root
    - USER sahayana<br>
 - **WORKDIR**: 컨테이너상에서 작업할 경로 전환, WORKDIR 설정이 없으면 RUN, CMD등의 명령문은 해당 디렉터리를 기준으로 실행
    - WORKDIR /workspace<br>
 - **ARG**: build 시점에서 변수의 값을 전달하기 위해 **--build-arg=인자**를 정의하여 사용, 민감한 정보 사용 주의
    - ARG db_name
    - docker build --build-arg db_name=test_db
    - CMD db_start.sh -h 127.0.0.1 -d ${db_name}<br>
 - **ONBUILD**: 부모 Dockerfile이 자식 Dockerfile에 명령 전달, 부모-> 개발 환경 설정 이후 자식-> ONBULILD에 지저오딘 소스 실행 
    - 1차 Dockerfile 빌드: ONBUILD ADD websource.tar.gz /user/share/nginx/html
    - 2차 Dockerfile 빌드: 위의 1차 Dockerfile에서 ONBUILD로 지정한 ADD명령어 실행<br>
 - **STOPSIGNAL**: 컨테이너 중지(stop 명령어)시 다른 시그널을 포함
    - STOPSIGNAL SIGKILL<br>
 - **HEALTHCHECK**: 컨테이너 프로세스 상태 체크, 하나의 명령(마지막)만 유효
    - HEALTHCHECK --interval=1m --timeout=3s --retries=5<br>
 - **SHELL**: Dockerfile 내부에서 기본 셸 지정, 기본값으로 '/bin/sh'
    - SHELL ["/bin/bash", "-c"]<br>