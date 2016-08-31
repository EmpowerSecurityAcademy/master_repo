import time
import datetime

instances = [{'_in_monitoring_element': False,
 'ami_launch_index': u'0',
 'architecture': u'x86_64',
 'block_device_mapping': {},
 'connection': "EC2Connection:ec2.amazonaws.com",
 'dns_name': u'ec2-xxx-xxx-xxx-xxx.compute-1.amazonaws.com',
 'id': u'i-xxxxxxxx',
 'image_id': u'ami-xxxxxxxx',
 'instanceState': u'\n                    ',
 'instance_class': None,
 'instance_type': u'm1.large',
 'ip_address': u'xxx.xxx.xxx.xxx',
 'item': u'\n                ',
 'kernel': None,
 'key_name': u'FARM-xxxx',
 'launch_time': u'2009-10-27T17:10:22.000Z',
 'monitored': False,
 'monitoring': u'\n                    ',
 'persistent': False,
 'placement': u'us-east-1d',
 'previous_state': None,
 'private_dns_name': u'ip-10-xxx-xxx-xxx.ec2.internal',
 'private_ip_address': u'10.xxx.xxx.xxx',
 'product_codes': [],
 'public_dns_name': u'ec2-xxx-xxx-xxx-xxx.compute-1.amazonaws.com',
 'ramdisk': None,
 'reason': '',
 'region': "RegionInfo:us-east-1",
 'requester_id': None,
 'rootDeviceType': u'instance-store',
 'root_device_name': None,
 'shutdown_state': None,
 'spot_instance_request_id': None,
 'state': u'running',
 'state_code': 16,
 'subnet_id': None,
 'vpc_id': None}, {'_in_monitoring_element': False,
 'ami_launch_index': u'0',
 'architecture': u'x86_64',
 'block_device_mapping': {},
 'connection': "EC2Connection:ec2.amazonaws.com",
 'dns_name': u'ec2-xxx-xxx-xxx-xxx.compute-1.amazonaws.com',
 'id': u'i-xxxxxxxx',
 'image_id': u'ami-xxxxxxxx',
 'instanceState': u'\n                    ',
 'instance_class': None,
 'instance_type': u'm1.large',
 'ip_address': u'xxx.xxx.xxx.xxx',
 'item': u'\n                ',
 'kernel': None,
 'key_name': u'FARM-xxxx',
 'launch_time': u'2009-10-27T17:10:22.000Z',
 'monitored': False,
 'monitoring': u'\n                    ',
 'persistent': False,
 'placement': u'us-east-1d',
 'previous_state': None,
 'private_dns_name': u'ip-10-xxx-xxx-xxx.ec2.internal',
 'private_ip_address': u'10.xxx.xxx.xxx',
 'product_codes': [],
 'public_dns_name': u'ec2-xxx-xxx-xxx-xxx.compute-1.amazonaws.com',
 'ramdisk': None,
 'reason': '',
 'region': "RegionInfo:us-east-1",
 'requester_id': None,
 'rootDeviceType': u'instance-store',
 'root_device_name': None,
 'shutdown_state': None,
 'spot_instance_request_id': None,
 'state': u'running',
 'state_code': 16,
 'subnet_id': None,
 'vpc_id': None}]

#1472515193.44
current_time = time.time()


print(current_time)


for instance in instances:
	diff = datetime.timedelta(current_time, instance.launch_time)
	if diff >= "fifteent_minutes":
		if instance.state == "terminated":
			print instance
			#send twillio alert
			#connect to pagerduty
	




