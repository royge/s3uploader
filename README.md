# Arcanys S3 File Uploader

## Deployment

1. Clone this repo

    `$ git clone <repo-url>`

1. Install `supervisor`

    `$ pip install supervisor`

1. Set environment variables

    ```
    $ export AWS_REGION=<aws-region>
    $ export AWS_ACCESS_KEY_ID=<your-access-key>
    $ export AWS_SECRET_ACCESS_KEY=<your-secret-key>
    $ export AWS_S3_BUCKET_NAME=<your-s3-bucket>
    ```

1. Update script config

   Edit `arcs3uploader.conf` file and provide the correct values for
   `<directory to watch>` and `<app directory>`.

1. Install requirements

    ```
    $ cd arcs3uploader
    $ pip install -r requirements/base.txt
    ```

1. Enable script

    ```
    $ sudo cp arcs3uploader.conf /etc/supervisor/conf.d/arcs3uploader.conf
    ```

1. Restart `supervisor`

    ```
    $ sudo supervisorctl restart arcs3uploader
    ```

## Test

1. Install requirements

    ```
    $ cd arcs3uploader
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
