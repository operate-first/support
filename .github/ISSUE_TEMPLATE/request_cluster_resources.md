---
name: General cluster-scoped resource request
about: "Requesting resources which require cluster-admin: CRDs, ClusterRoles, Operators, Quotas"
title: ""
labels: onboarding
assignees: ""
---

### Requested actions

#### Operator request

If you want to request an operator, please provide the following:

1. **Name of the Operator**:

2. **Operator version**:
   Desired operator version. If left blank we assume the latest version released by the operator maintainer.

3. **Operator scope**:
   Should the Operator be visible to a Single Namespace or All Namespaces

4. **Documentation and links**:
   Any documentations about this operator (if applicable) or links to OperatorHub.

#### Resource request

Please list all the resources you want to have deployed. Please list only the resources which can't be deployed by your project-admins. If possible, please include the resource manifest as a link to upstream definition or as an attachment file.

Requesting these resources to be deployed:

- A resource name: [links to manifests]()
- ...

### Questionnaire

1. **Team name**:
   Please specify on behalf of which team you are requesting this resource. If you don't have a team yet, please use our other "Onboarding to cluster" template.

---

If you don't want to wait for the maintainers to notice this issue, you can do the changes yourself. Please follow the docs [here](https://github.com/operate-first/apps/blob/master/cluster-scope/README.md).
