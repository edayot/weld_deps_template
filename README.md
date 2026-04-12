# WeldDeps Template

This readme will show you how to use the WeldDeps template to create a new datapack project.


## Getting Started

Install uv https://docs.astral.sh/uv/getting-started/installation and run `uv sync --group dev` in the root of the project to install the dependencies.



## Managing `smithed.net` dependencies

In `beet.yaml` you can find this section:
```yaml
meta:
	weld_deps:
		deps:
			- id: itemio
				version_: "1.2.6"
				source: smithed
```
Theses are smithed.net dependencies, this will automatically download the proper version and add it to the ctx object before your datapack is built. This use [weld](https://weld.smithed.dev/) internally to develop with the merging tool.

