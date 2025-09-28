# Automatic-EBS-Snapshot

## 💾 Assignment 4: Automatic EBS Snapshot and Cleanup Using AWS Lambda & Boto3

This project implements a Lambda-based automation to create EBS snapshots and remove older ones beyond a retention period (default 30 days). This ensures both backup and cost-optimization.

---

## 📁 Project Structure

```
Assignment_4_EBS_Snapshot_Cleanup/
├── 01_ebs_setup/             # Guide to create or identify EBS volume
├── 02_iam_role/              # IAM role with EC2 permissions
├── 03_lambda_function/       # Lambda function to manage EBS snapshots
└── 04_documentation/         # Final README file
```

---

## ✅ Tasks Overview

### Task 1: EBS Setup

- Go to EC2 Dashboard → Volumes
- Use existing or create a new EBS volume (e.g., 8 GiB, gp2)
- (Optional) Attach it to an EC2 instance for demo
- Copy its **Volume ID**

---

### Task 2: IAM Role for Lambda

- Create IAM Role: `LambdaEBSSnapshotManager`
- Attach policy: `AmazonEC2FullAccess` *(or custom least privilege policy)*
- Ensure this role is assigned to the Lambda function

---

### Task 3: Lambda Function

- Runtime: Python 3.x
- Assign the above IAM role
- Replace placeholder `VOLUME_ID` with actual one in:
  - `ebs_snapshot_lambda.py`
- Deploy the code via Console or ZIP upload

🧠 Function Logic:
- Creates a snapshot for the specified volume
- Tags snapshots with `CreatedBy=LambdaBackup`
- Deletes snapshots older than 30 days with the same tag

---

### Task 4: Event Source (CloudWatch Scheduled Trigger)

To automate the execution:

1. Go to **Amazon CloudWatch → Rules**
2. Create a new rule:
   - **Event Source**: Schedule (e.g., `rate(7 days)`)
   - **Targets**: Select your Lambda function
3. Name your rule (e.g., `WeeklyEBSSnapshot`)
4. Enable the rule

🎯 This will trigger snapshot creation and cleanup every 7 days.

---

## 🧪 Manual Testing

- Go to Lambda Console → Your Function
- Click **Test**
- Observe:
  - Snapshot created with correct tag
  - Older snapshots (tagged) are deleted if > 30 days

---
