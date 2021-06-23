# Operate First Support

Website:  https://www.operate-first.cloud/

GitHub Support Repository: https://github.com/operate-first/support

For any questions, concerns, and/or requests, please use the appropriate [Issue Template][1] to open an issue on our GitHub. If no template fits your requirement, then please make a regular GitHub issue [here][2].

## End User Support

We have a [community slack channel](https://join.slack.com/t/operatefirst/shared_invite/zt-o2gn4wn8-O39g7sthTAuPCvaCNRnLww) where we post announcements, general information, and more. If you have any questions, feel free to post a message to the `#support` channel.

## [MOC][14] Environment

The Operate First initiative currently manages two clusters within the MOC environment.

- `Zero` cluster for all user workloads
- `Infra` cluster for cluster management, housing ACM and ArgoCD

Please create an issue [here][3] if you would like to use a cluster. Note that unless you want to use ACM or operate ArgoCD, you are likely looking for access to the Zero cluster.

## Managed Services

Operate First manages various applications and services in the environments listed above. These services are accessible to the general public, and their availability dashboards can be found [here][22].

> Note: Access to monitoring and dashboards (i.e. Prometheus and Grafana) is currently restricted, pending discussions on EULAs and data licensing. If you need to access these services in the meantime, please make an issue. We will do our best to accommodate your request.

* [Open Data Hub][15]
    * We manage a deployment of Open Data Hub (ODH) on the MOC Zero cluster
    * [Read more](4) about our deployment of ODH and access our [dashboard](https://odh.operate-first.cloud/)

* [Kubeflow][16]
    * We deploy a selection of Kubeflow components on the MOC Zero cluster
    * [Read more](5) about our deployment of Kubeflow and access our [dashboard](http://istio-ingressgateway-istio-system.apps.zero.massopen.cloud/)

* [ArgoCD][17]
    * We manage a multi-tenant deployment of ArgoCD on the MOC Infra cluster
    * Anyone can be onboarded to this ArgoCD instance and use it to deploy to any cluster managed by Operate First
        * Before being onboarded to ArgoCD, you must be onboarded to the OCP cluster you wish to deploy your applications on
        * Request access to an OCP cluster by filing an issue [here][6] and ArgoCD by filing an issue [here][7]
    * Console: https://argocd.operate-first.cloud
    * Monitoring: https://grafana-route-opf-monitoring.apps.zero.massopen.cloud/d/97AYZMTGk/argocd?orgId=1

* [Observatorium][18]
    * We have an instance of Observatorium currently being used to provision Thanos and Loki
    * Thanos enables long term storage for Prometheus (deployed by ODH)
        * Anyone can enable their applications deployed on Zero cluster to be monitored by this Prometheus instance
        * To do so, follow the instructions [here][8] and make a pull request against this repo
    * Loki is used to query logs; click [here][9] to learn more about sending or retrieving logs using Loki
    * Thanos: http://thanos-query-frontend-opf-observatorium.apps.zero.massopen.cloud
    * Monitoring: https://grafana-route-opf-monitoring.apps.zero.massopen.cloud/dashboards/f/VYns1DlGz/thanos

* [Cluster Logging Operator][19]
    * We deploy the Cluster Logging Operator (CLO) with Elasticsearch and Kibana on the MOC Zero cluster
    * Anyone who has been onboarded to the Zero cluster can access their application logs via [Kibana](https://kibana-openshift-logging.apps.zero.massopen.cloud/)
    * You can also curl directly to Elasticsearch from [this route](https://elasticsearch-openshift-logging.apps.zero.massopen.cloud), but you will need to provide your OCP bearer token

* [Openshift Container Storage][20]
    * We deploy the Openshift Container Storage (OCS) operator on the MOC Zero cluster
    * OCS provides both persistent volumes and S3 compatible object storage via Rook Operator
    * Users can deploy their own S3 buckets via ObjectBucketClaims - see [here][10] for details

* [Dex OIDC Provider][21]
    * We manage an instance of Dex on the Zero cluster; we are working towards using Dex to provide authentication for some of our services
    * Our Dex instance can also be used to drive authentication for other users. While documents are not yet available for this, experienced users can find the configurations [here][11]

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
