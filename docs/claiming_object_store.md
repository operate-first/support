# Claiming S3-compatible object store buckets

This doc brings a brief summary on how to request a hosted S3 buckets within the Operate First managed deployments. We use the [Rook](https://rook.io/) operator.

## Claim a new bucket

Deploying a following resource within your application will grant you a bucket:

```yaml
---
apiVersion: objectbucket.io/v1alpha1
kind: ObjectBucketClaim
metadata:
  name: CLAIM_NAME # Must be unique: you can't name it the same as any of your secrets or configmap. More details below
spec:
  generateBucketName: CLAIM_NAME-
  storageClassName: ocs-storagecluster-ceph-rgw
  additionalConfig:
    maxObjects: "1000"
    maxSize: "2G"
```

> Note: Users are required to use the `ocs-storagecluster-ceph-rgw` storage class in the MOC deployment. Otherwise the claim does not work. The storage class may differ for other clusters.

Once deployed and bound, the `ObjectBucketClaim` resource will be updated. Additionally a new `Secret` and a `ConfigMap` are created in the same namespace. **Both the secret as well as the configmap use the same name as the claim resource. Please make sure you don't overwrite any of your current secrets/configmaps.**

### Secret

The autocreated secret `CLAIM_NAME` contains 2 properties, which provide access credentials for this bucket:

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`

### ConfigMap

The autocreated configmap `CLAIM_NAME` contains 4 additional properties, which specifies means to access the bucket:

- `BUCKET_HOST` which corresponds to an internal cluster route to the Rook operator deployment (`*.openshift-storage.svc.cluster.local`).
- `BUCKET_NAME` which holds the unique name (in the cluster) of the bucket, prefixed with what was specified in `spec.generateBucketName` of the `ObjectBucketClaim`
- `BUCKET_PORT`
- `BUCKET_REGION`
- `BUCKET_SUBREGION`

### Usage in deployment

In order to use the bucket within your deployment, you can mount the `Secret` and a `ConfigMap`:

```yaml
...
spec:
  containers:
    - name: mycontainer
      ...
      envFrom:
        - configMapRef:
          name: CLAIM_NAME
        - secretRef:
          name: CLAIM_NAME
```

## Resources and links

- [`ObjectBucketClaim` in Rook documentation](https://rook.io/docs/rook/v1.5/ceph-object-bucket-claim.html)
