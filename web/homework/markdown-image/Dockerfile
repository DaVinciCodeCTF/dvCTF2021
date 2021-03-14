FROM r-base

RUN apt-get update && apt-get install -y python3-pip vim pandoc
RUN pip3 install Flask

COPY ./rscripts /app/rscripts/

RUN Rscript /app/rscripts/install_pkg.R
