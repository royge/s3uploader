# Arcanys S3 Uploader

[![pipeline status](https://gitlab.com/roye/s3uploader/badges/master/pipeline.svg)](https://gitlab.com/roye/s3uploader/commits/master)
[![coverage report](https://gitlab.com/roye/s3uploader/badges/master/coverage.svg)](https://gitlab.com/roye/s3uploader/commits/master)

## Deployment

1. Clone this repo

    `$ git clone <repo-url>`

1. Install `supervisor`

    `$ sudo apt-get install -y supervisor`

1. Update script config

    ```
    $ cd s3uploader
    $ cp s3uploader.conf.example s3uploader.conf
    ```

     Edit `s3uploader.conf` file and provide the correct values for ff:

     `<aws region>`,
     `<your access key`,
     `<your secret key>`,
     `<s3 bucket name>`,
     `<directory to watch>`,
     `<app directory>`

1. Install requirements

    ```
    $ pip install -r requirements/base.txt
    ```

1. Enable script

    ```
    $ sudo cp s3uploader.conf /etc/supervisor/conf.d/s3uploader.conf
    ```

1. Restart `supervisor`

    ```
    $ sudo service supervisor restart
    ```

## Test

1. Install requirements

    ```
    $ cd s3uploader
    $ pip install -r requirements/test.txt
    ```

1. Run test

    ```
    $ python -m unittest discover
    ```

1. Coverage

    ```
    $ py.test --cov=aws
    ```
