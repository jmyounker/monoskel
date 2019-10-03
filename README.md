Monoskel: An opinionated monorepo
---

This is a skeleton monorepo. It uses the following tooling:

* `git` as the revision control system.
* `bazel` for the build tool.
* `zsh` as a shell.
* `lefthook` to manage git hooks.

* `github` for the central git repository. (gitlab?)
* `zgen` to manage shell plugins.
* `brew` as a package manager on OSX.
* `sdkman` to manage java family sdks in developer environments.
* `p4merge` as an external diff/merge tool.
* `idea` as a development tool. (VSCode?)
* `jira` for ticket tracking.
* `confluence` for an external documentation system.

Getting Started
---
By this point you've forked and cloned the repo, so you've already
got `git`. In the directory where you found this repo, run:
`./bin/init-repo PROJECT_NAME`.

To start developing you have two options.

* From the command line, run the command `./bin/update-build-environment`
* Or start intellij from the project root and run the `update-build-environemnt` task. 

Filesytem Layout
---
`.gitignore` -- files to ignore 

`.idea` -- intellij project dir; most things are omitted

`.idea/runConfigurations` -- intellij shared run configurations

`bin` -- scripts run by the build environment

`bin/create-repo` -- creates a new monorep from the skeleton

`bin/update-build-environment` -- install/update developer's environment 

`cell` -- developer level components go here

`skel` -- contains the template for a new repo

`WORKSPACE` -- master workspace file for  

`README.md` -- an overview of the repo; this file


Further Plans
---

Thinking this over further, I think the process for building will be
something like this:

* User checks out monoskel.
* User runs `bin/monoskel create PATH_TO_REPO` and it creates the
  skeleton based on this repo and creates a base project.
* Creates first commit.
* User manually pushes to gitlab/github.

Update process looks like on of these:

* User updates monoskel.
* User runs `bin/monoskel plan PATH_TO_REPO` and it creates a list
  of files which will be updated.
* User redirects these to file.
* User edits file.
* User runs plan `bin/monoskel apply`.

**Automate creation of upstream repo** 

**Automate application for Atlassian accounts**

Setting up the atlassian accounts will be documentation at first. Then
it will become real real code.

**Later Expansions**

After the basic system is sketched out I plan the following expansions:

* Support for `vscode`.
* Per-language setup:
  * Java
  * Kotlin
  * Python
  * Go
  * JavaScript
  * TypeScript
  * Php


