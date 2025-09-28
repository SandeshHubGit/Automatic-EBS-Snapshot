import boto3
from datetime import datetime, timedelta, timezone

# Replace with your actual EBS volume ID
VOLUME_ID = 'vol-xxxxxxxxxxxxxxxxx'
RETENTION_DAYS = 30

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    now = datetime.now(timezone.utc)
    deleted_snapshots = []
    created_snapshot_id = None

    # 1. Create new snapshot
    try:
        snapshot = ec2.create_snapshot(
            VolumeId=VOLUME_ID,
            Description=f"Automated backup - {now.strftime('%Y-%m-%d %H:%M:%S')}",
            TagSpecifications=[
                {
                    'ResourceType': 'snapshot',
                    'Tags': [{'Key': 'CreatedBy', 'Value': 'LambdaBackup'}]
                }
            ]
        )
        created_snapshot_id = snapshot['SnapshotId']
        print(f"✅ Snapshot created: {created_snapshot_id}")
    except Exception as e:
        print(f"❌ Error creating snapshot: {e}")

    # 2. Cleanup old snapshots created by this Lambda
    try:
        snapshots = ec2.describe_snapshots(
            Filters=[
                {'Name': 'volume-id', 'Values': [VOLUME_ID]},
                {'Name': 'tag:CreatedBy', 'Values': ['LambdaBackup']}
            ],
            OwnerIds=['self']
        )['Snapshots']

        for snap in snapshots:
            snap_time = snap['StartTime']
            snap_id = snap['SnapshotId']
            if snap_time < now - timedelta(days=RETENTION_DAYS):
                ec2.delete_snapshot(SnapshotId=snap_id)
                print(f"🗑️ Deleted old snapshot: {snap_id}")
                deleted_snapshots.append(snap_id)
    except Exception as e:
        print(f"⚠️ Error during cleanup: {e}")

    return {
        'CreatedSnapshot': created_snapshot_id,
        'DeletedSnapshots': deleted_snapshots,
        'DeletedCount': len(deleted_snapshots)
    }