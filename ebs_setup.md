# 💽 Task 1: EBS Volume Setup (for Snapshot & Cleanup Automation)

In this step, you will identify or create an Amazon EBS volume to be backed up using automated Lambda snapshots.

---

## ✅ Step-by-Step Instructions

### 1. Navigate to EC2 Dashboard

- Go to: [AWS EC2 Console](https://console.aws.amazon.com/ec2/)
- In the left panel, select **Elastic Block Store → Volumes**

---

### 2. Create or Use Existing EBS Volume

#### Option A: Use Existing Volume
- If you already have a volume attached to an EC2 instance, note its **Volume ID** (e.g., `vol-0123456789abcdef0`)

#### Option B: Create a New Volume
1. Click **Create Volume**
2. Select:
   - **Volume type**: General Purpose SSD (gp2)
   - **Size**: e.g., 8 GiB
   - **Availability Zone**: Same AZ as your EC2 instance (if attaching)
3. (Optional) Attach it to an instance using:
   - **Actions > Attach Volume**

---

### 3. Tag the Volume (Optional but Recommended)

Tag the volume to manage or identify it easily:

| Key        | Value            |
|------------|------------------|
| Name       | EBS-Backup-Demo  |
| Backup     | True             |

---

### 4. Copy the Volume ID

You will need the **Volume ID** for the Lambda function that creates snapshots.

✅ Format: `vol-xxxxxxxxxxxxxxxxx`

---

Once your EBS volume is ready and you have the Volume ID noted, proceed to IAM role creation.