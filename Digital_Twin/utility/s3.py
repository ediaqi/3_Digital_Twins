import logging
from pathlib import Path

import boto3

from utility.common import format_logger

logger = logging.getLogger(__name__)
format_logger(logger)

_IMAGE_EXTENSIONS = [".png", ".jpg", ".jpeg", ".tiff", ".bmp"]

s3_client = boto3.client('s3')

def get_bucket_and_prefix(s3_uri):
    s3_uri = s3_uri.replace("s3://", "")
    dirs = s3_uri.split("/")
    bucket_name = dirs[0]
    prefix = "/".join(dirs[1:])

    return bucket_name, prefix


def download_dir(prefix=None, bucket=None, s3_uri=None, output_path=None, client=s3_client, relative_download=True):
    """
    params:
    - prefix: pattern to match in s3
    - output_path: output_path path to folder in which to place files
    - bucket: s3 bucket with target contents
    - s3_uri: alternative to specifying prefix and bucket, path to an S3 object
    - client: initialized s3 client object
    """
    keys = []
    dirs = []
    next_token = ''

    if s3_uri:
        bucket, prefix = get_bucket_and_prefix(s3_uri)

    if not output_path:
        logger.error(f"Path to output_path directory not specified. Aborting download from S3 (S3 URI: {s3_uri}).")
        return

    output_path = Path(output_path)

    base_kwargs = {
        'Bucket': bucket,
        'Prefix': prefix,
    }
    while next_token is not None:
        kwargs = base_kwargs.copy()
        if next_token != '':
            kwargs.update({'ContinuationToken': next_token})

        results = client.list_objects_v2(**kwargs)
        contents = results.get('Contents')
        if not contents:
            logger.error(f"No contents found at s3://{bucket}/{prefix}!")
            return

        for i in contents:
            k = i.get('Key')
            if k[-1] != '/':
                keys.append(k)
            else:
                dirs.append(k)
        next_token = results.get('NextContinuationToken')
    for d in dirs:
        dest_pathname = output_path / d
        dest_pathname.mkdir(exist_ok=True, parents=True)
    for k in keys:
        if relative_download:
            try:
                relative_path = Path(k).relative_to(prefix)
            except ValueError:
                # this object is not a subdirectory of directory specified by the prefix, but has the prefix in its name
                continue
            dest_pathname = output_path / relative_path
        else:
            dest_pathname = output_path / k

        dest_pathname.parent.mkdir(exist_ok=True, parents=True)
        client.download_file(bucket, k, str(dest_pathname))

    logger.info(f"Downloaded s3://{bucket}/{prefix} to {output_path}.")
    