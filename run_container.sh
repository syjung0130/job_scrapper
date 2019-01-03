#!/bin/sh
docker run -it --volume="$PWD/../..:/workdir/job_scrapper" --volume="$PWD/build:/workdir/build" scrapper:imx-1
