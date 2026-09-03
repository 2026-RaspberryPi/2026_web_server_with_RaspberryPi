FROM mysql:8.0

# 한글 깨짐 방지를 위한 문자셋 설정
COPY conf/my.cnf /etc/mysql/conf.d/my.cnf

# 컨테이너가 처음 생성될 때(데이터 볼륨이 비어있을 때) 자동 실행되는 초기화 스크립트
COPY init/01_init.sql /docker-entrypoint-initdb.d/01_init.sql

EXPOSE 3306
