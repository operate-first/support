---
name: Onboard to Continuous Deployment
about: Requesting application to be automatically deployed via ArgoCD to any managed OpenShift cluster
title: ""
labels: onboarding
assignees: ""
---

### Requested actions

Select all that apply:

- [ ] Create a new ArgoCD project for existing team
- [ ] Enlist an application to be deployed automatically via ArgoCD

### Questionnaire

#### Creating a new project

1. **Team name**:
   Please tell us your team name, which corresponds to [an already available user `Group`](https://github.com/operate-first/apps/tree/master/cluster-scope/base/groups).

2. **Target cluster**:
   Choose an environment from [this list](https://github.com/operate-first/apps/tree/master/cluster-scope/overlays)

3. **Managed namespaces**:
   The target namespaces that should be managed by ArgoCD. Preferably using [a single (team name) prefix](https://github.com/operate-first/support/blob/main/docs/onboarding_to_argocd.md#additional-notes).

#### Deploying a new application:

1. **Team name or your Argo CD project**:
   Please specify your Argo CD project name. If you're using this template to request both, project and application, you can skip this field.

2. **Application source git repository**:
   URL to the source repository. Please specify if the repository is private. In that case we'll exchange credentials later on.

3. **Path to manifests within the repository**:
   Relative path within the repository to the resources you want Argo CD to deploy.

4. **Target cluster**:
   Choose an environment from [this list](https://github.com/operate-first/apps/tree/master/cluster-scope/overlays)

5. **Target namespace for the application**:
   Please specify an existing namespace in the target cluster which is owned by your team. If you want a new namespace to be created, please file an issue via the [Onboarding to a cluster](https://github.com/operate-first/support/issues/new/choose) template.

---

If you don't want to wait for the maintainers to notice this issue, you can do the changes yourself. Please follow the [docs/onboarding_team_to_argo_cd.md](https://github.com/operate-first/support/blob/main/docs/onboarding_to_argocd.md) and/or the [docs/add_application.md](https://github.com/operate-first/argocd-apps/blob/main/docs/add_application.md) guides.
