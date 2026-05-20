import boto3

aws_management=boto3.session.Session(profile_name='default')
iam_console=aws_management.client(service_name='iam')


for each_user in iam_console.list_users()['Users']:
    print(each_user['UserName'])
