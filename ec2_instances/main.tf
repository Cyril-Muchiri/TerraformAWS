provider "aws" {
  region = "us-east-1"
}


data "aws_ami" "ubuntu" {
    most_recent = true
    owners      = ["099720109477"] 

    filter {
        name   = "name"
        values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]
    }

    filter {
        name   = "virtualization-type"
        values = ["hvm"]
    }
}

resource "aws_instance" "ec2_instance" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = var.instance_type

  vpc_security_group_ids = ["sg-015d52317b0dd8a00"]  # Replace with your security group ID
  subnet_id              = "subnet-0539a13655de53fab"  # Replace with your subnet ID

  tags = {
    Name = "Mkurugenzi"
  }

  
}