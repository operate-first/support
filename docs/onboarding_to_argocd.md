# ArgoCD onboarding procedure

We have an ArgoCD instance deployed on MOC that can be used to deploy the application manifests located in this repo.

The ArgoCD instance is deployed on [MOC CNV Sandbox](https://github.com/operate-first/continuous-deployment/tree/master/manifests/overlays/moc-cnv) cluster.

Each team is given an [ArgoCD Project](https://argoproj.github.io/argo-cd/user-guide/projects/) that has an allow-list of clusters and namespaces to which they can deploy. They also have an allow-list of resources they can deploy within those namespaces. These restrictions exist to prevent teams from being able to use ArgoCD to deploy cluster scoped resources, or resources onto other team's namespaces.

> Currently, you can only use this ArgoCD instance to deploy to moc-cnv-sandbox cluster, other clusters are not yet supported, please make an issue if you have this requirement.

Teams are given edit access (via ui/cli console) to their ArgoCD Projects using OpenShift RBAC and OpenShift Groups.

The following steps should be completed to fully onboard and enable a team to use ArgoCD to deploy `Applications` to their ArgoCD `Projects`.

> Note: ArgoCD Projects should not to be confused with OpenShift Projects.

## Pre-requisites
Team requesting ArgoCD access must have been onboarded to the cluster. See [here](https://github.com/operate-first/support/blob/main/docs/onboarding_to_cluster.md)

Please fork/clone the [operate-first/argocd-apps](https://github.com/operate-first/argocd-apps) repository. **During this whole setup, we'll be working within this repository.**

## OpenShift Group

To add multi-tenancy support, we require the team to have an OpenShift group on the MOC cluster on which our ArgoCD instance resides. This OpenShift group should include all the people belonging to the team that will need write-level access to applications belonging to the team's ArgoCD Project (explained later). The team being onboarded to ArgoCD should have had a group already created during cluster onboarding, as described [here](https://github.com/operate-first/support/blob/main/docs/onboarding_to_cluster.md)

## Create project directories for this repository
To create the project directories, use the the following script provided:

```bash
./create-project.sh project_name
```

This will create the necessary folders/files that respects the project structure of this repository.

Teams should be directed [here](add_application.md) for instructions on where to create their ArgoCD Applications. All Applications should be pointed to the team's [ArgoCD Project](https://github.com/operate-first/continuous-deployment/tree/master/manifests/overlays/moc-cnv/projects) (i.e. the `project` field in the ArgoCD [Aplication](https://argoproj.github.io/argo-cd/operator-manual/declarative-setup/#applications) manifest), see below for instructions on adding an ArgoCD Project.

## Create the ArgoCD Project
The team will need a dedicated [ArgoCD Project](https://argoproj.github.io/argo-cd/user-guide/projects/) for their [ArgoCD Applications](https://argoproj.github.io/argo-cd/operator-manual/declarative-setup/#applications). The ArgoCD project should be added [here](https://github.com/operate-first/continuous-deployment/tree/master/manifests/overlays/moc-cnv/projects).

A typical project will look like the following:

```yaml
apiVersion: argoproj.io/v1alpha1
kind: AppProject
metadata:
  name: <team-name>
spec:
  destinations:
    - namespace: '<team-namespace-prefix>-*'
      server: 'https://kubernetes.default.svc'
  sourceRepos:
    - '*'
  roles:
    - name: project-admin
      description: Read/Write access to this project only
      policies:
        - p, proj:<team-name>:project-admin, applications, get, <team-name>/*, allow
        - p, proj:<team-name>:project-admin, applications, create, <team-name>/*, allow
        - p, proj:<team-name>:project-admin, applications, update, <team-name>/*, allow
        - p, proj:<team-name>:project-admin, applications, delete, <team-name>/*, allow
        - p, proj:<team-name>:project-admin, applications, sync, <team-name>/*, allow
        - p, proj:<team-name>:project-admin, applications, override, <team-name>/*, allow
        - p, proj:<team-name>:project-admin, applications, action/*, <team-name>/*, allow
      groups:
        - <team-openshift-group>
        - operate-first
  clusterResourceWhitelist:
    - group: ''
      kind: Namespace
  namespaceResourceWhitelist:
  ....
```

Some notes:

* Ensure that the `spec.destinations` field contains a prefix for the team's namespaces. The team will be required to prefix their namespaces with this attribute if they want ArgoCD to be able to deploy to them, any other namespaces not following the prefix will need to be added manually under this field. See additional notes for more details.
* Ensure `operate-first` is added into the `roles.groups` for each role. This allows the operate-first team to help diagnose issues.
* `namespaceResourceWhitelist` generally contains the list of resources a project `admin` has access to. The general idea is that a team should be able to deploy via ArgoCD what they can deploy using `oc apply`. See other projects for a list of such resources.

Ensure that the argocd project is included in the `kustomization.yaml` [here](https://github.com/operate-first/continuous-deployment/blob/master/manifests/overlays/moc-cnv/projects/kustomization.yaml).

## Enable OpenShift auth to ArgoCD Console
By default all users should be able to see the [ArgoCD console](https://argocd-server-aicoe-argocd.apps.ocp4.prod.psi.redhat.com). To be able to make changes to applications belonging to the team's ArgoCD Project (via the cli or ui), the team will need to be able to log into the console with appropriate access. This accomplished by adding the team's OpenShift group mentioned in the beginning under the dex config [here](https://github.com/operate-first/continuous-deployment/blob/master/manifests/overlays/moc-cnv/configs/argo_cm/dex.config#L11).


## Additional Notes:

### Namespace Prefix
An ArgoCD project allows us to ensure that a team cannot deploy applications onto another team's namespace via ArgoCD.

We accomplish this by allowing teams to add the namespaces that they will be deploying to in their ArgoCD Project CR under the `spec.destinations.` field. Example:

```yaml
apiVersion: argoproj.io/v1alpha1
kind: AppProject
metadata:
  name: example-project
  namespace: argocd
spec:
  destinations:
  - namespace: guestbook
    server: 'https://kubernetes.default.svc'
...
```

The project above can only deploy into the `guestbook` namespace in the host cluster.

It can get bit tedious having to always require a team to submit a pr updating the `spec.destinations` to include new namespaces their project applications can deploy onto, so we can use wildcards to include a set of namespaces that begin with a prefix. For example, the `thoth` team has the following prefix in their `spec.destinations`:

```yaml
spec:
  destinations:
    - namespace: 'thoth-*'
      server: 'https://kubernetes.default.svc'
```

Now, as long as all thoth team's namespaces have `metadata.name` beginning with a `thoth-` prefix, they can deploy into these namespaces using ArgoCD Applications that are part of the `thoth` project.

### Resources:

- To read more about ArgoCD Declarative setup [see here](https://argoproj.github.io/argo-cd/operator-manual/declarative-setup/)
- To understand our authentication setup [see here](https://argoproj.github.io/argo-cd/operator-manual/user-management/#dex)
- To read about ArgoCD Projects [see here](https://argoproj.github.io/argo-cd/user-guide/projects/)
- To learn about Kustomize bases & overlays [see here](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/#bases-and-overlays)
