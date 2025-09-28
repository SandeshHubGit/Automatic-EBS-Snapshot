# 🔐 Task 2: IAM Role for Lambda (EBS Snapshot Automation)

To allow your Lambda function to manage EBS snapshots, we need to create an IAM role with appropriate EC2 permissions.

---

## ✅ Step-by-Step Instructions

### 1. Open IAM Console

- Go to: [AWS IAM Console](https://console.aws.amazon.com/iam/)
- Click **Roles** → **Create Role**

---

### 2. Select Trusted Entity

- **AWS Service**
- Use Case: **Lambda**
- Click **Next**

---

### 3. Attach Permissions Policies

🔹 Attach the following managed policy:

```
AmazonEC2FullAccess
```

📌 Note: In real environments, use a restricted custom policy like:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:DescribeVolumes",
        "ec2:CreateSnapshot",
        "ec2:DeleteSnapshot",
        "ec2:DescribeSnapshots",
        "ec2:CreateTags"
      ],
      "Resource": "*"
    }
  ]
}
```

---

### 4. Name the Role

- Suggested name: `LambdaEBSSnapshotManager`
- Click **Create Role**

---

### 5. Confirm

- Go to **Roles** → Search for your role
- Ensure that `AmazonEC2FullAccess` or custom policy is attached

---

✅ You are now ready to create and assign this IAM role to your Lambda function in the next task.