ec2_conn = boto.connect_ec2(aws_access_key_id=key, aws_secret_access_key=access)

reservations = ec2conn.get_all_instances(instance_ids=['i-12345678'])
instance = reservations[0].instances[0]