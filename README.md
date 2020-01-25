# Utilities for AWS Lambda Layer

This is a versatile AWS Lambda Layer collection.

## Description

It contains libraries that are likely to be used frequently with the AWS Lambda Layer.

## Features

* Python
    * Slack notification

## Requirement

* zip
* awscli
* Pytest

## Usage

1. zip archive

    `zip -r hoge-layer.zip python`

2. Create a Layer

    ```Shell
    aws lambda publish-layer-version \
    --layer-name hogehoge \
    --zip-file fileb://layer.zip \
    --compatible-runtimes python3.8
    ```

3. Adds a Layer to the Lambda Function and invokes the process

    ```Python
    import slack_notification

    ...

    slack_notification.notify(WEBHOOK_URL, 'message')

    ```

## Installation

`git clone https://github.com/sinokuma/lambda-layer.git`

## Set your destination URL

Before you run Pytest, please set `'SLACK_WEBHOOK_URL'` to the URL of the notification destination.

## Reference

See https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html

## Author

[@sinocloudon](https://twitter.com/sinocloudon)

## License

[MIT](http://b4b4r07.mit-license.org)