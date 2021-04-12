# Operate First Support

Website:  https://www.operate-first.cloud/

This is the support repository for the Operate First Initiative.

For any questions, concerns, and/or requests, please use the appropriate [Issue Template][1]. If no template fits your requirement, then please make a regular GitHub issue [here][2].

## [MOC][14] Environment

Operate First initiative currently manages two clusters which are a part of the MOC environment. These are:

- `Zero` cluster. This cluster houses all user workloads.
- `Infra` cluster. This cluster is the management cluster, it is intentionally minimal and houses ACM and ArgoCD.

Please create an issue [here][3] if you would like to use a cluster. Note that unless you want to use ACM or operate ArgoCD, you are likely looking for access to the Zero cluster.

## Managed Services

Operate First also manages various applications and services in the environments listed above. Access to these services is available to the general public.

You can find our availability dashboards for various managed services [here][22].

#### [Open Data Hub (ODH)][15]
Dashboard:  https://odh.operate-first.cloud/

We manage a deployment of ODH on the MOC Zero cluster. You can read more about our deployment of Open Data Hub [here][4].

#### [Kubeflow][16]
Dashboard: http://istio-ingressgateway-istio-system.apps.zero.massopen.cloud/

We deploy a selection of Kubeflow components on the MOC Zero cluster. You can read more about our deployment of Kubeflow [here][5].

#### [ArgoCD][17]
Console: https://argocd.operate-first.cloud

Monitoring: https://grafana-route-opf-monitoring.apps.zero.massopen.cloud/d/97AYZMTGk/argocd?orgId=1

We manage a multi-tenant deployment of ArgoCD which runs on the MOC Infra cluster. Anyone can be onboarded to this ArgoCD instance and use it to deploy to any cluster managed by Operate First. You will first need to be onboarded to the OCP cluster you would like to deploy your applications on, then be onboarded to ArgoCD.

To request access to an OCP cluster file an issue [here][6].

To request access to ArgoCD file an issue [here][7].

#### [Observatorium][18]

Thanos: http://thanos-query-frontend-opf-observatorium.apps.zero.massopen.cloud

Monitoring: https://grafana-route-opf-monitoring.apps.zero.massopen.cloud/dashboards/f/VYns1DlGz/thanos

We have the Observatorium operator deployed on the Zero cluster. The operator deploys an instance of Observatorium which is currently used to provision Thanos for long term storage, and Loki for querying logs.

Thanos is used to enable long term storage for our Prometheus (Deployed by ODH). Anyone can enable their applications (deployed on Zero cluster) to be monitored by this Prometheus instance. To add monitoring to your applications, you can follow the instructions [here][8] and make a PR against this repo.

You can also send or retrieve logs using Loki. See [here][9] to learn more.

#### [Cluster Logging Operator][19]
Kibana UI: https://kibana-openshift-logging.apps.zero.massopen.cloud/

Elasticsearch Route: https://elasticsearch-openshift-logging.apps.zero.massopen.cloud

We deploy the CLO operator on the MOC Zero cluster. With it, we have Elasticsearch and Kibana deployed. Anyone that has been onboarded to the Zero cluster can access their Application logs via Kibana. You can also curl directly to Elasticsearch using the route above, but you will need to provide your OCP bearer token.

#### [Openshift Container Storage (OCS)][20]
We deploy the OCS operator on the MOC Zero cluster. OCS provides both persistent volumes and S3 compatible object storage via Rook Operator. Users can deploy their own S3 buckets via ObjectBucketClaims.  See [here][10] for details.

#### [Dex OIDC Provider][21]
We manage an instance of Dex on the Zero cluster that is currently being worked on to provide authentication for some of our services. This instance can be used to also drive authentication for other users. Docs for this are not yet available, but for the experienced, you can find the configurations [here][11].

## End User Support

Slack: https://join.slack.com/t/operatefirst/shared_invite/zt-o2gn4wn8-O39g7sthTAuPCvaCNRnLww

The community slack channel can be found in the link above. If you have any questions feel free to post a message to the `#support` channel.

[1]: https://github.com/operate-first/support/issues/new/choose
[2]: https://github.com/operate-first/odh-moc-support/issues
[3]: https://github.com/operate-first/support/issues/new?assignees=&labels=onboarding&template=onboarding_to_cluster.md&title=
[4]: ./docs/odh/README.md
[5]: ./docs/kubeflow/README.md
[6]: https://github.com/operate-first/support/issues/new?assignees=&labels=onboarding&template=onboarding_to_cluster.md&title=
[7]: https://github.com/operate-first/support/issues/new?assignees=&labels=onboarding&template=onboarding_argocd.md&title=
[8]: https://github.com/operate-first/support/blob/main/docs/add_service_monitoring.md
[9]: https://www.operate-first.cloud/users/apps/docs/observatorium/loki/README.md
[10]: https://rook.io/
[11]: https://www.operate-first.cloud/users/support/docs/claiming_object_store.md
[12]: https://github.com/operate-first/apps/blob/master/auth/overlays/moc/zero/dex-cm.yaml
[13]: https://github.com/operate-first/odh-moc-support/issues
[14]: https://massopen.cloud/
[15]: https://opendatahub.io/
[16]: https://www.kubeflow.org/
[17]: https://argoproj.github.io/argo-cd/
[18]: https://github.com/observatorium
[19]: https://docs.openshift.com/container-platform/4.7/logging/cluster-logging.html
[20]: https://www.openshift.com/blog/introducing-openshift-container-storage-4-2
[21]: https://github.com/dexidp/dex
[22]: https://grafana-route-opf-monitoring.apps.zero.massopen.cloud/d/r7WqgaBMk/operatefirst-availability?orgId=1&refresh=1m
