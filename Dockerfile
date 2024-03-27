FROM apisecuniversitymohsin/free-cicd-api-testing-baseimage:latest

WORKDIR /apisec

COPY ./entrypoint-free-api-testing-action.py /apisec/entrypoint-free-api-testing-action

RUN chmod +x /apisec/entrypoint-*
ENTRYPOINT ["/apisec/entrypoint-free-api-testing-action"]