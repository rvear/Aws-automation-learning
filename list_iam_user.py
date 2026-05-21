'''This is the python script to list all the iam users in the aws account'''

import boto3

aws_management=boto3.session.Session(profile_name='default')
iam_console=aws_management.resource(service_name='iam')


for each_user in iam_console.users.all():
    print(each_user.name)
