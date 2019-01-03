# job_scrapper
원하는 조건 Language, 분야에 따라 관련된 saramin, jobkorea 채용공고 및 url을 수집

# Docker build  
 - docker build -t scrapper:imx-1 .
  
# Run Docker container 
  - docker run -it --volume="$PWD/../..:/workdir/job_scrapper" --volume="$PWD/build:/workdir/build" scrapper:imx-1
  - or ./run_container.sh

