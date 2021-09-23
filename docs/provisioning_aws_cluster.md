# Provisioning an AWS Cluster

In this doc we describe how to provision a new AWS OCP cluster via ACM

The reference images describe the settings when using the AWS OCTO provider.

### Pre-requisite
Must be an Operate-First admin, with cluster-admin access to ACM


### Steps:

Navigate to https://multicloud-console.apps.moc-infra.massopen.cloud/multicloud/clusters

Click "Create Cluster"

![][1]

#### Infrastructure Provider
Select "Red Hat OpenShift Container Platform" as the Kubernetes distribution
Select "Amazon Web Services" as the infrastructure provider
Select the appropriate "Infrastructure Provider Credentials" from the drop down (`aws-octo` for the OCTO aws account)
Click Next

![][2]


#### Cluster Details
Choose an appropriate `cluster name`, keep in mind this name will appear on all the routes.
Leave `cluster set` and `additional labels` blank.
Choose the latest release image.
Base DNS domain will be auto filled in based on the configured provider you selected (`aws.operate-first.cloud` for OCTO aws account).

![][3]

#### Master Node
Select the appropriate aws region to deploy the master nodes to (`us-west-2` for OCTO aws account).
Leave the `Zones` section empty (i.e. do not select any zones). This will ensure all zones may be used.

For instance type we find `m5.2xlarge` to be sufficient.
Root Storage can be left at 100GiB.

![][4]

#### Worker Pools
Pool name can be left as `worker`.
Leave zones empty once again.
Select the Instance type as per your requirements, same with the node count.
Root storage can be kept 100.

![][5]


#### Networking
Network type should be OpenShiftSDN

Fill out the network details as needed. For the AWS OCTO account, the defaults are sufficient.

![][6]

#### Automation
Leave empty and click next.

#### Review
Review your changes, the examples above result in the following:

![][7]

Once everything is confirmed, click create.

You should be greeted with a "Creating Cluster screen."

![][8]

Once the cluster is successfully provisioned, you can login using the `kubeadmin` credentials provided via the ACM console.

The next step is to make sure it's properly onboarded. You can follow the guide [here][onboarding] on how to go about doing this.

[1]: assets/images/add_cluster/1.png
[2]: assets/images/add_cluster/2.png
[3]: assets/images/add_cluster/3.png
[4]: assets/images/add_cluster/4.png
[5]: assets/images/add_cluster/5.png
[6]: assets/images/add_cluster/6.png
[7]: assets/images/add_cluster/7.png
[8]: assets/images/add_cluster/8.png

[onboarding]: https://github.com/operate-first/hitchhikers-guide/blob/main/pages/onboarding_new_cluster.ipynb
