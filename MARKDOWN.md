# Contribution Guide

## Setup

The only dependencies you need are [Git](https://git-scm.com/) and [uv](https://docs.astral.sh/uv/). 
You don't need to install Python manually or any dependencies using pip

```bash
git clone https://github.com/PabloFl07/sustentable.git && cd sustentable
uv sync                    
uv run pre-commit install
uv run sustentable         
uv run pytest              
```



## Workflow

> Notes on correct [commit messages](#commits) and [branch names](#branch-model)


**1. Create a new branch based on `dev`**

> [!IMPORTANT]
> Before creating a new branch or merging it, pull the latest dev to avoid conflicts.

```bash
git switch dev
git pull
git switch -c correctly-named-branch
```

**2. Work on it and push it**

```bash
git add ...
git commit -m "Correctly redacted commit message"
git push -u correctly-named-branch
```

**3. Switch to dev and merge your branch**

```bash
git switch dev && git pull
git merge correctly-named-branch
git push 
```


## Commits

## Branch Model

## Style guide

## Code testing

## Documentation

All forms of documentations must be written in English and in Markdown format. On top of that, you must ... :

- `README.md`: basic information about the project. You may not modify it
- `docs/`: detailed documentation (architecture, design decisions, user manual)
- `CHANGELOG.md`: brief description of the changes in each version

We highly value comments in the code. This can be a deciding factor in rejecting it.

## Use of AI

We support using AI (i.e., LLMs) as tools for coding. However, you remain responsible for any code you publish and we are responsible for any code we merge and release.
