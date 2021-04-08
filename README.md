# Operate First on MOC

This repository contains all the operational and user documentation for running the Operate First applications in MOC.

## Getting Started

We have Operate First applications deployed and running in a MOC ([Mass Open Cloud](https://massopen.cloud/)) cluster using the [Open Data Hub](https://opendatahub.io/) Operator.

You can find detailed information for the deployed apps on the Operate-First website: [operate-first.cloud](https://www.operate-first.cloud/)

For Open Data Hub specific applications, the ODH homepage on MOC can be found at ODH Dashboard: [odh.operate-first.cloud](https://odh.operate-first.cloud/). <br>

From there you can access any of the provided applications:

[![ODh Dashboard](docs/assets/images/odh-dashboard.png)](https://odh.operate-first.cloud/)

## Component status

| Component               | Availability      | Authentication (see below)                                                         |
| ----------------------- | ----------------- | ---------------------------------------------------------------------------------- |
| AI-Library              | ❌ (Not deployed) |                                                                                    |
| Airflow                 | ❌ (Not deployed) |                                                                                    |
| Argo                    | ✔️                | None (Login via OpenShift [WIP](https://github.com/operate-first/odh/issues/39))   |
| Grafana                 | ✔️                | Custom (Login via OpenShift [WIP](https://github.com/operate-first/odh/issues/37)) |
| Hue                     | ✔️                | user:`generic_user` pass:`operatefirst` (Login via OpenShift [WIP](https://github.com/operate-first/odh/issues/47)) |
| JupyterHub              | ✔️                | Login via OpenShift                                                                |
| Kafka                   | ✔️ (Stabilizing)  |                                                                                    |
| ODH Dashboard           | ✔️                | None                                                                               |
| Prometheus              | ✔️                | None                                                                               |
| Seldon                  | ❌ (Not deployed) |                                                                                    |
| Spark                   | ✔️                | None                                                                               |
| Spark SQL Thrift Server | ✔️                | None                                                                               |
| Superset                | ✔️                | user:`generic_user` pass:`operatefirst` (Login via OpenShift [WIP](https://github.com/operate-first/odh/issues/48)) |
| Kubeflow Dashboard      | ✔️                | None                                                                               |
| Kubeflow Pipelines      | ✔️                | None                                                                               |

### Authenticate via OpenShift

We aim to support authentication via the underlying OpenShift platform for all the components.

Each supported component provides a login button which states "Login via OpenShift" or "Sign in with OpenShift". This will lead you to authentication provider selection screen:

![Auth provider selection screen in OpenShift](docs/assets/images/openshift-login.png)

Please select `moc-sso` provider. Then choose the final account provider that fits you the most:

![MOC auth provider selection screen](docs/assets/images/moc-login.png)

## End User Support

If you have any problems, questions and feature requests please report them by opening an issue in this repo [here](https://github.com/operate-first/odh-moc-support/issues) and we will be happy to assist!

## Community

- Website: https://www.operate-first.cloud/
- Slack Chat Room: https://join.slack.com/t/operatefirst/shared_invite/zt-o2gn4wn8-O39g7sthTAuPCvaCNRnLww
