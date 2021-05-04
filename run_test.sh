#!/bin/bash

docker build -t learning_run .

docker run --name run_test learning_run

docker cp run_test:app/report/ .

allure serve report/allure-results

docker container rm run_test