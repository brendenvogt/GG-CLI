from ggcli.commands.s3 import S3


def get_plugins():
    return [
        ('s3', S3())
    ]
