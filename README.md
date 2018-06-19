# Intellias DevOps meetup
Repository is created for Intellias meetup. Enjoy AWS ECS, CloudFormation and Lambda

# 1-st Demo
0. Login to your AWS account (Make sure it is not Production one :D)
1. Make sure you have at least one already created ssh key in your AWS account. If not, got to navigation console, choose `EC2` and on left verticale panel find and choose `Key Pairs`. Now I think you know what tot do :)
2. Open CloudFormation console and click on `Create Stack`
3. Now press `Choose File` and open `generic_ecs.json`, press `Next`
4. Fill `Stack name` field, choose ssh `KeyName`, choose `SubnetId` and VpcId for deployment and press `Next` once again

# 2-nd Demo
1. Open CloudFormation console and click on `Create Stack`
2. Now press `Choose File` and open `generate_random_number_for_security_group.json`, press `Next`
3. Fill `Stack name` field and press `Next`
4. Once stack has beed deployed create another one stack but now with `call_custom_lambda_function.json`. Type `SecurityGroupName` (what ever you want), and choose `VPC`
5. Voila, your firs custom function is creaed. Enjoy