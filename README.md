# lambda-mailer
Python script to send feedback via AWS API Gateway, SES and Lambda. Features recaptcha verification.

## How to use

Register yourself with [Google reCAPTCHA](https://www.google.com/recaptcha), create a key and build a form. Note that you will need the key later on.

Clone this repo to some place, download the dependencies to your current work directory and create a constants file:

```
git clone https://github.com/moegyver/lambda-mailer.git
cd lamdba-mailer
pip install -r requirements.txt -t .
vim constants.py
```

The constants file needs to define a few variables:

```
FROM = '<source mailaddress>'
TO = ['<destination-mail-address>']
RECAPTCHA_SECRET = 'your-recaptcha-secret'
```

Edit the `feedback.py` file. Remove or add fields and change stuff like the subject and the message. 

Build a form that includes your reCAPTCHA and that triggers the lambda function. You can use AWS API Gateway for that. The lamdba function expects a JSON string as event input that looks something like this:

```
{
    "name": "<some string>",
    "contact": "<another string>",
    "publish": "<some other string>",
    "message": "<a longer string>",
    "recaptcha": "<the recaptcha response the form gets after solving the captcha>"
}
```

Obviously the keys have to match the keys in `feedback.py`.

You also have to sign up for AWS SES and AWS Lamdba. Don't forget to add some AWS IAM magic to allow the lambda function to use your SES setup.

Tie your API to your Lamdba function. This is pretty straight forward if you follow the instructions in the AWS documentation. I'll add some more info about this later, as well as an example form and the proper SES, Lamdba and API Gateway setup.

Enjoy and ping me if you have troubles!
