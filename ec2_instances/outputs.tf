output "instance_id" {
  value = aws_instance.ec2_instance.id
}

output "public_ip" {
  value = aws_instance.ec2_instance.public_ip
}

output "zone" {
  value = aws_instance.ec2_instance.availability_zone
}