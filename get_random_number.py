from random import randint
import cfnresponse

def random_number():
    ''' Returns random number from 1 to 100'''
    return randint(1, 100)

def lambda_handler(event, context):
    ''' Returns name of security group '''
    if event['RequestType'] == 'Delete':
        cfnresponse.send(event, context, cfnresponse.SUCCESS, {'Value': '0'})
        return
    else:
        random_num = random_number()
        security_group_name = '{0}-{1}'.format(event['ResourceProperties']['SecurityGroupName'], random_num)
        cfnresponse.send(event, context, cfnresponse.SUCCESS, {'Value': security_group_name }, security_group_name)
        return security_group_name
