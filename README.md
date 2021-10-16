Monoskel: An opinionated monorepo
---

This is a skeleton monorepo. It uses the following tooling:

* `git` as the revision control system.
* `bazel` for the build tool.
* `brew` as a package manager on OSX.
* `zsh` as a shell.
* `zgen` to manage shell plugins.
* `lefthook` to manage git hooks.
* `idea` as a development tool. (VSCode?)
* `jira` for ticket tracking.
* `confluence` for an external documentation system.
* `p4merge` as an external diff tool.

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

`bin/initialize-repo` -- initializes repo

`bin/update-build-environment` -- install/update developer's environment 

`cell` -- developer level components go here

`WORKSPACE` -- master workspace file for  

`README.md` -- an overview of the repo; this file

`WORKSPACE.tmpl` -- template file for WORKSPACE which may eventually go away; pay no attention

Further Plans
---

**Set license for project**

**Create github project(s)**

**Turn target repo into a build artifact.**

I'm quickly realizing that some amount of initialization and testing
will be necessary to separate my tooling from the final repo.

Thinking this over further, I think the process for building will be
something like this:

* User checks out monoskel.
* User runs `bin/initialize-repo PATH_TO_REPO GIT_PROJECT_NAME` and it crates the
  skeleton based on this repo. The basic skeleton probably gets moved elsewhere.
 

Things that currently need to be separated out are:
* remove `bin/initialize-repo` after it runs successfully.
* remove `bin/initialize-repo` from distribution repo.
* remove `WORKSPACE.tmpl` from distribution repo.

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


